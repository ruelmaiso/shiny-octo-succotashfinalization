# Defense Demonstration Script

## IoT-Based Smart Laboratory Management System for ESSU Arteche Campus

> **How to use this script:** Basahin lamang ang text na nasa quotation marks. Ang **Demo Action** at **What the Panel Will See** ay guide mo habang nagde-demonstrate at hindi kailangang basahin word-for-word.

---

# 1. Bago Magsimula

## Quick preparation checklist

- [ ] Magkakonekta sa parehong LAN ang Teacher PC, Student PC, at ESP32.
- [ ] Tama ang Teacher PC address na naka-save sa Student Agent at ESP32.
- [ ] May prepared student account na alam ang password.
- [ ] May at least one Student PC na kilala na ng system bilang PC01 o PC02.
- [ ] Nakakabit at nasubukan na ang temperature at fan sensors.
- [ ] May simple window na nakabukas sa Student PC para madaling makita ang screen monitoring.
- [ ] Huwag gamitin ang main demonstration PC para sa live Shutdown o Restart.
- [ ] I-demo lamang ang recording at screen-share audio kung nasubukan na sa exact defense computers.

## Recommended startup order

1. Ihanda ang LAN or router.
2. Buksan ang Teacher Application.
3. Buksan ang Student Agent.
4. Mag-login sa Student PC.
5. I-on ang ESP32.

---

# 2. Opening Introduction

> “Good day, panel members. Ang aming project ay **IoT-Based Smart Laboratory Management System for ESSU Arteche Campus**.”
>
> “Ang purpose ng system ay tulungan ang instructor sa pag-monitor at pag-manage ng laboratory computers gamit ang isang central application.”
>
> “Sa system, makikita ng instructor kung aling computers ang connected, kung sino ang gumagamit ng PC, ang current screen nito, at ang available temperature at fan readings.”
>
> “May tatlong main parts ang project: ang Teacher Application, ang Student Agent sa bawat laboratory computer, at ang ESP32 with sensors. Nag-uusap ang mga ito sa loob ng local network.”

---

# 3. Simple Introduction of Components

## Teacher Application

> “Ang Teacher Application ang ginagamit ng instructor. Dito niya makikita ang laboratory computers at dito rin niya magagamit ang available controls.”

## Student Agent

> “Ang Student Agent naman ay tumatakbo sa bawat student computer. Ito ang nagbibigay ng information tungkol sa PC at tumatanggap ng commands mula sa teacher side.”

## ESP32 and Sensors

> “Ang ESP32 ang kumukuha ng readings mula sa temperature at fan sensors. Pagkatapos, ipinapadala nito ang readings sa Teacher Application para makita sa dashboard.”

## Local Network

> “Ang Teacher PC, Student PCs, at ESP32 ay connected sa parehong LAN. Dahil local ang setup, hindi kailangan ng internet para sa normal operation ng system.”

## Local Storage

> “May local database din ang Teacher Application. Dito sine-save ang student accounts, session records, at reservations. May local files din para sa settings, PC assignments, at active timers.”

---

# 4. Complete Live Demonstration

## Step 1 — Start the Teacher Application

### DEMO ACTION

Buksan ang Teacher/Admin Application at hintaying lumabas ang dashboard.

### WHAT THE PANEL WILL SEE

Makikita ang:

- workstation information sa top panel;
- malaking screen-view area sa gitna;
- listahan ng PC previews;
- PC selection at controls sa bottom panel;
- buttons para sa Students, Chat, Reservations, Share Screen, History, at Settings.

### SIMPLE TECHNICAL EXPLANATION

> “Unahin ko munang buksan ang Teacher Application.”
>
> “Ito ang main dashboard na ginagamit ng instructor. Dito makikita ang connected computers, kanilang status, at iba pang importanteng information.”
>
> “Sa background, inihahanda ng application ang connection para matanggap nito ang information mula sa Student PCs at ESP32.”

### RESULT

> “Ready na ngayon ang Teacher Application para sa monitoring at control.”

---

## Step 2 — Start the Student Agent

### DEMO ACTION

