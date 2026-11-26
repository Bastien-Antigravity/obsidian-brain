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
- [[universal-logger/src/utils/logger_utils.go.md|LogWithMetadata]] (function: calls) — *It delegates directly to LogWithCaller on the Logger interface for maximum performance.*
- [[universal-logger/src/utils/notif_message.go.md|notif_message.go]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/src/cgo_bridge/logger.go.md|UniLog_AddMetadata]] (function: belongs_to) — *export UniLog_AddMetadata*
- [[universal-logger/src/cgo_bridge/logger.go.md|UniLog_Flush]] (function: belongs_to) — *export UniLog_Flush*
- [[universal-logger/src/cgo_bridge/logger.go.md|UniLog_GetLevel]] (function: belongs_to) — *export UniLog_GetLevel*
- [[universal-logger/src/cgo_bridge/logger.go.md|UniLog_LogWithMetadata]] (function: belongs_to) — *export UniLog_LogWithMetadata*
- [[universal-logger/src/cgo_bridge/logger.go.md|UniLog_SetLevel]] (function: belongs_to) — *export UniLog_SetLevel*
- [[universal-logger/src/cgo_bridge/logger.go.md|UniLog_SetMetadata]] (function: belongs_to) — *export UniLog_SetMetadata*
- [[universal-logger/unilog/cpp/UniversalLogger.hpp.md|UniversalLogger.hpp]] (calls)
- [[universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (calls)
- [[universal-logger/unilog/rust/src/lib.rs.md|lib.rs]] (calls)
<!-- SYNC:END -->
