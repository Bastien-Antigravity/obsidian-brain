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
Automatically generated mirror for `tele-remote/src/models/ui_types.go`.

> **Essential Process**:
> Defines the in-memory UI menu tree models, conversation scoping keys, and pending interactive state structures for Tele-Remote.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[tele-remote/src/models/ui_types.go.md|BtnCancel]] (constant: belongs_to)
- [[tele-remote/src/models/ui_types.go.md|BtnCloseAll]] (constant: belongs_to)
- [[tele-remote/src/models/ui_types.go.md|BtnConfirmCloseAll]] (constant: belongs_to)
- [[tele-remote/src/models/ui_types.go.md|BtnConfirmPowerOff]] (constant: belongs_to)
- [[tele-remote/src/models/ui_types.go.md|BtnPowerOff]] (constant: belongs_to)
- [[tele-remote/src/models/ui_types.go.md|CmdPowerOff]] (constant: belongs_to)
- [[tele-remote/src/models/ui_types.go.md|CmdStop]] (constant: belongs_to)
- [[tele-remote/src/models/ui_types.go.md|CommandButton]] (struct: belongs_to) — *CommandButton represents a single button in a row*
- [[tele-remote/src/models/ui_types.go.md|CommandMenu]] (struct: belongs_to) — *CommandMenu represents a structured Telegram keyboard mapping*
- [[tele-remote/src/models/ui_types.go.md|CommandRow]] (struct: belongs_to) — *CommandRow represents a single row of buttons in a menu*
- [[tele-remote/src/models/ui_types.go.md|ComponentMenu]] (struct: belongs_to) — *ComponentMenu holds the structured tree for a single registered component*
- [[tele-remote/src/models/ui_types.go.md|ConversationKey]] (struct: belongs_to) — *ConversationKey scopes user navigation, pending inputs, and confirmations by chat and sender*
- [[tele-remote/src/models/ui_types.go.md|PendingConfirmation]] (struct: belongs_to) — *PendingConfirmation tracks a 2-step confirmation gate for critical fleet commands*
- [[tele-remote/src/models/ui_types.go.md|PendingInput]] (struct: belongs_to) — *PendingInput tracks an in-flight text prompt bound to the originating component*
- [[tele-remote/src/telegram/core/bot.go.md|bot.go]] (imports)
- [[tele-remote/src/telegram/routes/routes.go.md|routes.go]] (imports)
- [[tele-remote/src/telegram/ui/menus.go.md|menus.go]] (imports)
- [[tele-remote/src/telegram/ui/menus_test.go.md|menus_test.go]] (imports)
<!-- SYNC:END -->
