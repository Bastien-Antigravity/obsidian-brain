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
Automatically generated mirror for `log-server/src/facade/log_writer.rs`.

> **Essential Process**:
> ! Asynchronous single-authority FIFO file writer and rotation coordinator. Assigns ! monotonic sequence numbers upon channel dequeue, drains bursts into contiguous batches, ! flushes transactionally to _main.log, handles size-based rotation, and feeds the ! in-memory circular ring buffer in exact persistence order. ! ! DATA FLOW: ! 1. LogPacket stream from MPSC channel (FIFO arrival order) ! 2. Single-authority sequence assignment and burst draining up to batch_size ! 3. Transactional disk batch write, rotation check, and flush ! 4. Committed LogRingBuffer publication and non-blocking background console dispatch ! ! KEY PARAMETERS: ! - max_file_bytes: 10MB per log chunk before rotation. ! - backup_count: Number of historical rotated log files preserved (default 10). ! - gap_timeout_ms: Periodic flush interval clamping window in milliseconds. use crate::core::log_formatter::format_log_message; use crate::core::transactional_writer::TransactionalFileWriter; use crate::models::log_entry::LogEntry; use crate::models::log_packet::LogPacket; use crate::utils::helpers::{get_hostname, get_utc_timestamp}; use std::path::PathBuf; use std::sync::atomic::AtomicBool; use std::sync::Arc; use tokio::{ sync::mpsc, time::Duration, }; / Log writer configuration [derive(Clone)] pub struct WriterConfig { pub initial_batch_size: usize, pub buffer_size: usize, pub max_retries: usize, pub retry_delay_ms: u64, pub max_file_bytes: u64, pub backup_count: usize, pub gap_timeout_ms: u64, pub sync_on_flush: Arc<AtomicBool>, }

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/log-server/src/core/log_formatter.rs.md|format_log_message]] (function: calls) — *Unified log message formatting - used by both protocols*
- [[log-server/log-server/src/core/log_formatter.rs.md|log_formatter.rs]] (imports)
- [[log-server/log-server/src/core/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer.get_tail]] (method: calls) — *Retrieve the most recent entries up to `limit`, with optional filters*
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer.push]] (method: calls) — *Push a new log entry into the circular buffer and broadcast to live subscribers*
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer]] (struct: calls) — *Thread-safe in-memory circular ring buffer with real-time broadcast*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.check_and_rotate]] (method: calls) — *Check if rotation threshold is met and perform cascading rotation*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.flush]] (method: calls) — *Flush the active file to disk, optionally executing hardware durability commit (fsync/fdatasync).*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.with_sync]] (method: calls) — *Initialize a transactional file writer with a shared hardware durability barrier atomic*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.write_batch]] (method: calls) — *- Tier 3: Poisoned handle recovery (close and reopen) if rollback fails.*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter]] (struct: calls) — *Transactional log file manager providing atomic batch commits and rollback*
- [[log-server/log-server/src/core/transactional_writer.rs.md|transactional_writer.rs]] (imports)
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter._flush_pending_batch]] (method: defines_method) — *Writes pending batch to disk, performs rotation check, flushes, and publishes to ring buffer*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter._stage_packet]] (method: defines_method) — *Assigns monotonic sequence ID, dispatches console formatting, and stages file batch entry*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.is_sync_on_flush]] (method: defines_method) — *Query active hardware durability barrier (fsync) state.*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.new]] (method: defines_method) — *Create new log writer with default config*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.rotate_files]] (method: defines_method) — *Rotate log files (delegates to TransactionalFileWriter)*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.set_sync_on_flush]] (method: defines_method) — *Dynamically toggle hardware durability barrier (fsync) on the fly.*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.start_writer_task]] (method: defines_method) — *and the background task JoinHandle for lifecycle supervision and fail-fast termination.*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.sync_on_flush_handle]] (method: defines_method) — *Access the underlying shared atomic boolean handle.*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.with_config]] (method: defines_method) — *Create new log writer with custom config*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.with_config_and_path]] (method: defines_method) — *Create new log writer with custom config and explicit file path*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.writer_task]] (method: defines_method) — *Main writer task implementation (single serialization and sequence authority)*
- [[log-server/log-server/src/facade/log_writer.rs.md|WriterConfig.default]] (method: defines_method)
- [[log-server/log-server/src/models/log_entry.rs.md|LEVEL_STRINGS]] (constant: calls) — *Human-readable log level strings*
- [[log-server/log-server/src/models/log_entry.rs.md|LogEntry]] (struct: calls) — *Internal log request wrapper for internal use*
- [[log-server/log-server/src/models/log_entry.rs.md|log_entry.rs]] (imports)
- [[log-server/log-server/src/models/log_packet.rs.md|LogPacket]] (struct: calls) — *A packet containing a sequence number and the log entry*
- [[log-server/log-server/src/models/log_packet.rs.md|log_packet.rs]] (imports)
- [[log-server/log-server/src/models/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/protocols/capnp/logger_msg.rs.md|Reader<'_,>.clone]] (method: calls)
- [[log-server/log-server/src/utils/helpers.rs.md|create_log_folder]] (function: calls) — *Create log folder if not exists*
- [[log-server/log-server/src/utils/helpers.rs.md|get_hostname]] (function: calls) — *Get system hostname (cached)*
- [[log-server/log-server/src/utils/helpers.rs.md|get_utc_timestamp]] (function: calls) — *Get current UTC timestamp as string*
- [[log-server/log-server/src/utils/helpers.rs.md|helpers.rs]] (imports)
- [[log-server/log-server/src/utils/helpers.rs.md|resolve_log_dir]] (function: calls) — *Resolve target log directory: LOG_DIR env var -> /var/log/log-server (Docker) -> <exec_parent>/logs.*
- [[log-server/log-server/src/utils/mod.rs.md|mod.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/config/config.rs.md|config.rs]] (calls)
- [[log-server/log-server/src/core/reorder_test.rs.md|reorder_test.rs]] (calls)
- [[log-server/log-server/src/core/reorder_test.rs.md|reorder_test.rs]] (imports)
- [[log-server/log-server/src/core/ring_buffer.rs.md|ring_buffer.rs]] (calls)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (calls)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (imports)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (same_package)
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter._flush_pending_batch]] (method: belongs_to) — *Writes pending batch to disk, performs rotation check, flushes, and publishes to ring buffer*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter._stage_packet]] (method: belongs_to) — *Assigns monotonic sequence ID, dispatches console formatting, and stages file batch entry*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.is_sync_on_flush]] (method: belongs_to) — *Query active hardware durability barrier (fsync) state.*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.new]] (method: belongs_to) — *Create new log writer with default config*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.rotate_files]] (method: belongs_to) — *Rotate log files (delegates to TransactionalFileWriter)*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.set_sync_on_flush]] (method: belongs_to) — *Dynamically toggle hardware durability barrier (fsync) on the fly.*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.start_writer_task]] (method: belongs_to) — *and the background task JoinHandle for lifecycle supervision and fail-fast termination.*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.sync_on_flush_handle]] (method: belongs_to) — *Access the underlying shared atomic boolean handle.*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.with_config]] (method: belongs_to) — *Create new log writer with custom config*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.with_config_and_path]] (method: belongs_to) — *Create new log writer with custom config and explicit file path*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.writer_task]] (method: belongs_to) — *Main writer task implementation (single serialization and sequence authority)*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter]] (struct: belongs_to) — *File writer with single-authority FIFO sequencing and rotation*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter]] (struct: defines_method) — *File writer with single-authority FIFO sequencing and rotation*
- [[log-server/log-server/src/facade/log_writer.rs.md|WriterConfig.default]] (method: belongs_to)
- [[log-server/log-server/src/facade/log_writer.rs.md|WriterConfig]] (struct: belongs_to) — *Log writer configuration*
- [[log-server/log-server/src/facade/log_writer.rs.md|WriterConfig]] (struct: defines_method) — *Log writer configuration*
- [[log-server/log-server/src/facade/log_writer.rs.md|notify_disk_failure]] (function: belongs_to) — *Broadcast and record a fatal unrecoverable disk failure*
- [[log-server/log-server/src/facade/log_writer.rs.md|test_rotate_files_cascading_and_pruning]] (function: belongs_to)
- [[log-server/log-server/src/facade/log_writer.rs.md|test_rotate_files_zero_backups]] (function: belongs_to)
- [[log-server/log-server/src/facade/log_writer.rs.md|test_writer_task_fatal_disk_failure_pushes_critical_and_terminates]] (function: belongs_to)
- [[log-server/log-server/src/lib.rs.md|lib.rs]] (imports)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (calls)
<!-- SYNC:END -->
