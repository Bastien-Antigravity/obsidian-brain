---
source: safe-socket/cmd/test/probe_resilience_test.go
workspace: safe-socket
type: code-mirror
status: auto-generated
last_sync: 2026-10-01T01:10:03.094442
---

# Mirror: probe_resilience_test.go

## 📝 Description
Automatically generated mirror for `safe-socket/cmd/test/probe_resilience_test.go`.

> **Essential Process**:
> Tests server socket resilience against raw TCP health checks and immediate disconnects before protocol initiation.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.Close]] (method: calls)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|MockTransport.Write]] (method: calls)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|identity_test.go]] (same_package)
- [[safe-socket/safe-socket/safe_socket.go.md|CreateWithConfig]] (function: calls) — *Use this to set Deadlines or other advanced config options.*
- [[safe-socket/safe-socket/safe_socket.go.md|safe_socket.go]] (imports)
- [[safe-socket/safe-socket/src/models/socket_config.go.md|socket_config.go]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/test/probe_resilience_test.go.md|TestTCPInvalidProtocolFailsStrictly]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/test/probe_resilience_test.go.md|TestTCPProbeResilience]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