Buksan ang Student Agent sa Student PC. Kung connecting pa, ipakita sandali ang connection screen.

### WHAT THE PANEL WILL SEE

Habang wala pang connection, may Connecting screen at field para sa Teacher/Admin Server IP.

### SIMPLE TECHNICAL EXPLANATION

> “Ngayon, bubuksan ko naman ang Student Agent sa laboratory computer.”
>
> “Kapag hindi pa nito makita ang Teacher Application, mananatili ito sa Connecting screen at automatic na susubukang kumonekta ulit.”
>
> “Kung magbago ang address ng Teacher PC, puwede rin itong palitan at i-save dito.”

### RESULT

> “Hindi kailangang paulit-ulit i-restart ang Student Agent kapag pansamantalang wala ang connection.”

---

## Step 3 — Show the Connected Student PC

### DEMO ACTION

Hintaying mag-connect ang Student Agent. Sa Teacher Application, ipakita ang lumabas na PC at piliin ito.

### WHAT THE PANEL WILL SEE

Lalabas ang PC bilang PC01, PC02, o ibang assigned PC number. Magbabago ang status nito mula Offline papunta sa online status.

### SIMPLE TECHNICAL EXPLANATION

> “Kapag connected na ang Student Agent, makikita na natin ang computer dito sa Teacher Application.”
>
> “Bawat recognized computer ay may sariling PC number. Kapag bumalik ang parehong computer, ginagamit ulit ng system ang dati nitong assignment.”
>
> “Makikita rin natin kung connected ang PC at ang available information tulad ng CPU, RAM, disk usage, at uptime.”

### RESULT

> “Hindi na kailangang puntahan ng instructor ang bawat workstation para malaman kung active o connected ito.”

---

## Step 4 — Student Login

### DEMO ACTION

Sa Student PC, mag-login gamit ang prepared account. Gamitin lamang ang registration kung hihilingin ng panel.

### WHAT THE PANEL WILL SEE

Kapag successful ang login:

- mawawala ang login screen;
- magagamit na ang computer;
- lalabas sa Teacher Application ang student name at student number;
- magsisimula ang session timer.

### SIMPLE TECHNICAL EXPLANATION

> “Magla-login ako gamit ang prepared student account.”
>
> “Tinitingnan ng system kung tama ang account, kung may remaining usage time pa ang student, at kung ang PC ay hindi naka-reserve sa ibang student sa oras na ito.”
>
> “Kapag valid ang login, magsisimula ang student session at lalabas ang student information sa Teacher Application.”

### RESULT

> “Alam ng instructor kung sino ang kasalukuyang gumagamit ng bawat computer at gaano pa katagal ang session.”

---

## Step 5 — Show the Dashboard Information

### DEMO ACTION

Piliin ang connected PC at ituro ang information sa top panel.

### WHAT THE PANEL WILL SEE

Makikita ang available information tulad ng:

- PC number;
- current student at student number;
- remaining session time;
- CPU, RAM, disk usage, at uptime;
- temperature at fan RPM;
- last sensor update;
- current workstation status.

### SIMPLE TECHNICAL EXPLANATION

> “Kapag pinili ko ang PC, makikita natin dito ang importanteng information tungkol sa workstation.”
>
> “Kasama rito ang current user, remaining session time, computer usage information, at readings mula sa sensors.”
>
> “Ang purpose ng dashboard ay bigyan ang instructor ng mabilis na overview nang hindi niya kailangang isa-isang puntahan ang computers.”

### RESULT

> “Pinagsasama ng dashboard ang student information, computer status, at sensor readings sa isang view.”

### Simple status explanation if asked

> “Healthy means available ang expected PC, screen, at sensor information. Video Delay means connected ang PC pero wala pang updated screen. Sensor Waiting means wala pang reading, habang Sensor Stale means matagal nang walang bagong sensor data. Locked means naka-lock ang PC, at Offline means wala nang current connection.”

---

## Step 6 — Demonstrate Screen Monitoring

### DEMO ACTION

Magbukas o maglipat ng harmless window sa Student PC. Piliin ang PC tile sa Teacher Application.

