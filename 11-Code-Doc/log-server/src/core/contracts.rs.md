---
source: log-server/src/core/contracts.rs
workspace: log-server
type: code-mirror
status: auto-generated
last_sync: 2026-11-10 13:21:51.380906
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: contracts.rs

## 📝 Description
Automatically generated mirror for `log-server/src/core/contracts.rs`.

> **Essential Process**:
> ! Constructs exhaustive, compile-time embedded Exchange Contracts directly ! from log-server schemas (log_service.proto, logger.capnp, and SafeSocket framing) ! and publishes ServiceSpec metadata to web-interface. ! ! DATA FLOW: ! 1. Active AppConfig + Config -> build_exchange_contracts_value() / resolve_web_interface_addr() ! 2. spawn_web_interface_registration() -> HTTP POST /api/v1/register -> web-interface ! ! KEY PARAMETERS: ! - config: Runtime TCP/gRPC host and port configuration. ! - ring_capacity: In-memory LogRingBuffer capacity reported in ServiceSpec. ! - app_config: Active pre-loaded AppConfig for web_interface service discovery. use microservice_toolbox::config::loader::AppConfig; pub use microservice_toolbox::contracts::LOGGER_CAPNP_SCHEMA; use microservice_toolbox::contracts::extract_capnp_operations; use microservice_toolbox::spec::{publish, ExchangeContract, ServiceSpec}; use serde_json::{json, Value}; use std::collections::HashMap; use crate::config::config::Config; pub const LOG_SERVICE_PROTO: &str = include_str!("../schema/proto/log_service.proto");

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/src/config/config.rs.md|Config.with_grpc_host]] (method: calls) — *Override the gRPC bind host verbatim*
- [[log-server/src/config/config.rs.md|Config]] (struct: calls) — *Server configuration*
- [[log-server/src/config/config.rs.md|config.rs]] (imports)
- [[log-server/src/core/ring_buffer.rs.md|LogRingBuffer.new]] (method: calls) — *Create new ring buffer with given capacity and internal broadcast channel*
- [[log-server/src/core/ring_buffer.rs.md|ring_buffer.rs]] (same_package)
- [[log-server/src/facade/log_writer.rs.md|WriterConfig.default]] (method: calls)
- [[log-server/src/protocols/capnp/logger_msg.rs.md|Reader<'_,>.clone]] (method: calls)

### 🔌 Consumers (Inbound)
- [[log-server/src/core/contracts.rs.md|LOG_SERVICE_PROTO]] (constant: belongs_to)
- [[log-server/src/core/contracts.rs.md|build_exchange_contracts_json]] (function: belongs_to) — *Build JSON string of exchange contracts for gRPC GetExchangeContracts.*
- [[log-server/src/core/contracts.rs.md|build_exchange_contracts_value]] (function: belongs_to) — *Build exhaustive list of log-server exchange contracts anchored to runtime config & real schema files.*
- [[log-server/src/core/contracts.rs.md|build_service_spec]] (function: belongs_to) — *Build canonical OpenMFE ServiceSpec for log-server.*
- [[log-server/src/core/contracts.rs.md|build_service_spec_payload]] (function: belongs_to) — *Build canonical OpenMFE ServiceSpec payload JSON string for log-server.*
- [[log-server/src/core/contracts.rs.md|display_host]] (function: belongs_to)
- [[log-server/src/core/contracts.rs.md|resolve_web_interface_addr]] (function: belongs_to) — *Resolve the `web_interface` registration address from the active `AppConfig`.*
- [[log-server/src/core/contracts.rs.md|spawn_web_interface_registration]] (function: belongs_to) — *Non-blocking registration publishing log-server's ServiceSpec & ExchangeContracts via microservice-toolbox.*
- [[log-server/src/core/contracts.rs.md|test_build_exchange_contracts_embeds_real_schemas]] (function: belongs_to)
- [[log-server/src/core/contracts.rs.md|test_display_host_normalization]] (function: belongs_to)
- [[log-server/src/core/contracts.rs.md|test_resolve_web_interface_addr_from_app_config]] (function: belongs_to)
- [[log-server/src/facade/log_server.rs.md|log_server.rs]] (calls)
- [[log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (calls)
- [[log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
