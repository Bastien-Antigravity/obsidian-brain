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
Automatically generated mirror for `microservice-toolbox/go/pkg/network/grpc_server_test.go`.

> **Essential Process**:
> Configures and launches gRPC servers with Docker Guard address binding rules.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|NewGRPCServer]] (function: calls) — *NewGRPCServer creates a new gRPC server wrapper with default logging.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|grpc_server.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server_test.go.md|TestNewGRPCServer_DockerGuard]] (function: belongs_to)
<!-- SYNC:END -->
