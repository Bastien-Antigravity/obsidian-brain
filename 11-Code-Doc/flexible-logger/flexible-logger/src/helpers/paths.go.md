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
- [[flexible-logger/flexible-logger/src/helpers/paths.go.md|GetDefaultLogPath]] (function: belongs_to) — *GetDefaultLogPath returns the default log path using the executable name.*
- [[flexible-logger/flexible-logger/src/helpers/paths.go.md|GetLogPath]] (function: belongs_to) — *If name is empty, it falls back to the executable name.*
- [[flexible-logger/flexible-logger/src/helpers/paths.go.md|getCallerDir]] (function: belongs_to) — *This provides an extremely robust anchor for 'go run' where os.Executable is in /tmp/.*
- [[flexible-logger/flexible-logger/src/helpers/paths_test.go.md|paths_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/helpers/paths_test.go.md|paths_test.go]] (same_package)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/devel.go.md|devel.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/devel.go.md|devel.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|notif_logger.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|notif_logger.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (imports)
<!-- SYNC:END -->
