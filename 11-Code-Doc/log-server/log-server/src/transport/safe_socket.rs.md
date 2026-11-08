---
microservice: log-server
type: note
status: active
tags:
- '#service/log-server'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `log-server/src/transport/safe_socket.rs`.

> **Essential Process**:
> ! Safe TCP socket wrapper with 4-byte big-endian length prefix framing, ! zero-length heartbeat packet filtering, and split read/write halves. ! ! DATA FLOW: ! 1. TcpStream -> SafeSocket::new() -> (SafeSocketReader, SafeSocketWriter) ! 2. SafeSocketReader::receive() -> Discards heartbeats -> Returns payload bytes ! ! KEY PARAMETERS: ! - MAX_MESSAGE_SIZE: 10MB guard against unbounded allocation attacks. ! - 4-byte big-endian integer length framing header. use bytes::{BufMut, BytesMut}; use tokio::io::{self, AsyncReadExt, AsyncWriteExt}; use tokio::net::tcp::{OwnedReadHalf, OwnedWriteHalf}; use tokio::net::TcpStream; / Reader half of a safe socket pub struct SafeSocketReader { reader: OwnedReadHalf, } / Maximum allowed message size (10MB) to prevent OOM attacks. const MAX_MESSAGE_SIZE: usize = 10 * 1024 * 1024; / Writer half of a safe socket pub struct SafeSocketWriter { writer: OwnedWriteHalf, } / Safe TCP socket with message framing pub struct SafeSocket { pub reader: SafeSocketReader, pub writer: SafeSocketWriter, }

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket.new]] (method: defines_method)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket.split]] (method: defines_method)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketReader.receive_data]] (method: defines_method) — *Receive framed data from socket. Returns empty BytesMut on 0-length heartbeat frames.*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.send_data]] (method: defines_method)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.send_heartbeat]] (method: defines_method)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.shutdown]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (calls)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (imports)
- [[log-server/log-server/src/transport/safe_socket.rs.md|MAX_MESSAGE_SIZE]] (constant: belongs_to) — *Maximum allowed message size (10MB) to prevent OOM attacks.*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket.new]] (method: belongs_to)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket.split]] (method: belongs_to)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketReader.receive_data]] (method: belongs_to) — *Receive framed data from socket. Returns empty BytesMut on 0-length heartbeat frames.*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketReader]] (struct: belongs_to) — *Reader half of a safe socket*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketReader]] (struct: defines_method) — *Reader half of a safe socket*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.send_data]] (method: belongs_to)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.send_heartbeat]] (method: belongs_to)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.shutdown]] (method: belongs_to)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter]] (struct: belongs_to) — *Writer half of a safe socket*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter]] (struct: defines_method) — *Writer half of a safe socket*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket]] (struct: belongs_to) — *Safe TCP socket with message framing*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket]] (struct: defines_method) — *Safe TCP socket with message framing*
- [[log-server/log-server/src/transport/safe_socket.rs.md|test_heartbeat_skip]] (function: belongs_to)
<!-- SYNC:END -->