### WHAT THE PANEL WILL SEE

Mag-u-update ang small preview at malaking selected view ayon sa current Student PC screen.

### SIMPLE TECHNICAL EXPLANATION

> “Ngayon, ipapakita ko ang screen monitoring.”
>
> “Kapag may ginagawa sa Student PC, makikita natin ang current screen nito sa Teacher Application.”
>
> “May Student Agent na kumukuha ng screen image at ipinapadala ito sa teacher side through the local network.”
>
> “Ang purpose nito ay magkaroon ang instructor ng centralized view ng laboratory activity.”

### RESULT

> “Nakikita ng instructor ang current screen ng selected computer mula sa dashboard.”

> **Important wording:** Sabihin na **screen monitoring** ito. Huwag tawaging remote desktop control dahil hindi nito kino-control ang mouse at keyboard ng student.

---

## Step 7 — Select a Target PC

### DEMO ACTION

Click **Show PCs**, pumili ng PC, at isara ang selector.

### WHAT THE PANEL WILL SEE

Makikita ang PC choices, search, Select Available, Clear, at Done. Magbabago ang Selected summary.

### SIMPLE TECHNICAL EXPLANATION

> “Bago gumamit ng control, pipili muna ako ng target computer.”
>
> “Puwedeng isang PC lamang o maraming available PCs ang piliin.”
>
> “Sa demonstration na ito, isang PC muna ang gagamitin ko para malinaw ang result.”

### RESULT

> “Ang command ay mapupunta lamang sa computers na pinili ng instructor.”

---

## Step 8 — Temporary Lock

### DEMO ACTION

Piliin ang **Temporary Lock** at click **Apply Lock Mode**.

### WHAT THE PANEL WILL SEE

Lalabas sa Student PC ang full-screen **Session Paused** display. Magiging Locked ang status sa teacher side.

### SIMPLE TECHNICAL EXPLANATION

> “Para naman pansamantalang pigilan ang paggamit ng computer, gagamitin ko ang Temporary Lock.”
>
> “Kapag pinindot ko ang Apply Lock Mode, lalabas ang Session Paused screen sa Student PC.”
>
> “Temporary lamang ito. Hindi nawawala ang student account at puwedeng ibalik ng instructor ang session gamit ang Unlock.”

### RESULT

> “Useful ito kapag kailangan munang kunin ng instructor ang attention ng student without ending the session.”

---

## Step 9 — Unlock

### DEMO ACTION

Click **Unlock**.

### WHAT THE PANEL WILL SEE

Mawawala ang Session Paused screen at babalik ang Student PC sa dating state.

### SIMPLE TECHNICAL EXPLANATION

> “Ngayon, ia-unlock ko naman ang computer.”
>
> “Kapag natanggap ng Student Agent ang command, aalisin nito ang temporary lock at makakapagpatuloy ang student.”

### RESULT

> “Naibalik ang paggamit ng workstation nang hindi na kailangan mag-login ulit.”

---

## Step 10 — Lock + Sign Out

### DEMO ACTION

Ituro muna ang option. I-apply lamang ito pagkatapos ng ibang student-session demonstrations dahil kailangan muling mag-login.

### WHAT THE PANEL WILL SEE

Kapag ginamit, mawawala ang active student access at kailangan ng panibagong login.

### SIMPLE TECHNICAL EXPLANATION

> “May second option din na Lock + Sign Out.”
>
> “Hindi lang nito pini-pause ang computer. Tinatanggal din nito ang current student access, kaya kailangan nang mag-login ulit bago magamit ang PC.”

### RESULT

> “Useful ito kapag tapos na ang student o kailangang ipagamit ang computer sa ibang authorized user.”

---

## Step 11 — Extend the Session

### DEMO ACTION

Mag-enter ng maliit na number sa **Minutes**, then click **Extend**. Ituro ang updated time. Gamitin ang Cancel kung gusto mong alisin ang idinagdag na time.

### WHAT THE PANEL WILL SEE

Madadagdagan ang remaining time at mag-u-update ang Extended Timer value.

