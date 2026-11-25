---
source: microservice-toolbox/rust/src/contracts.rs
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-11-23 01:29:28.226070
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: contracts.rs

## 📝 Description
Automatically generated mirror for `microservice-toolbox/rust/src/contracts.rs`.

> **Essential Process**:
> ! Re-exports canonical Exchange Contract types and IDL extractors from spec, ! together with compile-time embedded Platform Cap'n Proto Schemas (SSoT). ! ! DATA FLOW: ! 1. Embeds canonical logger.capnp and notifier.capnp from go/pkg/schemas (SSoT). ! 2. Exposes LOGGER_CAPNP_SCHEMA, NOTIFIER_CAPNP_SCHEMA, and extract_capnp_operations. ! ! KEY PARAMETERS: ! - LOGGER_CAPNP_SCHEMA: Canonical LoggerMsg Cap'n Proto IDL text. ! - NOTIFIER_CAPNP_SCHEMA: Canonical NotifierMsg Cap'n Proto IDL text. pub use crate::spec::{ build_contracts_envelope, display_address, extract_capnp_operations, extract_proto_operations, new_contracts_envelope, read_schema_file, resolve_contract_port, ContractOperation, ContractPeer, ContractsEnvelope, ExchangeContract, };

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/spec.rs.md|spec.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/contracts.rs.md|LOGGER_CAPNP_SCHEMA]] (constant: belongs_to) — *Canonical ecosystem Cap'n Proto LoggerMsg schema (SSoT).*
- [[microservice-toolbox/microservice-toolbox/rust/src/contracts.rs.md|NOTIFIER_CAPNP_SCHEMA]] (constant: belongs_to) — *Canonical ecosystem Cap'n Proto NotifierMsg schema (SSoT).*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
