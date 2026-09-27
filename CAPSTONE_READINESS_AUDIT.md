# Capstone Defense Readiness Audit

**System:** IoT-Based Smart Laboratory Management System for ESSU Arteche Campus  
**Review date:** 2026-09-27  
**Scope:** All tracked source code, firmware, configuration, runtime data, build notes, deployment notes, and thesis artifacts in this repository.

## Executive verdict

**Overall readiness: 51/100 — conditionally demonstrable, but not yet ready to defend as a validated final system.**

The repository contains a substantial, coherent prototype. Its teacher application, student agent, local persistence, reservation workflow, screen streaming, command/timer handling, telemetry firmware, and recovery-oriented runtime design are credible capstone work. A carefully staged single-laboratory demonstration can probably communicate the concept well.

The present submission should not, however, be represented as a fully validated final system. A small automated core reliability suite now passes, but the UI, media, network reconnection, packaged applications, and multi-PC workflows still lack automated or recorded end-to-end validation. The documented evaluation tables are empty, important imports cannot be exercised in the current environment, and dependency versions are not pinned. These are material defense risks because the manuscript promises testing, ISO/IEC 25010 evaluation, and a final implementation.

## Scorecard

| Area | Weight | Score | Assessment |
|---|---:|---:|---|
| Functional coverage and objective alignment | 20 | 16 | Strong prototype coverage: screen monitoring, student authentication, commands, timers, reservations, messaging, recordings, health data, and ESP32 telemetry. |
| Architecture and code organization | 15 | 10 | Sensible shared `core` modules and separated teacher/student entry points, but both main applications are monoliths (about 4,246 and 2,236 lines). |
| Reliability and recovery | 15 | 9 | Reconnect loops, heartbeats, bounded queues, timer persistence, and atomic JSON writes are positive; broad exception swallowing and limited lifecycle control reduce confidence. |
| Security and privacy | 15 | 4 | Salted hashes and parameterized SQL are positive, but SHA-256 is not a password KDF, the protocols are plaintext/unauthenticated, registration is open, and no administrator authentication is present. |
| Verification and evidence | 15 | 7 | Eight core protocol, settings, registry, authentication, session, and reservation tests pass, but UI/media/network/package tests and manuscript evaluation results remain incomplete. |
| Deployment and reproducibility | 10 | 3 | Firmware wiring notes and PyInstaller commands exist; dependencies are unpinned, host values are hard-coded/inconsistent, and there is no clean installation/runbook or CI pipeline. |
| Documentation and defense package | 10 | 2 | The thesis and diagrams exist, but the manuscript mixes ISO/IEC 25010 with ISO 9001, uses future tense for completed testing, and leaves the result table blank. |
| **Total** | **100** | **51** | **Prototype/demo stage; not final-defense ready without broader system testing and evidence.** |

## What is working well

1. **The implementation meaningfully matches the proposed problem.** The system is more than a UI mock-up: it includes workstation enrollment, screen frames, teacher commands, timers, student accounts, session history, reservations, messaging, recordings, resource metrics, and temperature/fan telemetry.
2. **The core data access is reasonably disciplined.** SQLite calls use parameters; database access is serialized by a lock; sessions and reservations have indexes; reservation overlap is checked; active sessions and recordings have explicit lifecycle state.
3. **There are practical resilience mechanisms.** The applications use heartbeat state, reconnect loops, bounded queues, command acknowledgements, command de-duplication, persisted timers, interrupted-session grace periods, and atomic JSON replacement.
4. **The media protocol has a frame-size guard.** Length-prefixed binary frames reject non-positive or greater-than-10 MB payloads.
5. **The ESP32 portion is concrete.** The firmware defines two fan pulse inputs, a OneWire temperature bus, Wi-Fi reconnection, periodic UDP JSON telemetry, and an accompanying pin/wiring/troubleshooting guide.
6. **The student runtime settings module correctly chooses a per-user writable location for frozen builds.** The startup path now preserves and uses the saved teacher host.

## Critical defense blockers

### 1. Incomplete system-level verification and evaluation evidence