### SIMPLE TECHNICAL EXPLANATION

> “May time limit ang bawat student session.”
>
> “Kung kailangan ng student ng additional time, puwedeng mag-enter ang instructor ng minutes at pindutin ang Extend.”
>
> “Makikita natin na nadagdagan ang available time. Nag-a-update ang teacher at student side para pareho ang countdown.”

### RESULT

> “Controlled ang laboratory usage, pero puwedeng magbigay ng authorized extension ang instructor.”

---

## Step 12 — Messaging

### DEMO ACTION

Buksan ang **Chat**, piliin ang student conversation, at mag-send ng maikling message. Sa Student PC, buksan ang chat at mag-reply.

### WHAT THE PANEL WILL SEE

Makikita ang teacher message sa Student PC at ang student reply sa Teacher Application. May unread indicator kapag may bagong message.

### SIMPLE TECHNICAL EXPLANATION

> “May messaging feature din para direktang makapagbigay ng instruction ang teacher.”
>
> “Magpapadala ako ng message na ‘Please save your work.’ Makikita natin ito sa Student PC.”
>
> “Puwede ring mag-reply ang student, at lalabas naman ang reply sa Teacher Application.”

### RESULT

> “May direct communication ang teacher at student kahit hindi lumapit ang instructor sa workstation.”

---

## Step 13 — Teacher Screen Sharing

### DEMO ACTION

Click **Share Screen**, ipakita ang Teacher screen sa Student PC, then click **Stop Sharing**.

### WHAT THE PANEL WILL SEE

Magpapakita ang Student PC ng Teacher screen. Magbabago ang button to Stop Sharing at makikita ang number of connected viewers.

### SIMPLE TECHNICAL EXPLANATION

> “Bukod sa pagtingin sa student screens, puwede ring i-share ng instructor ang kanyang screen sa connected Student PCs.”
>
> “Kapag pinindot ko ang Share Screen, makikita ng student ang Teacher screen. Magagamit ito sa lessons, instructions, o demonstrations.”
>
> “Habang naka-share ang Teacher screen, pansamantalang pini-pause ng system ang running student session time. Pag-stop ng sharing, magpapatuloy ulit ang affected timer.”

### RESULT

> “Nakakapag-present ang instructor directly sa laboratory computers.”

> **Optional only:** May support ang system para sa Teacher microphone audio. Huwag itong i-demo kung hindi pa nasubukan ang microphone at speakers sa actual defense setup.

---

## Step 14 — Temperature and Fan Monitoring

### DEMO ACTION

I-on ang ESP32 at hintaying lumabas ang readings. Kung safe, hawakan sandali ang temperature sensor para makita ang gradual change. Ipakita rin ang prepared fan input.

### WHAT THE PANEL WILL SEE

Makikita ang temperature, fan RPM, at last sensor update para sa configured PC.

### SIMPLE TECHNICAL EXPLANATION

> “Para naman sa IoT monitoring, gumagamit kami ng ESP32 at sensors.”
>
> “Ang temperature sensor ang kumukuha ng current temperature reading. Ang fan sensor naman ang nagbibigay ng pulses na ginagamit para malaman ang fan RPM.”
>
> “Ang ESP32 ang nagco-collect ng readings at ipinapadala ang information sa Teacher Application.”
>
> “Dito sa dashboard, makikita natin ang temperature, fan RPM, at kung kailan huling nakatanggap ng sensor update ang system.”

### RESULT

> “Bukod sa student activity, may basic hardware-condition monitoring din ang instructor.”

> **Important wording:** Fan monitoring ito, hindi automatic fan control. Temperature monitoring ito, hindi automatic cooling system.

---

## Step 15 — Show a Disconnection Condition

### DEMO ACTION

Pumili lamang ng isang safe test:

- pansamantalang i-off ang ESP32; or
- isara ang spare Student Agent.

Ibalik agad pagkatapos makita ang status change.

### WHAT THE PANEL WILL SEE

