---
source: web-interface/src/postgres_browser/query_runner.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 19:46:58.616508
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: query_runner.go

## 📝 Description
Automatically generated mirror for `web-interface/src/postgres_browser/query_runner.go`.

> **Essential Process**:
> Read-only SQL query execution engine. Validates incoming queries to ensure strictly non-destructive operations (SELECT / WITH CTEs) and prevents SQL injection.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|BrowserHandler.switchDatabase]] (method: calls) — *switchDatabase connects to an alternate database on the same host configuration.*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|connection.go]] (same_package)
- [[web-interface/web-interface/src/postgres_browser/connection_test.go.md|connection_test.go]] (same_package)
- [[web-interface/web-interface/src/postgres_browser/connection_test.go.md|noopLogger.Close]] (method: calls)
- [[web-interface/web-interface/src/postgres_browser/connection_test.go.md|noopLogger.Error]] (method: calls)
- [[web-interface/web-interface/src/postgres_browser/query_runner.go.md|BrowserHandler.ExecuteQuery]] (method: defines_method) — *ExecuteQuery runs a custom read-only SQL SELECT statement.*

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/postgres_browser/query_runner.go.md|BrowserHandler.ExecuteQuery]] (method: belongs_to) — *ExecuteQuery runs a custom read-only SQL SELECT statement.*
- [[web-interface/web-interface/src/postgres_browser/query_runner.go.md|BrowserHandler]] (struct: defines_method) — *ExecuteQuery runs a custom read-only SQL SELECT statement.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
