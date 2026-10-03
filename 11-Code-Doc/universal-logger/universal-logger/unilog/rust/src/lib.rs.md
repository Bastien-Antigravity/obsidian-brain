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

## 📝 Description
Automatically generated mirror for `universal-logger/unilog/rust/src/lib.rs`.

> **Essential Process**:
> Rust wrapper crate for universal-logger, providing safe Rust abstractions, RAII lifecycle (Drop), logging macros, metadata management, and C FFI bindings.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/src/cgo_bridge/config.go.md|UniLog_Config_Get]] (function: calls) — *export UniLog_Config_Get*
- [[universal-logger/universal-logger/src/cgo_bridge/config.go.md|UniLog_Config_Set]] (function: calls) — *export UniLog_Config_Set*
- [[universal-logger/universal-logger/src/cgo_bridge/config.go.md|UniLog_OnConfigUpdate]] (function: calls) — *export UniLog_OnConfigUpdate*
- [[universal-logger/universal-logger/src/cgo_bridge/initialize.go.md|UniLog_Close]] (function: calls) — *export UniLog_Close*
- [[universal-logger/universal-logger/src/cgo_bridge/initialize.go.md|UniLog_Init]] (function: calls) — *export UniLog_Init*
- [[universal-logger/universal-logger/src/cgo_bridge/logger.go.md|UniLog_AddMetadata]] (function: calls) — *export UniLog_AddMetadata*
- [[universal-logger/universal-logger/src/cgo_bridge/logger.go.md|UniLog_GetLevel]] (function: calls) — *export UniLog_GetLevel*
- [[universal-logger/universal-logger/src/cgo_bridge/logger.go.md|UniLog_LogWithMetadata]] (function: calls) — *export UniLog_LogWithMetadata*
- [[universal-logger/universal-logger/src/cgo_bridge/logger.go.md|UniLog_SetLevel]] (function: calls) — *export UniLog_SetLevel*
- [[universal-logger/universal-logger/src/cgo_bridge/logger.go.md|UniLog_SetMetadata]] (function: calls) — *export UniLog_SetMetadata*
- [[universal-logger/universal-logger/src/cgo_bridge/notif_callback.go.md|UniLog_RegisterNotifCallback]] (function: calls) — *export UniLog_RegisterNotifCallback*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.add_metadata]] (method: defines_method) — *Adds a single metadata field to all future logs.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.critical]] (method: defines_method)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.debug]] (method: defines_method)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.drop]] (method: defines_method)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.error]] (method: defines_method)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.get_config]] (method: defines_method) — *Retrieves a configuration value.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.get_level]] (method: defines_method) — *Retrieves the current log level from the Go core.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.info]] (method: defines_method) — *Convenience logging methods*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.log_with_metadata]] (method: defines_method) — *Logs a message with custom metadata.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.new]] (method: defines_method) — *Initializes a new logger session via the Go shared library.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.on_config_update]] (method: defines_method)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.on_notification]] (method: defines_method) — *Registers a callback to be executed when a local notification is received.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.set_config]] (method: defines_method) — *Updates a configuration value in memory.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.set_level]] (method: defines_method) — *Dynamically updates the log level.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.set_metadata]] (method: defines_method) — *Replaces all metadata with the provided JSON-serializable map.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.warning]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/unilog/rust/build.rs.md|build.rs]] (calls)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|LogLevel]] (enum: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.add_metadata]] (method: belongs_to) — *Adds a single metadata field to all future logs.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.critical]] (method: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.debug]] (method: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.drop]] (method: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.error]] (method: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.get_config]] (method: belongs_to) — *Retrieves a configuration value.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.get_level]] (method: belongs_to) — *Retrieves the current log level from the Go core.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.info]] (method: belongs_to) — *Convenience logging methods*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.log_with_metadata]] (method: belongs_to) — *Logs a message with custom metadata.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.new]] (method: belongs_to) — *Initializes a new logger session via the Go shared library.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.on_config_update]] (method: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.on_notification]] (method: belongs_to) — *Registers a callback to be executed when a local notification is received.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.set_config]] (method: belongs_to) — *Updates a configuration value in memory.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.set_level]] (method: belongs_to) — *Dynamically updates the log level.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.set_metadata]] (method: belongs_to) — *Replaces all metadata with the provided JSON-serializable map.*
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog.warning]] (method: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog]] (struct: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|UniLog]] (struct: defines_method)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|c_callback_bridge]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|c_notif_callback_bridge]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|test_config_operations]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|test_log_level_values]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|test_logger_lifecycle]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|test_logging_macros]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|test_metadata_operations]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|unilog_critical]] (macro: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|unilog_debug]] (macro: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|unilog_error]] (macro: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|unilog_info]] (macro: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/lib.rs.md|unilog_warning]] (macro: belongs_to)
- [[universal-logger/universal-logger/unilog/rust/src/main.rs.md|main.rs]] (calls)
- [[universal-logger/universal-logger/unilog/rust/src/main.rs.md|main.rs]] (same_package)
<!-- SYNC:END -->
