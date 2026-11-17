# Hi, I'm Rod Toledo 👋

**Senior Software Engineer · I automate the slow parts of software work with AI agents.**<br>
Philippines, remote (UTC+8) · 7 years in production · Java / Spring Boot · Angular · AWS

At work I chained our delivery process into one agent pipeline, from ticket to tested merge request.
Each stage has to prove its work before the next one starts, and engineers approve what ships:

| Stage | What the agent does | How it proves it |
|---|---|---|
| **Development** | Reads the ticket and codebase, plans, implements on its own branch | Must build before handing over |
| **Self-verifying loop** | Runs the build and tests, reads failures, fixes, runs again | Exits only on a green build |
| **Code review** | First review pass against team conventions | Findings fixed before a person reviews |
| **Git processing** | Branch, commits, rebase, merge request linked to the ticket | CI passes · an engineer approves |
| **Test cases in Zephyr** | Turns acceptance criteria into test cases | Every criterion has a test case |
| **Test execution** | Runs the cases, records results and evidence in Zephyr | Failures go back into the loop |

**Agents:** Claude Code · Codex · DeepSeek · Hermes · tool calling · agent skills · scheduled agents<br>
**Engineering:** Java · Spring Boot · Python · Angular · React · TypeScript · PostgreSQL · AWS · Docker · GitLab CI · GitHub Actions

---

## Featured work

### [Money Map](https://github.com/light691/money-map): a budget you talk to
Message it in Telegram and get a card back, built from your own numbers.<br>
**How it works:** plain words → the agent picks one fixed command → a Python engine over SQLite does the maths → headless Chromium renders the card.

<a href="https://github.com/light691/money-map"><img src="https://github.com/light691/money-map/raw/main/docs/screenshots/how-it-works.png" alt="Three sample chats with Money Map: checking the pay period, asking if a purchase fits, and a morning brief with a payment receipt" width="100%"></a>

`Python` `SQLite` `LLM agents` `Telegram` `Headless Chromium` `systemd`

---

### [raster-to-svg](https://github.com/light691/raster-to-svg): logos back to clean vectors
An agent skill for Claude Code, Gemini CLI and Codex that rebuilds raster logos and emblems as SVG.<br>
**How it works:** raster in → the agent traces and rebuilds shapes → Playwright renders the SVG and compares it to the source → corrections until they match. A self-verifying loop.

<a href="https://github.com/light691/raster-to-svg"><img src="https://github.com/light691/raster-to-svg/raw/main/docs/examples/stretch-gillam-before-after.png" alt="Original raster logo beside the reconstructed SVG" width="49%"></a>
<a href="https://github.com/light691/raster-to-svg"><img src="https://github.com/light691/raster-to-svg/raw/main/docs/examples/apple-before-after.png" alt="Gold apple emblem: raster source beside vector reconstruction" width="49%"></a>

`Python` `Playwright` `Agent skills` `GitHub Actions`

---

### [pickleOps-v2](https://github.com/light691/pickleOps-v2): running a pickleball venue
Bookings, Open Play sessions, payments and reports for a Philippine venue.<br>
**How it works:** pick a court and time in the booking drawer → the server rejects overlaps → the booking appears on the live Today board → payments roll into reports.

<a href="https://github.com/light691/pickleOps-v2"><img src="https://github.com/light691/pickleOps-v2/raw/master/docs/screenshots/booking-drawer.png" alt="pickleOps booking drawer: choosing court, time and player" width="49%"></a>
<a href="https://github.com/light691/pickleOps-v2"><img src="https://github.com/light691/pickleOps-v2/raw/master/docs/screenshots/today.png" alt="pickleOps Today board with live court status" width="49%"></a>

`React` `TypeScript` `Hono` `SQLite` `node:test` `Playwright`

---

## Recently shipped
<!-- shipped:start -->
- **[money-map](https://github.com/light691/money-map)** · [v0.1.0](https://github.com/light691/money-map/releases/tag/v0.1.0) · Nov 17, 2026: [Money Map: agent-first budget app](https://github.com/light691/money-map/commit/249e8f19bdda907c1ffb2217cc90eca54f39a3d0)
- **[pickleOps-v2](https://github.com/light691/pickleOps-v2)** · Nov 17, 2026: [Add app screenshots to README](https://github.com/light691/pickleOps-v2/commit/f7b6dcbce3c2771c10fd25bb944781624784c0bd)
- **[raster-to-svg](https://github.com/light691/raster-to-svg)** · [v1.0.0](https://github.com/light691/raster-to-svg/releases/tag/v1.0.0) · Nov 16, 2026: [Add before-and-after gallery with correction close-ups](https://github.com/light691/raster-to-svg/commit/f9937eca1563b8314283b9b137e9e1de521edd2c)
<!-- shipped:end -->
<sub>Updated daily by a GitHub Action in this repo.</sub>

🌐 [rodchristoledo.work](https://www.rodchristoledo.work) · 💼 Open to remote part-time or contract work: agent automation, backend and full-stack
