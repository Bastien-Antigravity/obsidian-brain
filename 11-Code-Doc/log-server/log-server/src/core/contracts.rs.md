---
source: log-server/src/core/contracts.rs
workspace: log-server
type: code-mirror
status: auto-generated
last_sync: 2026-11-10T13:21:51.380906
---

# Mirror: contracts.rs

## 📝 Description
Automatically generated mirror for `log-server/src/core/contracts.rs`.

> **Essential Process**:
> ! Constructs exhaustive, compile-time embedded Exchange Contracts directly ! from log-server schemas (log_service.proto, logger.capnp, and SafeSocket framing) ! and publishes ServiceSpec metadata to web-interface. ! ! DATA FLOW: ! 1. Active AppConfig + Config -> build_exchange_contracts_value() / resolve_web_interface_addr() ! 2. spawn_web_interface_registration() -> HTTP POST /api/v1/register -> web-interface ! ! KEY PARAMETERS: ! - config: Runtime TCP/gRPC host and port configuration. ! - ring_capacity: In-memory LogRingBuffer capacity reported in ServiceSpec. ! - app_config: Active pre-loaded AppConfig for web_interface service discovery. use microservice_toolbox::config::loader::AppConfig; pub use microservice_toolbox::contracts::LOGGER_CAPNP_SCHEMA; use microservice_toolbox::contracts::extract_capnp_operations; use serde_json::{json, Value}; use std::time::Duration; use tokio::io::{AsyncReadExt, AsyncWriteExt}; use tokio::net::TcpStream; use crate::config::config::Config; pub const LOG_SERVICE_PROTO: &str = include_str!("../schema/proto/log_service.proto");

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/log-server/src/config/config.rs.md|Config.with_grpc_host]] (method: calls) — *Override the gRPC bind host verbatim*
- [[log-server/log-server/src/config/config.rs.md|Config]] (struct: calls) — *Server configuration*
- [[log-server/log-server/src/config/config.rs.md|config.rs]] (imports)
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer.new]] (method: calls) — *Create new ring buffer with given capacity and internal broadcast channel*
- [[log-server/log-server/src/core/ring_buffer.rs.md|ring_buffer.rs]] (same_package)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/core/contracts.rs.md|LOG_SERVICE_PROTO]] (constant: belongs_to)
- [[log-server/log-server/src/core/contracts.rs.md|build_exchange_contracts_json]] (function: belongs_to) — *Build JSON string of exchange contracts for gRPC GetExchangeContracts.*
- [[log-server/log-server/src/core/contracts.rs.md|build_exchange_contracts_value]] (function: belongs_to) — *Build exhaustive list of log-server exchange contracts anchored to runtime config & real schema files.*
- [[log-server/log-server/src/core/contracts.rs.md|build_service_spec_payload]] (function: belongs_to) — *Build canonical OpenMFE ServiceSpec payload for POST /api/v1/register on web-interface.*
- [[log-server/log-server/src/core/contracts.rs.md|display_host]] (function: belongs_to)
- [[log-server/log-server/src/core/contracts.rs.md|resolve_web_interface_addr]] (function: belongs_to) — *Resolve the `web_interface` registration address from the active `AppConfig`.*
- [[log-server/log-server/src/core/contracts.rs.md|spawn_web_interface_registration]] (function: belongs_to) — *Non-blocking 30s heartbeat registering log-server's authoritative contracts with web-interface.*
- [[log-server/log-server/src/core/contracts.rs.md|test_build_exchange_contracts_embeds_real_schemas]] (function: belongs_to)
- [[log-server/log-server/src/core/contracts.rs.md|test_display_host_normalization]] (function: belongs_to)
- [[log-server/log-server/src/core/contracts.rs.md|test_resolve_web_interface_addr_from_app_config]] (function: belongs_to)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (calls)
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (calls)
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
