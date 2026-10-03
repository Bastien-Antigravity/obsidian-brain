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
Automatically generated mirror for `notif-server/src/server/connection.go`.

> **Essential Process**:
> Handles individual client connections and stable identity resolution. Implements the persistent message loop for TCP ingestion.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/server/connection.go.md|Server.handleConnection]] (method: defines_method)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Close]] (method: calls)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Error]] (method: calls)
- [[notif-server/notif-server/src/server/server_test.go.md|mockLogger.Info]] (method: calls)
- [[notif-server/notif-server/src/server/server_test.go.md|server_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/server/connection.go.md|Server.handleConnection]] (method: belongs_to)
- [[notif-server/notif-server/src/server/connection.go.md|Server]] (struct: defines_method)
- [[notif-server/notif-server/src/server/server.go.md|server.go]] (calls)
- [[notif-server/notif-server/src/server/server.go.md|server.go]] (same_package)
<!-- SYNC:END -->
