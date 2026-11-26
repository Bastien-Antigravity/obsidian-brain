---
microservice: flexible-logger
type: note
status: active
tags:
- '#service/flexible-logger'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/src/helpers/paths.go.md|GetDefaultLogPath]] (function: calls) — *GetDefaultLogPath returns the default log path using the executable name.*
- [[flexible-logger/src/helpers/paths.go.md|paths.go]] (same_package)
- [[flexible-logger/src/helpers/paths.go.md|resolveLogDir]] (function: calls)

### 🔌 Consumers (Inbound)
- [[flexible-logger/src/helpers/paths_test.go.md|TestGetDefaultLogPath]] (function: belongs_to)
- [[flexible-logger/src/helpers/paths_test.go.md|TestResolveLogDir]] (function: belongs_to)
<!-- SYNC:END -->
