# Hi, I'm Rod Toledo 👋

**Software Engineer · Java / Spring Boot · Angular · AWS**, Philippines (remote, UTC+8)

4+ years shipping and running production systems: cargo booking and tracking platforms used by
airlines and freight forwarders. Microservices, APIs, incident response, performance under real load.

- 🔧 **Now:** Software Engineer at CHAMP Cargosystems, on Java Spring Boot microservices and Angular
- 🛒 **Before:** Salesforce Commerce Cloud ↔ Marketplacer integrations at Accenture; AWS Lambda automation at Civicom
- 🤖 **On the side:** AI agents that do real work, and offline-first apps for small businesses
- 💼 **Open to:** remote part-time or contract backend and full-stack work

**Stack:** Java · Spring Boot · Node.js · Python · Angular · React · TypeScript · PostgreSQL · MySQL · MongoDB · SQLite · AWS · Docker · GitHub Actions

---

## Featured work

### [Money Map](https://github.com/light691/money-map): a budget you talk to
Message it in Telegram and get a card back, built from your own numbers.<br>
**How it works:** plain words → the AI agent picks one command → a Python engine over SQLite does the maths → headless Chromium renders the card.

<a href="https://github.com/light691/money-map"><img src="https://github.com/light691/money-map/raw/main/docs/screenshots/how-it-works.png" alt="Three sample chats with Money Map: checking the pay period, asking if a purchase fits, and a morning brief with a payment receipt" width="100%"></a>

`Python` `SQLite` `LLM agents` `Telegram` `Headless Chromium` `systemd`

---

### [pickleOps-v2](https://github.com/light691/pickleOps-v2): running a pickleball venue
Bookings, Open Play sessions, payments and reports for a Philippine venue.<br>
**How it works:** pick a court and time in the booking drawer → the server rejects overlaps → the booking appears on the live Today board → payments roll into reports.

<a href="https://github.com/light691/pickleOps-v2"><img src="https://github.com/light691/pickleOps-v2/raw/master/docs/screenshots/booking-drawer.png" alt="pickleOps booking drawer: choosing court, time and player" width="49%"></a>
<a href="https://github.com/light691/pickleOps-v2"><img src="https://github.com/light691/pickleOps-v2/raw/master/docs/screenshots/today.png" alt="pickleOps Today board with live court status" width="49%"></a>

`React` `TypeScript` `Hono` `SQLite` `node:test` `Playwright`

---

### [raster-to-svg](https://github.com/light691/raster-to-svg): logos back to clean vectors
An agent skill for Claude Code, Gemini CLI and Codex that rebuilds raster logos and emblems as SVG.<br>
**How it works:** raster in → the agent traces and rebuilds shapes → Playwright renders the SVG and compares it to the source → corrections until they match.

<a href="https://github.com/light691/raster-to-svg"><img src="https://github.com/light691/raster-to-svg/raw/main/docs/examples/stretch-gillam-before-after.png" alt="Original raster logo beside the reconstructed SVG" width="49%"></a>
<a href="https://github.com/light691/raster-to-svg"><img src="https://github.com/light691/raster-to-svg/raw/main/docs/examples/apple-before-after.png" alt="Gold apple emblem: raster source beside vector reconstruction" width="49%"></a>

`Python` `Playwright` `GitHub Actions`

---

### [bentaGo](https://github.com/light691/bentaGo): offline point of sale for a sari-sari store
A Windows POS that never needs internet. Each day is the accounting unit: open the register, sell, then count the drawer.<br>
**How it works:** every sale prints an 80 mm receipt → the day close compares expected cash with counted cash → a closed day locks, and reopening needs a reason and an approver.

```text
            ALING NENA SARI-SARI                 DAY CLOSE · Nov 17
       Purok 3, Brgy. San Isidro                 ----------------------------
------------------------------------------      Opening float     ₱1,000.00
Lucky Me Pancit Canton   3 x 15.00   45.00      Cash sales        ₱8,415.50
Coke 1.5L                1 x 78.00   78.00      Utang pay-downs     ₱650.00
Kopiko 3in1 (10s)        1 x 62.00   62.00      Expected          ₱10,065.50
------------------------------------------      Counted           ₱10,065.50
TOTAL                               185.00      ----------------------------
CASH                                200.00      BALANCED            ✓ locked
CHANGE                               15.00
```
<sub>Illustration of the 42-column receipt and day-close formats, not a screenshot.</sub>

`C#` `.NET 10` `WPF` `EF Core` `SQLite` `400+ tests`

---

🌐 [rodchristoledo.work](https://rodchristoledo.work)
