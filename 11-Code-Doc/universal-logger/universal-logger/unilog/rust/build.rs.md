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
Automatically generated mirror for `universal-logger/unilog/rust/build.rs`.

> **Essential Process**:
> Cargo build script for unilog-rs, locating, compiling, and linking libunilog shared dynamic library across macOS, Linux, and Windows.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.new]] (method: calls) — *Initializes a new logger session via the Go shared library.*

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/unilog/rust/build.rs.md|main]] (function: belongs_to)
<!-- SYNC:END -->
