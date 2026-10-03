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
Automatically generated mirror for `web-interface/src/renderer/renderer.go`.

> **Essential Process**:
> Renders page templates dynamically, embedding CSRF tokens, user session state, dynamic host-resolved base URLs, and WebSocket endpoints.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (imports)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|main_test.go]] (imports)
- [[web-interface/web-interface/src/renderer/renderer.go.md|PageData]] (struct: belongs_to) — *PageData wraps page-specific data with global site config and auth state for templates.*
- [[web-interface/web-interface/src/renderer/renderer.go.md|RenderPage]] (function: belongs_to) — *RenderPage parses templates and executes them using context-resolved configuration parameters.*
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (imports)
- [[web-interface/web-interface/src/router/static.go.md|static.go]] (calls)
- [[web-interface/web-interface/src/router/static.go.md|static.go]] (imports)
<!-- SYNC:END -->
