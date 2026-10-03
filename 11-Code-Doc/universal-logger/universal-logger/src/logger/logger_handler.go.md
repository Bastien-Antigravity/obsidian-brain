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
- [[universal-logger/universal-logger/src/interfaces/models.go.md|models.go]] (imports)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.AddMetadata]] (method: defines_method) — *AddMetadata adds a single key-value pair to the logger's metadata.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Close]] (method: defines_method) — *Close closes the underlying logger idempotently and unregisters the GC finalizer.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Critical]] (method: defines_method) — *Critical logs a message at Critical level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Debug]] (method: defines_method) — *Debug logs a message at Debug level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Error]] (method: defines_method) — *Error logs a message at Error level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.GetLevel]] (method: defines_method) — *GetLevel returns the current log level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.GetMetadata]] (method: defines_method) — *GetMetadata returns a thread-safe copy of the logger's metadata.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.GetNotifQueue]] (method: defines_method) — *If the notifier was not enabled during Init, this will return nil.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Info]] (method: defines_method) — *Info logs a message at Info level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.LogWithCaller]] (method: defines_method) — *LogWithCaller logs a message with explicit caller stack metadata.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Log]] (method: defines_method) — *Log logs a message at a specific level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Logon]] (method: defines_method) — *Logon logs a message at Logon level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Logout]] (method: defines_method) — *Logout logs a message at Logout level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Report]] (method: defines_method) — *Report logs a message at Report level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Schedule]] (method: defines_method) — *Schedule logs a message at Schedule level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetCallerSkip]] (method: defines_method) — *It automatically adds 1 to the provided skip value to account for this facade layer.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetLevel]] (method: defines_method) — *SetLevel sets the current log level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetLocalNotifQueue]] (method: defines_method) — *It performs a type assertion to find the appropriate wrapper that supports this.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetMetadata]] (method: defines_method) — *SetMetadata replaces all existing metadata with the provided map.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Stream]] (method: defines_method) — *Stream logs a message at Stream level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Trade]] (method: defines_method) — *Trade logs a message at Trade level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Unwrap]] (method: defines_method) — *This is used by internal utilities for high-performance sink access.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Warning]] (method: defines_method) — *Warning logs a message at Warning level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.formatMessageWithMetadata]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/notif_message.go.md|notif_message.go]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|unilog.go]] (calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|NewUniLog]] (function: belongs_to) — *when the logger instance is about to be garbage collected.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.AddMetadata]] (method: belongs_to) — *AddMetadata adds a single key-value pair to the logger's metadata.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Close]] (method: belongs_to) — *Close closes the underlying logger idempotently and unregisters the GC finalizer.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Critical]] (method: belongs_to) — *Critical logs a message at Critical level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Debug]] (method: belongs_to) — *Debug logs a message at Debug level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Error]] (method: belongs_to) — *Error logs a message at Error level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.GetLevel]] (method: belongs_to) — *GetLevel returns the current log level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.GetMetadata]] (method: belongs_to) — *GetMetadata returns a thread-safe copy of the logger's metadata.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.GetNotifQueue]] (method: belongs_to) — *If the notifier was not enabled during Init, this will return nil.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Info]] (method: belongs_to) — *Info logs a message at Info level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.LogWithCaller]] (method: belongs_to) — *LogWithCaller logs a message with explicit caller stack metadata.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Log]] (method: belongs_to) — *Log logs a message at a specific level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Logon]] (method: belongs_to) — *Logon logs a message at Logon level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Logout]] (method: belongs_to) — *Logout logs a message at Logout level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Report]] (method: belongs_to) — *Report logs a message at Report level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Schedule]] (method: belongs_to) — *Schedule logs a message at Schedule level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetCallerSkip]] (method: belongs_to) — *It automatically adds 1 to the provided skip value to account for this facade layer.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetLevel]] (method: belongs_to) — *SetLevel sets the current log level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetLocalNotifQueue]] (method: belongs_to) — *It performs a type assertion to find the appropriate wrapper that supports this.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetMetadata]] (method: belongs_to) — *SetMetadata replaces all existing metadata with the provided map.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Stream]] (method: belongs_to) — *Stream logs a message at Stream level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Trade]] (method: belongs_to) — *Trade logs a message at Trade level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Unwrap]] (method: belongs_to) — *This is used by internal utilities for high-performance sink access.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.Warning]] (method: belongs_to) — *Warning logs a message at Warning level.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.formatMessageWithMetadata]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog]] (struct: belongs_to) — *Close closes the underlying logger idempotently and unregisters the GC finalizer.*
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog]] (struct: defines_method) — *Close closes the underlying logger idempotently and unregisters the GC finalizer.*
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|logger_handler_test.go]] (calls)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|logger_handler_test.go]] (same_package)
<!-- SYNC:END -->
