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
Automatically generated mirror for `safe-socket/safesock/python/safesocket/safesocket.py`.

> **Essential Process**:
> Python wrapper for libsafesocket. Provides native access to the safe-socket ecosystem, allowing high-performance, resilient network connections across multiple protocols.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Accept]] (function: calls) — *export SafeSocket_Accept*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Close]] (function: calls) — *export SafeSocket_Close*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_CreateExtended]] (function: calls) — *export SafeSocket_CreateExtended*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_GetSocketError]] (function: calls) — *export SafeSocket_GetSocketError*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Listen]] (function: calls) — *export SafeSocket_Listen*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Open]] (function: calls) — *export SafeSocket_Open*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Receive]] (function: calls) — *export SafeSocket_Receive*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Send]] (function: calls) — *export SafeSocket_Send*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_SetDeadline]] (function: calls) — *export SafeSocket_SetDeadline*
- [[safe-socket/safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_SetIdleTimeout]] (function: calls) — *export SafeSocket_SetIdleTimeout*

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|SafeSocketConnection]] (class: belongs_to) — *Represents an active connection returned by Accept().*
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|SafeSocketError]] (class: belongs_to) — *Base exception for SafeSocket operations.*
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|SafeSocket]] (class: belongs_to) — *High-level Socket manager for Clients and Servers.*
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|SocketConfig]] (class: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|__enter__]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|__exit__]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|__init__]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|_get_last_error]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|accept]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|close]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|create]] (function: belongs_to) — *Simplified entry point matching Go safesocket.Create() signature.*
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|create_with_config]] (function: belongs_to) — *Advanced entry point matching Go safesocket.CreateWithConfig() signature.*
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|listen]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|open]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|receive]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|send]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|set_deadline]] (function: belongs_to)
- [[safe-socket/safe-socket/safesock/python/safesocket/safesocket.py.md|set_idle_timeout]] (function: belongs_to)
<!-- SYNC:END -->
