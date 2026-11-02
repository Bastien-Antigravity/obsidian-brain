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
Automatically generated mirror for `web-interface/src/router/static.go`.

> **Essential Process**:
> Registers and serves the core static HTML page templates for the web-interface dashboard (Home, Login, PostgresBrowser, Standalone Demos). General static pages and documentation articles are automatically handled by `autodiscovery.go`.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/renderer/renderer.go.md|RenderPage]] (function: calls) — *RenderPage parses templates and executes them using context-resolved configuration parameters.*
- [[web-interface/web-interface/src/renderer/renderer.go.md|renderer.go]] (imports)
- [[web-interface/web-interface/src/router/autodiscovery.go.md|FindStaticPage]] (function: calls) — *FindStaticPage searches for a static page by its route path or legacy alias.*
- [[web-interface/web-interface/src/router/autodiscovery.go.md|RenderStaticPage]] (function: calls) — *RenderStaticPage renders an auto-discovered static page with its active category indicators.*
- [[web-interface/web-interface/src/router/autodiscovery.go.md|autodiscovery.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (calls)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (same_package)
- [[web-interface/web-interface/src/router/static.go.md|registerStaticRoutes]] (function: belongs_to) — *registerStaticRoutes binds core system endpoints (Login, Home, PostgresBrowser, Frameless Demos).*
<!-- SYNC:END -->
