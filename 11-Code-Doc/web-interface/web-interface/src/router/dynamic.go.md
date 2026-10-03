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
Automatically generated mirror for `web-interface/src/router/dynamic.go`.

> **Essential Process**:
> Handles all dynamic API endpoints, stock analysis dashboards, OpenMFE mounting hooks, and system status listings.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/fundamental_analysis/fundamental_analysis.go.md|GetTopStocks]] (function: calls) — *GetTopStocks fetches top stocks from the specified table ordered by overall score.*
- [[web-interface/web-interface/src/fundamental_analysis/fundamental_analysis.go.md|fundamental_analysis.go]] (imports)
- [[web-interface/web-interface/src/renderer/renderer.go.md|RenderPage]] (function: calls) — *RenderPage parses templates and executes them using context-resolved configuration parameters.*
- [[web-interface/web-interface/src/renderer/renderer.go.md|renderer.go]] (imports)
- [[web-interface/web-interface/src/router/router.go.md|requireAuth]] (function: calls) — *If the user_id session property is missing (0), the request is redirected to the /login endpoint.*
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|router_test.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Close]] (method: calls)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/router/dynamic.go.md|FleetHealthResponse]] (struct: belongs_to) — *FleetHealthResponse summarizes overall fleet health for UI alerting.*
- [[web-interface/web-interface/src/router/dynamic.go.md|RegisterDynamicRoutes]] (function: belongs_to) — *RegisterDynamicRoutes binds all API, Stock query, and OpenMFE dynamic routes.*
- [[web-interface/web-interface/src/router/dynamic.go.md|ServiceHealthStatus]] (struct: belongs_to) — *ServiceHealthStatus holds individual service reachability state.*
- [[web-interface/web-interface/src/router/dynamic.go.md|checkFleetServicesHealth]] (function: belongs_to) — *checkFleetServicesHealth probes all base microservices concurrently with tight timeouts.*
- [[web-interface/web-interface/src/router/dynamic.go.md|targetSvc]] (struct: belongs_to)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (calls)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|router_test.go]] (calls)
- [[web-interface/web-interface/src/router/router_test.go.md|router_test.go]] (same_package)
<!-- SYNC:END -->
