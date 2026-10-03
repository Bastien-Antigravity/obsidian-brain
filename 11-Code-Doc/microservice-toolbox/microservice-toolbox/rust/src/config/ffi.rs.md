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
Automatically generated mirror for `microservice-toolbox/rust/src/config/ffi.rs`.

> **Essential Process**:
> Dynamic foreign function interface (FFI) bindings to the CGO libdistconf engine.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/ffi.rs.md|DistConfLib]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/ffi.rs.md|get_lib]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/ffi.rs.md|to_rust_string]] (function: belongs_to) — ** After calling this function, `c_ptr` must not be used again.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|loader.rs]] (imports)
<!-- SYNC:END -->
