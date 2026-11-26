---
source: safe-socket/src/facade/telemetry_wrapper_test.go
workspace: safe-socket
type: code-mirror
status: auto-generated
last_sync: 2026-11-07 14:41:19.461135
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: telemetry_wrapper_test.go

## 📝 Description
Automatically generated mirror for `safe-socket/src/facade/telemetry_wrapper_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/src/facade/telemetry_wrapper.go.md|FlushTelemetry]] (function: calls) — *or until the timeout expires. Returns true if the queue was drained within timeout.*
- [[safe-socket/src/facade/telemetry_wrapper.go.md|IsTelemetryEnabled]] (function: calls) — *IsTelemetryEnabled atomically returns whether real-time connection tracking is active.*
- [[safe-socket/src/facade/telemetry_wrapper.go.md|NewTelemetryConnection]] (function: calls) — *NewTelemetryConnection wraps a TransportConnection in a lock-free switchable telemetry decorator.*
- [[safe-socket/src/facade/telemetry_wrapper.go.md|SetTelemetryEnabled]] (function: calls) — *SetTelemetryEnabled atomically enables or disables real-time connection tracking.*
- [[safe-socket/src/facade/telemetry_wrapper.go.md|SetTelemetryHook]] (function: calls) — *SetTelemetryHook atomically registers or clears the telemetry callback hook.*
- [[safe-socket/src/facade/telemetry_wrapper.go.md|TelemetryConnection.Stats]] (method: calls) — *Stats returns the current atomic counters for bytes and frames on this connection.*
- [[safe-socket/src/facade/telemetry_wrapper.go.md|WrapConnectionWithTelemetry]] (function: calls) — *If telemetry is enabled, it decorates conn with a TelemetryConnection.*
- [[safe-socket/src/facade/telemetry_wrapper.go.md|telemetry_wrapper.go]] (same_package)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.Close]] (method: defines_method)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.LocalAddr]] (method: defines_method)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.ReadMessage]] (method: defines_method)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.Read]] (method: defines_method)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.RemoteAddr]] (method: defines_method)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.SetDeadline]] (method: defines_method)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.SetIdleTimeout]] (method: defines_method)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.SetReadDeadline]] (method: defines_method)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.SetWriteDeadline]] (method: defines_method)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.Write]] (method: defines_method)
- [[safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|TestSegregatedChannelExtraction]] (function: belongs_to)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|TestTelemetryNonBlockingSlowHook]] (function: belongs_to)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|TestTelemetryPanicResilience]] (function: belongs_to)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|TestTelemetryWrapperAtomicSwitchAndSegregation]] (function: belongs_to)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|TestZeroOverheadWhenDisabled]] (function: belongs_to)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.Close]] (method: belongs_to)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.LocalAddr]] (method: belongs_to)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.ReadMessage]] (method: belongs_to)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.Read]] (method: belongs_to)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.RemoteAddr]] (method: belongs_to)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.SetDeadline]] (method: belongs_to)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.SetIdleTimeout]] (method: belongs_to)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.SetReadDeadline]] (method: belongs_to)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.SetWriteDeadline]] (method: belongs_to)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn.Write]] (method: belongs_to)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn]] (struct: belongs_to)
- [[safe-socket/src/facade/telemetry_wrapper_test.go.md|mockTransportConn]] (struct: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
