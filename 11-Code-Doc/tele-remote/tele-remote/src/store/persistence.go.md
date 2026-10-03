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
- [[tele-remote/tele-remote/src/models/ui_types.go.md|ui_types.go]] (imports)
- [[tele-remote/tele-remote/src/store/persistence.go.md|PersistenceManager.Load]] (method: defines_method) — *Load reads the state from disk*
- [[tele-remote/tele-remote/src/store/persistence.go.md|PersistenceManager.Save]] (method: defines_method) — *Save writes the current state to disk*

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/src/store/persistence.go.md|NewPersistenceManager]] (function: belongs_to) — *NewPersistenceManager creates a new manager with a target file path*
- [[tele-remote/tele-remote/src/store/persistence.go.md|PersistenceManager.Load]] (method: belongs_to) — *Load reads the state from disk*
- [[tele-remote/tele-remote/src/store/persistence.go.md|PersistenceManager.Save]] (method: belongs_to) — *Save writes the current state to disk*
- [[tele-remote/tele-remote/src/store/persistence.go.md|PersistenceManager]] (struct: belongs_to) — *Save writes the current state to disk*
- [[tele-remote/tele-remote/src/store/persistence.go.md|PersistenceManager]] (struct: defines_method) — *Save writes the current state to disk*
<!-- SYNC:END -->
