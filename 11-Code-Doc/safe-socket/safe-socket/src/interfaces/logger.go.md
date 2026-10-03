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

## 📝 Description
Automatically generated mirror for `safe-socket/src/interfaces/logger.go`.

> **Essential Process**:
> Defines the universal logging interface contract for safe-socket components, decoupling transport, facade, and protocol logging from concrete logger backends.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger.Close]] (method: defines_method)
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger.Critical]] (method: defines_method)
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger.Debug]] (method: defines_method)
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger.Error]] (method: defines_method)
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger.Info]] (method: defines_method)
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger.Warning]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|main.go]] (calls)
- [[safe-socket/safe-socket/cmd/test/deadline_test.go.md|deadline_test.go]] (calls)
- [[safe-socket/safe-socket/safesock/rust/src/lib.rs.md|lib.rs]] (calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (calls)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (calls)
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|EnsureSafeLogger]] (function: belongs_to) — *In strict mode (STRICT_LOGGER=true), it panics immediately.*
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|Logger]] (interface: belongs_to) — *Logger is the main interface for logging*
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger.Close]] (method: belongs_to)
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger.Critical]] (method: belongs_to)
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger.Debug]] (method: belongs_to)
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger.Error]] (method: belongs_to)
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger.Info]] (method: belongs_to)
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger.Warning]] (method: belongs_to)
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger]] (struct: defines_method)
- [[safe-socket/safe-socket/src/interfaces/logger_test.go.md|logger_test.go]] (calls)
- [[safe-socket/safe-socket/src/interfaces/logger_test.go.md|logger_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/oom_test.go.md|oom_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/zombie_test.go.md|zombie_test.go]] (calls)
<!-- SYNC:END -->
