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
Automatically generated mirror for `log-server/src/facade/log_server.rs`.

> **Essential Process**:
> ! Main log server orchestrator coordinating TCP socket (Cap'n Proto) and ! high-throughput gRPC (HTTP/2) with single-authority FIFO asynchronous file writing, ! rotation, and real-time broadcast streaming. ! ! DATA FLOW: ! 1. TCP/gRPC clients -> writer_tx FIFO channel ! 2. WriterTask sequences and flushes ordered batches to files and updates LogRingBuffer ! 3. gRPC StreamLogs -> ring_buffer broadcast -> real-time HTTP/2 stream ! ! KEY PARAMETERS: ! - name: Microservice identity ("log_server"). ! - host / port: TCP socket binding (default 0.0.0.0:9020). ! - grpc_port: gRPC bridge endpoint (default 9021). use microservice_toolbox::config::loader::AppConfig; use std::sync::Arc; use crate::config::config::Config; use crate::core::ring_buffer::LogRingBuffer; use crate::facade::log_writer::LogWriter; use crate::line_str; use crate::servers::grpc_server::LogBridgeGateway; use crate::servers::tcp_server::TcpServer; use crate::utils::terminal_ui::print_internal_log; / Main log server orchestrator pub struct LogServer { name: String, config: Config, writer: Arc<LogWriter>, enable_grpc: bool, app_config: Option<Arc<AppConfig>>, }

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/src/config/config.rs.md|Config]] (struct: calls) — *Server configuration*
- [[log-server/src/config/config.rs.md|config.rs]] (imports)
- [[log-server/src/config/config.rs.md|parse_fsync_config]] (function: calls) — *Helper to parse fsync durability setting from AppConfig or environment*
- [[log-server/src/core/contracts.rs.md|spawn_web_interface_registration]] (function: calls) — *Non-blocking registration publishing log-server's ServiceSpec & ExchangeContracts via microservice-toolbox.*
- [[log-server/src/core/mod.rs.md|mod.rs]] (imports)
- [[log-server/src/core/ring_buffer.rs.md|ring_buffer.rs]] (imports)
- [[log-server/src/facade/log_server.rs.md|LogServer.is_sync_on_flush]] (method: defines_method) — *Query active hardware durability barrier (fsync) state.*
- [[log-server/src/facade/log_server.rs.md|LogServer.new]] (method: defines_method) — *Create new log server instance*
- [[log-server/src/facade/log_server.rs.md|LogServer.new_with_config]] (method: defines_method) — *Create new log server instance from a full `Config` and optional active `AppConfig`*
- [[log-server/src/facade/log_server.rs.md|LogServer.run]] (method: defines_method) — *Run the log server with all components*
- [[log-server/src/facade/log_server.rs.md|LogServer.set_sync_on_flush]] (method: defines_method) — *Dynamic runtime control for hardware durability barrier (fsync).*
- [[log-server/src/facade/log_writer.rs.md|LogWriter.start_writer_task]] (method: calls) — *and the background task JoinHandle for lifecycle supervision and fail-fast termination.*
- [[log-server/src/facade/log_writer.rs.md|LogWriter.with_config]] (method: calls) — *Create new log writer with custom config*
- [[log-server/src/facade/log_writer.rs.md|LogWriter]] (struct: calls) — *File writer with single-authority FIFO sequencing and rotation*
- [[log-server/src/facade/log_writer.rs.md|WriterConfig.default]] (method: calls)
- [[log-server/src/facade/log_writer.rs.md|WriterConfig]] (struct: calls) — *Log writer configuration*
- [[log-server/src/facade/log_writer.rs.md|log_writer.rs]] (imports)
- [[log-server/src/facade/log_writer.rs.md|log_writer.rs]] (same_package)
- [[log-server/src/facade/mod.rs.md|mod.rs]] (imports)
- [[log-server/src/protocols/capnp/logger_msg.rs.md|Reader<'_,>.clone]] (method: calls)
- [[log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (imports)
- [[log-server/src/servers/mod.rs.md|mod.rs]] (imports)
- [[log-server/src/servers/tcp_server.rs.md|tcp_server.rs]] (imports)
- [[log-server/src/utils/helpers.rs.md|create_log_folder]] (function: calls) — *Create log folder if not exists*
- [[log-server/src/utils/helpers.rs.md|resolve_log_dir]] (function: calls) — *Resolve target log directory: LOG_DIR env var -> /var/log/log-server (Docker) -> <exec_parent>/logs.*
- [[log-server/src/utils/mod.rs.md|mod.rs]] (imports)
- [[log-server/src/utils/terminal_ui.rs.md|print_internal_log]] (function: calls) — *Formats and prints an internal server log message (visual alignment only)*
- [[log-server/src/utils/terminal_ui.rs.md|set_internal_logger]] (function: calls) — *Initialize the internal logger with a sender and counter*
- [[log-server/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[log-server/src/facade/log_server.rs.md|LogServer.is_sync_on_flush]] (method: belongs_to) — *Query active hardware durability barrier (fsync) state.*
- [[log-server/src/facade/log_server.rs.md|LogServer.new]] (method: belongs_to) — *Create new log server instance*
- [[log-server/src/facade/log_server.rs.md|LogServer.new_with_config]] (method: belongs_to) — *Create new log server instance from a full `Config` and optional active `AppConfig`*
- [[log-server/src/facade/log_server.rs.md|LogServer.run]] (method: belongs_to) — *Run the log server with all components*
- [[log-server/src/facade/log_server.rs.md|LogServer.set_sync_on_flush]] (method: belongs_to) — *Dynamic runtime control for hardware durability barrier (fsync).*
- [[log-server/src/facade/log_server.rs.md|LogServer]] (struct: belongs_to) — *Main log server orchestrator*
- [[log-server/src/facade/log_server.rs.md|LogServer]] (struct: defines_method) — *Main log server orchestrator*
- [[log-server/src/lib.rs.md|lib.rs]] (imports)
- [[log-server/src/main.rs.md|main.rs]] (calls)
- [[log-server/src/main.rs.md|main.rs]] (imports)
<!-- SYNC:END -->
