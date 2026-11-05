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
Automatically generated mirror for `web-interface/src/router/router.go`.

> **Essential Process**:
> Manages and routes all HTTP requests for the web dashboard interface. Segregates static template actions from dynamic JSON API and MFE endpoints. Initializes static page auto-discovery and binds navigation category provider.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/renderer/renderer.go.md|renderer.go]] (imports)
- [[web-interface/web-interface/src/router/autodiscovery.go.md|GetStaticCategories]] (function: calls) — *GetStaticCategories returns a thread-safe deep copy of all discovered static categories.*
- [[web-interface/web-interface/src/router/autodiscovery.go.md|InitAutoDiscovery]] (function: calls) — *InitAutoDiscovery scans the filesystem for static pages and compiles the navigation catalog.*
- [[web-interface/web-interface/src/router/autodiscovery.go.md|RegisterAutoDiscoveryRoutes]] (function: calls) — *RegisterAutoDiscoveryRoutes binds static page discovery routes, alias redirects, and API.*
- [[web-interface/web-interface/src/router/autodiscovery.go.md|autodiscovery.go]] (same_package)
- [[web-interface/web-interface/src/router/dynamic.go.md|RegisterDynamicRoutes]] (function: calls) — *RegisterDynamicRoutes binds all API, Stock query, and OpenMFE dynamic routes.*
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|router_test.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Info]] (method: calls)
- [[web-interface/web-interface/src/router/static.go.md|registerStaticRoutes]] (function: calls) — *registerStaticRoutes binds core system endpoints (Login, Home, PostgresBrowser, Frameless Demos).*
- [[web-interface/web-interface/src/router/static.go.md|static.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/home_dynamic_test.go.md|home_dynamic_test.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|main_test.go]] (calls)
- [[web-interface/web-interface/src/router/architecture_hygiene_test.go.md|architecture_hygiene_test.go]] (calls)
- [[web-interface/web-interface/src/router/architecture_hygiene_test.go.md|architecture_hygiene_test.go]] (same_package)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (same_package)
- [[web-interface/web-interface/src/router/router.go.md|RegisterRoutes]] (function: belongs_to) — *RegisterRoutes initializes the web interface endpoints on the provided ServeMux.*
- [[web-interface/web-interface/src/router/router.go.md|requireAuth]] (function: belongs_to) — *If the user_id session property is missing (0), the request is redirected to the /login endpoint.*
- [[web-interface/web-interface/src/router/static.go.md|static.go]] (calls)
- [[web-interface/web-interface/src/router/static.go.md|static.go]] (same_package)
<!-- SYNC:END -->
