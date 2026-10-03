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
- [[flexible-logger/flexible-logger/src/engine/log_engine.go.md|LogEngine.Info]] (method: calls)
- [[flexible-logger/flexible-logger/src/profiles/audit.go.md|audit.go]] (imports)
- [[flexible-logger/flexible-logger/src/profiles/high_perf.go.md|NewHighPerfLogger]] (function: calls) — *- Notif (Async)*
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|NewNoLockLogger]] (function: calls) — *- Notif (Async)*
- [[flexible-logger/flexible-logger/src/test_utils/mock_server.go.md|StartMockServer]] (function: calls) — *It returns the assigned address (host:port) and a cleanup function to stop the server.*
- [[flexible-logger/flexible-logger/src/test_utils/mock_server.go.md|mock_server.go]] (imports)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/cmd/test-log-server/connection_test.go.md|BenchmarkLogServerThroughput]] (function: belongs_to)
- [[flexible-logger/flexible-logger/cmd/test-log-server/connection_test.go.md|TestLogServerConnection]] (function: belongs_to)
<!-- SYNC:END -->
