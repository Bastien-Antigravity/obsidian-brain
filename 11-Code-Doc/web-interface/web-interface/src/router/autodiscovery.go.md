---
source: web-interface/src/router/autodiscovery.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-10-26 17:19:17.698165
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: autodiscovery.go

## 📝 Description
Automatically generated mirror for `web-interface/src/router/autodiscovery.go`.

> **Essential Process**:
> Auto-discovers static HTML pages from the filesystem, extracts page metadata, organizes pages into hierarchical categories for the left sidebar, and binds dynamic routes and legacy aliases to the unified renderer.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/renderer/renderer.go.md|RenderPageWithMetadata]] (function: calls) — *RenderPageWithMetadata renders a page with category, title, subtitle, icon, and navigation categories.*
- [[web-interface/web-interface/src/renderer/renderer.go.md|renderer.go]] (imports)
- [[web-interface/web-interface/src/router/router_test.go.md|router_test.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Close]] (method: calls)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Error]] (method: calls)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Info]] (method: calls)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Warning]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/router/autodiscovery.go.md|CategoryMeta]] (struct: belongs_to) — *CategoryMeta defines optional metadata stored in a category.json file.*
- [[web-interface/web-interface/src/router/autodiscovery.go.md|FindStaticPage]] (function: belongs_to) — *FindStaticPage searches for a static page by its route path or legacy alias.*
- [[web-interface/web-interface/src/router/autodiscovery.go.md|GetStaticCategories]] (function: belongs_to) — *GetStaticCategories returns a thread-safe deep copy of all discovered static categories.*
- [[web-interface/web-interface/src/router/autodiscovery.go.md|InitAutoDiscovery]] (function: belongs_to) — *InitAutoDiscovery scans the filesystem for static pages and compiles the navigation catalog.*
- [[web-interface/web-interface/src/router/autodiscovery.go.md|RegisterAutoDiscoveryRoutes]] (function: belongs_to) — *RegisterAutoDiscoveryRoutes binds static page discovery routes, alias redirects, and API.*
- [[web-interface/web-interface/src/router/autodiscovery.go.md|RenderStaticPage]] (function: belongs_to) — *RenderStaticPage renders an auto-discovered static page with its active category indicators.*
- [[web-interface/web-interface/src/router/autodiscovery.go.md|StaticCategory]] (struct: belongs_to) — *StaticCategory represents a group of static pages in the left sidebar accordion.*
- [[web-interface/web-interface/src/router/autodiscovery.go.md|StaticPage]] (struct: belongs_to) — *StaticPage represents an auto-discovered static HTML page.*
- [[web-interface/web-interface/src/router/autodiscovery.go.md|cleanTitle]] (function: belongs_to)
- [[web-interface/web-interface/src/router/autodiscovery.go.md|humanizeTitle]] (function: belongs_to) — *humanizeTitle converts camelCase or kebab-case file names into readable title strings.*
- [[web-interface/web-interface/src/router/autodiscovery.go.md|parseCategoryMetadata]] (function: belongs_to)
- [[web-interface/web-interface/src/router/autodiscovery.go.md|parseFileMetadata]] (function: belongs_to)
- [[web-interface/web-interface/src/router/autodiscovery.go.md|parseOrderAndBase]] (function: belongs_to)
- [[web-interface/web-interface/src/router/autodiscovery.go.md|parseOrderAndTitle]] (function: belongs_to)
- [[web-interface/web-interface/src/router/autodiscovery.go.md|slugify]] (function: belongs_to)
- [[web-interface/web-interface/src/router/autodiscovery_test.go.md|autodiscovery_test.go]] (calls)
- [[web-interface/web-interface/src/router/autodiscovery_test.go.md|autodiscovery_test.go]] (same_package)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (calls)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (same_package)
- [[web-interface/web-interface/src/router/static.go.md|static.go]] (calls)
- [[web-interface/web-interface/src/router/static.go.md|static.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
