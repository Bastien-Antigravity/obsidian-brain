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
Automatically generated mirror for `safe-socket/src/cgo_bridge/socket.go`.

> **Essential Process**:
> Implements Go-level orchestration for CGO bridge functions, exposing socket lifecycle (create, open, accept, read, write, close) through integer handles.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/safe_socket.go.md|safe_socket.go]] (imports)
- [[safe-socket/safe-socket/src/cgo_bridge/initialize.go.md|Get]] (function: calls) — *Get retrieves a value from the registry.*
- [[safe-socket/safe-socket/src/cgo_bridge/initialize.go.md|Register]] (function: calls) — *Register stores a socket/connection and returns a handle.*
- [[safe-socket/safe-socket/src/cgo_bridge/initialize.go.md|Unregister]] (function: calls) — *Unregister removes a handle from the registry.*
- [[safe-socket/safe-socket/src/cgo_bridge/initialize.go.md|initialize.go]] (same_package)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|Accept]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|Close]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|CreateWithConfig]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|Create]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|Listen]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|Open]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|Receive]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|Send]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|SetDeadline]] (function: belongs_to)
- [[safe-socket/safe-socket/src/cgo_bridge/socket.go.md|SetIdleTimeout]] (function: belongs_to)
<!-- SYNC:END -->
