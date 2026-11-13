---
source: microservice-toolbox/rust/src/business/helpers.rs
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-11-11T05:40:10.032111
---

# Mirror: helpers.rs

## 📝 Description
Automatically generated mirror for `microservice-toolbox/rust/src/business/helpers.rs`.

> **Essential Process**:
> Helper utilities and conversion routines for core business domain models.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/serializer.py.md|T]] (constant: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|MarketEventType]] (enum: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|MarketEvent]] (struct: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|models.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|models.rs]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/helpers.rs.md|deserialize]] (function: belongs_to) — *Converts a JSON byte array into the target business object.*
- [[microservice-toolbox/microservice-toolbox/rust/src/business/helpers.rs.md|serialize]] (function: belongs_to) — *Converts a business object into a JSON byte array.*
- [[microservice-toolbox/microservice-toolbox/rust/src/business/helpers.rs.md|system_timestamp]] (function: belongs_to) — *Returns the current unix timestamp in milliseconds.*
- [[microservice-toolbox/microservice-toolbox/rust/src/business/helpers.rs.md|wrap_market_event]] (function: belongs_to) — *Creates a MarketEvent envelope for a typed business payload.*
- [[microservice-toolbox/microservice-toolbox/rust/src/business/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
