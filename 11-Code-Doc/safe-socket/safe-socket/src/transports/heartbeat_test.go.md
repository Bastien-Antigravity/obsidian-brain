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
Automatically generated mirror for `safe-socket/src/transports/heartbeat_test.go`.

> **Essential Process**:
> Unit tests verifying framed TCP heartbeat (ping/pong) transmission and consumption.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.Close]] (method: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.ReadMessage]] (method: calls) — *HEARTBEAT UPDATE: Automatically skips frames with length 0.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.Read]] (method: calls) — *HEARTBEAT UPDATE: Automatically skips frames with length 0.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.Write]] (method: calls) — *Write prepends length and writes data.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|NewFramedTCPSocket]] (function: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|framed_tcp_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|Listen]] (function: calls) — *Listen creates a new FramedTCPListener.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|framed_tcp_server.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|ShmAddr.String]] (method: calls)
- [[safe-socket/safe-socket/src/transports/shm_connection.go.md|shm_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener.Accept]] (method: calls) — *bound to that sender.*
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener.Addr]] (method: calls)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|udp_server.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/transports/heartbeat_test.go.md|TestFramedTCPHeartbeatReadMessage]] (function: belongs_to)
- [[safe-socket/safe-socket/src/transports/heartbeat_test.go.md|TestFramedTCPHeartbeatRead]] (function: belongs_to)
<!-- SYNC:END -->
