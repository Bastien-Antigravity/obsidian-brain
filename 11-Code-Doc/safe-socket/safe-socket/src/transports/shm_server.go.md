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
Automatically generated mirror for `safe-socket/src/transports/shm_server.go`.

> **Essential Process**:
> Implements server listener handling for shared memory (SHM) point-to-point IPC.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.LocalAddr]] (method: calls) — *LocalAddr returns the local network address.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|framed_tcp_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|NewShmTransport]] (function: calls)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|shm_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|ShmListener.Accept]] (method: defines_method) — *Note: Current implementation is 1-to-1 (Point-to-Point).*
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|ShmListener.Addr]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|ShmListener.Close]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (calls)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|ListenShm]] (function: belongs_to) — *ListenShm creates (or opens) the SHM file and prepares it for a client connection.*
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|ShmListener.Accept]] (method: belongs_to) — *Note: Current implementation is 1-to-1 (Point-to-Point).*
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|ShmListener.Addr]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|ShmListener.Close]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|ShmListener]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|ShmListener]] (struct: defines_method)
<!-- SYNC:END -->
