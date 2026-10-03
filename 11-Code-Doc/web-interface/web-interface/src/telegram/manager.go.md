---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `web-interface/src/telegram/manager.go`.

> **Essential Process**:
> Manages the telegram bot integration and interactive control menu for the web-interface microservice.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/core/controller.go.md|controller.go]] (imports)
- [[web-interface/web-interface/src/telegram/manager.go.md|MenuManager.BuildMenu]] (method: defines_method) — *BuildMenu dynamically updates actions with custom callbacks for the Telegram bot*

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (imports)
- [[web-interface/web-interface/src/telegram/manager.go.md|MenuManager.BuildMenu]] (method: belongs_to) — *BuildMenu dynamically updates actions with custom callbacks for the Telegram bot*
- [[web-interface/web-interface/src/telegram/manager.go.md|MenuManager]] (struct: belongs_to) — *BuildMenu dynamically updates actions with custom callbacks for the Telegram bot*
- [[web-interface/web-interface/src/telegram/manager.go.md|MenuManager]] (struct: defines_method) — *BuildMenu dynamically updates actions with custom callbacks for the Telegram bot*
- [[web-interface/web-interface/src/telegram/manager.go.md|NewMenuManager]] (function: belongs_to) — *NewMenuManager creates a new MenuManager*
- [[web-interface/web-interface/src/telegram/manager.go.md|elegram(appCo]] (function: belongs_to) — *SetupTelegram initializes the Tele-Remote client, registers callbacks, and hooks into lifecycle*
<!-- SYNC:END -->
