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
Automatically generated mirror for `log-server/src/core/reorder_test.rs`.

> **Essential Process**:
> ! Regression and concurrency tests for single-authority FIFO sequencing inside LogWriter, ! clean shutdown draining when senders drop, identical disk-to-ring-buffer ordering, ! and multi-producer concurrent burst ingestion without synthetic gaps or packet drops. ! ! DATA FLOW: ! 1. Concurrent producers / protocol handlers -> MPSC writer_tx channel ! 2. Single-authority LogWriter assigns monotonic sequence in FIFO dequeue order ! 3. Batched transactional writes to _main.log followed by exact-order LogRingBuffer commits ! 4. Clean loop termination when all writer_tx senders are dropped ! ! KEY PARAMETERS: ! - initial_batch_size: Dynamic burst draining threshold per write_batch syscall. ! - gap_timeout_ms: Periodic flush interval clamping window. [cfg(test)] mod tests { use crate::core::protocol_handlers::handle_grpc_message; use crate::facade::log_writer::{LogWriter, WriterConfig}; use crate::models::log_entry::LogEntry; use crate::models::log_packet::LogPacket; use std::fs; use std::path::PathBuf; use std::sync::atomic::{AtomicU64, Ordering}; use std::sync::Arc; use tokio::time::{sleep, timeout, Duration}; static TEST_COUNTER: AtomicU64 = AtomicU64::new(0); fn unique_test_log_path(test_name: &str) -> (PathBuf, PathBuf) { let count = TEST_COUNTER.fetch_add(1, Ordering::SeqCst); let dir = std::env::temp_dir().join(format!( "log_server_test_{}_{}_{}", test_name, std::process::id(), count )); let _ = fs::create_dir_all(&dir); let log_file = dir.join("_main.log"); (dir, log_file) }

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/src/core/mod.rs.md|mod.rs]] (imports)
- [[log-server/src/core/protocol_handlers.rs.md|handle_grpc_message]] (function: calls) — *Handle gRPC log message*
- [[log-server/src/core/protocol_handlers.rs.md|protocol_handlers.rs]] (imports)
- [[log-server/src/core/protocol_handlers.rs.md|protocol_handlers.rs]] (same_package)
- [[log-server/src/core/ring_buffer.rs.md|LogRingBuffer.get_tail]] (method: calls) — *Retrieve the most recent entries up to `limit`, with optional filters*
- [[log-server/src/core/ring_buffer.rs.md|LogRingBuffer.new]] (method: calls) — *Create new ring buffer with given capacity and internal broadcast channel*
- [[log-server/src/core/ring_buffer.rs.md|LogRingBuffer.push]] (method: calls) — *Push a new log entry into the circular buffer and broadcast to live subscribers*
- [[log-server/src/core/ring_buffer.rs.md|ring_buffer.rs]] (same_package)
- [[log-server/src/facade/log_writer.rs.md|LogWriter.start_writer_task]] (method: calls) — *and the background task JoinHandle for lifecycle supervision and fail-fast termination.*
- [[log-server/src/facade/log_writer.rs.md|LogWriter.with_config_and_path]] (method: calls) — *Create new log writer with custom config and explicit file path*
- [[log-server/src/facade/log_writer.rs.md|WriterConfig.default]] (method: calls)
- [[log-server/src/facade/log_writer.rs.md|WriterConfig]] (struct: calls) — *Log writer configuration*
- [[log-server/src/facade/log_writer.rs.md|log_writer.rs]] (imports)
- [[log-server/src/facade/mod.rs.md|mod.rs]] (imports)
- [[log-server/src/models/log_entry.rs.md|LogEntry]] (struct: calls) — *Internal log request wrapper for internal use*
- [[log-server/src/models/log_entry.rs.md|log_entry.rs]] (imports)
- [[log-server/src/models/log_packet.rs.md|LogPacket]] (struct: calls) — *A packet containing a sequence number and the log entry*
- [[log-server/src/models/log_packet.rs.md|log_packet.rs]] (imports)
- [[log-server/src/models/mod.rs.md|mod.rs]] (imports)
- [[log-server/src/protocols/capnp/logger_msg.rs.md|Reader<'_,>.clone]] (method: calls)
- [[log-server/src/transport/safe_socket.rs.md|SafeSocket.split]] (method: calls) — *Split into its component halves*

### 🔌 Consumers (Inbound)
- [[log-server/src/core/reorder_test.rs.md|test_clean_shutdown_drains_all_pending_messages_without_hanging]] (function: belongs_to)
- [[log-server/src/core/reorder_test.rs.md|test_concurrent_producers_1000_messages_strict_fifo_and_identical_disk_ring_order]] (function: belongs_to)
- [[log-server/src/core/reorder_test.rs.md|test_single_authority_fifo_ordering_ignores_caller_sequence_drift]] (function: belongs_to)
- [[log-server/src/core/reorder_test.rs.md|unique_test_log_path]] (function: belongs_to)
<!-- SYNC:END -->
