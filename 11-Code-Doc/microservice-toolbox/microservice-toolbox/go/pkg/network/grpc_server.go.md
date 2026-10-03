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

## 📝 Description
Automatically generated mirror for `microservice-toolbox/go/pkg/network/grpc_server.go`.

> **Essential Process**:
> Configures and launches gRPC servers with Docker Guard address binding rules.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|NewResolver]] (function: calls) — *NewResolver creates a new network resolver.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.ResolveFullBindAddr]] (method: calls) — *using the Docker Guard logic.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver_test.go.md|resolver_test.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|EnsureSafeLogger]] (function: calls) — *production microservices from silently running dark without operational logs.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|logger.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Error]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Info]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|GRPCServer.Start]] (method: defines_method) — *Start begins listening and serving.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|GRPCServer.Stop]] (method: defines_method) — *Stop performs a graceful shutdown.*

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|GRPCServer.Start]] (method: belongs_to) — *Start begins listening and serving.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|GRPCServer.Stop]] (method: belongs_to) — *Stop performs a graceful shutdown.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|GRPCServer]] (struct: belongs_to) — *Stop performs a graceful shutdown.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|GRPCServer]] (struct: defines_method) — *Stop performs a graceful shutdown.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|NewGRPCServerWithLogger]] (function: belongs_to) — *It automatically applies the "Docker Guard" policy to the binding address.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|NewGRPCServer]] (function: belongs_to) — *NewGRPCServer creates a new gRPC server wrapper with default logging.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server_test.go.md|grpc_server_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server_test.go.md|grpc_server_test.go]] (same_package)
<!-- SYNC:END -->
