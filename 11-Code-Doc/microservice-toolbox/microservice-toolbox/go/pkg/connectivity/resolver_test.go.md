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
Automatically generated mirror for `microservice-toolbox/go/pkg/connectivity/resolver_test.go`.

> **Essential Process**:
> Resolves capability network addresses and applies Docker Guard suppression rules.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|NewResolver]] (function: calls) — *NewResolver creates a new network resolver.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.ResolveBindAddr]] (method: calls) — *(Docker/K8s) works regardless of what was specified in the configuration.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.isLoopback]] (method: calls) — *isLoopback checks if the IP is in the 127.0.0.0/8 range.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|resolver.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|loader.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|loader_test.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver_test.go.md|TestNewResolver]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver_test.go.md|TestResolver_ResolveBindAddr]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|grpc_server.go]] (imports)
<!-- SYNC:END -->
