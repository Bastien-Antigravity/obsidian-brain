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

## 📝 Description
Automatically generated mirror for `tele-remote/src/telegram/ui/menus.go`.

> **Essential Process**:
> Handles atomic dynamic menu registration, Reply Keyboard rendering, 2-step emergency command confirmations, scoped pending-input routing, and direct button action dispatch.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[tele-remote/tele-remote/src/interfaces/subscriber.go.md|subscriber.go]] (imports)
- [[tele-remote/tele-remote/src/models/ui_types.go.md|ui_types.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|GetConvKey]] (function: calls) — *falling back to UserID: 0 when c.Sender() is nil.*
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Error]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Info]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Warning]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher.PublishCommand]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher.RequestRefresh]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|fakeUIContext.Send]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|fakeUIContext.Text]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|menus_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/routes/routes.go.md|routes.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|HandleDynamicText]] (function: belongs_to) — *HandleDynamicText routes text messages from Reply buttons and user prompts back to actions.*
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|OnComponentConnected]] (function: belongs_to) — *never wipe out an existing valid component session.*
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|RenderMenu]] (function: belongs_to) — *RenderMenu builds and displays a CommandMenu as a Reply Keyboard.*
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|RequestEmergencyConfirmation]] (function: belongs_to) — *RequestEmergencyConfirmation initiates a 2-step confirmation workflow for CmdPowerOff or CmdStop.*
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|ShowMainMenu]] (function: belongs_to) — *ShowMainMenu displays the dynamic top-level menu.*
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|clonePath]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|commandTimeout]] (constant: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|emergencyConfirmTTL]] (constant: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|executeButtonAction]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|executeEmergencyBroadcast]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|findButtonInMenu]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|getConvKey]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|getMenuByPath]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|parseButton]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|parseMenuRow]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|pendingInputTTL]] (constant: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|menus_test.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|menus_test.go]] (same_package)
<!-- SYNC:END -->
