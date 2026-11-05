---
source: web-interface/src/router/autodiscovery_test.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-10-26 17:19:17.687421
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: autodiscovery_test.go

## 📝 Description
Automatically generated mirror for `web-interface/src/router/autodiscovery_test.go`.

> **Essential Process**:
> Unit tests for the static page auto-discovery engine. Verifies directory scanning, metadata extraction, hierarchical categorization, alias resolution, and JSON navigation tree endpoints.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/router/autodiscovery.go.md|FindStaticPage]] (function: calls) — *FindStaticPage searches for a static page by its route path or legacy alias.*
- [[web-interface/web-interface/src/router/autodiscovery.go.md|GetStaticCategories]] (function: calls) — *GetStaticCategories returns a thread-safe deep copy of all discovered static categories.*
- [[web-interface/web-interface/src/router/autodiscovery.go.md|InitAutoDiscovery]] (function: calls) — *InitAutoDiscovery scans the filesystem for static pages and compiles the navigation catalog.*
- [[web-interface/web-interface/src/router/autodiscovery.go.md|RegisterAutoDiscoveryRoutes]] (function: calls) — *RegisterAutoDiscoveryRoutes binds static page discovery routes, alias redirects, and API.*
- [[web-interface/web-interface/src/router/autodiscovery.go.md|autodiscovery.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/router/autodiscovery_test.go.md|TestAutoDiscoveryScanningAndHierarchy]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
