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

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|UnimplementedNotifServiceServer.SendNotification]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|UnimplementedNotifServiceServer.mustEmbedUnimplementedNotifServiceServer]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|UnimplementedNotifServiceServer.testEmbeddedByValue]] (method: defines_method)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|notifServiceClient.SendNotification]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|NewNotifServiceClient]] (function: belongs_to)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|NotifServiceClient]] (interface: belongs_to) — *For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/...*
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|NotifServiceServer]] (interface: belongs_to) — *for forward compatibility.*
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|NotifService_SendNotification_FullMethodName]] (constant: belongs_to)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|RegisterNotifServiceServer]] (function: belongs_to)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|UnimplementedNotifServiceServer.SendNotification]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|UnimplementedNotifServiceServer.mustEmbedUnimplementedNotifServiceServer]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|UnimplementedNotifServiceServer.testEmbeddedByValue]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|UnimplementedNotifServiceServer]] (struct: belongs_to)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|UnimplementedNotifServiceServer]] (struct: defines_method)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|UnsafeNotifServiceServer]] (interface: belongs_to) — *result in compilation errors.*
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|_NotifService_SendNotification_Handler]] (function: belongs_to)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|_]] (constant: belongs_to) — *Requires gRPC-Go v1.64.0 or later.*
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|notifServiceClient.SendNotification]] (method: belongs_to)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|notifServiceClient]] (struct: belongs_to)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service_grpc.pb.go.md|notifServiceClient]] (struct: defines_method)
- [[notif-server/notif-server/src/server/server.go.md|server.go]] (calls)
<!-- SYNC:END -->
