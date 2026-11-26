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
- [[flexible-logger/src/engine/log_engine_test.go.md|log_engine_test.go]] (imports)
- [[flexible-logger/src/factory/factory_test.go.md|DummySink.Close]] (method: defines_method)
- [[flexible-logger/src/factory/factory_test.go.md|DummySink.Write]] (method: defines_method)
- [[flexible-logger/src/factory/logger_factory.go.md|CreateLogEngine]] (function: calls) — *CreateLogEngine creates a new fully configured LogEngine instance.*
- [[flexible-logger/src/factory/logger_factory.go.md|logger_factory.go]] (same_package)
- [[flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)

### 🔌 Consumers (Inbound)
- [[flexible-logger/src/factory/factory_test.go.md|DummySink.Close]] (method: belongs_to)
- [[flexible-logger/src/factory/factory_test.go.md|DummySink.Write]] (method: belongs_to)
- [[flexible-logger/src/factory/factory_test.go.md|DummySink]] (struct: belongs_to)
- [[flexible-logger/src/factory/factory_test.go.md|DummySink]] (struct: defines_method)
- [[flexible-logger/src/factory/factory_test.go.md|TestCreateLogEngine_PopulatesMetadata]] (function: belongs_to)
<!-- SYNC:END -->
