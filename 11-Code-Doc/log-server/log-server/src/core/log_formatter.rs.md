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
Automatically generated mirror for `log-server/src/core/log_formatter.rs`.

> **Essential Process**:
> High-performance log message formatting with fixed-width column alignment, optional ANSI coloring, and structured metadata tail.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer.new]] (method: calls) — *Create new ring buffer with given capacity and internal broadcast channel*
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer.push]] (method: calls) — *Push a new log entry into the circular buffer and broadcast to live subscribers*
- [[log-server/log-server/src/core/ring_buffer.rs.md|ring_buffer.rs]] (same_package)
- [[log-server/log-server/src/utils/helpers.rs.md|helpers.rs]] (imports)
- [[log-server/log-server/src/utils/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/utils/terminal_ui.rs.md|colorize_level]] (function: calls) — *Returns colorized level string for console*

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/core/log_formatter.rs.md|format_log_message]] (function: belongs_to) — *Unified log message formatting - used by both protocols*
- [[log-server/log-server/src/core/log_formatter.rs.md|test_format_log_message_basic]] (function: belongs_to)
- [[log-server/log-server/src/core/log_formatter.rs.md|test_format_log_message_with_metadata]] (function: belongs_to)
- [[log-server/log-server/src/core/log_formatter.rs.md|test_truncation]] (function: belongs_to)
- [[log-server/log-server/src/facade/log_writer.rs.md|log_writer.rs]] (calls)
- [[log-server/log-server/src/facade/log_writer.rs.md|log_writer.rs]] (imports)
<!-- SYNC:END -->
