import io
import json
import socket
import threading
from pathlib import Path

from core.auth_db import AuthDatabase
from core.client_registry import ClientRegistry
from core.protocol import MAX_JSON_LINE_BYTES, recv_frame, recv_json_line, send_frame, send_json
from core.student_settings import StudentSettings, StudentSettingsStore, normalize_teacher_host


def test_json_protocol_round_trip() -> None:
    left, right = socket.socketpair()
    try:
        send_json(left, {"type": "heartbeat", "pc_id": "PC01"})
        assert recv_json_line(right.makefile("rb")) == {"type": "heartbeat", "pc_id": "PC01"}
    finally:
        left.close()
        right.close()


def test_json_protocol_rejects_malformed_non_object_and_oversized_messages() -> None:
    assert recv_json_line(io.BytesIO(b"not-json\n")) is None
    assert recv_json_line(io.BytesIO(b"[1, 2, 3]\n")) is None
    assert recv_json_line(io.BytesIO((b"x" * (MAX_JSON_LINE_BYTES + 1)) + b"\n")) is None


def test_frame_protocol_round_trip_and_truncated_frame() -> None:
    left, right = socket.socketpair()
    try:
        payload = b"frame payload"
        send_frame(left, payload)
        assert recv_frame(right) == payload
        left.sendall(b"\x00\x00\x00\x05abc")
        left.shutdown(socket.SHUT_WR)
        assert recv_frame(right) is None
    finally:
        left.close()
        right.close()


def test_student_settings_round_trip_and_fallback(tmp_path: Path) -> None:
    path = tmp_path / "student.json"
    store = StudentSettingsStore(path=path, default_teacher_host="127.0.0.1")
    assert store.load().teacher_host == "127.0.0.1"
    store.save(StudentSettings(teacher_host="192.168.10.2"))
    assert store.load().teacher_host == "192.168.10.2"
    path.write_text("invalid", encoding="utf-8")
    assert store.load().teacher_host == "127.0.0.1"


def test_teacher_host_validation() -> None:
    assert normalize_teacher_host("  lab-teacher.local ") == "lab-teacher.local"
    for value in ("", "has a space", "x" * 256):
        try:
            normalize_teacher_host(value)
        except ValueError:
            pass
        else:
            raise AssertionError(f"Expected invalid host to fail: {value!r}")


def test_client_registry_recovers_from_corrupt_file(tmp_path: Path) -> None:
    path = tmp_path / "clients.json"
    path.write_text("invalid", encoding="utf-8")
    registry = ClientRegistry(path)
    assert registry.list_pc_ids() == []
    assert json.loads(path.read_text(encoding="utf-8")) == {"clients": [], "next_id": 1}


def test_client_registry_assignments_are_thread_safe(tmp_path: Path) -> None:
    registry = ClientRegistry(tmp_path / "clients.json")
    results: list[str] = []
    result_lock = threading.Lock()

    def register() -> None:
        pc_id = registry.get_or_assign_id("AA:BB:CC:DD:EE:FF", "student-pc")
        with result_lock:
            results.append(pc_id)

    workers = [threading.Thread(target=register) for _ in range(20)]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()

    assert results == ["PC01"] * 20
    assert registry.list_pc_ids() == ["PC01"]


def test_auth_session_and_reservation_lifecycle(tmp_path: Path) -> None:
    database = AuthDatabase(tmp_path / "auth.db")
    assert database.register_student("Student One", "BSIT 4A", "24-00001", "password") == (True, "registered")
    user = database.verify_login("24-00001", "password")
    assert user is not None
    assert database.verify_login("24-00001", "wrong") is None

    ok, reason, reservation_id = database.create_reservation("24-00001", "PC01", 1_000, 2_000, "teacher")
    assert (ok, reason) == (True, "created")
    assert reservation_id is not None
    assert database.create_reservation("24-00001", "PC01", 1_500, 2_500, "teacher")[:2] == (
        False,
        "reservation_conflict",
    )

    session_id = database.open_session("PC01", user)
    assert session_id > 0
    assert len(database.get_active_sessions()) == 1
    database.close_active_session("PC01")
    assert database.get_active_sessions() == []
