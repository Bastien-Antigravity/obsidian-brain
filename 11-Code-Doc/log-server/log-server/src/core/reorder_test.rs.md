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
> ! Regression tests for sequence reordering, gap detection, timeout recovery, ! buffer pressure handling, and late packet recovery. ! ! DATA FLOW: ! 1. Out-of-order LogPackets -> Writer task BTreeMap reorder buffer ! 2. Gap timeout force-flush triggers on missing sequence ! 3. Buffer saturation forces progression when buffer.len() >= batch_size ! 4. Late packets (sequence < current_sequence) write immediately ! ! KEY PARAMETERS: ! - gap_timeout_ms: Shortened interval (100ms) for fast, deterministic test execution. ! - initial_batch_size: Configured threshold for buffer saturation testing. [cfg(test)] mod tests { use crate::facade::log_writer::{LogWriter, WriterConfig}; use crate::models::log_entry::LogEntry; use crate::models::log_packet::LogPacket; use std::fs; use std::path::PathBuf; use std::sync::atomic::{AtomicU64, Ordering}; use tokio::time::{sleep, Duration}; static TEST_COUNTER: AtomicU64 = AtomicU64::new(0); fn unique_test_log_path(test_name: &str) -> (PathBuf, PathBuf) { let count = TEST_COUNTER.fetch_add(1, Ordering::SeqCst); let dir = std::env::temp_dir().join(format!( "log_server_test_{}_{}_{}", test_name, std::process::id(), count )); let _ = fs::create_dir_all(&dir); let log_file = dir.join("_main.log"); (dir, log_file) }

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer.get_tail]] (method: calls) — *Retrieve the most recent entries up to `limit`, with optional filters*
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer.new]] (method: calls) — *Create new ring buffer with given capacity and internal broadcast channel*
- [[log-server/log-server/src/core/ring_buffer.rs.md|ring_buffer.rs]] (same_package)
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.start_writer_task]] (method: calls) — *and the background task JoinHandle for lifecycle supervision and fail-fast termination.*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.with_config_and_path]] (method: calls) — *Create new log writer with custom config and explicit file path*
- [[log-server/log-server/src/facade/log_writer.rs.md|WriterConfig.default]] (method: calls)
- [[log-server/log-server/src/facade/log_writer.rs.md|WriterConfig]] (struct: calls) — *Log writer configuration*
- [[log-server/log-server/src/facade/log_writer.rs.md|log_writer.rs]] (imports)
- [[log-server/log-server/src/facade/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/models/log_entry.rs.md|LogEntry]] (struct: calls) — *Internal log request wrapper for internal use*
- [[log-server/log-server/src/models/log_entry.rs.md|log_entry.rs]] (imports)
- [[log-server/log-server/src/models/log_packet.rs.md|LogPacket]] (struct: calls) — *A packet containing a sequence number and the log entry*
- [[log-server/log-server/src/models/log_packet.rs.md|log_packet.rs]] (imports)
- [[log-server/log-server/src/models/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/protocols/capnp/logger_msg.rs.md|Reader<'_,>.clone]] (method: calls)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/core/reorder_test.rs.md|test_buffer_pressure_force_progress]] (function: belongs_to)
- [[log-server/log-server/src/core/reorder_test.rs.md|test_gap_timeout_recovery]] (function: belongs_to)
- [[log-server/log-server/src/core/reorder_test.rs.md|test_late_arriving_sequence_written_directly]] (function: belongs_to)
- [[log-server/log-server/src/core/reorder_test.rs.md|test_reorder_out_of_order_stream]] (function: belongs_to)
- [[log-server/log-server/src/core/reorder_test.rs.md|unique_test_log_path]] (function: belongs_to)
<!-- SYNC:END -->
