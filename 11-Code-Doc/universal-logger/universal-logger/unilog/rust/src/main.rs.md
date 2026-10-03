---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `universal-logger/unilog/rust/src/main.rs`.

> **Essential Process**:
> Rust example and demonstration CLI showcasing unilog-rs integration.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.add_metadata]] (method: calls) — *Adds a single metadata field to all future logs.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.get_config]] (method: calls) — *Retrieves a configuration value.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.log_with_metadata]] (method: calls) — *Logs a message with custom metadata.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.new]] (method: calls) — *Initializes a new logger session via the Go shared library.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.on_config_update]] (method: calls)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.set_config]] (method: calls) — *Updates a configuration value in memory.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.set_metadata]] (method: calls) — *Replaces all metadata with the provided JSON-serializable map.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|lib.rs]] (same_package)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/unilog/rust/src/main.rs.md|main]] (function: belongs_to)
<!-- SYNC:END -->
