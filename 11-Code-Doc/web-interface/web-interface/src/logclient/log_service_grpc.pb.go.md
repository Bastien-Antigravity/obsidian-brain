---
source: web-interface/src/logclient/log_service_grpc.pb.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-07T23:19:48.786427
---

# Mirror: log_service_grpc.pb.go

## 📝 Description
Automatically generated mirror for `web-interface/src/logclient/log_service_grpc.pb.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|UnimplementedLogBridgeServer.GetTailLogs]] (method: defines_method)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|UnimplementedLogBridgeServer.LogMessage]] (method: defines_method)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|UnimplementedLogBridgeServer.StreamLogs]] (method: defines_method)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|UnimplementedLogBridgeServer.mustEmbedUnimplementedLogBridgeServer]] (method: defines_method)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|UnimplementedLogBridgeServer.testEmbeddedByValue]] (method: defines_method)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|logBridgeClient.GetTailLogs]] (method: defines_method)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|logBridgeClient.LogMessage]] (method: defines_method)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|logBridgeClient.StreamLogs]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|LogBridgeClient]] (interface: belongs_to) — *For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/...*
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|LogBridgeServer]] (interface: belongs_to) — *for forward compatibility.*
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|LogBridge_GetTailLogs_FullMethodName]] (constant: belongs_to)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|LogBridge_LogMessage_FullMethodName]] (constant: belongs_to)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|LogBridge_StreamLogs_FullMethodName]] (constant: belongs_to)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|NewLogBridgeClient]] (function: belongs_to)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|RegisterLogBridgeServer]] (function: belongs_to)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|UnimplementedLogBridgeServer.GetTailLogs]] (method: belongs_to)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|UnimplementedLogBridgeServer.LogMessage]] (method: belongs_to)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|UnimplementedLogBridgeServer.StreamLogs]] (method: belongs_to)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|UnimplementedLogBridgeServer.mustEmbedUnimplementedLogBridgeServer]] (method: belongs_to)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|UnimplementedLogBridgeServer.testEmbeddedByValue]] (method: belongs_to)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|UnimplementedLogBridgeServer]] (struct: belongs_to) — *pointer dereference when methods are called.*
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|UnimplementedLogBridgeServer]] (struct: defines_method) — *pointer dereference when methods are called.*
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|UnsafeLogBridgeServer]] (interface: belongs_to) — *result in compilation errors.*
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|_LogBridge_GetTailLogs_Handler]] (function: belongs_to)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|_LogBridge_LogMessage_Handler]] (function: belongs_to)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|_LogBridge_StreamLogs_Handler]] (function: belongs_to)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|_]] (constant: belongs_to) — *Requires gRPC-Go v1.64.0 or later.*
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|logBridgeClient.GetTailLogs]] (method: belongs_to)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|logBridgeClient.LogMessage]] (method: belongs_to)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|logBridgeClient.StreamLogs]] (method: belongs_to)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|logBridgeClient]] (struct: belongs_to)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|logBridgeClient]] (struct: defines_method)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (imports)
- [[web-interface/web-interface/src/router/log_bridge.go.md|log_bridge.go]] (calls)
- [[web-interface/web-interface/src/router/log_bridge.go.md|log_bridge.go]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
