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
Automatically generated mirror for `tele-remote/src/subscribers/grpc.go`.

> **Essential Process**:
> Implements the gRPC transport listener for Tele-Remote, managing bidirectional component streams, menu registration callbacks, telemetry forwarding, and session-safe disconnects.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[tele-remote/tele-remote/src/grpc_control/teleremote.pb.go.md|teleremote.pb.go]] (imports)
- [[tele-remote/tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|RegisterTeleRemoteServiceServer]] (function: calls)
- [[tele-remote/tele-remote/src/interfaces/subscriber.go.md|subscriber.go]] (imports)
- [[tele-remote/tele-remote/src/publishers/grpc.go.md|NewGrpcPublisher]] (function: calls) — *NewGrpcPublisher creates a thread-safe gRPC stream publisher.*
- [[tele-remote/tele-remote/src/publishers/grpc.go.md|grpc.go]] (imports)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.Close]] (method: defines_method) — *Close gracefully stops the gRPC server.*
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.Connect]] (method: defines_method) — *Connect implements the grpc_control.TeleRemoteServiceServer stream loop*
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.StartListen]] (method: defines_method) — *StartListen binds the TCP socket and serves incoming gRPC component streams.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.OnDisconnect]] (method: calls) — *preventing a late disconnect from an older stream from deleting a newly reconnected session.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.OnTelemetry]] (method: calls) — *OnTelemetry enqueues incoming logs or events non-blockingly for asynchronous delivery to the admin chat.*

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main.go]] (calls)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main.go]] (imports)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.Close]] (method: belongs_to) — *Close gracefully stops the gRPC server.*
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.Connect]] (method: belongs_to) — *Connect implements the grpc_control.TeleRemoteServiceServer stream loop*
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.StartListen]] (method: belongs_to) — *StartListen binds the TCP socket and serves incoming gRPC component streams.*
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber]] (struct: belongs_to) — *GrpcSubscriber acts as the Tele-Remote generic gRPC Listener*
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber]] (struct: defines_method) — *GrpcSubscriber acts as the Tele-Remote generic gRPC Listener*
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|NewGrpcSubscriber]] (function: belongs_to) — *NewGrpcSubscriber instantiates a gRPC transport listener bound to ip:port.*
<!-- SYNC:END -->
