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
- [[log-server/log-server/src/core/log_formatter.rs.md|format_log_message]] (function: calls) — *Unified log message formatting - used by both protocols*
- [[log-server/log-server/src/core/log_formatter.rs.md|log_formatter.rs]] (imports)
- [[log-server/log-server/src/core/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.new]] (method: defines_method) — *Create new log writer with default config*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.rotate_files]] (method: defines_method) — *Rotate log files*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.start_writer_task]] (method: defines_method) — *Start the writer task*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.with_config]] (method: defines_method) — *Create new log writer with custom config*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.write_batch]] (method: defines_method) — *Write batch with retry logic*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.writer_task]] (method: defines_method) — *Main writer task implementation*
- [[log-server/log-server/src/facade/log_writer.rs.md|WriterConfig.default]] (method: defines_method)
- [[log-server/log-server/src/models/log_entry.rs.md|LEVEL_STRINGS]] (constant: calls) — *Human-readable log level strings*
- [[log-server/log-server/src/models/log_entry.rs.md|LogEntry]] (struct: calls) — *Internal log request wrapper for internal use*
- [[log-server/log-server/src/models/log_entry.rs.md|log_entry.rs]] (imports)
- [[log-server/log-server/src/models/log_packet.rs.md|LogPacket]] (struct: calls) — *A packet containing a sequence number and the log entry*
- [[log-server/log-server/src/models/log_packet.rs.md|log_packet.rs]] (imports)
- [[log-server/log-server/src/models/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/protocols/capnp/logger_msg.rs.md|Reader<'_,>.clone]] (method: calls)
- [[log-server/log-server/src/utils/helpers.rs.md|create_log_folder]] (function: calls) — *Create log folder if not exists*
- [[log-server/log-server/src/utils/helpers.rs.md|get_exec_parent_dir]] (function: calls) — *Get executable parent directory*

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/core/reorder_test.rs.md|reorder_test.rs]] (calls)
- [[log-server/log-server/src/core/reorder_test.rs.md|reorder_test.rs]] (imports)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (calls)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (imports)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (same_package)
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.new]] (method: belongs_to) — *Create new log writer with default config*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.rotate_files]] (method: belongs_to) — *Rotate log files*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.start_writer_task]] (method: belongs_to) — *Start the writer task*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.with_config]] (method: belongs_to) — *Create new log writer with custom config*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.write_batch]] (method: belongs_to) — *Write batch with retry logic*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter.writer_task]] (method: belongs_to) — *Main writer task implementation*
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter]] (struct: belongs_to)
- [[log-server/log-server/src/facade/log_writer.rs.md|LogWriter]] (struct: defines_method)
- [[log-server/log-server/src/facade/log_writer.rs.md|WriterConfig.default]] (method: belongs_to)
- [[log-server/log-server/src/facade/log_writer.rs.md|WriterConfig]] (struct: belongs_to)
- [[log-server/log-server/src/facade/log_writer.rs.md|WriterConfig]] (struct: defines_method)
- [[log-server/log-server/src/lib.rs.md|lib.rs]] (imports)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|terminal_ui.rs]] (calls)
<!-- SYNC:END -->