- Kapag walang bagong sensor reading, magiging Sensor Stale ang status.
- Kapag wala nang update mula sa Student Agent, magiging Offline ang PC.
- Kapag bumalik ang device, mag-u-update ulit ang dashboard.

### SIMPLE TECHNICAL EXPLANATION

> “Ipinapakita rin ng system kapag may nawawalang connection.”
>
> “Kapag tumigil ang sensor updates, hindi nito ipapakita na fresh pa rin ang old reading. Lalabas ang Sensor Stale status.”
>
> “Kapag ang Student Agent naman ang nawala, magiging Offline ang PC.”
>
> “Once bumalik ang connection, automatic na susubukan ng device na mag-connect ulit at magre-refresh ang dashboard.”

### RESULT

> “Mas madaling makita ng instructor kung ang issue ay nasa student computer o sa sensor connection.”

---

## Step 16 — Session History

### DEMO ACTION

Piliin ang PC at click **View Selected History**, or open **Settings** then **Overall Session History**. Magpakita ng saved record. Optional: export the visible records to CSV or PDF.

### WHAT THE PANEL WILL SEE

Makikita ang student, student number, PC, login time, logout time, session status, at recording link kung mayroon. May search, filter, paging, at export controls.

### SIMPLE TECHNICAL EXPLANATION

> “Ang student sessions ay sine-save sa local database ng Teacher PC.”
>
> “Dito sa Session History, makikita natin kung sino ang gumamit ng computer, kailan siya nag-login, kailan natapos ang session, at ang session status.”
>
> “Puwede ring mag-filter ng records at mag-export ng visible results as CSV or PDF.”

### RESULT

> “May local usage record ang laboratory na puwedeng gamitin para sa review at reporting.”

---

## Step 17 — Student Management and Reservations

### DEMO ACTION

Buksan ang **Students**, ipakita ang list, then close. Buksan ang **Reservations**, ipakita ang form at records, then close.

### WHAT THE PANEL WILL SEE

Sa Students:

- list of accounts;
- Add Student;
- Reset Password;
- Delete Student.

Sa Reservations:

- student at PC selection;
- start at end time;
- Created By;
- create, refresh, at cancel controls.

### SIMPLE TECHNICAL EXPLANATION

> “Sa Student Management, puwedeng tingnan at i-manage ng instructor ang local student accounts.”
>
> “Sa Reservations naman, puwedeng mag-assign ng student sa specific computer for a selected schedule.”
>
> “Kapag may active reservation para sa ibang student, hindi papayagan ng system ang maling student na mag-login sa PC na iyon.”

### RESULT

> “Kasama na sa same application ang basic account at laboratory scheduling management.”

---

# 5. Closing Statement

> “To summarize, naipakita natin ang connection ng Student PC, student login, dashboard monitoring, screen preview, lock and unlock, session extension, messaging, Teacher screen sharing, IoT temperature and fan monitoring, disconnection status, at session history.”
>
> “Ang main contribution ng system ay ang pagsasama ng student-computer monitoring at basic IoT hardware monitoring sa isang Teacher Application.”
>
> “Dahil dito, mas organized at centralized ang pag-monitor at pag-manage ng computers sa laboratory.”

---

# 6. Important Claims to Avoid

## Not implemented

Huwag sabihing mayroon ang system ng:

- file-system monitoring or file browsing;
- browser-history monitoring;
- application or process tracking;
- keyboard logging;
- remote mouse and keyboard control;
- cloud or mobile access;
- automatic fan control;
- automatic cooling;
- predictive maintenance.

## Correct terms to use

- Say **screen monitoring**, not remote desktop control.
- Say **fan RPM monitoring**, not fan control.
- Say **temperature monitoring**, not automatic cooling.
- Say **local database**, not cloud database.
- Say **automatic reconnect attempt**, not guaranteed uninterrupted connection.
- Say **near real-time monitoring**, not zero-delay monitoring.

---

# 7. Possible Panel Questions and Suggested Answers

## 1. What is the main purpose of the system?

> “Ang main purpose nito ay bigyan ang instructor ng centralized way para makita at ma-manage ang laboratory computers. Kasama rito ang student session, screen monitoring, available controls, at sensor readings.”

