---
microservice: universal-logger
type: note
status: active
tags:
- '#service/universal-logger'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/src/interfaces/models.go.md|models.go]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/cmd/universal-logger/main.go.md|main.go]] (calls)
- [[universal-logger/src/bootstrap/unilog.go.md|unilog.go]] (calls)
- [[universal-logger/src/utils/levels.go.md|GetLogLevel]] (function: belongs_to) — *GetLogLevel converts string to Level.*
- [[universal-logger/src/utils/levels.go.md|LevelCritical]] (constant: belongs_to)
- [[universal-logger/src/utils/levels.go.md|LevelDebug]] (constant: belongs_to)
- [[universal-logger/src/utils/levels.go.md|LevelError]] (constant: belongs_to)
- [[universal-logger/src/utils/levels.go.md|LevelInfo]] (constant: belongs_to)
- [[universal-logger/src/utils/levels.go.md|LevelLogon]] (constant: belongs_to)
- [[universal-logger/src/utils/levels.go.md|LevelLogout]] (constant: belongs_to)
- [[universal-logger/src/utils/levels.go.md|LevelNotSet]] (constant: belongs_to)
- [[universal-logger/src/utils/levels.go.md|LevelReport]] (constant: belongs_to)
- [[universal-logger/src/utils/levels.go.md|LevelSchedule]] (constant: belongs_to)
- [[universal-logger/src/utils/levels.go.md|LevelStream]] (constant: belongs_to)
- [[universal-logger/src/utils/levels.go.md|LevelTrade]] (constant: belongs_to)
- [[universal-logger/src/utils/levels.go.md|LevelWarning]] (constant: belongs_to)
<!-- SYNC:END -->
