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
Automatically generated mirror for `safe-socket/cmd/libsafesocket/main.go`.

> **Essential Process**:
> Exports C-compatible shared library symbols (libsafesocket) for polyglot consumers (Python, Rust, C++) to interact with safe-socket over the standard C ABI.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/cgo_bridge/errors.c.md|set_socket_error]] (function: calls)
- [[safe-socket/safe-socket/src/cgo_bridge/initialize.go.md|initialize.go]] (imports)
- [[safe-socket/safe-socket/src/cgo_bridge/sanitizer.go.md|SanitizeString]] (function: calls) — *SanitizeString ensures that strings coming from C are clean.*
- [[safe-socket/safe-socket/src/interfaces/logger.go.md|NoOpLogger.Error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Accept]] (function: belongs_to) — *export SafeSocket_Accept*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Close]] (function: belongs_to) — *export SafeSocket_Close*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_CreateExtended]] (function: belongs_to) — *export SafeSocket_CreateExtended*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Create]] (function: belongs_to) — *export SafeSocket_Create*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_FreeString]] (function: belongs_to) — *export SafeSocket_FreeString*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_GetSocketError]] (function: belongs_to) — *export SafeSocket_GetSocketError*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Listen]] (function: belongs_to) — *export SafeSocket_Listen*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Open]] (function: belongs_to) — *export SafeSocket_Open*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Receive]] (function: belongs_to) — *export SafeSocket_Receive*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Send]] (function: belongs_to) — *export SafeSocket_Send*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_SetDeadline]] (function: belongs_to) — *export SafeSocket_SetDeadline*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_SetIdleTimeout]] (function: belongs_to) — *export SafeSocket_SetIdleTimeout*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|main]] (function: belongs_to)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|setError]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.hpp]] (calls)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|safesocket.py]] (calls)
<!-- SYNC:END -->
