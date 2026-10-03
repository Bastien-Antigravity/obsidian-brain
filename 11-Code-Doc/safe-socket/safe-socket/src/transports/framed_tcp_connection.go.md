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
Automatically generated mirror for `safe-socket/src/transports/framed_tcp_connection.go`.

> **Essential Process**:
> Implements length-prefixed TCP streaming transport (FramedTCPSocket), framing application payloads with 4-byte big-endian integers and handling framed packet read and write streams with idle deadline refreshes.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.Close]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.LocalAddr]] (method: defines_method) — *LocalAddr returns the local network address.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.ReadMessage]] (method: defines_method) — *HEARTBEAT UPDATE: Automatically skips frames with length 0.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.Read]] (method: defines_method) — *HEARTBEAT UPDATE: Automatically skips frames with length 0.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.RemoteAddr]] (method: defines_method) — *RemoteAddr returns the remote network address.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetDeadline]] (method: defines_method) — *SetDeadline sets the read and write deadlines associated with the connection.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetIdleTimeout]] (method: defines_method) — *SetIdleTimeout updates the internal idle timeout and refreshes current deadlines.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetKeepAlive]] (method: defines_method) — *SetKeepAlive enables TCP keepalive with the specified period.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetNoDelay]] (method: defines_method) — *SetNoDelay controls Nagle's algorithm (true = disable Nagle, lower latency).*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetReadBuffer]] (method: defines_method) — *SetReadBuffer sets the size of the operating system's receive buffer.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetReadDeadline]] (method: defines_method) — *SetReadDeadline sets the deadline for future Read calls.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetWriteBuffer]] (method: defines_method) — *SetWriteBuffer sets the size of the operating system's transmit buffer.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetWriteDeadline]] (method: defines_method) — *SetWriteDeadline sets the deadline for future Write calls.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.Write]] (method: defines_method) — *Write prepends length and writes data.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.refreshReadDeadline]] (method: defines_method)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.refreshWriteDeadline]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[safe-socket/safe-socket/src/facade/heartbeat_restart_test.go.md|heartbeat_restart_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/forever_test.go.md|forever_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/forever_test.go.md|forever_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/framed_tcp_client.go.md|framed_tcp_client.go]] (calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_client.go.md|framed_tcp_client.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.Close]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.LocalAddr]] (method: belongs_to) — *LocalAddr returns the local network address.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.ReadMessage]] (method: belongs_to) — *HEARTBEAT UPDATE: Automatically skips frames with length 0.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.Read]] (method: belongs_to) — *HEARTBEAT UPDATE: Automatically skips frames with length 0.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.RemoteAddr]] (method: belongs_to) — *RemoteAddr returns the remote network address.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetDeadline]] (method: belongs_to) — *SetDeadline sets the read and write deadlines associated with the connection.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetIdleTimeout]] (method: belongs_to) — *SetIdleTimeout updates the internal idle timeout and refreshes current deadlines.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetKeepAlive]] (method: belongs_to) — *SetKeepAlive enables TCP keepalive with the specified period.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetNoDelay]] (method: belongs_to) — *SetNoDelay controls Nagle's algorithm (true = disable Nagle, lower latency).*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetReadBuffer]] (method: belongs_to) — *SetReadBuffer sets the size of the operating system's receive buffer.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetReadDeadline]] (method: belongs_to) — *SetReadDeadline sets the deadline for future Read calls.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetWriteBuffer]] (method: belongs_to) — *SetWriteBuffer sets the size of the operating system's transmit buffer.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.SetWriteDeadline]] (method: belongs_to) — *SetWriteDeadline sets the deadline for future Write calls.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.Write]] (method: belongs_to) — *Write prepends length and writes data.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.refreshReadDeadline]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket.refreshWriteDeadline]] (method: belongs_to)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket]] (struct: belongs_to) — *RemoteAddr returns the remote network address.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|FramedTCPSocket]] (struct: defines_method) — *RemoteAddr returns the remote network address.*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|MaxPayloadSize]] (constant: belongs_to) — *MaxPayloadSize defines the upper limit for incoming frames (default 64MB).*
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection.go.md|NewFramedTCPSocket]] (function: belongs_to)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection_test.go.md|framed_tcp_connection_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_connection_test.go.md|framed_tcp_connection_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|framed_tcp_server.go]] (calls)
- [[safe-socket/safe-socket/src/transports/framed_tcp_server.go.md|framed_tcp_server.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/heartbeat_test.go.md|heartbeat_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/heartbeat_test.go.md|heartbeat_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/oom_test.go.md|oom_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/oom_test.go.md|oom_test.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/shm_client.go.md|shm_client.go]] (calls)
- [[safe-socket/safe-socket/src/transports/shm_client.go.md|shm_client.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|shm_server.go]] (calls)
- [[safe-socket/safe-socket/src/transports/shm_server.go.md|shm_server.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/udp_client.go.md|udp_client.go]] (calls)
- [[safe-socket/safe-socket/src/transports/udp_client.go.md|udp_client.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|udp_server.go]] (calls)
- [[safe-socket/safe-socket/src/transports/udp_server.go.md|udp_server.go]] (same_package)
- [[safe-socket/safe-socket/src/transports/zombie_test.go.md|zombie_test.go]] (calls)
- [[safe-socket/safe-socket/src/transports/zombie_test.go.md|zombie_test.go]] (same_package)
<!-- SYNC:END -->
