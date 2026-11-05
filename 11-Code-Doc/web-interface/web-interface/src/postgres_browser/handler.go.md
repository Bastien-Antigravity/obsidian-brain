---
source: web-interface/src/postgres_browser/handler.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 19:46:58.608866
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: handler.go

## 📝 Description
Automatically generated mirror for `web-interface/src/postgres_browser/handler.go`.

> **Essential Process**:
> HTTP router registration and lazy initialization worker for the PostgreSQL and TimescaleDB browser endpoints.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|BrowserHandler.getDatabase]] (method: calls) — *getDatabase resolves connection settings from config and caches/returns the active pool.*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|connection.go]] (same_package)
- [[web-interface/web-interface/src/postgres_browser/connection_test.go.md|connection_test.go]] (same_package)
- [[web-interface/web-interface/src/postgres_browser/connection_test.go.md|noopLogger.Error]] (method: calls)
- [[web-interface/web-interface/src/postgres_browser/connection_test.go.md|noopLogger.Info]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (imports)
- [[web-interface/web-interface/src/postgres_browser/handler.go.md|RegisterPostgresBrowserRoutes]] (function: belongs_to) — *RegisterPostgresBrowserRoutes maps browser HTTP endpoints and returns the wrapped handler.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
