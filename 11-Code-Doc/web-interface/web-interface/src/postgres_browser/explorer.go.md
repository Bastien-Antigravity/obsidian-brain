---
source: web-interface/src/postgres_browser/explorer.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 19:46:58.624995
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: explorer.go

## 📝 Description
Automatically generated mirror for `web-interface/src/postgres_browser/explorer.go`.

> **Essential Process**:
> Schema explorer providing catalog queries for databases, schemas, tables, column attributes, and paginated table record inspections.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.Get]] (method: calls) — *Get looks up a registered service by name or tag (case-insensitive, flexible with hyphens/underscores/spaces).*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|BrowserHandler.getDatabase]] (method: calls) — *getDatabase resolves connection settings from config and caches/returns the active pool.*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|BrowserHandler.switchDatabase]] (method: calls) — *switchDatabase connects to an alternate database on the same host configuration.*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|connection.go]] (same_package)
- [[web-interface/web-interface/src/postgres_browser/connection_test.go.md|connection_test.go]] (same_package)
- [[web-interface/web-interface/src/postgres_browser/connection_test.go.md|noopLogger.Close]] (method: calls)
- [[web-interface/web-interface/src/postgres_browser/connection_test.go.md|noopLogger.Error]] (method: calls)
- [[web-interface/web-interface/src/postgres_browser/explorer.go.md|BrowserHandler.GetColumns]] (method: defines_method) — *GetColumns gets detailed schema parameter attributes for columns in a table.*
- [[web-interface/web-interface/src/postgres_browser/explorer.go.md|BrowserHandler.GetDatabases]] (method: defines_method) — *GetDatabases returns a list of database namespaces on the host.*
- [[web-interface/web-interface/src/postgres_browser/explorer.go.md|BrowserHandler.GetSchemas]] (method: defines_method) — *GetSchemas returns database schemas (excluding catalog/toast namespaces).*
- [[web-interface/web-interface/src/postgres_browser/explorer.go.md|BrowserHandler.GetTableData]] (method: defines_method) — *GetTableData scans rows within a table limit/offset scope on a targeted database.*
- [[web-interface/web-interface/src/postgres_browser/explorer.go.md|BrowserHandler.GetTables]] (method: defines_method) — *GetTables lists all tables within the specified database and schema scope.*

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/postgres_browser/explorer.go.md|BrowserHandler.GetColumns]] (method: belongs_to) — *GetColumns gets detailed schema parameter attributes for columns in a table.*
- [[web-interface/web-interface/src/postgres_browser/explorer.go.md|BrowserHandler.GetDatabases]] (method: belongs_to) — *GetDatabases returns a list of database namespaces on the host.*
- [[web-interface/web-interface/src/postgres_browser/explorer.go.md|BrowserHandler.GetSchemas]] (method: belongs_to) — *GetSchemas returns database schemas (excluding catalog/toast namespaces).*
- [[web-interface/web-interface/src/postgres_browser/explorer.go.md|BrowserHandler.GetTableData]] (method: belongs_to) — *GetTableData scans rows within a table limit/offset scope on a targeted database.*
- [[web-interface/web-interface/src/postgres_browser/explorer.go.md|BrowserHandler.GetTables]] (method: belongs_to) — *GetTables lists all tables within the specified database and schema scope.*
- [[web-interface/web-interface/src/postgres_browser/explorer.go.md|BrowserHandler]] (struct: defines_method) — *GetDatabases returns a list of database namespaces on the host.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