## 2. What are the main parts of the system?

> “May Teacher Application, Student Agent, at ESP32 with sensors. Ang Teacher Application ang main dashboard, ang Student Agent ang tumatakbo sa laboratory PC, at ang ESP32 ang kumukuha ng sensor readings.”

## 3. Why did you use LAN?

> “LAN ang ginamit dahil para ito sa loob ng computer laboratory. Local ang communication, mabilis ang response, at hindi kailangan ng internet para sa normal operation.”

## 4. How does a computer appear in the Teacher Application?

> “Kapag binuksan ang Student Agent at nakonekta ito sa Teacher Application, nakikilala ng system ang computer at binibigyan o inuulit ang assigned PC number nito.”

## 5. How do you know if a PC is connected?

> “Regular na nagbibigay ng status update ang Student Agent. Kapag tumigil ang updates nang lampas sa allowed time, nagiging Offline ang PC sa dashboard.”

## 6. What information can the teacher see?

> “Makikita ang PC number, current student, session time, screen preview, CPU, RAM, disk usage, uptime, temperature, fan RPM, at current status.”

## 7. How does screen monitoring work?

> “Kinukuha ng Student Agent ang current screen image at ipinapadala ito sa Teacher Application through the LAN. Doon ito ipinapakita bilang preview at larger selected view.”

## 8. Can the teacher control the student's mouse and keyboard?

> “Hindi. Screen monitoring at specific commands ang implemented. Walang remote mouse or keyboard control.”

## 9. What controls are available?

> “May Temporary Lock, Lock + Sign Out, Unlock, session extension, messaging, Teacher screen sharing, Shutdown, at Restart.”

## 10. What is the difference between Temporary Lock and Lock + Sign Out?

> “Sa Temporary Lock, naka-pause lang ang paggamit at nananatili ang current student session. Sa Lock + Sign Out, kailangan nang mag-login ulit bago magamit ang PC.”

## 11. What happens when the session time ends?

> “Ila-lock ng system ang Student PC at aalisin ang active student access. Sa teacher side, matatapos ang session record with a timeout status.”

## 12. Can the teacher add more time?

> “Yes. Pipiliin ng teacher ang logged-in PC, maglalagay ng minutes, at pipindutin ang Extend. Mag-u-update ang remaining time sa teacher at student side.”

## 13. What is the purpose of messaging?

> “Para makapagbigay ng direct instruction ang teacher at makapag-reply ang student without leaving the system.”

## 14. What is Teacher screen sharing?

> “Ito ang feature kung saan ang Teacher screen ang ipinapakita sa connected Student PCs. Puwede itong gamitin para sa lesson or demonstration.”

## 15. What is the role of the ESP32?

> “Ang ESP32 ang kumukuha ng information mula sa sensors at ipinapadala ito sa Teacher Application.”

## 16. What sensors are used?

> “DS18B20 sensors ang ginagamit para sa temperature. May fan pulse inputs din para makuha ang estimated fan RPM.”

## 17. How does sensor information appear in the system?

> “Ipinapadala ng ESP32 ang readings sa Teacher Application. Ina-associate ng system ang reading sa PC number at ipinapakita ito sa dashboard.”

## 18. What happens if the ESP32 disconnects?

> “Kapag walang bagong reading, magiging Sensor Stale ang status. Sinusubukan din ng ESP32 na bumalik sa Wi-Fi at magpatuloy ng readings kapag available na ulit ang connection.”

## 19. What data is stored?

> “Sine-save locally ang student accounts, session history, reservations, settings, PC assignments, active timers, at references ng recordings.”

## 20. What database is used?

> “SQLite ang local database na ginagamit sa Teacher PC. May JSON files din para sa settings, PC assignments, at timer recovery.”

## 21. What is recorded in session history?

> “Kasama ang student information, PC number, login and logout time, session status, at recording reference kung may saved recording.”

## 22. Can reports be exported?

> “Yes. Ang visible session-history results ay puwedeng i-export as CSV or PDF.”

## 23. How do reservations work?

