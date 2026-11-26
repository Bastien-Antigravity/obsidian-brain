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
Automatically generated mirror for `microservice-toolbox/python/microservice_toolbox/connectivity/resolver.py`.

> **Essential Process**:
> Resolver handles network address validation and resolution strictly from AppConfig.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/resolver.py.md|Resolver]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/resolver.py.md|__init__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/resolver.py.md|get_primary_interface_ip]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/resolver.py.md|is_docker_env]] (function: belongs_to) — *Returns whether the resolver detected a Docker container environment.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/resolver.py.md|is_loopback]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/resolver.py.md|new_resolver]] (function: belongs_to) — *Factory method for Resolver.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/resolver.py.md|resolve_bind_addr]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/connectivity/resolver.py.md|resolve_full_bind_addr]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/network/grpc_server.py.md|grpc_server.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/network/grpc_server.py.md|grpc_server.py]] (imports)
<!-- SYNC:END -->
