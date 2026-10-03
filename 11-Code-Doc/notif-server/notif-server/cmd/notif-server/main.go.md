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
Automatically generated mirror for `notif-server/cmd/notif-server/main.go`.

> **Essential Process**:
> Application entry point for the notif-server. Initializes configuration, logging, and the core notification engine. Manages the server lifecycle and graceful shutdown.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/core/controller.go.md|NewController]] (function: calls) — *NewController creates a new Controller instance.*
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (imports)
- [[notif-server/notif-server/src/core/notifier.go.md|NewNotifier]] (function: calls) — *NewNotifier creates a new instance of the notification service.*
- [[notif-server/notif-server/src/rest/mfe.js.md|mfe.js]] (imports)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|NewRESTHandler]] (function: calls) — *NewRESTHandler creates a new RESTHandler instance*
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.StartServer]] (method: calls) — *StartServer starts an HTTP server for the REST API on the specified address (e.g. "127.0.0.1:1029" or ":1029").*
- [[notif-server/notif-server/src/server/server.go.md|NewServer]] (function: calls) — *NewServer creates a new Notification Server.*
- [[notif-server/notif-server/src/server/server.go.md|server.go]] (imports)
- [[notif-server/notif-server/src/telegram/manager.go.md|manager.go]] (imports)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/cmd/notif-server/main.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->
