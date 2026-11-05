---
source: microservice-toolbox/rust/src/spec.rs
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-11-01 17:12:29.596505
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: spec.rs

## 📝 Description
Automatically generated mirror for `microservice-toolbox/rust/src/spec.rs`.

> **Essential Process**:
> ! Standardizes self-describing microservice specifications and dynamic ! registration with web-interface across the Bastien-Antigravity fleet for Rust. ! Auto-resolves runtime listen/REST addresses, dynamic semver, active ! profile, and documentation links from AppConfig. ! ! FAIL-FAST PRINCIPLE: ! Zero silent fallbacks, zero default values, and zero dummy placeholders. ! Microservices must explicitly declare their own specification metadata ! (name, tag, layer, category, description, doc_link, protocol, framing). ! Configuration addresses (including web_interface) must resolve strictly; ! missing capabilities, missing ports, or missing metadata FAIL FAST immediately. ! ! DATA FLOW: ! 1. Microservice ServiceSpec + Capability Name -> Dynamic AppConfig Lookups ! 2. Strict Fail-Fast Validation of all required fields & dynamic endpoints ! 3. POST to /api/v1/register with exponential backoff and randomized jitter ! ! KEY PARAMETERS: ! - app_config: Active AppConfig for capability host/port/version resolution. ! - logger: Universal Logger for status logging and retry diagnostics. ! - capability: Capability key in AppConfig e.g. "config_server". ! - base: Microservice-provided ServiceSpec containing domain metadata. use crate::config::loader::AppConfig; use crate::utils::logger::Logger; use serde::{Deserialize, Serialize}; use std::collections::HashMap; use std::sync::Arc; use std::time::Duration; use tokio::io::{AsyncReadExt, AsyncWriteExt}; use tokio::net::TcpStream;

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|get_grpc_listen_addr]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|get_listen_addr]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|get_rest_addr]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|loader.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/lifecycle/manager.rs.md|LifecycleManager.register_background]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.critical]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.debug]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.info]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|Logger]] (trait: calls) — *Logger trait defines the standard interface for structured logging across the toolbox.*
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|UniLogger.new]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|logger.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/mod.rs.md|mod.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/spec.rs.md|ProtocolSpec]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/spec.rs.md|ServiceSpec]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/spec.rs.md|_extract_port]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/spec.rs.md|build_spec_from_config]] (function: belongs_to) — *Zero silent fallback or dummy placeholders.*
- [[microservice-toolbox/microservice-toolbox/rust/src/spec.rs.md|publish]] (function: belongs_to) — *Dynamic registration alias adhering to fleet standards.*
- [[microservice-toolbox/microservice-toolbox/rust/src/spec.rs.md|publish_service_spec]] (function: belongs_to) — *FAIL-FAST: Validates web_interface reachability and specification synchronously before spawning.*
- [[microservice-toolbox/microservice-toolbox/rust/src/spec.rs.md|publish_service_spec_internal]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/spec.rs.md|publish_service_spec_sync]] (function: belongs_to) — *FAIL-FAST: Returns error immediately if web_interface or specification validation fails.*
- [[microservice-toolbox/microservice-toolbox/rust/src/spec.rs.md|publish_with_lifecycle]] (function: belongs_to) — *Dynamic registration with lifecycle integration alias adhering to fleet standards.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
