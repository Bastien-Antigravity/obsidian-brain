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
- [[universal-logger/src/bootstrap/unilog.go.md|Init]] (function: calls) — *existingConfig: OPTIONAL. If provided, the logger will use this configuration instance instead of creating a new one.*
- [[universal-logger/src/bootstrap/unilog_test.go.md|unilog_test.go]] (imports)
- [[universal-logger/src/config/config_handler.go.md|config_handler.go]] (imports)
- [[universal-logger/src/interfaces/models.go.md|models.go]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/src/cgo_bridge/distconf_bridge.go.md|distconf_bridge.go]] (calls)
- [[universal-logger/src/cgo_bridge/distconf_bridge.go.md|distconf_bridge.go]] (same_package)
- [[universal-logger/src/cgo_bridge/initialize.go.md|FacadeSession]] (struct: belongs_to) — *FacadeSession holds the state for a single library instantiation.*
- [[universal-logger/src/cgo_bridge/initialize.go.md|UniLog_Close]] (function: belongs_to) — *export UniLog_Close*
- [[universal-logger/src/cgo_bridge/initialize.go.md|UniLog_Init]] (function: belongs_to) — *export UniLog_Init*
- [[universal-logger/src/cgo_bridge/initialize.go.md|main]] (function: belongs_to)
- [[universal-logger/src/cgo_bridge/initialize.go.md|sanitizeFFIString]] (function: belongs_to) — *sanitizeFFIString cleans C strings coming across the frontier*
- [[universal-logger/unilog/cpp/UniversalLogger.hpp.md|UniversalLogger.hpp]] (calls)
- [[universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (calls)
- [[universal-logger/unilog/rust/src/lib.rs.md|lib.rs]] (calls)
<!-- SYNC:END -->
