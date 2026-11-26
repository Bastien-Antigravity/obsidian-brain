---
microservice: safe-socket
type: note
status: active
tags:
- '#service/safe-socket'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `safe-socket/safesock/cpp/SafeSocket.hpp`.

> **Essential Process**:
> C++ header-only client wrapper for the safe-socket library, providing RAII connection management, framed read/write operations, and CGO bridge interop.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Accept]] (function: calls) — *export SafeSocket_Accept*
- [[safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Close]] (function: calls) — *export SafeSocket_Close*
- [[safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_CreateExtended]] (function: calls) — *export SafeSocket_CreateExtended*
- [[safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_GetSocketError]] (function: calls) — *export SafeSocket_GetSocketError*
- [[safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Listen]] (function: calls) — *export SafeSocket_Listen*
- [[safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Open]] (function: calls) — *export SafeSocket_Open*
- [[safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Receive]] (function: calls) — *export SafeSocket_Receive*
- [[safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_Send]] (function: calls) — *export SafeSocket_Send*
- [[safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_SetDeadline]] (function: calls) — *export SafeSocket_SetDeadline*
- [[safe-socket/cmd/libsafesocket/main.go.md|SafeSocket_SetIdleTimeout]] (function: calls) — *export SafeSocket_SetIdleTimeout*
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.SafeSocket]] (method: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.accept]] (method: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.close]] (method: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.getLastError]] (method: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.listen]] (method: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.open]] (method: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.receive]] (method: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.send]] (method: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.set_deadline]] (method: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.set_idle_timeout]] (method: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketConnection.SafeSocketConnection]] (method: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketConnection.close]] (method: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketConnection.getLastError]] (method: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketConnection.receive]] (method: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketConnection.send]] (method: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketConnection.set_deadline]] (method: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketConnection.set_idle_timeout]] (method: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketError.SafeSocketError]] (method: defines_method)
- [[safe-socket/safesock/libsafesocket/libsafesocket.h.md|libsafesocket.h]] (imports)

### 🔌 Consumers (Inbound)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SAFESOCKET_HPP]] (macro: belongs_to) — *ifndef SAFESOCKET_HPP*
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.SafeSocket]] (method: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.accept]] (method: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.close]] (method: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.getLastError]] (method: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.listen]] (method: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.open]] (method: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.receive]] (method: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.send]] (method: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.set_deadline]] (method: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket.set_idle_timeout]] (method: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketConnection.SafeSocketConnection]] (method: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketConnection.close]] (method: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketConnection.getLastError]] (method: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketConnection.receive]] (method: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketConnection.send]] (method: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketConnection.set_deadline]] (method: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketConnection.set_idle_timeout]] (method: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketConnection]] (class: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketConnection]] (class: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketError.SafeSocketError]] (method: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketError]] (class: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocketError]] (class: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket]] (class: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SafeSocket]] (class: defines_method)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|SocketConfig]] (struct: belongs_to)
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|create]] (function: belongs_to) — *Factory functions*
- [[safe-socket/safesock/cpp/SafeSocket.hpp.md|create_with_config]] (function: belongs_to)
- [[safe-socket/safesock/cpp/examples/basic_usage.cpp.md|basic_usage.cpp]] (calls)
- [[safe-socket/safesock/cpp/examples/basic_usage.cpp.md|basic_usage.cpp]] (imports)
- [[safe-socket/safesock/cpp/examples/matrix_client.cpp.md|matrix_client.cpp]] (calls)
- [[safe-socket/safesock/cpp/examples/matrix_client.cpp.md|matrix_client.cpp]] (imports)
<!-- SYNC:END -->
