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
Automatically generated mirror for `web-interface/src/router/static.go`.

> **Essential Process**:
> Registers and serves the static HTML page templates for the web-interface dashboard. Connects incoming paths to the unified rendering engine.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/renderer/renderer.go.md|RenderPage]] (function: calls) — *RenderPage parses templates and executes them using context-resolved configuration parameters.*
- [[web-interface/web-interface/src/renderer/renderer.go.md|renderer.go]] (imports)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (calls)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (same_package)
- [[web-interface/web-interface/src/router/static.go.md|registerStaticRoutes]] (function: belongs_to) — *registerStaticRoutes binds all static HTML rendering endpoints to the serve mux.*
<!-- SYNC:END -->
