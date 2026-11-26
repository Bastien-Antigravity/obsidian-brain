---
source: microservice-toolbox/rust/src/trace.rs
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-11-26T19:45:06.323227
---

# Mirror: trace.rs

## 📝 Description
Automatically generated mirror for `microservice-toolbox/rust/src/trace.rs`.

> **Essential Process**:
> Cross-service and cross-brain mission trace correlation (X-Bastien-Mission-ID) for Rust microservices. Sanitizes, extracts, injects, and binds mission_id into structured Logger metadata.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.add_metadata]] (method: calls)
- [[microservice-toolbox/rust/src/utils/logger.rs.md|Logger]] (trait: calls) — *Logger trait defines the standard interface for structured logging across the toolbox.*
- [[microservice-toolbox/rust/src/utils/logger.rs.md|UniLogger.new]] (method: calls)
- [[microservice-toolbox/rust/src/utils/logger.rs.md|logger.rs]] (imports)
- [[microservice-toolbox/rust/src/utils/mod.rs.md|mod.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/rust/src/trace.rs.md|ENV_MISSION_ID]] (constant: belongs_to)
- [[microservice-toolbox/rust/src/trace.rs.md|HEADER_MISSION_ID]] (constant: belongs_to)
- [[microservice-toolbox/rust/src/trace.rs.md|MAX_MISSION_ID_LEN]] (constant: belongs_to)
- [[microservice-toolbox/rust/src/trace.rs.md|METADATA_KEY]] (constant: belongs_to)
- [[microservice-toolbox/rust/src/trace.rs.md|bind_logger_mission]] (function: belongs_to) — *Binds mission_id onto a toolbox Logger when valid.*
- [[microservice-toolbox/rust/src/trace.rs.md|extract_mission_id]] (function: belongs_to) — *Extracts X-Bastien-Mission-ID case-insensitively from a string header map.*
- [[microservice-toolbox/rust/src/trace.rs.md|inject_mission_id]] (function: belongs_to) — *Injects X-Bastien-Mission-ID into an outbound header map if valid.*
- [[microservice-toolbox/rust/src/trace.rs.md|resolve_env_mission_id]] (function: belongs_to) — *Resolves X_BASTIEN_MISSION_ID from the process environment if set and valid.*
- [[microservice-toolbox/rust/src/trace.rs.md|sanitize_mission_id]] (function: belongs_to) — *Validates and trims a raw mission ID, rejecting whitespace/control characters or >128 bytes.*
- [[microservice-toolbox/rust/src/trace.rs.md|test_mission_id_roundtrip_and_sanitize]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