> “Pipili ang instructor ng student, PC, start time, at end time. Kapag active ang reservation, chine-check ito during login para hindi magamit ng ibang student ang reserved PC.”

## 24. Does the system work without internet?

> “Yes. Ang core operation ay nasa local network. Kailangan lang na connected sa parehong LAN ang Teacher PC, Student PCs, at ESP32.”

## 25. What happens when a Student PC disconnects?

> “May short recovery period ang session para sa temporary connection problem. Kapag bumalik agad ang client, maaari itong magpatuloy. Kapag hindi, kino-close ng teacher side ang abandoned session.”

## 26. Does the system automatically reconnect?

> “The Student Agent and ESP32 both attempt to reconnect. Pero ang tamang claim ay automatic reconnect attempt, dahil nakadepende pa rin ang success sa network availability.”

## 27. Does the system record screens?

> “May off, manual, at automatic recording modes. Default na off ang current configuration. Ire-recommend lang naming i-demo ang recording kapag nasubukan na ang codec at storage sa exact Teacher PC.”

## 28. What are the limitations of the system?

> “LAN-only ito at para sa configured laboratory setup. Wala itong cloud or mobile access, file monitoring, application tracking, remote mouse and keyboard control, automatic cooling, at predictive maintenance.”

## 29. Why is this useful for the laboratory?

> “Mas mabilis makita ng instructor ang connected computers, current users, screens, session times, at sensor information. Hindi na kailangang manual na isa-isang i-check ang bawat workstation.”

## 30. How are software and IoT combined?

> “Ang Student Agent ang nagbibigay ng information tungkol sa computer at student session. Ang ESP32 naman ang nagbibigay ng sensor readings. Pareho silang ipinapakita sa Teacher dashboard using the corresponding PC number.”

---

# 8. Feature Check for the Actual Defense

## FULLY IMPLEMENTED — Safe to Demonstrate After Normal Rehearsal

- Teacher dashboard startup.
- Student Agent connecting screen and saved Teacher address.
- PC identification and persistent PC number.
- Student registration and login.
- Student account list and basic management.
- Student name, student number, and session timer display.
- Online and Offline status.
- CPU, RAM, disk usage, and uptime.
- Student screen preview and large selected view.
- Individual and multiple-PC selection.
- Temporary Lock and Unlock.
- Lock + Sign Out.
- Direct session extension and canceling the added extension.
- Teacher and student messaging.
- Teacher screen-sharing video after rehearsal.
- Temperature and fan RPM display for configured PC01 and PC02 sensors.
- Sensor Waiting and Sensor Stale status.
- Student and reservation management.
- Session history, filters, CSV export, and PDF export.
- Student Agent reconnect attempt and short-session recovery.

## PARTIALLY IMPLEMENTED OR HARDWARE-DEPENDENT

- **Recording:** Implemented but default is off; depends on video, codec, and disk space.
- **Screen-share audio:** Implemented for the Teacher microphone but depends on actual audio devices.
- **Student-requested extension:** Communication support exists, but there is no clear student request button in the current chat screen. Use direct Teacher extension in the demo.
- **Near-limit warning:** Exists, but the visible warning experience is limited.
- **Pause timer during Temporary Lock:** Depends on the saved setting.
- **Session recovery:** Good for short connection loss; full Student Agent or PC restart normally needs login again.
- **Sensor-to-PC order:** Check the physical sensor order before defense because the firmware maps the first sensor to PC01 and the second to PC02.
- **Many simultaneous high-resolution screens:** Depends on the Teacher PC and network performance.

## NOT RECOMMENDED FOR LIVE DEMO

- Shutdown or Restart on the main demonstration computer.
- Recording crash or recovery test.
- Screen-share audio without prior hardware rehearsal.
- Student-requested extension workflow unless its visible trigger is separately verified.
- Mass commands on many PCs without rehearsal.
- Any claim of file monitoring, application tracking, or browser monitoring.
- Any claim of remote mouse or keyboard control.
- Any claim of cloud, web, or mobile access.
- Any claim of predictive maintenance or automatic cooling.

