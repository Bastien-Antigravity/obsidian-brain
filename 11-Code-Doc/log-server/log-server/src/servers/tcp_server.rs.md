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
Automatically generated mirror for `log-server/src/servers/tcp_server.rs`.

> **Essential Process**:
> ! High-throughput TCP server handling SafeSocket-framed Cap'n Proto log streams ! from universal-logger instances across the microservice ecosystem. ! ! DATA FLOW: ! 1. TCP Stream -> SafeSocket framing -> Cap'n Proto deserialization ! 2. LogEntry + Sequence Counter -> LogPacket -> writer_tx ! ! KEY PARAMETERS: ! - host / port: Socket bind address (default 0.0.0.0:9020). ! - writer_tx: Channel to async file writer task. ! - sequence_counter: Atomic sequence tracking for global ordering. use crate::models::log_packet::LogPacket; use std::sync::atomic::AtomicU64; use std::sync::Arc; use tokio::net::{TcpListener, TcpStream}; use tokio::sync::mpsc; use tokio::time::{timeout, Duration}; use crate::config::config::Config; use crate::core::protocol_handlers::{handle_tcp_message, identify_client_from_handshake}; use crate::line_str; use crate::transport::safe_socket::SafeSocket; use crate::utils::terminal_ui::print_internal_log; / TCP server for Cap'n Proto log messages pub struct TcpServer { config: Config, }

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/log-server/src/config/config.rs.md|Config]] (struct: calls) — *Server configuration*
- [[log-server/log-server/src/config/config.rs.md|config.rs]] (imports)
- [[log-server/log-server/src/core/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/core/protocol_handlers.rs.md|handle_tcp_message]] (function: calls) — *Handle incoming TCP client connection*
- [[log-server/log-server/src/core/protocol_handlers.rs.md|identify_client_from_handshake]] (function: calls) — *without needing to manually link or re-generate safe-socket schemas in Rust.*
- [[log-server/log-server/src/core/protocol_handlers.rs.md|protocol_handlers.rs]] (imports)
- [[log-server/log-server/src/models/log_packet.rs.md|LogPacket]] (struct: calls) — *A packet containing a sequence number and the log entry*
- [[log-server/log-server/src/models/log_packet.rs.md|log_packet.rs]] (imports)
- [[log-server/log-server/src/models/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/protocols/capnp/logger_msg.rs.md|Reader<'_,>.clone]] (method: calls)
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer.handle_tcp_connection]] (method: defines_method) — *Handle individual TCP connection*
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer.name]] (method: defines_method) — *Get server name*
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer.new]] (method: defines_method) — *Create new TCP server*
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer.run]] (method: defines_method) — *Run the TCP server*
- [[log-server/log-server/src/transport/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocket.split]] (method: calls) — *Split into its component halves*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketReader.receive_data]] (method: calls) — *Receive framed data from socket. Automatically skips 0-length heartbeat frames.*
- [[log-server/log-server/src/transport/safe_socket.rs.md|SafeSocketWriter.send_heartbeat]] (method: calls) — *Send a 0-length heartbeat frame*
- [[log-server/log-server/src/transport/safe_socket.rs.md|safe_socket.rs]] (imports)
- [[log-server/log-server/src/utils/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|print_internal_log]] (function: calls) — *Formats and prints an internal server log message (visual alignment only)*
- [[log-server/log-server/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (imports)
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer.handle_tcp_connection]] (method: belongs_to) — *Handle individual TCP connection*
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer.name]] (method: belongs_to) — *Get server name*
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer.new]] (method: belongs_to) — *Create new TCP server*
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer.run]] (method: belongs_to) — *Run the TCP server*
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer]] (struct: belongs_to) — *TCP server for Cap'n Proto log messages*
- [[log-server/log-server/src/servers/tcp_server.rs.md|TcpServer]] (struct: defines_method) — *TCP server for Cap'n Proto log messages*
<!-- SYNC:END -->
