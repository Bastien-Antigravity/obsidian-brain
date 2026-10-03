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
- [[universal-logger/universal-logger/src/interfaces/models.go.md|models.go]] (imports)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|logger_utils_test.go]] (same_package)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.LogWithCaller]] (method: calls)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/bootstrap/integration_test.go.md|integration_test.go]] (calls)
- [[universal-logger/universal-logger/src/cgo_bridge/logger.go.md|logger.go]] (calls)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|logger_handler_test.go]] (calls)
- [[universal-logger/universal-logger/src/utils/logger_utils.go.md|GetUnderlyingLogger]] (function: belongs_to) — *GetUnderlyingLogger is a helper to access the raw interface (maintained for compatibility/utility).*
- [[universal-logger/universal-logger/src/utils/logger_utils.go.md|LogWithMetadata]] (function: belongs_to) — *It delegates directly to LogWithCaller on the Logger interface for maximum performance.*
- [[universal-logger/universal-logger/src/utils/logger_utils.go.md|Log]] (function: belongs_to) — *Log logs a message at a specific level using the provided logger.*
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|logger_utils_test.go]] (calls)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|logger_utils_test.go]] (same_package)
<!-- SYNC:END -->
