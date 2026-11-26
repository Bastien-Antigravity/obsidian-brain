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
> ! High-performance log message formatting with fixed-width column alignment, ! optional ANSI coloring, and structured metadata tail. ! ! DATA FLOW: ! 1. LogEntry fields -> format_log_message() ! 2. Column formatting and optional ANSI color injection ! 3. Formatted string output (console or disk persistence) ! ! KEY PARAMETERS: ! - use_color: True for stdout ANSI coloration, false for disk persistence. ! - Fixed-width column padding for timestamp, host, logger, level, file, func, line. use crate::utils::helpers::truncate; / Unified log message formatting - used by both protocols [allow(clippy::too_many_arguments)] pub fn format_log_message( timestamp: &str, hostname: &str, logger_name: &str, level: &str, module: &str, filename: &str, function_name: &str, line_number: &str, message: &str, path_name: &str, process_id: &str, process_name: &str, thread_id: &str, thread_name: &str, service_name: &str, stack_trace: &str, use_color: bool, ) -> String { let display_level = if use_color { crate::utils::terminal_ui::colorize_level(level) } else { format!("{:<10}", truncate(level, 10)) }; 1. Basic 8 columns (Fixed width) Note: display_level already contains padding and ANSI codes if use_color is true let base = format!( "{:<33} {:<12} {:<22} {} {:<20} {:<25} {:<6} {}", timestamp, truncate(hostname, 12), truncate(logger_name, 22), display_level, truncate(filename, 20), truncate(function_name, 25), truncate(line_number, 6), message ); 2. Extra metadata (key=value) let mut meta = Vec::new(); if !module.is_empty() { meta.push(format!("mod={module}")); } if !path_name.is_empty() { meta.push(format!("path={path_name}")); } if !process_id.is_empty() { meta.push(format!("pid={process_id}")); } if !process_name.is_empty() { meta.push(format!("pname={process_name}")); } if !thread_id.is_empty() { meta.push(format!("tid={thread_id}")); } if !thread_name.is_empty() { meta.push(format!("tname={thread_name}")); } if !service_name.is_empty() { meta.push(format!("svc={service_name}")); } Stack trace handling: append it last if !stack_trace.is_empty() { meta.push(format!("stack={}", stack_trace.replace('
', " | "))); } if meta.is_empty() { base } else { format!("{base} [metadata: {meta}]", meta = meta.join(" ")) } } [cfg(test)] mod tests { use super::*; [test] fn test_format_log_message_basic() { let timestamp = "2024-03-20T10:00:00.000Z"; let formatted = format_log_message( timestamp, "host1", "logger1", "INFO", "mod1", "file1.rs", "func1", "10", "Hello World", "", "", "", "", "", "", "", false, ); Check fixed columns (33 timestamp + 12 host + 22 logger + 10 level + 20 file + 25 func + 6 line + message) assert!(formatted.starts_with(timestamp)); assert!(formatted.contains("INFO")); assert!(formatted.contains("Hello World")); Metadata mod=mod1 should be present assert!(formatted.contains("[metadata: mod=mod1]")); } [test] fn test_format_log_message_with_metadata() { let formatted = format_log_message( "time", "host", "log", "DEBUG", "mod", "file", "func", "1", "msg", "path", "123", "pname", "456", "tname", "svc", "stack", false, ); assert!(formatted.contains("path=path")); assert!(formatted.contains("pid=123")); assert!(formatted.contains("pname=pname")); assert!(formatted.contains("tid=456")); assert!(formatted.contains("tname=tname")); assert!(formatted.contains("svc=svc")); assert!(formatted.contains("stack=stack")); } [test] fn test_truncation() { let long_host = "very-long-hostname-that-should-be-truncated"; let formatted = format_log_message( "time", long_host, "log", "INFO", "", "", "", "", "msg", "", "", "", "", "", "", "", false, ); The helper truncate(hostname, 12) should be used assert!(formatted.contains("very-long-ho")); assert!(!formatted.contains(long_host)); }

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/src/core/ring_buffer.rs.md|LogRingBuffer.new]] (method: calls) — *Create new ring buffer with given capacity and internal broadcast channel*
- [[log-server/src/core/ring_buffer.rs.md|LogRingBuffer.push]] (method: calls) — *Push a new log entry into the circular buffer and broadcast to live subscribers*
- [[log-server/src/core/ring_buffer.rs.md|ring_buffer.rs]] (same_package)
- [[log-server/src/utils/helpers.rs.md|helpers.rs]] (imports)
- [[log-server/src/utils/mod.rs.md|mod.rs]] (imports)
- [[log-server/src/utils/terminal_ui.rs.md|colorize_level]] (function: calls) — *Returns colorized level string for console*

### 🔌 Consumers (Inbound)
- [[log-server/src/core/log_formatter.rs.md|format_log_message]] (function: belongs_to) — *Unified log message formatting - used by both protocols*
- [[log-server/src/core/log_formatter.rs.md|test_format_log_message_basic]] (function: belongs_to)
- [[log-server/src/core/log_formatter.rs.md|test_format_log_message_with_color]] (function: belongs_to)
- [[log-server/src/core/log_formatter.rs.md|test_format_log_message_with_metadata]] (function: belongs_to)
- [[log-server/src/core/log_formatter.rs.md|test_truncation]] (function: belongs_to)
- [[log-server/src/facade/log_writer.rs.md|log_writer.rs]] (calls)
- [[log-server/src/facade/log_writer.rs.md|log_writer.rs]] (imports)
<!-- SYNC:END -->
