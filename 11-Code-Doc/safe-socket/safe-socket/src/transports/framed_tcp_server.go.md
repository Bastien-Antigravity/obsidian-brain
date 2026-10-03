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
Automatically generated mirror for `safe-socket/src/transports/framed_tcp_server.go`.

> **Essential Process**:
> Implements server listener implementations for cleartext and TLS-secured framed TCP sockets.

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
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|FramedTCPListener.Accept]] (method: defines_method) — *Accept waits for and returns the next connection to the listener.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|FramedTCPListener.Addr]] (method: defines_method) — *Addr returns the listener's network address.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|FramedTCPListener.Close]] (method: defines_method) — *Close closes the listener.*

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/facade/socket_server.go.md|socket_server.go]] (calls)
- [[safe-socket/safe-socket/src/transports/forever_test.go.md|forever_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/forever_test.go.md|forever_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection_test.go.md|framed_tcp_connection_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection_test.go.md|framed_tcp_connection_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|FramedTCPListener.Accept]] (method: belongs_to) — *Accept waits for and returns the next connection to the listener.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|FramedTCPListener.Addr]] (method: belongs_to) — *Addr returns the listener's network address.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|FramedTCPListener.Close]] (method: belongs_to) — *Close closes the listener.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|FramedTCPListener]] (struct: belongs_to) — *Addr returns the listener's network address.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|FramedTCPListener]] (struct: defines_method) — *Addr returns the listener's network address.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|ListenTLS]] (function: belongs_to) — *ListenTLS creates a new TLS-enabled FramedTCPListener.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|Listen]] (function: belongs_to) — *Listen creates a new FramedTCPListener.*
- [[safe-socket/safe-socket/src/transports/heartbeat_test.go.md|heartbeat_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/heartbeat_test.go.md|heartbeat_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/oom_test.go.md|oom_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/oom_test.go.md|oom_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/zombie_test.go.md|zombie_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/zombie_test.go.md|zombie_test.go]] (same_package)
<!-- SYNC:END -->
