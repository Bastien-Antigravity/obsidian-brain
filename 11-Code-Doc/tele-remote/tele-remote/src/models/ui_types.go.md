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

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/src/models/ui_types.go.md|CallbackAction]] (struct: belongs_to) — *CallbackAction defines the function signature for an inline button trigger*
- [[tele-remote/tele-remote/src/models/ui_types.go.md|CmdPowerOff]] (constant: belongs_to)
- [[tele-remote/tele-remote/src/models/ui_types.go.md|CmdStop]] (constant: belongs_to)
- [[tele-remote/tele-remote/src/models/ui_types.go.md|CommandButton]] (struct: belongs_to) — *CommandButton represents a single button in a row*
- [[tele-remote/tele-remote/src/models/ui_types.go.md|CommandMenu]] (struct: belongs_to) — *CommandMenu represents a structured Telegram keyboard mapping*
- [[tele-remote/tele-remote/src/models/ui_types.go.md|CommandRow]] (struct: belongs_to) — *CommandRow represents a single row of buttons in a menu*
- [[tele-remote/tele-remote/src/models/ui_types.go.md|ComponentMenu]] (struct: belongs_to) — *ComponentMenu holds the structured tree for a single registered component*
- [[tele-remote/tele-remote/src/store/persistence.go.md|persistence.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|bot.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/routes/routes.go.md|routes.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|menus.go]] (imports)
<!-- SYNC:END -->
