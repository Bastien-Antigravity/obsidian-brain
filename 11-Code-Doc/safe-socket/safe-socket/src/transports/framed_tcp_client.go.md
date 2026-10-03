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
Automatically generated mirror for `safe-socket/src/transports/framed_tcp_client.go`.

> **Essential Process**:
> Implements client dialing functions for plain and TLS-secured framed TCP connections.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/interfaces/transport.go.md|transport.go]] (imports)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetKeepAlive]] (method: calls) — *SetKeepAlive enables TCP keepalive with the specified period.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetNoDelay]] (method: calls) — *SetNoDelay controls Nagle's algorithm (true = disable Nagle, lower latency).*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetReadBuffer]] (method: calls) — *SetReadBuffer sets the size of the operating system's receive buffer.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetWriteBuffer]] (method: calls) — *SetWriteBuffer sets the size of the operating system's transmit buffer.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|NewFramedTCPSocket]] (function: calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|framed_tcp_connection.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/facade/socket_client.go.md|socket_client.go]] (calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_client.go.md|ConnectTLS]] (function: belongs_to) — *ConnectTLS dialer helper for TLS-wrapped FramedTCPSocket.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_client.go.md|Connect]] (function: belongs_to) — *Connect dialer helper for FramedTCPSocket.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_client.go.md|wrapTCP]] (function: belongs_to)
<!-- SYNC:END -->
