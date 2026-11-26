---
microservice: safe-socket
type: note
status: active
tags:
- '#service/safe-socket'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `safe-socket/safe_socket.go`.

> **Essential Process**:
> Serves as the primary public entrypoint and package facade for safe-socket, exposing zero-boilerplate socket creation and peer identity inspection helpers.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/src/facade/enveloped_connection.go.md|EnvelopedConnection.GetLastIdentity]] (method: calls) — *GetLastIdentity returns the sender identity of the last decapsulated packet in a thread-safe manner.*
- [[safe-socket/src/facade/socket_client.go.md|socket_client.go]] (imports)
- [[safe-socket/src/factory/socket_factory_test.go.md|socket_factory_test.go]] (imports)
- [[safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/src/models/hybrid_timeout.go.md|IsDockerRuntime]] (function: calls) — *IsDockerRuntime detects containerized execution from DOCKER_ENV or CONTAINER environment markers.*
- [[safe-socket/src/models/hybrid_timeout.go.md|NewHybridSocketConfig]] (function: calls) — *and infinite reconnect resilience (MaxRetries: -1) for clients.*
- [[safe-socket/src/models/hybrid_timeout_test.go.md|hybrid_timeout_test.go]] (imports)
- [[safe-socket/src/schemas/messages.capnp.go.md|messages.capnp.go]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/cmd/test/identity_test.go.md|identity_test.go]] (calls)
- [[safe-socket/cmd/test/identity_test.go.md|identity_test.go]] (imports)
- [[safe-socket/cmd/test/matrix_server/main.go.md|main.go]] (calls)
- [[safe-socket/cmd/test/matrix_server/main.go.md|main.go]] (imports)
- [[safe-socket/cmd/test/probe_resilience_test.go.md|probe_resilience_test.go]] (calls)
- [[safe-socket/cmd/test/probe_resilience_test.go.md|probe_resilience_test.go]] (imports)
- [[safe-socket/safe_socket.go.md|CreateHybrid]] (function: belongs_to) — *hybrid timeouts (0 on SHM; 10m/60s on local TCP; 3m/30s on Docker TCP with 2.5x auto-heartbeats).*
- [[safe-socket/safe_socket.go.md|CreateWithConfig]] (function: belongs_to) — *Use this to set Deadlines or other advanced config options.*
- [[safe-socket/safe_socket.go.md|Create]] (function: belongs_to) — *- autoConnect: if true, immediately calls Open() / Listen()*
- [[safe-socket/safe_socket.go.md|DroppedTelemetryEvents]] (function: belongs_to) — *DroppedTelemetryEvents returns the count of dropped events due to buffer saturation.*
- [[safe-socket/safe_socket.go.md|FlushTelemetry]] (function: belongs_to) — *FlushTelemetry waits for all queued telemetry events to be dispatched or timeout.*
- [[safe-socket/safe_socket.go.md|GetIdentity]] (function: belongs_to) — *It traverses through Heartbeat, Handshake, or Envelope wrappers to find the HelloMsg.*
- [[safe-socket/safe_socket.go.md|IsTelemetryEnabled]] (function: belongs_to) — *IsTelemetryEnabled atomically returns whether real-time connection tracking is active.*
- [[safe-socket/safe_socket.go.md|ResolveHybridTimeouts]] (function: belongs_to) — *ResolveHybridTimeouts returns the canonical (Deadline, HeartbeatInterval) pair for a transport & mode.*
- [[safe-socket/safe_socket.go.md|SetTelemetryEnabled]] (function: belongs_to) — *SetTelemetryEnabled atomically enables or disables real-time connection tracking across safe-socket.*
- [[safe-socket/safe_socket.go.md|SetTelemetryHook]] (function: belongs_to) — *SetTelemetryHook atomically registers or clears the non-blocking telemetry callback.*
- [[safe-socket/safe_socket.go.md|TelemetryEventAccept]] (constant: belongs_to)
- [[safe-socket/safe_socket.go.md|TelemetryEventConnect]] (constant: belongs_to)
- [[safe-socket/safe_socket.go.md|TelemetryEventDisconnect]] (constant: belongs_to)
- [[safe-socket/safe_socket.go.md|TelemetryEventRead]] (constant: belongs_to)
- [[safe-socket/safe_socket.go.md|TelemetryEventWrite]] (constant: belongs_to)
- [[safe-socket/safe_socket.go.md|TransportFramedTCP]] (constant: belongs_to)
- [[safe-socket/safe_socket.go.md|TransportSHM]] (constant: belongs_to)
- [[safe-socket/safe_socket.go.md|TransportUDP]] (constant: belongs_to)
- [[safe-socket/safe_socket.go.md|WrapConnectionWithTelemetry]] (function: belongs_to) — *or wraps it with TelemetryConnection if telemetry is enabled.*
- [[safe-socket/src/cgo_bridge/socket.go.md|socket.go]] (imports)
<!-- SYNC:END -->
