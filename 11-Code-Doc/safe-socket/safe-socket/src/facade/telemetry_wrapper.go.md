---
source: safe-socket/src/facade/telemetry_wrapper.go
workspace: safe-socket
type: code-mirror
status: auto-generated
last_sync: 2026-11-07T14:41:19.468328
---

# Mirror: telemetry_wrapper.go

## 📝 Description
Automatically generated mirror for `safe-socket/src/facade/telemetry_wrapper.go`.

> **Essential Process**:
> Provides a distinct, lock-free atomic switchable telemetry wrapper for safe-socket TransportConnections to track real-time inter-service connections and segregated frame channels (data frames vs heartbeats) with zero overhead when disabled.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/facade/enveloped_connection.go.md|EnvelopedConnection.LocalAddr]] (method: calls) — *LocalAddr returns the local network address.*
- [[safe-socket/safe-socket/src/facade/enveloped_connection.go.md|EnvelopedConnection.RemoteAddr]] (method: calls) — *RemoteAddr returns the remote network address.*
- [[safe-socket/safe-socket/src/facade/enveloped_connection.go.md|enveloped_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryConnection.Close]] (method: defines_method) — *Close closes the underlying transport and atomically emits a disconnect event once if enabled.*
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryConnection.ReadMessage]] (method: defines_method) — *ReadMessage reads a complete frame from the underlying transport and atomically records inbound metrics if enabled.*
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryConnection.Read]] (method: defines_method) — *Read proxies stream reads and atomically records inbound metrics if enabled.*
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryConnection.Stats]] (method: defines_method) — *Stats returns the current atomic counters for bytes and frames on this connection.*
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryConnection.Write]] (method: defines_method) — *Write proxies data to the underlying transport and atomically records outbound metrics if enabled.*
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/test/identity_test.go.md|identity_test.go]] (calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (calls)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (calls)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (same_package)
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|IsTelemetryEnabled]] (function: belongs_to) — *IsTelemetryEnabled atomically returns whether real-time connection tracking is active.*
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|NewTelemetryConnection]] (function: belongs_to) — *NewTelemetryConnection wraps a TransportConnection in a lock-free switchable telemetry decorator.*
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|SetTelemetryEnabled]] (function: belongs_to) — *SetTelemetryEnabled atomically enables or disables real-time connection tracking.*
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|SetTelemetryHook]] (function: belongs_to) — *SetTelemetryHook atomically registers or clears the telemetry callback hook.*
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryConnection.Close]] (method: belongs_to) — *Close closes the underlying transport and atomically emits a disconnect event once if enabled.*
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryConnection.ReadMessage]] (method: belongs_to) — *ReadMessage reads a complete frame from the underlying transport and atomically records inbound metrics if enabled.*
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryConnection.Read]] (method: belongs_to) — *Read proxies stream reads and atomically records inbound metrics if enabled.*
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryConnection.Stats]] (method: belongs_to) — *Stats returns the current atomic counters for bytes and frames on this connection.*
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryConnection.Write]] (method: belongs_to) — *Write proxies data to the underlying transport and atomically records outbound metrics if enabled.*
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryConnection]] (struct: belongs_to) — *TelemetryConnection decorates a TransportConnection with lock-free atomic telemetry.*
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryConnection]] (struct: defines_method) — *TelemetryConnection decorates a TransportConnection with lock-free atomic telemetry.*
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryEventAccept]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryEventConnect]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryEventDisconnect]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryEventRead]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryEventType]] (struct: belongs_to) — *TelemetryEventType categorizes the lifecycle or I/O event on a safe-socket connection.*
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryEventWrite]] (constant: belongs_to)
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryEvent]] (struct: belongs_to) — *TelemetryEvent represents a single observed connection or segregated frame event.*
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryHookFunc]] (struct: belongs_to) — *TelemetryHookFunc is the non-blocking callback invoked when telemetry is enabled.*
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper.go.md|emitTelemetryEvent]] (function: belongs_to)
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper_test.go.md|telemetry_wrapper_test.go]] (calls)
- [[safe-socket/safe-socket/src/facade/telemetry_wrapper_test.go.md|telemetry_wrapper_test.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
