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
Automatically generated mirror for `notif-server/src/rest/rest_handler.go`.

> **Essential Process**:
> Provides HTTP REST endpoints and hosts OpenMFE web component assets for notif-server. Allows external clients and web-interface to inspect notifiers, send test notifications, and dynamically reconfigure alerting providers.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/core/controller.go.md|Controller.AddProvider]] (method: calls) — *AddProvider initializes a new provider section with default template.*
- [[notif-server/notif-server/src/core/controller.go.md|Controller.GetAlertingConfig]] (method: calls) — *GetAlertingConfig returns a deep copy of the current internal configuration of notification providers.*
- [[notif-server/notif-server/src/core/controller.go.md|Controller.GetStatus]] (method: calls) — *GetStatus returns server health and metadata.*
- [[notif-server/notif-server/src/core/controller.go.md|Controller.GetSupportedTypes]] (method: calls) — *GetSupportedTypes returns the list of hardcoded drivers available.*
- [[notif-server/notif-server/src/core/controller.go.md|Controller.ListNotifiers]] (method: calls) — *ListNotifiers returns the list of configured notifiers.*
- [[notif-server/notif-server/src/core/controller.go.md|Controller.ReloadConfig]] (method: calls) — *ReloadConfig triggers a manual reload of the configuration.*
- [[notif-server/notif-server/src/core/controller.go.md|Controller.RemoveProvider]] (method: calls) — *RemoveProvider deletes a provider section.*
- [[notif-server/notif-server/src/core/controller.go.md|Controller.SendTestNotification]] (method: calls) — *SendTestNotification triggers a test notification through the engine and logger.*
- [[notif-server/notif-server/src/core/controller.go.md|Controller.SetAlertingConfig]] (method: calls) — *SetAlertingConfig updates a specific setting for a notification provider.*
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (imports)
- [[notif-server/notif-server/src/grpc_control/service.go.md|NewControlService]] (function: calls) — *NewControlService creates a new ControlServiceImpl instance*
- [[notif-server/notif-server/src/grpc_control/service.go.md|service.go]] (imports)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.Handler]] (method: defines_method) — *Handler returns the REST API handler with route registration and CORS wrapping.*
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.RegisterRoutes]] (method: defines_method) — *RegisterRoutes registers the REST routes to the provided mux*
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.StartServerPort]] (method: defines_method) — *StartServerPort is a convenience helper that accepts an integer port.*
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.StartServer]] (method: defines_method) — *StartServer starts an HTTP server for the REST API on the specified address (e.g. "127.0.0.1:1029" or ":1029").*
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.Stop]] (method: defines_method) — *Stop gracefully shuts down the HTTP server.*
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleAddProvider]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleGetAlertingConfig]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleGetSupportedTypes]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleListNotifiers]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleReloadConfig]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleRemoveProvider]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleSendTest]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleSetAlertingConfig]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleStatus]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.sendJSON]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/cmd/notif-server/main.go.md|main.go]] (calls)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|NewRESTHandler]] (function: belongs_to) — *NewRESTHandler creates a new RESTHandler instance*
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.Handler]] (method: belongs_to) — *Handler returns the REST API handler with route registration and CORS wrapping.*
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.RegisterRoutes]] (method: belongs_to) — *RegisterRoutes registers the REST routes to the provided mux*
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.StartServerPort]] (method: belongs_to) — *StartServerPort is a convenience helper that accepts an integer port.*
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.StartServer]] (method: belongs_to) — *StartServer starts an HTTP server for the REST API on the specified address (e.g. "127.0.0.1:1029" or ":1029").*
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.Stop]] (method: belongs_to) — *Stop gracefully shuts down the HTTP server.*
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleAddProvider]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleGetAlertingConfig]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleGetSupportedTypes]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleListNotifiers]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleReloadConfig]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleRemoveProvider]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleSendTest]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleSetAlertingConfig]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.handleStatus]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.sendJSON]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler]] (struct: belongs_to) — *Stop gracefully shuts down the HTTP server.*
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler]] (struct: defines_method) — *Stop gracefully shuts down the HTTP server.*
<!-- SYNC:END -->
