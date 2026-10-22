---
source: microservice-toolbox/rust/src/version/mod.rs
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:58.819606
---

# Mirror: mod.rs

## 📝 Description
Automatically generated mirror for `microservice-toolbox/rust/src/version/mod.rs`.

> **Essential Process**:
> Standardized dynamic version resolution for Rust microservices and crates. Adheres to VERSION.txt as the ecosystem Single Source of Truth.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/version/mod.rs.md|DEFAULT_FALLBACK_VERSION]] (constant: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/version/mod.rs.md|climb_for_version]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/version/mod.rs.md|get_version]] (function: belongs_to) — *Returns the resolved semantic version for the running microservice.*
- [[microservice-toolbox/microservice-toolbox/rust/src/version/mod.rs.md|setup_version]] (function: belongs_to) — *Emits `cargo:rustc-env=APP_VERSION=<version>` and `cargo:rerun-if-changed`.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
