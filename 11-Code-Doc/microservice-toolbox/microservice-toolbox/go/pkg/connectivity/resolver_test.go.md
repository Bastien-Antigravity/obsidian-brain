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
Automatically generated mirror for `microservice-toolbox/go/pkg/connectivity/resolver_test.go`.

> **Essential Process**:
> Resolves capability network addresses and applies Docker Guard suppression rules.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|NewResolver]] (function: calls) — *NewResolver creates a new network resolver.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.IsLoopback]] (method: calls) — *IsLoopback checks if the IP or hostname refers to a loopback address.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.ResolveBindAddr]] (method: calls) — *ResolveBindAddr validates and returns the configured IP without substituting any hardcoded default.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.ResolveFullBindAddr]] (method: calls) — *ResolveFullBindAddr validates and returns a configured "host:port", "[ipv6]:port", or bare host string.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.isLoopback]] (method: calls) — *isLoopback delegates to IsLoopback for package-internal compatibility.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|resolver.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|loader.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|loader_test.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver_test.go.md|TestNewResolver]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver_test.go.md|TestResolver_ResolveBindAddr]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|grpc_server.go]] (imports)
<!-- SYNC:END -->
