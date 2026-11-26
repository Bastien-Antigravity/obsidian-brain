---
microservice: tele-remote
type: note
status: active
tags:
- '#service/tele-remote'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `tele-remote/src/publishers/grpc.go`.

> **Essential Process**:
> Wraps an active bidirectional gRPC server stream into a thread-safe IPublisher that enforces bounded caller context cancellation and deadlines during sends.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[tele-remote/src/grpc_control/teleremote.pb.go.md|BotCommand_CommandType]] (struct: calls)
- [[tele-remote/src/grpc_control/teleremote.pb.go.md|teleremote.pb.go]] (imports)
- [[tele-remote/src/interfaces/subscriber.go.md|subscriber.go]] (imports)
- [[tele-remote/src/publishers/grpc.go.md|GrpcPublisher.Close]] (method: defines_method) — *Close satisfies interfaces.IPublisher.*
- [[tele-remote/src/publishers/grpc.go.md|GrpcPublisher.PublishCommand]] (method: defines_method) — *PublishCommand sends a command to the connected microservice if the context has not expired.*
- [[tele-remote/src/publishers/grpc.go.md|GrpcPublisher.RequestRefresh]] (method: defines_method) — *RequestRefresh asks the connected microservice to push a fresh menu definition.*
- [[tele-remote/src/publishers/grpc.go.md|GrpcPublisher.sendWithContext]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[tele-remote/src/publishers/grpc.go.md|GrpcPublisher.Close]] (method: belongs_to) — *Close satisfies interfaces.IPublisher.*
- [[tele-remote/src/publishers/grpc.go.md|GrpcPublisher.PublishCommand]] (method: belongs_to) — *PublishCommand sends a command to the connected microservice if the context has not expired.*
- [[tele-remote/src/publishers/grpc.go.md|GrpcPublisher.RequestRefresh]] (method: belongs_to) — *RequestRefresh asks the connected microservice to push a fresh menu definition.*
- [[tele-remote/src/publishers/grpc.go.md|GrpcPublisher.sendWithContext]] (method: belongs_to)
- [[tele-remote/src/publishers/grpc.go.md|GrpcPublisher]] (struct: belongs_to) — *GrpcPublisher wraps a bidirectional gRPC stream and implements interfaces.IPublisher*
- [[tele-remote/src/publishers/grpc.go.md|GrpcPublisher]] (struct: defines_method) — *GrpcPublisher wraps a bidirectional gRPC stream and implements interfaces.IPublisher*
- [[tele-remote/src/publishers/grpc.go.md|NewGrpcPublisher]] (function: belongs_to) — *NewGrpcPublisher creates a thread-safe gRPC stream publisher.*
- [[tele-remote/src/subscribers/grpc.go.md|grpc.go]] (calls)
- [[tele-remote/src/subscribers/grpc.go.md|grpc.go]] (imports)
- [[tele-remote/src/subscribers/grpc_test.go.md|grpc_test.go]] (calls)
- [[tele-remote/src/subscribers/grpc_test.go.md|grpc_test.go]] (imports)
<!-- SYNC:END -->
