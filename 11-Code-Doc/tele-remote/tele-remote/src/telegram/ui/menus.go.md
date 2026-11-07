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
- [[tele-remote/tele-remote/src/interfaces/subscriber.go.md|subscriber.go]] (imports)
- [[tele-remote/tele-remote/src/models/ui_types.go.md|ui_types.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Send]] (method: calls) — *Send wraps tb.Context.Send to intercept and log all outgoing responses*
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Error]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Info]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Warning]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher.PublishCommand]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher.RequestRefresh]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|menus_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/routes/routes.go.md|routes.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|HandleDynamicText]] (function: belongs_to) — *HandleDynamicText routes text messages from Reply buttons back to actions*
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|OnComponentConnected]] (function: belongs_to) — *OnComponentConnected is triggered when a client connects via gRPC or NATS*
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|RenderMenu]] (function: belongs_to) — *RenderMenu builds and displays a CommandMenu as a Reply Keyboard*
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|ShowMainMenu]] (function: belongs_to) — *ShowMainMenu displays the dynamic top-level menu*
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|createCommandAction]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|findButtonByLabel]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|findButtonInMenu]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|getMenuByPath]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|parseButton]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|parseMenuRow]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|registerAction]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|menus_test.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|menus_test.go]] (same_package)
<!-- SYNC:END -->
