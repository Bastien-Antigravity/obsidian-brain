---
source: notif-server/notif/rust/src/lib.rs
workspace: notif-server
type: code-mirror
status: auto-generated
last_sync: 2026-10-11T22:43:29.327716
---

# Mirror: lib.rs

## 📝 Description
Automatically generated mirror for `notif-server/notif/rust/src/lib.rs`.

> **Essential Process**:
> Standalone Rust wrapper crate for notif-server, providing safe abstractions and FFI bindings to the libnotif CGO shared library.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/notif/rust/src/lib.rs.md|NotificationClient.new]] (method: defines_method) — *Connects to a target notif-server instance using the libnotif dynamic library.*
- [[notif-server/notif-server/notif/rust/src/lib.rs.md|NotificationClient.send]] (method: defines_method) — *Dispatches an untyped notification message with optional tags.*
- [[notif-server/notif-server/notif/rust/src/lib.rs.md|NotificationClient.send_alert]] (method: defines_method) — *Dispatches a categorized alert with level and optional tags.*
- [[notif-server/notif-server/notif/rust/src/lib.rs.md|NotificationClient.send_with_attachment]] (method: defines_method) — *Dispatches a notification with level, message, attachment, and tags.*
- [[notif-server/notif-server/notif/rust/src/lib.rs.md|NotificationClient.set_timeout]] (method: defines_method) — *Sets default RPC timeout in seconds.*

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/notif/rust/src/lib.rs.md|NotificationClient.new]] (method: belongs_to) — *Connects to a target notif-server instance using the libnotif dynamic library.*
- [[notif-server/notif-server/notif/rust/src/lib.rs.md|NotificationClient.send]] (method: belongs_to) — *Dispatches an untyped notification message with optional tags.*
- [[notif-server/notif-server/notif/rust/src/lib.rs.md|NotificationClient.send_alert]] (method: belongs_to) — *Dispatches a categorized alert with level and optional tags.*
- [[notif-server/notif-server/notif/rust/src/lib.rs.md|NotificationClient.send_with_attachment]] (method: belongs_to) — *Dispatches a notification with level, message, attachment, and tags.*
- [[notif-server/notif-server/notif/rust/src/lib.rs.md|NotificationClient.set_timeout]] (method: belongs_to) — *Sets default RPC timeout in seconds.*
- [[notif-server/notif-server/notif/rust/src/lib.rs.md|NotificationClient]] (struct: belongs_to)
- [[notif-server/notif-server/notif/rust/src/lib.rs.md|NotificationClient]] (struct: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
