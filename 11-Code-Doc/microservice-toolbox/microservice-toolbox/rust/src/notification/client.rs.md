---
source: microservice-toolbox/rust/src/notification/client.rs
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-10-11T22:43:29.197102
---

# Mirror: client.rs

## 📝 Description
Automatically generated mirror for `microservice-toolbox/rust/src/notification/client.rs`.

> **Essential Process**:
> High-level client facade enabling L2 and L3 Rust microservices to send direct, multi-channel notifications to notif-server via the libnotif CGO FFI bridge.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|get_grpc_listen_addr]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/ffi.rs.md|ffi.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|loader.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.close]] (method: defines_method) — *Closes active notification client.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.from_config]] (method: defines_method) — *Fails fast if the notif_server capability or its gRPC address is unresolvable.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.new]] (method: defines_method) — *Initializes a NotificationClient pointing to a specific target address.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.send]] (method: defines_method) — *with optional destination tags (e.g. "telegram", "discord").*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.send_alert]] (method: defines_method) — *(e.g., "TRADE", "CRITICAL", "WARNING", "REPORT", "INFO") and optional tags.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.send_alert_sync]] (method: defines_method) — *Synchronous helper dispatching a categorized alert.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.send_sync]] (method: defines_method) — *Synchronous helper dispatching an untyped notification.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.send_with_attachment]] (method: defines_method) — *attachment reference, and destination tags.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.send_with_attachment_sync]] (method: defines_method) — *Synchronous helper dispatching a notification over blocking libnotif bridge.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.set_timeout]] (method: defines_method) — *Sets default RPC dispatch timeout.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/ffi.rs.md|ffi.rs]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/ffi.rs.md|get_lib]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.debug]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.info]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.warning]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|Logger]] (trait: calls) — *Logger trait defines the standard interface for structured logging across the toolbox.*
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|ensure_safe_logger]] (function: calls) — *In strict mode (STRICT_LOGGER=true), panics to prevent microservices from running dark.*
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|logger.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/mod.rs.md|mod.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|DEFAULT_TIMEOUT]] (constant: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.close]] (method: belongs_to) — *Closes active notification client.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.from_config]] (method: belongs_to) — *Fails fast if the notif_server capability or its gRPC address is unresolvable.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.new]] (method: belongs_to) — *Initializes a NotificationClient pointing to a specific target address.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.send]] (method: belongs_to) — *with optional destination tags (e.g. "telegram", "discord").*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.send_alert]] (method: belongs_to) — *(e.g., "TRADE", "CRITICAL", "WARNING", "REPORT", "INFO") and optional tags.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.send_alert_sync]] (method: belongs_to) — *Synchronous helper dispatching a categorized alert.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.send_sync]] (method: belongs_to) — *Synchronous helper dispatching an untyped notification.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.send_with_attachment]] (method: belongs_to) — *attachment reference, and destination tags.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.send_with_attachment_sync]] (method: belongs_to) — *Synchronous helper dispatching a notification over blocking libnotif bridge.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient.set_timeout]] (method: belongs_to) — *Sets default RPC dispatch timeout.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient]] (struct: belongs_to) — *notifications directly from Rust microservices to notif-server via libnotif.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|NotificationClient]] (struct: defines_method) — *notifications directly from Rust microservices to notif-server via libnotif.*
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/ffi.rs.md|ffi.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/ffi.rs.md|ffi.rs]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/mod.rs.md|mod.rs]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
