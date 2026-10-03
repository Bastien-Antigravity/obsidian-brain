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
Automatically generated mirror for `web-interface/cmd/web-interface/main.go`.

> **Essential Process**:
> Serves as the main entry point for the web-interface microservice. Boots up the web dashboard, configures routes, and connects to tele-remote.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|main_test.go]] (same_package)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Close]] (method: calls)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Critical]] (method: calls)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Error]] (method: calls)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Info]] (method: calls)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Warning]] (method: calls)
- [[web-interface/web-interface/src/core/controller.go.md|NewController]] (function: calls) — *NewController creates a new Controller instance with dynamic config support.*
- [[web-interface/web-interface/src/core/controller.go.md|controller.go]] (imports)
- [[web-interface/web-interface/src/fundamental_analysis/fundamental_analysis.go.md|ConnectStockDatabase]] (function: calls) — *ConnectStockDatabase initializes the database connection for financial analysis.*
- [[web-interface/web-interface/src/fundamental_analysis/fundamental_analysis.go.md|fundamental_analysis.go]] (imports)
- [[web-interface/web-interface/src/mfe/registry.go.md|NewRegistry]] (function: calls) — *NewRegistry instantiates a new Registry, loading existing services from disk.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.RegisterHandlers]] (method: calls) — *RegisterHandlers binds the MFE endpoints to the HTTP ServeMux.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.Register]] (method: calls) — *Register adds or updates a microfrontend service in the registry.*
- [[web-interface/web-interface/src/mfe/registry.go.md|registry.go]] (imports)
- [[web-interface/web-interface/src/middleware/middleware.go.md|LoggerMiddleware]] (function: calls) — *LoggerMiddleware console output*
- [[web-interface/web-interface/src/middleware/middleware.go.md|middleware.go]] (imports)
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|RegisterPostgresBrowserRoutes]] (function: calls) — *RegisterPostgresBrowserRoutes maps browser HTTP endpoints and returns the wrapped handler.*
- [[web-interface/web-interface/src/postgres_browser/postgres_browser.go.md|postgres_browser.go]] (imports)
- [[web-interface/web-interface/src/renderer/renderer.go.md|renderer.go]] (imports)
- [[web-interface/web-interface/src/router/router.go.md|RegisterRoutes]] (function: calls) — *RegisterRoutes initializes the web interface endpoints on the provided ServeMux.*
- [[web-interface/web-interface/src/router/router_test.go.md|router_test.go]] (imports)
- [[web-interface/web-interface/src/server/facade.go.md|NewServerFacade]] (function: calls)
- [[web-interface/web-interface/src/server/facade.go.md|ServerFacade.Start]] (method: calls)
- [[web-interface/web-interface/src/server/facade.go.md|ServerFacade.Stop]] (method: calls)
- [[web-interface/web-interface/src/server/facade.go.md|facade.go]] (imports)
- [[web-interface/web-interface/src/telegram/manager.go.md|manager.go]] (imports)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|TimescaleDBCap]] (struct: belongs_to) — *4. Database Setup for stock analysis integration*
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->
