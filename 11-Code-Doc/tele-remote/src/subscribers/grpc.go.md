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
> Implements the gRPC transport listener for Tele-Remote, delegating dynamic local/remote TLS/mTLS policy enforcement to microservice-toolbox while enforcing bearer token authentication, registration-first stream gating, and bounded shutdown.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[tele-remote/src/grpc_control/teleremote.pb.go.md|teleremote.pb.go]] (imports)
- [[tele-remote/src/grpc_control/teleremote_grpc.pb.go.md|RegisterTeleRemoteServiceServer]] (function: calls)
- [[tele-remote/src/interfaces/subscriber.go.md|subscriber.go]] (imports)
- [[tele-remote/src/publishers/grpc.go.md|NewGrpcPublisher]] (function: calls) — *NewGrpcPublisher creates a thread-safe gRPC stream publisher.*
- [[tele-remote/src/publishers/grpc.go.md|grpc.go]] (imports)
- [[tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.Close]] (method: defines_method) — *Close gracefully stops the gRPC server within the bounded graceful timeout.*
- [[tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.ConfigureSecurity]] (method: defines_method) — *ConfigureSecurity validates and initializes Option A TLS/mTLS credentials and auth token on the cold path.*
- [[tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.Connect]] (method: defines_method) — *Connect implements the grpc_control.TeleRemoteServiceServer stream loop*
- [[tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.StartListen]] (method: defines_method) — *StartListen binds the TCP socket and serves incoming gRPC component streams.*
- [[tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.UpdateRuntimeSecurity]] (method: defines_method) — *UpdateRuntimeSecurity updates TLS enforcement policy and auth token dynamically while retaining valid active creds on...*
- [[tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.shutdown]] (method: defines_method)
- [[tele-remote/src/subscribers/grpc_test.go.md|grpc_test.go]] (same_package)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockConnectStream.Context]] (method: calls)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockConnectStream.Recv]] (method: calls)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockLogger.Error]] (method: calls)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockLogger.Info]] (method: calls)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockLogger.Warning]] (method: calls)
- [[tele-remote/src/telegram/core/bot.go.md|Bot.OnDisconnect]] (method: calls) — *preventing a late disconnect from an older stream from deleting a newly reconnected session.*
- [[tele-remote/src/telegram/core/bot.go.md|Bot.OnTelemetry]] (method: calls) — *OnTelemetry enqueues incoming logs or events non-blockingly for asynchronous delivery to the admin chat.*

### 🔌 Consumers (Inbound)
- [[tele-remote/cmd/tele-remote/main.go.md|main.go]] (calls)
- [[tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.Close]] (method: belongs_to) — *Close gracefully stops the gRPC server within the bounded graceful timeout.*
- [[tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.ConfigureSecurity]] (method: belongs_to) — *ConfigureSecurity validates and initializes Option A TLS/mTLS credentials and auth token on the cold path.*
- [[tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.Connect]] (method: belongs_to) — *Connect implements the grpc_control.TeleRemoteServiceServer stream loop*
- [[tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.StartListen]] (method: belongs_to) — *StartListen binds the TCP socket and serves incoming gRPC component streams.*
- [[tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.UpdateRuntimeSecurity]] (method: belongs_to) — *UpdateRuntimeSecurity updates TLS enforcement policy and auth token dynamically while retaining valid active creds on...*
- [[tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.shutdown]] (method: belongs_to)
- [[tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber]] (struct: belongs_to) — *GrpcSubscriber acts as the Tele-Remote generic gRPC Listener*
- [[tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber]] (struct: defines_method) — *GrpcSubscriber acts as the Tele-Remote generic gRPC Listener*
- [[tele-remote/src/subscribers/grpc.go.md|NewGrpcSubscriber]] (function: belongs_to) — *NewGrpcSubscriber instantiates a gRPC transport listener bound to ip:port.*
- [[tele-remote/src/subscribers/grpc.go.md|streamRecvResult]] (struct: belongs_to)
- [[tele-remote/src/subscribers/grpc.go.md|validateStreamAuth]] (function: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|grpc_test.go]] (calls)
- [[tele-remote/src/subscribers/grpc_test.go.md|grpc_test.go]] (same_package)
<!-- SYNC:END -->
