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

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket.new]] (method: defines_method) — *Create new safe socket by splitting a TcpStream*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket.split]] (method: defines_method) — *Split into its component halves*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketReader.receive_data]] (method: defines_method) — *Receive framed data from socket. Automatically skips 0-length heartbeat frames.*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.send_data]] (method: defines_method) — *Send framed data to socket*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.send_heartbeat]] (method: defines_method) — *Send a 0-length heartbeat frame*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.shutdown]] (method: defines_method) — *Shutdown the underlying connection*

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/main.rs.md|main.rs]] (calls)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (calls)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (imports)
- [[log-server/log-server/src/transport/safe_socket.rs.md|MAX_MESSAGE_SIZE]] (constant: belongs_to) — *Maximum allowed message size (10MB) to prevent OOM attacks.*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket.new]] (method: belongs_to) — *Create new safe socket by splitting a TcpStream*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket.split]] (method: belongs_to) — *Split into its component halves*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketReader.receive_data]] (method: belongs_to) — *Receive framed data from socket. Automatically skips 0-length heartbeat frames.*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketReader]] (struct: belongs_to)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketReader]] (struct: defines_method)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.send_data]] (method: belongs_to) — *Send framed data to socket*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.send_heartbeat]] (method: belongs_to) — *Send a 0-length heartbeat frame*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.shutdown]] (method: belongs_to) — *Shutdown the underlying connection*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter]] (struct: belongs_to)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter]] (struct: defines_method)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket]] (struct: belongs_to)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket]] (struct: defines_method)
- [[log-server/log-server/src/transport/safe_socket.rs.md|test_heartbeat_skip]] (function: belongs_to)
<!-- SYNC:END -->
