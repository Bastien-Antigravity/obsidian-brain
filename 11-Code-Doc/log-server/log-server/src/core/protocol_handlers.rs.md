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
Automatically generated mirror for `log-server/src/core/protocol_handlers.rs`.

> **Essential Process**:
> ! Binary protocol decoding and message validation handlers. Unpacks Cap'n Proto ! messages from SafeSocket frames and translates gRPC payloads into LogPacket instances. ! ! DATA FLOW: ! 1. SafeSocket bytes -> Cap'n Proto Reader -> LogEntry ! 2. gRPC ProtoLogRequest -> LogEntry ! 3. LogEntry + Sequence Counter -> LogPacket -> writer_tx ! ! KEY PARAMETERS: ! - identify_client_from_handshake: Extracts sender identity from initial connection. ! - handle_tcp_message: Unpacks packed Cap'n Proto bytes into LogPacket. ! - handle_grpc_message: Wraps gRPC LogEntry with sequence number into LogPacket. use crate::models::log_entry::LogEntry; use crate::models::log_packet::LogPacket; use capnp::{message::ReaderOptions, serialize, serialize_packed}; use std::sync::atomic::{AtomicU64, Ordering}; use std::sync::Arc; use tokio::sync::mpsc; [allow(clippy::all)] [rustfmt::skip] mod capnp_protocol { include!("../protocols/capnp/logger_msg.rs"); } / Identify client from SafeSocket Hello handshake (Unpacked Cap'n Proto) / / ⚠️ ARCHITECTURAL HACK: / This implementation abuses the fact that 'HelloMsg' (from safe-socket) and / 'LoggerMsg' (from log-server) both start with two Text fields at @0 and @1. / / Layout Comparison: / - HelloMsg:  @0:fromName, @1:fromHost / - LoggerMsg: @0:timestamp, @1:hostname / / This allows us to use the generated LoggerMsg reader to extract identity / without needing to manually link or re-generate safe-socket schemas in Rust. pub fn identify_client_from_handshake(data: &[u8]) -> Result<String, String> { Note: Handshake is UNPACKED, so we use serialize::read_message let reader = serialize::read_message(&mut &data[..], ReaderOptions::new()) .map_err(|e| format!("handshake read failed: {e}"))?; let hello_as_log = reader .get_root::<capnp_protocol::logger_msg::Reader<'_>>() .map_err(|e| format!("handshake root failed: {e}"))?; Extraction (using aliases for clarity) let from_name = hello_as_log .get_timestamp() // @0 -> fromName .map_err(|e| format!("failed to extract 'fromName' from handshake: {e}"))?; let from_host = hello_as_log .get_hostname() // @1 -> fromHost .map_err(|e| format!("failed to extract 'fromHost' from handshake: {e}"))?; Ok(format!( "{}@{}", from_name.to_str().map_err(|e| format!("invalid UTF-8 in fromName: {e}"))?, from_host.to_str().map_err(|e| format!("invalid UTF-8 in fromHost: {e}"))? )) }

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer.new]] (method: calls) — *Create new ring buffer with given capacity and internal broadcast channel*
- [[log-server/log-server/src/core/ring_buffer.rs.md|ring_buffer.rs]] (same_package)
- [[log-server/log-server/src/models/log_entry.rs.md|LogEntry]] (struct: calls) — *Internal log request wrapper for internal use*
- [[log-server/log-server/src/models/log_entry.rs.md|log_entry.rs]] (imports)
- [[log-server/log-server/src/models/log_packet.rs.md|LogPacket]] (struct: calls) — *A packet containing a sequence number and the log entry*
- [[log-server/log-server/src/models/log_packet.rs.md|log_packet.rs]] (imports)
- [[log-server/log-server/src/models/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/protocols/capnp/logger_msg.rs.md|Reader]] (struct: calls)
- [[log-server/log-server/src/protocols/capnp/mod.rs.md|mod.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/core/protocol_handlers.rs.md|handle_grpc_message]] (function: belongs_to) — *Handle gRPC log message*
- [[log-server/log-server/src/core/protocol_handlers.rs.md|handle_tcp_message]] (function: belongs_to) — *Handle incoming TCP client connection*
- [[log-server/log-server/src/core/protocol_handlers.rs.md|identify_client_from_handshake]] (function: belongs_to) — *without needing to manually link or re-generate safe-socket schemas in Rust.*
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (calls)
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (imports)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (calls)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (imports)
<!-- SYNC:END -->
