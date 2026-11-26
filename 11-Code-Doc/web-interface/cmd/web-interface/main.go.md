---
microservice: web-interface
type: note
status: active
tags:
- '#service/web-interface'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `web-interface/cmd/web-interface/main.go`.

> **Essential Process**:
> Serves as the main entry point for the web-interface microservice. Boots up the web dashboard, configures routes, and connects to tele-remote.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/cmd/web-interface/main_test.go.md|main_test.go]] (same_package)
- [[web-interface/cmd/web-interface/main_test.go.md|mockLogger.Close]] (method: calls)
- [[web-interface/cmd/web-interface/main_test.go.md|mockLogger.Critical]] (method: calls)
- [[web-interface/cmd/web-interface/main_test.go.md|mockLogger.Error]] (method: calls)
- [[web-interface/cmd/web-interface/main_test.go.md|mockLogger.Info]] (method: calls)
- [[web-interface/src/core/controller.go.md|NewController]] (function: calls) — *NewController creates a new Controller instance with dynamic config support.*
- [[web-interface/src/core/controller.go.md|controller.go]] (imports)
- [[web-interface/src/mfe/registry.go.md|NewRegistry]] (function: calls) — *NewRegistry instantiates a new Registry, loading existing services from disk.*
- [[web-interface/src/mfe/registry.go.md|Registry.EnsureFoundationalServices]] (method: calls) — *have complete self-describing manifests loaded into the registry using dynamic parameters from appConfig.*
- [[web-interface/src/mfe/registry.go.md|Registry.HandleGetContracts]] (method: calls) — *HandleGetContracts serves the ContractsEnvelope JSON published for a registered microservice.*
- [[web-interface/src/mfe/registry.go.md|Registry.RegisterHandlers]] (method: calls) — *RegisterHandlers binds the MFE endpoints to the HTTP ServeMux.*
- [[web-interface/src/mfe/registry.go.md|Registry.Register]] (method: calls) — *Register adds or updates a microfrontend service in the registry with automatic deduplication.*
- [[web-interface/src/mfe/registry.go.md|Registry.SetAllowedPublicHost]] (method: calls) — *(such as local.web_interface.public_url) so MFE script URLs served from that host are permitted.*
- [[web-interface/src/mfe/registry.go.md|registry.go]] (imports)
- [[web-interface/src/middleware/middleware.go.md|CSRFMiddleware]] (function: calls) — *CSRFMiddleware Protection*
- [[web-interface/src/middleware/middleware.go.md|LoggerMiddleware]] (function: calls) — *LoggerMiddleware console output*
- [[web-interface/src/middleware/middleware.go.md|middleware.go]] (imports)
- [[web-interface/src/postgres_browser/connection.go.md|CloseAllPools]] (function: calls) — *CloseAllPools closes all cached PostgreSQL connection pools during graceful shutdown.*
- [[web-interface/src/postgres_browser/handler.go.md|RegisterPostgresBrowserRoutes]] (function: calls) — *RegisterPostgresBrowserRoutes maps browser HTTP endpoints and returns the wrapped handler.*
- [[web-interface/src/postgres_browser/handler.go.md|handler.go]] (imports)
- [[web-interface/src/renderer/renderer_test.go.md|renderer_test.go]] (imports)
- [[web-interface/src/router/base_ecosystem.go.md|base_ecosystem.go]] (imports)
- [[web-interface/src/router/dynamic.go.md|SetMFERegistry]] (function: calls) — *SetMFERegistry associates the active MFE registry instance with the router.*
- [[web-interface/src/router/log_bridge.go.md|CloseLogBridge]] (function: calls) — *CloseLogBridge closes the active gRPC log bridge connection on service shutdown.*
- [[web-interface/src/router/router.go.md|RegisterRoutes]] (function: calls) — *RegisterRoutes initializes the web interface endpoints on the provided ServeMux.*
- [[web-interface/src/server/facade.go.md|NewServerFacade]] (function: calls)
- [[web-interface/src/server/facade.go.md|ServerFacade.Start]] (method: calls)
- [[web-interface/src/server/facade.go.md|ServerFacade.Stop]] (method: calls)
- [[web-interface/src/server/facade.go.md|facade.go]] (imports)
- [[web-interface/src/telegram/manager.go.md|SetupTelegram]] (function: calls) — *SetupTelegram initializes the Tele-Remote client, registers callbacks, and hooks into lifecycle*
- [[web-interface/src/telegram/manager.go.md|manager.go]] (imports)

### 🔌 Consumers (Inbound)
- [[web-interface/cmd/web-interface/main.go.md|buildMainHTTPHandler]] (function: belongs_to) — *buildMainHTTPHandler wires the split public/protected HTTP handler used in production and integration tests.*
- [[web-interface/cmd/web-interface/main.go.md|isLoopbackCaller]] (function: belongs_to)
- [[web-interface/cmd/web-interface/main.go.md|main]] (function: belongs_to)
- [[web-interface/cmd/web-interface/main_test.go.md|main_test.go]] (calls)
- [[web-interface/cmd/web-interface/main_test.go.md|main_test.go]] (same_package)
<!-- SYNC:END -->
