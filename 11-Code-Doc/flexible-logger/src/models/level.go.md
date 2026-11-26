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
- [[flexible-logger/src/models/level.go.md|Level.String]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[flexible-logger/cmd/test-log-server/connection_test.go.md|connection_test.go]] (calls)
- [[flexible-logger/src/engine/log_engine.go.md|log_engine.go]] (calls)
- [[flexible-logger/src/error_handler/error_handler_test.go.md|error_handler_test.go]] (calls)
- [[flexible-logger/src/models/level.go.md|Level.String]] (method: belongs_to)
- [[flexible-logger/src/models/level.go.md|LevelCritical]] (constant: belongs_to)
- [[flexible-logger/src/models/level.go.md|LevelDebug]] (constant: belongs_to)
- [[flexible-logger/src/models/level.go.md|LevelError]] (constant: belongs_to)
- [[flexible-logger/src/models/level.go.md|LevelInfo]] (constant: belongs_to)
- [[flexible-logger/src/models/level.go.md|LevelLogon]] (constant: belongs_to)
- [[flexible-logger/src/models/level.go.md|LevelLogout]] (constant: belongs_to)
- [[flexible-logger/src/models/level.go.md|LevelNotSet]] (constant: belongs_to)
- [[flexible-logger/src/models/level.go.md|LevelReport]] (constant: belongs_to)
- [[flexible-logger/src/models/level.go.md|LevelSchedule]] (constant: belongs_to)
- [[flexible-logger/src/models/level.go.md|LevelStream]] (constant: belongs_to)
- [[flexible-logger/src/models/level.go.md|LevelTrade]] (constant: belongs_to)
- [[flexible-logger/src/models/level.go.md|LevelWarning]] (constant: belongs_to)
- [[flexible-logger/src/models/level.go.md|Level]] (struct: belongs_to) — *Level defines log levels*
- [[flexible-logger/src/models/level.go.md|Level]] (struct: defines_method) — *Level defines log levels*
- [[flexible-logger/src/models/level.go.md|ParseLevel]] (function: belongs_to)
- [[flexible-logger/src/models/level_test.go.md|level_test.go]] (calls)
- [[flexible-logger/src/models/level_test.go.md|level_test.go]] (same_package)
- [[flexible-logger/src/profiles/profiles_test.go.md|profiles_test.go]] (calls)
- [[flexible-logger/src/serializers/serializer_test.go.md|serializer_test.go]] (calls)
- [[flexible-logger/src/serializers/text_serializer.go.md|text_serializer.go]] (calls)
- [[flexible-logger/src/sink/async.go.md|async.go]] (calls)
- [[flexible-logger/src/sink/sink_test.go.md|sink_test.go]] (calls)
- [[flexible-logger/src/test_utils/mock_server.go.md|mock_server.go]] (calls)
<!-- SYNC:END -->
