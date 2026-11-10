---
source: web-interface/src/router/log_bridge.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-07T23:21:55.557024
---

# Mirror: log_bridge.go

## 📝 Description
Automatically generated mirror for `web-interface/src/router/log_bridge.go`.

> **Essential Process**:
> High-performance gRPC bridge connecting web-interface to log-server (port 9021). Provides real-time Server-Sent Events (SSE) streaming and buffered log history directly to the ecosystem web console without intermediate REST overhead.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|NewLogBridgeClient]] (function: calls)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|logBridgeClient.GetExchangeContracts]] (method: calls)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|logBridgeClient.GetTailLogs]] (method: calls)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|logBridgeClient.StreamLogs]] (method: calls)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|log_service_grpc.pb.go]] (imports)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.Get]] (method: calls) — *Get looks up a registered service by name or tag (case-insensitive, flexible with hyphens/underscores/spaces).*
- [[web-interface/web-interface/src/router/router_test.go.md|router_test.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Close]] (method: calls)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (same_package)
- [[web-interface/web-interface/src/router/log_bridge.go.md|formatLevelString]] (function: belongs_to) — *formatLevelString converts numeric protobuf enum to string representation*
- [[web-interface/web-interface/src/router/log_bridge.go.md|getLogBridgeClient]] (function: belongs_to) — *getLogBridgeClient resolves or reuses the singleton gRPC connection to log-server.*
- [[web-interface/web-interface/src/router/log_bridge.go.md|handleGetLogContracts]] (function: belongs_to) — *falling back only to log-server's own published ServiceSpec in the MFE registry if gRPC is unavailable.*
- [[web-interface/web-interface/src/router/log_bridge.go.md|handleGetTailLogs]] (function: belongs_to) — *handleGetTailLogs queries recent buffered logs from log-server ring buffer via gRPC*
- [[web-interface/web-interface/src/router/log_bridge.go.md|handleStreamLogsSSE]] (function: belongs_to) — *handleStreamLogsSSE streams incoming fleet logs in real-time over HTTP Server-Sent Events (SSE).*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
