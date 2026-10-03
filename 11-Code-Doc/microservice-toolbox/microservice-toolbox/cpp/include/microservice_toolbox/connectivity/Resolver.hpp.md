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
Automatically generated mirror for `microservice-toolbox/cpp/include/microservice_toolbox/connectivity/Resolver.hpp`.

> **Essential Process**:
> Resolves capability network addresses and applies Docker Guard suppression rules.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/connectivity/Resolver.hpp.md|Resolver.Resolver]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/connectivity/Resolver.hpp.md|Resolver.is_docker_env]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/connectivity/Resolver.hpp.md|Resolver.is_loopback]] (method: defines_method) — *Checks if the IP is a loopback address.*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/connectivity/Resolver.hpp.md|Resolver.resolve_bind_addr]] (method: defines_method) — *and forces a bind to 0.0.0.0.*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/connectivity/Resolver.hpp.md|Resolver.resolve_full_bind_addr]] (method: defines_method) — *Takes a "host:port" string and returns a resolved "host:port" using Docker Guard logic.*

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/connectivity/Resolver.hpp.md|MICROSERVICE_TOOLBOX_CONNECTIVITY_RESOLVER_HPP]] (macro: belongs_to) — *ifndef MICROSERVICE_TOOLBOX_CONNECTIVITY_RESOLVER_HPP*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/connectivity/Resolver.hpp.md|Resolver.Resolver]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/connectivity/Resolver.hpp.md|Resolver.is_docker_env]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/connectivity/Resolver.hpp.md|Resolver.is_loopback]] (method: belongs_to) — *Checks if the IP is a loopback address.*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/connectivity/Resolver.hpp.md|Resolver.resolve_bind_addr]] (method: belongs_to) — *and forces a bind to 0.0.0.0.*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/connectivity/Resolver.hpp.md|Resolver.resolve_full_bind_addr]] (method: belongs_to) — *Takes a "host:port" string and returns a resolved "host:port" using Docker Guard logic.*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/connectivity/Resolver.hpp.md|Resolver]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/connectivity/Resolver.hpp.md|Resolver]] (class: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/connectivity/Resolver.hpp.md|new_resolver]] (function: belongs_to)
<!-- SYNC:END -->
