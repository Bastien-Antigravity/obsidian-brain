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
Automatically generated mirror for `microservice-toolbox/go/pkg/connectivity/resolver.go`.

> **Essential Process**:
> Resolves capability network addresses and applies Docker Guard suppression rules.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.ResolveBindAddr]] (method: defines_method) — *(Docker/K8s) works regardless of what was specified in the configuration.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.ResolveFullBindAddr]] (method: defines_method) — *using the Docker Guard logic.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.getPrimaryInterfaceIP]] (method: defines_method) — *Keep as utility for potential client-side discovery.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.isLoopback]] (method: defines_method) — *isLoopback checks if the IP is in the 127.0.0.0/8 range.*

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|loader.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|NewResolver]] (function: belongs_to) — *NewResolver creates a new network resolver.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.ResolveBindAddr]] (method: belongs_to) — *(Docker/K8s) works regardless of what was specified in the configuration.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.ResolveFullBindAddr]] (method: belongs_to) — *using the Docker Guard logic.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.getPrimaryInterfaceIP]] (method: belongs_to) — *Keep as utility for potential client-side discovery.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.isLoopback]] (method: belongs_to) — *isLoopback checks if the IP is in the 127.0.0.0/8 range.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver]] (struct: belongs_to) — *Keep as utility for potential client-side discovery.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver]] (struct: defines_method) — *Keep as utility for potential client-side discovery.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver_test.go.md|resolver_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver_test.go.md|resolver_test.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|grpc_server.go]] (calls)
<!-- SYNC:END -->
