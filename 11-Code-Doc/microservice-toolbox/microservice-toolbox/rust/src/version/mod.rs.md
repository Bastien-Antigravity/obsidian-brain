---
source: microservice-toolbox/rust/src/version/mod.rs
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-10-22 16:53:58.819606
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: mod.rs

## 📝 Description
Automatically generated mirror for `microservice-toolbox/rust/src/version/mod.rs`.

> **Essential Process**:
> Standardized dynamic version resolution for Rust microservices and crates. Adheres to VERSION.txt as the ecosystem Single Source of Truth with caching.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/version/mod.rs.md|climb_dir_for_version]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/version/mod.rs.md|climb_for_version]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/version/mod.rs.md|compile_time_version]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/version/mod.rs.md|get_version]] (function: belongs_to) — *Panics fail-fast if VERSION.txt and environment overrides are all absent.*
- [[microservice-toolbox/microservice-toolbox/rust/src/version/mod.rs.md|read_version_file]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/version/mod.rs.md|reset_version]] (function: belongs_to) — *Clears the cached version so the next `get_version()` re-resolves.*
- [[microservice-toolbox/microservice-toolbox/rust/src/version/mod.rs.md|resolve_version]] (function: belongs_to) — *Panics fail-fast if unresolved.*
- [[microservice-toolbox/microservice-toolbox/rust/src/version/mod.rs.md|resolve_version_with_hints]] (function: belongs_to) — *Panics fail-fast if unresolved.*
- [[microservice-toolbox/microservice-toolbox/rust/src/version/mod.rs.md|set_version]] (function: belongs_to) — *Explicitly sets the cached version. Panics fail-fast on empty/whitespace values.*
- [[microservice-toolbox/microservice-toolbox/rust/src/version/mod.rs.md|setup_version]] (function: belongs_to) — *Emits `cargo:rustc-env=APP_VERSION=<version>` and `cargo:rerun-if-changed`, failing fast if absent.*
- [[microservice-toolbox/microservice-toolbox/rust/src/version/mod.rs.md|try_resolve_version]] (function: belongs_to) — *Non-panicking hierarchical semver resolution returning Err if VERSION.txt and env overrides are absent.*
- [[microservice-toolbox/microservice-toolbox/rust/src/version/mod.rs.md|try_resolve_version_in_dir]] (function: belongs_to) — *Non-panicking resolution scoped strictly to a specific starting directory (VERSION.txt only).*
- [[microservice-toolbox/microservice-toolbox/rust/src/version/mod.rs.md|try_resolve_version_with_hints]] (function: belongs_to) — *Non-panicking hierarchical semver resolution with optional explicit candidate paths.*
- [[microservice-toolbox/microservice-toolbox/rust/src/version/mod.rs.md|version_cache]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
