---
microservice: tele-remote
type: note
status: active
tags:
- '#service/tele-remote'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[tele-remote/tele-remote/src/models/ui_types.go.md|ui_types.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Send]] (method: calls) — *Send wraps tb.Context.Send to intercept and log all outgoing responses*
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|HandleDynamicText]] (function: calls) — *HandleDynamicText routes text messages from Reply buttons back to actions*
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|ShowMainMenu]] (function: calls) — *ShowMainMenu displays the dynamic top-level menu*
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Info]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher.PublishCommand]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|menus_test.go]] (imports)

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main.go]] (calls)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/routes/routes.go.md|SetupRoutes]] (function: belongs_to) — *SetupRoutes initializes all static handlers and maps fallback dynamic routing*
<!-- SYNC:END -->
