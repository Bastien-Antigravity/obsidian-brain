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
Automatically generated mirror for `safe-socket/src/factory/socket_factory_test.go`.

> **Essential Process**:
> Unit tests verifying factory configuration resolution and timeout handling.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|CreateWithConfig]] (function: calls) — *- autoConnect: if true, automatically calls Open() / Listen()*
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|Create]] (function: calls) — *An interfaces.Socket which can be used to Send/Receive (Client) or Accept (Server).*
- [[safe-socket/safe-socket/src/factory/socket_factory.go.md|socket_factory.go]] (same_package)
- [[safe-socket/safe-socket/src/models/socket_config.go.md|socket_config.go]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/test/deadline_test.go.md|deadline_test.go]] (imports)
- [[safe-socket/safe-socket/cmd/test/factory_test.go.md|factory_test.go]] (imports)
- [[safe-socket/safe-socket/cmd/test/heartbeat_audit_test.go.md|heartbeat_audit_test.go]] (imports)
- [[safe-socket/safe-socket/cmd/test/scenario_test.go.md|scenario_test.go]] (imports)
- [[safe-socket/safe-socket/cmd/test/stress_test.go.md|stress_test.go]] (imports)
- [[safe-socket/safe-socket/safe_socket.go.md|safe_socket.go]] (imports)
- [[safe-socket/safe-socket/src/factory/socket_factory_test.go.md|TestAutoHelloProfile_LocalVsRemote]] (function: belongs_to)
- [[safe-socket/safe-socket/src/factory/socket_factory_test.go.md|TestRegression_IgnoreEnvOverrides]] (function: belongs_to)
<!-- SYNC:END -->
