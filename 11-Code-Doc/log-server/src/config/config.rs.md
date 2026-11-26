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
> ! Log server configuration structure holding host, TCP socket port, gRPC port, ! and dynamic hardware durability barrier (fsync) configuration. ! ! DATA FLOW: ! 1. CLI / Environment / standalone.yaml -> Config::new() -> parse_fsync_config() ! 2. Config injected into TCP and gRPC Server components and LogWriter ! ! KEY PARAMETERS: ! - name: Service name (default "log_server"). ! - host: Network bind address for TCP server. ! - port: TCP socket port. ! - grpc_host: Network bind address for gRPC bridge. ! - grpc_port: gRPC bridge port. ! - sync_on_flush: Atomic hardware durability barrier (default false: OS page cache). use std::sync::atomic::{AtomicBool, Ordering}; use std::sync::Arc; use microservice_toolbox::config::loader::AppConfig; / Server configuration [derive(Clone)] pub struct Config { pub name: String, pub version: String, pub host: String, pub port: u16, pub grpc_host: String, pub grpc_port: u16, pub sync_on_flush: Arc<AtomicBool>, }

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/src/config/config.rs.md|Config.is_sync_on_flush]] (method: defines_method) — *Query current hardware durability barrier state*
- [[log-server/src/config/config.rs.md|Config.new]] (method: defines_method) — *Create new server configuration resolving version strictly from VERSION.txt via microservice-toolbox*
- [[log-server/src/config/config.rs.md|Config.set_sync_on_flush]] (method: defines_method) — *Dynamic runtime toggle for hardware durability barrier (fsync)*
- [[log-server/src/config/config.rs.md|Config.with_grpc_host]] (method: defines_method) — *Override the gRPC bind host verbatim*
- [[log-server/src/config/config.rs.md|Config.with_sync_on_flush]] (method: defines_method) — *Configure hardware durability barrier (fsync)*
- [[log-server/src/config/config.rs.md|Config.with_version]] (method: defines_method) — *Set authoritative service version resolved via AppConfig::get_version()*
- [[log-server/src/facade/log_writer.rs.md|WriterConfig.default]] (method: calls)
- [[log-server/src/protocols/capnp/logger_msg.rs.md|Reader<'_,>.clone]] (method: calls)

### 🔌 Consumers (Inbound)
- [[log-server/src/config/config.rs.md|Config.is_sync_on_flush]] (method: belongs_to) — *Query current hardware durability barrier state*
- [[log-server/src/config/config.rs.md|Config.new]] (method: belongs_to) — *Create new server configuration resolving version strictly from VERSION.txt via microservice-toolbox*
- [[log-server/src/config/config.rs.md|Config.set_sync_on_flush]] (method: belongs_to) — *Dynamic runtime toggle for hardware durability barrier (fsync)*
- [[log-server/src/config/config.rs.md|Config.with_grpc_host]] (method: belongs_to) — *Override the gRPC bind host verbatim*
- [[log-server/src/config/config.rs.md|Config.with_sync_on_flush]] (method: belongs_to) — *Configure hardware durability barrier (fsync)*
- [[log-server/src/config/config.rs.md|Config.with_version]] (method: belongs_to) — *Set authoritative service version resolved via AppConfig::get_version()*
- [[log-server/src/config/config.rs.md|Config]] (struct: belongs_to) — *Server configuration*
- [[log-server/src/config/config.rs.md|Config]] (struct: defines_method) — *Server configuration*
- [[log-server/src/config/config.rs.md|parse_fsync_config]] (function: belongs_to) — *Helper to parse fsync durability setting from AppConfig or environment*
- [[log-server/src/config/config.rs.md|test_config_fsync_toggle_on_the_fly]] (function: belongs_to)
- [[log-server/src/config/config.rs.md|test_config_new]] (function: belongs_to)
- [[log-server/src/config/config.rs.md|test_config_with_grpc_host]] (function: belongs_to)
- [[log-server/src/config/config.rs.md|test_parse_fsync_config_defaults]] (function: belongs_to)
- [[log-server/src/core/contracts.rs.md|contracts.rs]] (calls)
- [[log-server/src/core/contracts.rs.md|contracts.rs]] (imports)
- [[log-server/src/facade/log_server.rs.md|log_server.rs]] (calls)
- [[log-server/src/facade/log_server.rs.md|log_server.rs]] (imports)
- [[log-server/src/lib.rs.md|lib.rs]] (imports)
- [[log-server/src/main.rs.md|main.rs]] (calls)
- [[log-server/src/main.rs.md|main.rs]] (imports)
- [[log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (calls)
- [[log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (imports)
- [[log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (calls)
- [[log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (imports)
<!-- SYNC:END -->
