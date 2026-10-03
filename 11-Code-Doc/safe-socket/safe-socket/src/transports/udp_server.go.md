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
Automatically generated mirror for `safe-socket/src/transports/udp_server.go`.

> **Essential Process**:
> Implements UDP listener handling for receiving connectionless datagram packets and converting them into virtual connection streams for the socket server.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.LocalAddr]] (method: calls) — *LocalAddr returns the local network address.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetReadBuffer]] (method: calls) — *SetReadBuffer sets the size of the operating system's receive buffer.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetReadDeadline]] (method: calls) — *SetReadDeadline sets the deadline for future Read calls.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetWriteBuffer]] (method: calls) — *SetWriteBuffer sets the size of the operating system's transmit buffer.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|framed_tcp_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|NewTransientUdpSocket]] (function: calls) — *NewTransientUdpSocket creates a socket representing a single packet from a sender.*
- [[safe-socket/safe-socket/src/transports/udp_connection.go.md|udp_connection.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener.Accept]] (method: defines_method) — *bound to that sender.*
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener.Addr]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener.Close]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (calls)
- [[safe-socket/safe-socket/src/transports/forever_test.go.md|forever_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/forever_test.go.md|forever_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection_test.go.md|framed_tcp_connection_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection_test.go.md|framed_tcp_connection_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/heartbeat_test.go.md|heartbeat_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/heartbeat_test.go.md|heartbeat_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/oom_test.go.md|oom_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/oom_test.go.md|oom_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|ListenUDP]] (function: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener.Accept]] (method: belongs_to) — *bound to that sender.*
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener.Addr]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener.Close]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener]] (struct: belongs_to)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|UdpListener]] (struct: defines_method)
- [[safe-socket/safe-socket/src/transports/zombie_test.go.md|zombie_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/zombie_test.go.md|zombie_test.go]] (same_package)
<!-- SYNC:END -->
