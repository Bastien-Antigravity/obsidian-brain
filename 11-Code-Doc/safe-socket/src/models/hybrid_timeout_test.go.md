---
source: safe-socket/src/models/hybrid_timeout_test.go
workspace: safe-socket
type: code-mirror
status: auto-generated
last_sync: 2026-11-26T19:45:07.083391
---

# Mirror: hybrid_timeout_test.go

## 📝 Description
Automatically generated mirror for `safe-socket/src/models/hybrid_timeout_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/src/models/hybrid_timeout.go.md|NewHybridSocketConfig]] (function: calls) — *and infinite reconnect resilience (MaxRetries: -1) for clients.*
- [[safe-socket/src/models/hybrid_timeout.go.md|ResolveHybridTimeouts]] (function: calls) — *profile/transport name, socket role ("client" or "server"), and deployment mode (isDocker).*
- [[safe-socket/src/models/hybrid_timeout.go.md|hybrid_timeout.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[safe-socket/cmd/test/deadline_test.go.md|deadline_test.go]] (imports)
- [[safe-socket/cmd/test/factory_test.go.md|factory_test.go]] (imports)
- [[safe-socket/cmd/test/heartbeat_audit_test.go.md|heartbeat_audit_test.go]] (imports)
- [[safe-socket/cmd/test/probe_resilience_test.go.md|probe_resilience_test.go]] (imports)
- [[safe-socket/cmd/test/scenario_test.go.md|scenario_test.go]] (imports)
- [[safe-socket/safe_socket.go.md|safe_socket.go]] (imports)
- [[safe-socket/src/facade/enveloped_connection.go.md|enveloped_connection.go]] (imports)
- [[safe-socket/src/facade/shutdown_test.go.md|shutdown_test.go]] (imports)
- [[safe-socket/src/facade/socket_client.go.md|socket_client.go]] (imports)
- [[safe-socket/src/facade/socket_server.go.md|socket_server.go]] (imports)
- [[safe-socket/src/factory/socket_factory.go.md|socket_factory.go]] (imports)
- [[safe-socket/src/factory/socket_factory_test.go.md|socket_factory_test.go]] (imports)
- [[safe-socket/src/interfaces/protocol.go.md|protocol.go]] (imports)
- [[safe-socket/src/models/hybrid_timeout_test.go.md|TestResolveHybridTimeouts_LocalVsDockerTCP]] (function: belongs_to)
- [[safe-socket/src/models/hybrid_timeout_test.go.md|TestResolveHybridTimeouts_SHMAndUDP]] (function: belongs_to)
- [[safe-socket/src/protocols/hello_protocol.go.md|hello_protocol.go]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
