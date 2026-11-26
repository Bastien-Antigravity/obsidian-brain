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
Automatically generated mirror for `log-server/src/utils/terminal_ui.rs`.

> **Essential Process**:
> ! Terminal UI formatting, ANSI color palettes, and internal log-server self-logging. ! ! DATA FLOW: ! 1. Internal logging calls -> print_internal_log() ! 2. Colored formatting output to stdout ! 3. Asynchronous FIFO queue dispatch to writer task for disk persistence ! ! KEY PARAMETERS: ! - INTERNAL_SENDER: OnceLock channel to writer task for self-logging. ! - INTERNAL_COUNTER: OnceLock atomic handle retained for signature compatibility. use chrono::Utc; use std::sync::atomic::{AtomicU64, Ordering}; use std::sync::{Arc, RwLock}; use tokio::sync::mpsc; use crate::models::log_entry::LogEntry; use crate::models::log_packet::LogPacket; use crate::utils::helpers::{get_hostname, truncate}; static INTERNAL_SENDER: RwLock<Option<mpsc::Sender<LogPacket>>> = RwLock::new(None); static INTERNAL_COUNTER: RwLock<Option<Arc<AtomicU64>>> = RwLock::new(None); static DROPPED_INTERNAL_LOGS: AtomicU64 = AtomicU64::new(0);

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/log-server/src/facade/log_writer.rs.md|WriterConfig.default]] (method: calls)
- [[log-server/log-server/src/models/log_entry.rs.md|LogEntry]] (struct: calls) — *Internal log request wrapper for internal use*
- [[log-server/log-server/src/models/log_entry.rs.md|log_entry.rs]] (imports)
- [[log-server/log-server/src/models/log_packet.rs.md|LogPacket]] (struct: calls) — *A packet containing a sequence number and the log entry*
- [[log-server/log-server/src/models/log_packet.rs.md|log_packet.rs]] (imports)
- [[log-server/log-server/src/models/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/protocols/capnp/logger_msg.rs.md|Reader<'_,>.clone]] (method: calls)
- [[log-server/log-server/src/utils/helpers.rs.md|get_hostname]] (function: calls) — *Get system hostname (cached)*
- [[log-server/log-server/src/utils/helpers.rs.md|helpers.rs]] (imports)
- [[log-server/log-server/src/utils/helpers.rs.md|helpers.rs]] (same_package)
- [[log-server/log-server/src/utils/mod.rs.md|mod.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/core/log_formatter.rs.md|log_formatter.rs]] (calls)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (calls)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (imports)
- [[log-server/log-server/src/main.rs.md|main.rs]] (calls)
- [[log-server/log-server/src/main.rs.md|main.rs]] (imports)
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (calls)
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (imports)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (calls)
- [[log-server/log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (imports)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|COLOR_CYAN]] (constant: belongs_to)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|COLOR_GREEN]] (constant: belongs_to)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|COLOR_MAGENTA]] (constant: belongs_to)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|COLOR_RED]] (constant: belongs_to)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|COLOR_RESET]] (constant: belongs_to) — *ANSI color codes*
- [[log-server/log-server/src/utils/terminal_ui.rs.md|COLOR_YELLOW]] (constant: belongs_to)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|clear_internal_logger]] (function: belongs_to) — *Clear the internal logger during graceful shutdown to drop the writer channel sender*
- [[log-server/log-server/src/utils/terminal_ui.rs.md|colorize_level]] (function: belongs_to) — *Returns colorized level string for console*
- [[log-server/log-server/src/utils/terminal_ui.rs.md|get_dropped_internal_logs]] (function: belongs_to) — *Returns total count of internal log messages dropped due to channel saturation*
- [[log-server/log-server/src/utils/terminal_ui.rs.md|print_internal_log]] (function: belongs_to) — *Formats and prints an internal server log message (visual alignment only)*
- [[log-server/log-server/src/utils/terminal_ui.rs.md|set_internal_logger]] (function: belongs_to) — *Initialize the internal logger with a sender and counter*
<!-- SYNC:END -->
