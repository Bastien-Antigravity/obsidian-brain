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
Automatically generated mirror for `web-interface/src/router/router.go`.

> **Essential Process**:
> Manages and routes all HTTP requests for the web dashboard interface. Segregates static template actions from dynamic JSON API and MFE endpoints.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/router/dynamic.go.md|RegisterDynamicRoutes]] (function: calls) — *RegisterDynamicRoutes binds all API, Stock query, and OpenMFE dynamic routes.*
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|router_test.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Info]] (method: calls)
- [[web-interface/web-interface/src/router/static.go.md|registerStaticRoutes]] (function: calls) — *registerStaticRoutes binds all static HTML rendering endpoints to the serve mux.*
- [[web-interface/web-interface/src/router/static.go.md|static.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|main_test.go]] (calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (same_package)
- [[web-interface/web-interface/src/router/router.go.md|RegisterRoutes]] (function: belongs_to) — *RegisterRoutes initializes the web interface endpoints on the provided ServeMux.*
- [[web-interface/web-interface/src/router/router.go.md|requireAuth]] (function: belongs_to) — *If the user_id session property is missing (0), the request is redirected to the /login endpoint.*
<!-- SYNC:END -->
