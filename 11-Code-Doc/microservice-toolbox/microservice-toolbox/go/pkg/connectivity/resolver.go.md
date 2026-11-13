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
Automatically generated mirror for `microservice-toolbox/go/pkg/connectivity/resolver.go`.

> **Essential Process**:
> Resolves configured capability network addresses strictly from AppConfig inputs.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.GetPrimaryInterfaceIP]] (method: defines_method) — *GetPrimaryInterfaceIP finds the first non-loopback IPv4 interface address.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.IsDockerEnv]] (method: defines_method) — *IsDockerEnv returns whether the resolver detected or was configured for a Docker environment.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.IsLoopback]] (method: defines_method) — *IsLoopback checks if the IP or hostname refers to a loopback address.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.ResolveBindAddr]] (method: defines_method) — *ResolveBindAddr validates and returns the configured IP without substituting any hardcoded default.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.ResolveFullBindAddr]] (method: defines_method) — *ResolveFullBindAddr validates and returns a configured "host:port", "[ipv6]:port", or bare host string.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.getPrimaryInterfaceIP]] (method: defines_method) — *getPrimaryInterfaceIP delegates to GetPrimaryInterfaceIP for internal compatibility.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.isLoopback]] (method: defines_method) — *isLoopback delegates to IsLoopback for package-internal compatibility.*

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|NewResolver]] (function: belongs_to) — *NewResolver creates a new network resolver.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.GetPrimaryInterfaceIP]] (method: belongs_to) — *GetPrimaryInterfaceIP finds the first non-loopback IPv4 interface address.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.IsDockerEnv]] (method: belongs_to) — *IsDockerEnv returns whether the resolver detected or was configured for a Docker environment.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.IsLoopback]] (method: belongs_to) — *IsLoopback checks if the IP or hostname refers to a loopback address.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.ResolveBindAddr]] (method: belongs_to) — *ResolveBindAddr validates and returns the configured IP without substituting any hardcoded default.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.ResolveFullBindAddr]] (method: belongs_to) — *ResolveFullBindAddr validates and returns a configured "host:port", "[ipv6]:port", or bare host string.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.getPrimaryInterfaceIP]] (method: belongs_to) — *getPrimaryInterfaceIP delegates to GetPrimaryInterfaceIP for internal compatibility.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver.isLoopback]] (method: belongs_to) — *isLoopback delegates to IsLoopback for package-internal compatibility.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver]] (struct: belongs_to) — *Resolver handles network address resolution strictly from configuration.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|Resolver]] (struct: defines_method) — *Resolver handles network address resolution strictly from configuration.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver_test.go.md|resolver_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver_test.go.md|resolver_test.go]] (same_package)
<!-- SYNC:END -->