- Eight core reliability tests cover JSON/frame protocol behavior, settings persistence and fallback, registry corruption/concurrency, authentication, sessions, and reservation conflicts.
- There are still no automated UI, media, reconnect, long-duration, packaged-build, or multi-workstation integration tests.
- The manuscript says unit, integration, alpha, and beta testing *will* be conducted rather than presenting reproducible completed procedures.
- Chapter IV's alpha-testing table is blank, so the claimed ISO-based evaluation cannot be audited.
- The manuscript says the objectives use ISO/IEC 25010 but Chapter IV calls ISO 9001 a software product quality model. ISO 9001 is a quality-management-system standard, not the ISO/IEC 25010 software product-quality model.

**Required:** Add automated tests for protocol framing, authentication, reservation conflicts, sessions, timers, registry corruption recovery, command authorization, and telemetry parsing. Add a LAN integration test plan with measured latency, FPS, reconnect time, packet loss, CPU/RAM usage, and concurrent workstation count. Complete the survey and statistical results with respondent counts, raw/aggregated data, formulas, dates, and ethical/privacy handling.

### 2. Plaintext, unauthenticated control and monitoring channels

- The control server accepts any client that presents a non-empty MAC string. A MAC is client-supplied and can be spoofed.
- Video viewers register using only a `pc_id`; telemetry is accepted over UDP; student commands and credentials travel as plaintext JSON over TCP.
- There is no TLS, pre-shared key, signed message, nonce, certificate, or teacher/admin login boundary.
- A hostile or simply misconfigured host on the LAN could impersonate a workstation, inject telemetry, capture credentials/screens, or disrupt a client session. The “trusted LAN” scope reduces exposure but does not eliminate this defense question.

**Required:** At minimum, provision a unique per-client secret, authenticate registration and every UDP message with an HMAC plus timestamp/nonce, restrict enrollment, bind video/control channels to the authenticated client session, add teacher authentication, and document firewall/VLAN rules. Prefer TLS for control/media if feasible.

### 3. Student host configuration defect (resolved in this review)

`student.main()` previously loaded the saved `StudentSettings`, constructed a client with that host, and immediately overwrote it with a second client constructed from the compiled network default. The duplicate construction has been removed, so the persisted teacher address is now used on startup.

**Remaining validation:** Demonstrate changing the teacher host and restarting a packaged student build on the defense network.

### 4. Reproducibility is insufficient

- All Python requirements are unpinned, so an installation made on defense day may resolve incompatible versions.
- The provided build command refers to a nonexistent `core.runtime_paths` hidden import.
- There is no README that states supported Windows/Python/ESP32 versions, installation order, firewall ports, startup order, database backup/restore, clean demo data, or known limitations.
- The repository tracks exports, user-interface position/settings, client registry records, and an empty invalid JSON file. Runtime artifacts should be separated from source-controlled fixtures.

**Required:** Pin and hash dependencies, create tested build scripts, build from a clean checkout/VM, publish checksums for defense binaries, add an operator/deployment guide, remove or anonymize runtime artifacts, and prepare a scripted rollback/demo reset.

### 5. Password and account controls are prototype-grade

Passwords are salted but processed with a single SHA-256 round. There is no minimum length, rate limiting, lockout, forced initial password change, recovery audit trail, or administrator role. Student self-registration is enabled through the control channel.

**Required:** Use Argon2id, scrypt, or PBKDF2 with a calibrated work factor; enforce a password policy; rate-limit and temporarily lock repeated failures; make self-registration configurable/approval-based; and record security-relevant administrative events.

## High-priority engineering risks

