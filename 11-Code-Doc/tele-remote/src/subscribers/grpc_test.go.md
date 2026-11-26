---
source: tele-remote/src/subscribers/grpc_test.go
workspace: tele-remote
type: code-mirror
status: auto-generated
last_sync: 2026-11-23 20:26:03.005419
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: grpc_test.go

## 📝 Description
Automatically generated mirror for `tele-remote/src/subscribers/grpc_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[tele-remote/src/grpc_control/teleremote.pb.go.md|teleremote.pb.go]] (imports)
- [[tele-remote/src/interfaces/subscriber.go.md|subscriber.go]] (imports)
- [[tele-remote/src/publishers/grpc.go.md|GrpcPublisher.PublishCommand]] (method: calls) — *PublishCommand sends a command to the connected microservice if the context has not expired.*
- [[tele-remote/src/publishers/grpc.go.md|NewGrpcPublisher]] (function: calls) — *NewGrpcPublisher creates a thread-safe gRPC stream publisher.*
- [[tele-remote/src/publishers/grpc.go.md|grpc.go]] (imports)
- [[tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.Close]] (method: calls) — *Close gracefully stops the gRPC server within the bounded graceful timeout.*
- [[tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.ConfigureSecurity]] (method: calls) — *ConfigureSecurity validates and initializes Option A TLS/mTLS credentials and auth token on the cold path.*
- [[tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.Connect]] (method: calls) — *Connect implements the grpc_control.TeleRemoteServiceServer stream loop*
- [[tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.UpdateRuntimeSecurity]] (method: calls) — *UpdateRuntimeSecurity updates TLS enforcement policy and auth token dynamically while retaining valid active creds on...*
- [[tele-remote/src/subscribers/grpc.go.md|NewGrpcSubscriber]] (function: calls) — *NewGrpcSubscriber instantiates a gRPC transport listener bound to ip:port.*
- [[tele-remote/src/subscribers/grpc.go.md|grpc.go]] (same_package)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockConnectStream.Context]] (method: defines_method)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockConnectStream.Recv]] (method: defines_method)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockConnectStream.Send]] (method: defines_method)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockLogger.Critical]] (method: defines_method)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockLogger.Debug]] (method: defines_method)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockLogger.Error]] (method: defines_method)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockLogger.Info]] (method: defines_method)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockLogger.Warning]] (method: defines_method)
- [[tele-remote/src/subscribers/grpc_test.go.md|peerOverrideConn.RemoteAddr]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[tele-remote/cmd/tele-remote/main.go.md|main.go]] (imports)
- [[tele-remote/src/subscribers/grpc.go.md|grpc.go]] (calls)
- [[tele-remote/src/subscribers/grpc.go.md|grpc.go]] (same_package)
- [[tele-remote/src/subscribers/grpc_test.go.md|TestConnect_AuthTokenEnforcement]] (function: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|TestConnect_RejectsComponentIdentityMismatch]] (function: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|TestConnect_RejectsTelemetryBeforeRegistration]] (function: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|TestGrpcPublisher_PublishCommandUnblocksOnContextTimeout]] (function: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|TestGrpcSubscriber_ConfigureSecurity_FailFastAndCleartextBoot]] (function: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|TestGrpcSubscriber_OptionAMTLSAndRuntimeUpdate]] (function: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|generateTestFleetPKI]] (function: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockConnectStream.Context]] (method: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockConnectStream.Recv]] (method: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockConnectStream.Send]] (method: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockConnectStream]] (struct: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockConnectStream]] (struct: defines_method)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockLogger.Critical]] (method: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockLogger.Debug]] (method: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockLogger.Error]] (method: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockLogger.Info]] (method: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockLogger.Warning]] (method: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockLogger]] (struct: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|mockLogger]] (struct: defines_method)
- [[tele-remote/src/subscribers/grpc_test.go.md|peerOverrideConn.RemoteAddr]] (method: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|peerOverrideConn]] (struct: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|peerOverrideConn]] (struct: defines_method)
- [[tele-remote/src/subscribers/grpc_test.go.md|runCleartextHandshake]] (function: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|runTLSHandshake]] (function: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|testFleetPKI]] (struct: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|writeCertKeyPEM]] (function: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|writeSignedCert]] (function: belongs_to)
- [[tele-remote/src/subscribers/grpc_test.go.md|writeTempCA]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
