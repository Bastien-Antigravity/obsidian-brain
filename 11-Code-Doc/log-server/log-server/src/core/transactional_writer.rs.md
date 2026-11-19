---
source: log-server/src/core/transactional_writer.rs
workspace: log-server
type: code-mirror
status: auto-generated
last_sync: 2026-11-16T15:52:37.150955
---

# Mirror: transactional_writer.rs

## 📝 Description
Automatically generated mirror for `log-server/src/core/transactional_writer.rs`.

> **Essential Process**:
> ! Transactional disk persistence engine with in-memory batch staging (Tier 1), ! checkpointed ftruncate rollback on partial write errors (Tier 2), ! and poisoned file handle recovery (Tier 3). ! ! DATA FLOW: ! 1. Formatted log entry batch -> In-memory contiguous staging buffer (Vec<u8>) ! 2. Capture clean record boundary checkpoint (*file_size) ! 3. Atomic write_all() execution to file descriptor ! 4. On write error: invoke ftruncate to checkpoint_offset to drop partial bytes ! 5. On rollback failure: poison handle, close descriptor, reopen, and resynchronize ! ! KEY PARAMETERS: ! - max_retries: Number of retry attempts on transient write failures. ! - retry_delay_ms: Backoff duration between retries in milliseconds. use std::path::PathBuf; use std::time::Duration; use tokio::fs::{self, File, OpenOptions}; use tokio::io::{AsyncSeekExt, AsyncWriteExt, SeekFrom}; use tokio::time::sleep; / Transactional log file manager providing atomic batch commits and rollback pub struct TransactionalFileWriter { base_file_path: PathBuf, file: File, file_size: u64, max_retries: usize, retry_delay_ms: u64, }

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer.push]] (method: calls) — *Push a new log entry into the circular buffer and broadcast to live subscribers*
- [[log-server/log-server/src/core/ring_buffer.rs.md|ring_buffer.rs]] (same_package)
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.check_and_rotate]] (method: defines_method) — *Check if rotation threshold is met and perform cascading rotation*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.file_size]] (method: defines_method) — *Return current tracked file size*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.flush]] (method: defines_method) — *Flush the active file to disk*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.new]] (method: defines_method) — *Initialize a new transactional file writer for the given base path*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.recover_poisoned_handle]] (method: defines_method) — *Drops the current corrupted handle, opens a fresh descriptor, and synchronizes metadata.*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.rollback_to]] (method: defines_method) — *Roll back the file length and cursor to the specified clean checkpoint offset*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.rotate_files]] (method: defines_method) — *Cascading file rotation implementation*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.write_batch]] (method: defines_method) — *- Tier 3: Poisoned handle recovery (close and reopen) if rollback fails.*
- [[log-server/log-server/src/protocols/capnp/logger_msg.rs.md|Reader<'_,>.clone]] (method: calls)
- [[log-server/log-server/src/utils/helpers.rs.md|create_log_folder]] (function: calls) — *Create log folder if not exists*

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.check_and_rotate]] (method: belongs_to) — *Check if rotation threshold is met and perform cascading rotation*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.file_size]] (method: belongs_to) — *Return current tracked file size*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.flush]] (method: belongs_to) — *Flush the active file to disk*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.new]] (method: belongs_to) — *Initialize a new transactional file writer for the given base path*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.recover_poisoned_handle]] (method: belongs_to) — *Drops the current corrupted handle, opens a fresh descriptor, and synchronizes metadata.*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.rollback_to]] (method: belongs_to) — *Roll back the file length and cursor to the specified clean checkpoint offset*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.rotate_files]] (method: belongs_to) — *Cascading file rotation implementation*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter.write_batch]] (method: belongs_to) — *- Tier 3: Poisoned handle recovery (close and reopen) if rollback fails.*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter]] (struct: belongs_to) — *Transactional log file manager providing atomic batch commits and rollback*
- [[log-server/log-server/src/core/transactional_writer.rs.md|TransactionalFileWriter]] (struct: defines_method) — *Transactional log file manager providing atomic batch commits and rollback*
- [[log-server/log-server/src/core/transactional_writer.rs.md|test_transactional_rotation_cascading]] (function: belongs_to)
- [[log-server/log-server/src/core/transactional_writer.rs.md|test_transactional_write_and_flush]] (function: belongs_to)
- [[log-server/log-server/src/core/transactional_writer.rs.md|test_transactional_write_truncation_rollback]] (function: belongs_to)
- [[log-server/log-server/src/facade/log_writer.rs.md|log_writer.rs]] (calls)
- [[log-server/log-server/src/facade/log_writer.rs.md|log_writer.rs]] (imports)
- [[log-server/log-server/src/transport/safe_socket.rs.md|safe_socket.rs]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
