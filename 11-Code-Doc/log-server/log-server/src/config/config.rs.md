---
microservice: log-server
type: note
status: active
tags:
- '#service/log-server'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `log-server/src/config/config.rs`.

> **Essential Process**:
> ! Log server configuration structure holding host, TCP socket port, and gRPC port. ! ! DATA FLOW: ! 1. CLI / Environment / standalone.yaml -> Config::new() ! 2. Config injected into TCP and gRPC Server components ! ! KEY PARAMETERS: ! - name: Service name (default "log_server"). ! - host: Network bind address (default 0.0.0.0). ! - port: TCP socket port (default 9020). ! - grpc_port: gRPC bridge port (default 9021). / Server configuration [derive(Clone)] pub struct Config { pub name: String, pub host: String, pub port: u16, pub grpc_port: u16, }

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/log-server/src/config/config.rs.md|Config.new]] (method: defines_method) — *Create new server configuration*

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/config/config.rs.md|Config.new]] (method: belongs_to) — *Create new server configuration*
- [[log-server/log-server/src/config/config.rs.md|Config]] (struct: belongs_to) — *Server configuration*
- [[log-server/log-server/src/config/config.rs.md|Config]] (struct: defines_method) — *Server configuration*
- [[log-server/log-server/src/config/config.rs.md|test_config_new]] (function: belongs_to)
- [[log-server/log-server/src/core/contracts.rs.md|contracts.rs]] (calls)
- [[log-server/log-server/src/core/contracts.rs.md|contracts.rs]] (imports)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (calls)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (imports)
- [[log-server/log-server/src/lib.rs.md|lib.rs]] (imports)
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (calls)
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (imports)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (calls)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (imports)
<!-- SYNC:END -->
