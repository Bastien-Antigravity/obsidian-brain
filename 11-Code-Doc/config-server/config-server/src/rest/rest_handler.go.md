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
Automatically generated mirror for `config-server/src/rest/rest_handler.go`.

> **Essential Process**:
> Implements the HTTP REST management interface and OpenMFE micro-frontend host for config-server, exposing JSON API endpoints for querying, tweaking, and persisting configuration.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/config-server/src/core/controller.go.md|controller.go]] (imports)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.Handler]] (method: defines_method) — *Handler returns the REST API handler with route registration and CORS wrapping.*
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.RegisterRoutes]] (method: defines_method) — *RegisterRoutes registers the REST routes to the provided mux*
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.StartServer]] (method: defines_method) — *StartServer starts a HTTP server for the REST API on the specified address (e.g. "127.0.0.1:3308" or ":3308").*
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.Stop]] (method: defines_method) — *Stop gracefully shuts down the HTTP server.*
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleGetConfig]] (method: defines_method)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleListConfig]] (method: defines_method)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handlePersistConfig]] (method: defines_method)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleReloadConfig]] (method: defines_method)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleSetConfig]] (method: defines_method)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleStatus]] (method: defines_method)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.sendJSON]] (method: defines_method)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockControl.GetConfig]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockControl.GetStatus]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockControl.ListConfig]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockControl.PersistConfig]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockControl.ReloadConfig]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockControl.SetConfig]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockLogger.Error]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockLogger.Info]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|rest_handler_test.go]] (same_package)
- [[config-server/config-server/src/store/store.go.md|Store.Get]] (method: calls) — *Callers MUST treat the returned map as immutable.*

### 🔌 Consumers (Inbound)
- [[config-server/config-server/cmd/config-server/main.go.md|main.go]] (calls)
- [[config-server/config-server/src/rest/rest_handler.go.md|NewRESTHandler]] (function: belongs_to) — *NewRESTHandler creates a new RESTHandler instance*
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.Handler]] (method: belongs_to) — *Handler returns the REST API handler with route registration and CORS wrapping.*
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.RegisterRoutes]] (method: belongs_to) — *RegisterRoutes registers the REST routes to the provided mux*
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.StartServer]] (method: belongs_to) — *StartServer starts a HTTP server for the REST API on the specified address (e.g. "127.0.0.1:3308" or ":3308").*
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.Stop]] (method: belongs_to) — *Stop gracefully shuts down the HTTP server.*
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleGetConfig]] (method: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleListConfig]] (method: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handlePersistConfig]] (method: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleReloadConfig]] (method: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleSetConfig]] (method: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.handleStatus]] (method: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.sendJSON]] (method: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler]] (struct: belongs_to) — *Stop gracefully shuts down the HTTP server.*
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler]] (struct: defines_method) — *Stop gracefully shuts down the HTTP server.*
- [[config-server/config-server/src/rest/rest_handler.go.md|httpControlResponse]] (struct: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|httpGetResponse]] (struct: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|httpListResponse]] (struct: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|httpSetConfigRequest]] (struct: belongs_to)
- [[config-server/config-server/src/rest/rest_handler.go.md|httpStatusResponse]] (struct: belongs_to)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|rest_handler_test.go]] (calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|rest_handler_test.go]] (same_package)
<!-- SYNC:END -->