---

# 9. Demonstration Summary Table

| FEATURE | WHAT I WILL DO | WHAT THE PANEL WILL SEE | SIMPLE EXPLANATION | RESULT |
|---|---|---|---|---|
| Teacher startup | Open Teacher Application | Main dashboard | Teacher side prepares the monitoring system | System becomes ready |
| Student connection | Open Student Agent | PC appears in dashboard | Student Agent gives PC information to teacher side | PC becomes visible |
| Student login | Enter prepared account | Student name and timer appear | System checks the account and starts a session | Usage is linked to a student |
| Dashboard | Select a PC | PC, user, status, and readings | Important information is shown in one view | Easier laboratory monitoring |
| Screen monitoring | Change Student PC window | Preview updates | Student Agent sends the current screen image | Teacher sees current activity |
| PC selection | Select target PC | Selected summary changes | Controls apply only to chosen PCs | Correct PC receives the action |
| Temporary Lock | Apply Temporary Lock | Session Paused screen | Student Agent receives a lock command | PC use is temporarily paused |
| Unlock | Click Unlock | Lock screen disappears | Temporary lock is removed | Session continues |
| Sign out lock | Apply Lock + Sign Out | Login is required again | Current student access is cleared | PC is ready for another login |
| Session extension | Add minutes | Timer increases | Teacher adds authorized time | Student receives more time |
| Messaging | Send and reply | Messages appear on both sides | Teacher and student communicate through the system | Direct instruction is possible |
| Teacher screen share | Click Share Screen | Teacher screen appears on Student PC | Teacher display is sent to connected students | Instructor can demonstrate lessons |
| Temperature | Show sensor | Temperature changes | ESP32 sends the sensor reading | Current temperature is visible |
| Fan monitoring | Show fan input | RPM changes | Fan pulses are converted to RPM | Fan activity is visible |
| Sensor disconnect | Stop ESP32 briefly | Sensor Stale appears | System notices that readings stopped | Sensor problem is visible |
| Client disconnect | Stop spare Student Agent | PC becomes Offline | System notices that PC updates stopped | Connection problem is visible |
| Session history | Open History | Saved session records | Local database keeps usage history | Past usage can be reviewed |
| Export | Export CSV or PDF | Report file is created | Visible records are saved as a report | Data can be presented or archived |
| Reservations | Open Reservations | Schedule and records appear | Instructor assigns a student to a PC and time | Scheduled PC use is supported |

---

# 10. One-Minute Backup Script

> “Ang system namin ay may Teacher Application, Student Agent, at ESP32 with sensors. Connected sila sa iisang local network.”
>
> “Dito sa Teacher Application, makikita natin ang connected PC, logged-in student, remaining time, computer status, screen preview, temperature, at fan RPM.”
>
> “Puwedeng piliin ng instructor ang PC at gumamit ng available controls tulad ng Temporary Lock, Unlock, session extension, at messaging.”
>
> “Ang ESP32 naman ang kumukuha ng temperature at fan readings at ipinapakita ang information sa same dashboard.”
>
> “Sine-save rin ng system ang student accounts, reservations, at session history locally. Sa kabuuan, pinagsasama nito ang computer monitoring at IoT monitoring sa isang application para mas organized ang laboratory management.”

---

# 11. Final Presenter Reminders

1. Ipakita muna ang feature bago mag-explain.
2. Sabihin muna ang purpose bago ang simple background explanation.
3. Gumamit ng isang prepared Student PC para malinaw ang main demo.
4. Huwag madaliin ang screen; hintaying makita ng panel ang result.
5. Huwag magbanggit ng programming terms kung hindi tinatanong.
6. Kapag may delay, sabihin: “Hinihintay lang po natin ang latest update from the connected device.”
7. Kapag may feature na hindi gumana, bumalik sa dashboard at gamitin ang prepared fallback record.
8. Huwag i-overclaim ang system.
9. Gumamit ng “monitoring,” “status,” “information,” at “control” instead of implementation terms.
10. Tapusin sa benefit: mas centralized, visible, at organized ang laboratory management.
