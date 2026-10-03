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
Automatically generated mirror for `universal-logger/unilog/python/unilog/facade.py`.

> **Essential Process**:
> Primary Python facade for the universal-logger library, providing synchronous and asynchronous logging methods, caller stack inspection, and CGO bridge interop.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/src/cgo_bridge/config.go.md|UniLog_Config_Get]] (function: calls) — *export UniLog_Config_Get*
- [[universal-logger/universal-logger/src/cgo_bridge/config.go.md|UniLog_Config_Set]] (function: calls) — *export UniLog_Config_Set*
- [[universal-logger/universal-logger/src/cgo_bridge/config.go.md|UniLog_OnConfigUpdate]] (function: calls) — *export UniLog_OnConfigUpdate*
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_FreeString]] (function: calls) — *export DistConf_FreeString*
- [[universal-logger/universal-logger/src/cgo_bridge/initialize.go.md|UniLog_Close]] (function: calls) — *export UniLog_Close*
- [[universal-logger/universal-logger/src/cgo_bridge/initialize.go.md|UniLog_Init]] (function: calls) — *export UniLog_Init*
- [[universal-logger/universal-logger/src/cgo_bridge/logger.go.md|UniLog_AddMetadata]] (function: calls) — *export UniLog_AddMetadata*
- [[universal-logger/universal-logger/src/cgo_bridge/logger.go.md|UniLog_GetLevel]] (function: calls) — *export UniLog_GetLevel*
- [[universal-logger/universal-logger/src/cgo_bridge/logger.go.md|UniLog_LogWithMetadata]] (function: calls) — *export UniLog_LogWithMetadata*
- [[universal-logger/universal-logger/src/cgo_bridge/logger.go.md|UniLog_SetLevel]] (function: calls) — *export UniLog_SetLevel*
- [[universal-logger/universal-logger/src/cgo_bridge/logger.go.md|UniLog_SetMetadata]] (function: calls) — *export UniLog_SetMetadata*
- [[universal-logger/universal-logger/src/cgo_bridge/notif_callback.go.md|UniLog_RegisterNotifCallback]] (function: calls) — *export UniLog_RegisterNotifCallback*
- [[universal-logger/universal-logger/unilog/python/unilog/lib_loader.py.md|CALLBACK_TYPE]] (constant: calls) — *Shared Bridge Callbacks (defined globally to prevent ImportErrors)*
- [[universal-logger/universal-logger/unilog/python/unilog/lib_loader.py.md|lib_loader.py]] (imports)
- [[universal-logger/universal-logger/unilog/python/unilog/lib_loader.py.md|lib_loader.py]] (same_package)
- [[universal-logger/universal-logger/unilog/python/unilog/listeners.py.md|ConfigUpdateListener]] (class: calls) — *Async config listener*
- [[universal-logger/universal-logger/unilog/python/unilog/listeners.py.md|_put]] (function: calls) — *Internal thread-safe bridge to push data from Go into the Python event loop*
- [[universal-logger/universal-logger/unilog/python/unilog/listeners.py.md|listeners.py]] (imports)
- [[universal-logger/universal-logger/unilog/python/unilog/listeners.py.md|listeners.py]] (same_package)
- [[universal-logger/universal-logger/unilog/python/unilog/models.py.md|LogLevel]] (class: calls) — *Log Levels*
- [[universal-logger/universal-logger/unilog/python/unilog/models.py.md|from_str]] (function: calls) — *Helper to convert string-based levels from config to enum*
- [[universal-logger/universal-logger/unilog/python/unilog/models.py.md|models.py]] (imports)
- [[universal-logger/universal-logger/unilog/python/unilog/models.py.md|models.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/unilog/python/debug_callback.py.md|debug_callback.py]] (calls)
- [[universal-logger/universal-logger/unilog/python/test_async_logging.py.md|test_async_logging.py]] (calls)
- [[universal-logger/universal-logger/unilog/python/test_leak_comparison.py.md|test_leak_comparison.py]] (calls)
- [[universal-logger/universal-logger/unilog/python/test_leak_comparison.py.md|test_leak_comparison.py]] (imports)
- [[universal-logger/universal-logger/unilog/python/test_memory_leak.py.md|test_memory_leak.py]] (calls)
- [[universal-logger/universal-logger/unilog/python/test_memory_leak.py.md|test_memory_leak.py]] (imports)
- [[universal-logger/universal-logger/unilog/python/test_metadata_capture.py.md|test_metadata_capture.py]] (calls)
- [[universal-logger/universal-logger/unilog/python/test_unilog.py.md|test_unilog.py]] (calls)
- [[universal-logger/universal-logger/unilog/python/unilog/__init__.py.md|__init__.py]] (imports)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|UniLog]] (class: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|__aenter__]] (function: belongs_to) — *Support for 'async with' context manager*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|__aexit__]] (function: belongs_to) — *Automatic cleanup when exiting 'async with' block*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|__del__]] (function: belongs_to) — *Ensure resources are released if the object is garbage collected*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|__enter__]] (function: belongs_to) — *Support for standard 'with' context manager*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|__exit__]] (function: belongs_to) — *Automatic cleanup when exiting 'with' block*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|__init__]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|_async_log]] (function: belongs_to) — *Internal async Logging Method*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|_bridge_cb]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|_dispatch_log_to_cgo]] (function: belongs_to) — *Primary bridge to the Go shared library for all logging events*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|_dispatch_update]] (function: belongs_to) — *Internal bridge called from Go shared library background thread.*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|_get_caller_info]] (function: belongs_to) — *Capture caller metadata from the current stack trace*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|_log]] (function: belongs_to) — *Internal sync Logging Method*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|add_metadata]] (function: belongs_to) — *Add a single key-value pair to all future logs.*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|async_critical]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|async_debug]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|async_error]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|async_info]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|async_warning]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|close]] (function: belongs_to) — *Manually release the logger session and associated resources.*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|critical]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|debug]] (function: belongs_to) — *Logging Methods*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|error]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|get_config]] (function: belongs_to) — *Retrieve a configuration value from the distributed config service (Zero-Leak FFI).*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|get_level]] (function: belongs_to) — *Retrieve the current log level from the Go core.*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|info]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|logon]] (function: belongs_to) — *Specialized Domain Methods*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|logout]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|on_config_update]] (function: belongs_to) — *Trigger on_config_update*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|on_notification]] (function: belongs_to) — *Local Notifier Methods*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|report]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|schedule]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|set_config]] (function: belongs_to) — *Update a configuration value in the memory configuration.*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|set_level]] (function: belongs_to) — *Change the current log level dynamically.*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|set_metadata]] (function: belongs_to) — *Replace all existing metadata with the provided dictionary.*
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|stream]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|trade]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|warning]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/listeners.py.md|listeners.py]] (imports)
<!-- SYNC:END -->
