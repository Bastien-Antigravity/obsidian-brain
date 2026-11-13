---
microservice: microservice-toolbox
type: note
status: active
tags:
- '#service/microservice-toolbox'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `microservice-toolbox/go/pkg/network/grpc_server.go`.

> **Essential Process**:
> Configures and launches gRPC servers with Docker Guard address binding rules.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver_test.go.md|resolver_test.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|EnsureSafeLogger]] (function: calls) — *production microservices from silently running dark without operational logs.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|logger.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Error]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Info]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|GRPCServer.Start]] (method: defines_method) — *Start begins listening and serving.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|GRPCServer.Stop]] (method: defines_method) — *Stop performs a graceful shutdown.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/wiretap/grpc_wrapper.go.md|ServerOptions]] (function: calls) — *WireTap Unary and Stream server interceptors pre-configured.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/wiretap/wiretap_test.go.md|wiretap_test.go]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/lifecycle/manager.go.md|manager.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|GRPCServer.Start]] (method: belongs_to) — *Start begins listening and serving.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|GRPCServer.Stop]] (method: belongs_to) — *Stop performs a graceful shutdown.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|GRPCServer]] (struct: belongs_to) — *GRPCServer is a standardized wrapper for gRPC servers in the toolbox.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|GRPCServer]] (struct: defines_method) — *GRPCServer is a standardized wrapper for gRPC servers in the toolbox.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|NewGRPCServerWithLogger]] (function: belongs_to) — *It automatically applies the "Docker Guard" policy to the binding address.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|NewGRPCServer]] (function: belongs_to) — *NewGRPCServer creates a new gRPC server wrapper with default logging.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server_test.go.md|grpc_server_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server_test.go.md|grpc_server_test.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/notification/client_test.go.md|client_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/wiretap/wiretap.go.md|wiretap.go]] (calls)
<!-- SYNC:END -->
