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
Automatically generated mirror for `microservice-toolbox/rust/src/connectivity/resolver.rs`.

> **Essential Process**:
> Resolves configured capability network addresses strictly from AppConfig inputs.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Sync]] (method: calls) — *Synchronize with the Config Server*
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.default]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.get_primary_interface_ip]] (method: defines_method) — *Finds the first non-loopback IPv4 address for the local hostname without hardcoded probe IPs.*
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.is_docker_env]] (method: defines_method) — *Returns whether the resolver detected a Docker container environment.*
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.is_loopback]] (method: defines_method) — *Checks if the IP is in the 127.0.0.0/8 range or localhost.*
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.new]] (method: defines_method) — *Creates a new network resolver.*
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.resolve_bind_addr]] (method: defines_method) — *Validates and returns the configured IP directly (fail-fast if empty, no hardcoded fallback).*
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.resolve_full_bind_addr]] (method: defines_method) — *Validates and returns a configured "host:port", "[ipv6]:port", or bare host string.*

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.default]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.get_primary_interface_ip]] (method: belongs_to) — *Finds the first non-loopback IPv4 address for the local hostname without hardcoded probe IPs.*
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.is_docker_env]] (method: belongs_to) — *Returns whether the resolver detected a Docker container environment.*
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.is_loopback]] (method: belongs_to) — *Checks if the IP is in the 127.0.0.0/8 range or localhost.*
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.new]] (method: belongs_to) — *Creates a new network resolver.*
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.resolve_bind_addr]] (method: belongs_to) — *Validates and returns the configured IP directly (fail-fast if empty, no hardcoded fallback).*
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver.resolve_full_bind_addr]] (method: belongs_to) — *Validates and returns a configured "host:port", "[ipv6]:port", or bare host string.*
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver]] (struct: belongs_to) — *Resolver handles config-driven network address resolution with zero hardcoded defaults.*
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|Resolver]] (struct: defines_method) — *Resolver handles config-driven network address resolution with zero hardcoded defaults.*
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|new_resolver]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|test_is_loopback]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|test_resolve_bind_addr_preserves_config]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|test_resolve_full_bind_addr]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/grpc_server.rs.md|grpc_server.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/grpc_server.rs.md|grpc_server.rs]] (imports)
<!-- SYNC:END -->
