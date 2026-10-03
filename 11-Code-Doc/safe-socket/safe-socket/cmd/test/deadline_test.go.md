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
Automatically generated mirror for `safe-socket/cmd/test/deadline_test.go`.

> **Essential Process**:
> Integration tests verifying deadline timeout enforcement across server-accepted connections and client write operations.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.Close]] (method: calls)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.SetIdleTimeout]] (method: calls)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.SetReadDeadline]] (method: calls)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.Write]] (method: calls)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|identity_test.go]] (same_package)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|CreateSocket]] (function: calls) — *Useful for connection pools or when deferred connection is required.*
- [[safe-socket/safe-socket/src/factory/socket_factory_test.go.md|socket_factory_test.go]] (imports)
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger.Error]] (method: calls)
- [[safe-socket/safe-socket/src/models/socket_config.go.md|socket_config.go]] (imports)
- [[safe-socket/safe-socket/src/profiles/tcp_server_profile.go.md|NewTcpServerProfile]] (function: calls) — *NewTcpServerProfile creates a new instance of a TCP server profile without a protocol.*
- [[safe-socket/safe-socket/src/profiles/tcp_server_profile.go.md|tcp_server_profile.go]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/test/deadline_test.go.md|TestClientDynamicDeadline]] (function: belongs_to) — *TestClientDynamicDeadline verifies client can set deadlines dynamically.*
- [[safe-socket/safe-socket/cmd/test/deadline_test.go.md|TestIdleTimeoutRefresh]] (function: belongs_to) — *TestIdleTimeoutRefresh verifies that sending/receiving data refreshes the deadline.*
- [[safe-socket/safe-socket/cmd/test/deadline_test.go.md|TestServerConfigDeadline]] (function: belongs_to) — *enforces a timeout on the accepted connection.*
<!-- SYNC:END -->
