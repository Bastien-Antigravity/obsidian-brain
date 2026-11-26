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
Automatically generated mirror for `log-server/src/main.rs`.

> **Essential Process**:
> ! Log Server main executable entry point. Bootstraps the distributed runtime, ! resolves network addresses via microservice-toolbox, and initializes TCP ! and gRPC logging daemons. ! ! DATA FLOW: ! 1. Runtime environment -> resolve_config_profile() -> load_config(profile) ! 2. LogServer::new() -> LogServer::run() ! ! KEY PARAMETERS: ! - production.yaml / standalone.yaml: Listen host/port (TCP) and grpc_ip/grpc_port (gRPC). ! - CONFIG_PROFILE / DOCKER_ENV: Active configuration profile selection. use std::sync::Arc; use microservice_toolbox::config::loader::AppConfig; use log_server::config::config::Config; use log_server::facade::log_server::LogServer; use log_server::line_str; use log_server::utils::terminal_ui::print_internal_log;

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/src/config/config.rs.md|Config.new]] (method: calls) — *Create new server configuration resolving version strictly from VERSION.txt via microservice-toolbox*
- [[log-server/src/config/config.rs.md|Config.with_grpc_host]] (method: calls) — *Override the gRPC bind host verbatim*
- [[log-server/src/config/config.rs.md|Config.with_sync_on_flush]] (method: calls) — *Configure hardware durability barrier (fsync)*
- [[log-server/src/config/config.rs.md|Config.with_version]] (method: calls) — *Set authoritative service version resolved via AppConfig::get_version()*
- [[log-server/src/config/config.rs.md|Config]] (struct: calls) — *Server configuration*
- [[log-server/src/config/config.rs.md|config.rs]] (imports)
- [[log-server/src/config/config.rs.md|parse_fsync_config]] (function: calls) — *Helper to parse fsync durability setting from AppConfig or environment*
- [[log-server/src/facade/log_server.rs.md|LogServer.new_with_config]] (method: calls) — *Create new log server instance from a full `Config` and optional active `AppConfig`*
- [[log-server/src/facade/log_server.rs.md|LogServer.run]] (method: calls) — *Run the log server with all components*
- [[log-server/src/facade/log_server.rs.md|log_server.rs]] (imports)
- [[log-server/src/facade/mod.rs.md|mod.rs]] (imports)
- [[log-server/src/utils/mod.rs.md|mod.rs]] (imports)
- [[log-server/src/utils/terminal_ui.rs.md|print_internal_log]] (function: calls) — *Formats and prints an internal server log message (visual alignment only)*
- [[log-server/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[log-server/src/main.rs.md|Endpoint]] (struct: belongs_to)
- [[log-server/src/main.rs.md|ServiceEndpoints]] (struct: belongs_to)
- [[log-server/src/main.rs.md|config_file_exists]] (function: belongs_to) — *Checks whether a profile configuration file exists in standard lookup locations.*
- [[log-server/src/main.rs.md|main]] (function: belongs_to)
- [[log-server/src/main.rs.md|parse_host_port]] (function: belongs_to) — *Parse a `host:port` (or `[ipv6]:port`) endpoint string verbatim without silent fallbacks.*
- [[log-server/src/main.rs.md|resolve_config_profile]] (function: belongs_to) — *Resolves the configuration profile based on `CONFIG_PROFILE` or runtime environment (`DOCKER_ENV=true`).*
- [[log-server/src/main.rs.md|resolve_service_addrs]] (function: belongs_to) — *Resolve TCP and gRPC endpoints verbatim from `AppConfig`.*
- [[log-server/src/main.rs.md|run_server]] (function: belongs_to) — *Main server execution function*
- [[log-server/src/main.rs.md|test_parse_host_port_preserves_host_verbatim]] (function: belongs_to)
- [[log-server/src/main.rs.md|test_resolve_service_addrs_fails_fast_when_missing]] (function: belongs_to)
- [[log-server/src/main.rs.md|test_resolve_service_addrs_preserves_distinct_grpc_host]] (function: belongs_to)
<!-- SYNC:END -->