1. **Unbounded JSON line input:** `readline()` has no byte limit, so a connected peer can cause excessive memory use. Introduce an explicit maximum message size and reject non-object JSON.
2. **Identity binding gaps:** After registration, heartbeat messages can name another `pc_id`; validate that message identity equals the authenticated socket's assigned ID. Apply equivalent binding to acknowledgements and media streams.
3. **Broad exception handling:** Many loops catch `Exception`, sleep, and restart or disconnect without preserving enough context. This aids recovery but can conceal deterministic defects during a defense. Catch expected failures narrowly and surface actionable health errors.
4. **Thread shutdown:** Most workers use `while True` daemon loops. Add a shared stop event, socket timeouts/closure, joins, and deterministic database/media cleanup.
5. **Data validation:** Registration accepts any non-empty password/name/section at the database layer; settings accept unchecked ranges; sensor values lack plausible bounds; message lengths are not capped.
6. **Firmware sensor identity:** DS18B20 devices are mapped by discovery order, which is not a durable physical identity. Store and configure ROM addresses per PC to prevent PC01/PC02 swapping after wiring or boot changes.
7. **Firmware counter race:** Pulse counters are copied and zeroed without a critical section. Protect the read/reset pair against interrupts.
8. **Wi-Fi loop behavior:** The firmware guide calls scheduling non-blocking, but reconnection can block for up to five seconds and temperature conversion may also block. Describe this accurately and measure its effect on telemetry gaps.
9. **Configuration duplication:** Defaults appear in both `deploy_settings.py`, `AppSettings`, JSON, firmware, and build notes. Establish one documented deployment template and validate all port/host/profile values at startup.
10. **Maintainability:** Split teacher and student monoliths into transport, service, state, UI, and media components so they can be tested independently.

## Defense-readiness acceptance gate

Do not call the system “final-defense ready” until all of the following are true:

- [x] Fix the duplicate student-client construction so the persisted host is selected at startup.
- [ ] Verify persisted host selection in the packaged Windows student application.
- [ ] Complete a clean install and PyInstaller build on the exact defense Windows version.
- [ ] Run a minimum two-PC plus ESP32 end-to-end rehearsal on an isolated LAN.
- [ ] Demonstrate login/register policy, screen tiles, lock/unlock, timer expiry, messaging, extension, reservation, sensor display, recording/history export, reconnect, and graceful shutdown.
- [x] Add initial automated core reliability tests.
- [ ] Expand coverage to timers, commands, telemetry, UI/media integration, and long-duration operation; retain a dated test report.
- [ ] Authenticate clients and administrator actions, or explicitly label the build a controlled academic prototype and present a concrete threat model and mitigation roadmap.
- [ ] Replace SHA-256 password hashing with a password KDF and add login throttling.
- [ ] Pin dependencies and remove the nonexistent hidden import from build instructions.
- [ ] Finish Chapter IV with real data and reconcile ISO/IEC 25010 terminology throughout the manuscript.
- [ ] Prepare privacy/consent, retention, access-control, and incident-response explanations for captured screens, audio, identities, and recordings.
- [ ] Back up the database, prepare known-good binaries/firmware, and create an offline demo dataset/video in case hardware or LAN conditions fail.

## Recommended defense narrative

If the defense occurs before every hardening item is complete, present the system honestly as a **LAN-only academic prototype validated in a controlled laboratory**, not as production-ready surveillance/security software. Lead with the integrated value proposition and live workflow; explicitly disclose the threat model and limitations; distinguish implemented features from planned work; and support every quality claim with a test artifact or measurement.

Likely panel questions to rehearse:

1. Why is an ESP32 needed when CPU temperature/fan data might be read through software, and how are sensors physically mapped to PCs?
2. What prevents another LAN device from impersonating PC01 or sending shutdown/control traffic?
3. How many simultaneous 720p streams were measured, at what FPS/latency/bandwidth, and on what hardware?
4. What happens when the teacher PC, router, student PC, or ESP32 restarts mid-session?
5. How do you obtain consent and protect screen/audio recordings and student credentials?
6. Why do the results mention ISO 9001 when the evaluation instrument is based on ISO/IEC 25010?
7. Where are the unit/integration test cases and the raw respondent results?
8. How does the system prevent timer, reservation, and session inconsistencies after a disconnect?

## Reassessment target

Completing the critical blockers, obtaining credible test/evaluation evidence, and passing a repeatable multi-device rehearsal would reasonably move the project into the **75–85/100, defense-ready academic prototype** range. Production deployment would still require a formal security review, privacy governance, stronger endpoint control, load testing, monitoring, backup/restore drills, and maintainable release engineering.
