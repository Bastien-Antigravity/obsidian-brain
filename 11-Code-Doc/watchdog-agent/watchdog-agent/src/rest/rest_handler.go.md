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
Automatically generated mirror for `watchdog-agent/src/rest/rest_handler.go`.

> **Essential Process**:
> HTTP REST management API and OpenMFE micro-frontend host for watchdog-agent. Serves live node telemetry, system health status, process restart endpoints, and embedded OpenMFE frontend script assets.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/core/controller.go.md|controller.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler.Handler]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler.RegisterRoutes]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler.StartServer]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler.handleRestartAll]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler.handleRestartService]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler.handleStartPostgres]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler.handleStatus]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler.sendJSON]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.GetStatus]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.RestartAll]] (method: calls) — *RestartService forcefully terminates the process group of a service to let it auto-restart*
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.RestartService]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/postgres_launcher.go.md|LaunchPostgresAttempt]] (function: calls) — *if it is not already running. It returns true if successful or if it was already running.*
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|types.go]] (imports)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|NewRESTHandler]] (function: belongs_to) — *NewRESTHandler creates a new RESTHandler instance*
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler.Handler]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler.RegisterRoutes]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler.StartServer]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler.handleRestartAll]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler.handleRestartService]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler.handleStartPostgres]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler.handleStatus]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler.sendJSON]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler]] (struct: belongs_to) — *RESTHandler handles HTTP management requests for watchdog*
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler]] (struct: defines_method) — *RESTHandler handles HTTP management requests for watchdog*
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|httpControlResponse]] (struct: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|httpRestartRequest]] (struct: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|httpStatusResponse]] (struct: belongs_to)
<!-- SYNC:END -->
