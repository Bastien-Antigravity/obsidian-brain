---
source: web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 19:46:58.568614
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: postgres_browser.go

## 📝 Description
Automatically generated mirror for `web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go`.

> **Essential Process**:
> Implements the Postgres database metadata browser and SQL query runner. Integrates with the dashboard to allow developers to inspect database states.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.ExecuteQuery]] (method: defines_method) — *ExecuteQuery runs a custom read-only SQL SELECT statement.*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetColumns]] (method: defines_method) — *GetColumns gets detailed schema parameter attributes for columns in a table.*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetDatabases]] (method: defines_method) — *GetDatabases returns a list of database namespaces on the host.*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetSchemas]] (method: defines_method) — *GetSchemas returns database schemas (excluding catalog/toast namespaces).*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetTableData]] (method: defines_method) — *GetTableData scans rows within a table limit/offset scope on a targeted database.*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetTables]] (method: defines_method) — *GetTables lists all tables within the specified database and schema scope.*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetTimescaleStats]] (method: defines_method) — *GetTimescaleStats queries TimescaleDB hypertables, chunk statistics, and active connections.*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.getDatabase]] (method: defines_method) — *getDatabase resolves connection settings from config and caches/returns the active pool.*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.resolveTimescaleConfig]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.switchDatabase]] (method: defines_method) — *switchDatabase connects to an alternate database on the same host configuration.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.Get]] (method: calls) — *Get looks up a registered service by name or tag (case-insensitive, flexible with hyphens/underscores/spaces).*
- [[web-interface/web-interface/src/middleware/middleware.go.md|CorsMiddleware]] (function: calls) — *CorsMiddleware allows cross-origin requests*
- [[web-interface/web-interface/src/middleware/middleware.go.md|middleware.go]] (imports)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.ExecuteQuery]] (method: belongs_to) — *ExecuteQuery runs a custom read-only SQL SELECT statement.*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetColumns]] (method: belongs_to) — *GetColumns gets detailed schema parameter attributes for columns in a table.*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetDatabases]] (method: belongs_to) — *GetDatabases returns a list of database namespaces on the host.*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetSchemas]] (method: belongs_to) — *GetSchemas returns database schemas (excluding catalog/toast namespaces).*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetTableData]] (method: belongs_to) — *GetTableData scans rows within a table limit/offset scope on a targeted database.*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetTables]] (method: belongs_to) — *GetTables lists all tables within the specified database and schema scope.*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.GetTimescaleStats]] (method: belongs_to) — *GetTimescaleStats queries TimescaleDB hypertables, chunk statistics, and active connections.*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.getDatabase]] (method: belongs_to) — *getDatabase resolves connection settings from config and caches/returns the active pool.*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.resolveTimescaleConfig]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler.switchDatabase]] (method: belongs_to) — *switchDatabase connects to an alternate database on the same host configuration.*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler]] (struct: belongs_to) — *BrowserHandler handles Postgres HTTP browser API operations.*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|BrowserHandler]] (struct: defines_method) — *BrowserHandler handles Postgres HTTP browser API operations.*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|ColumnInfo]] (struct: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|QueryRequest]] (struct: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|QueryResponse]] (struct: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|RegisterPostgresBrowserRoutes]] (function: belongs_to) — *RegisterPostgresBrowserRoutes maps browser HTTP endpoints and returns the wrapped handler.*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|TableData]] (struct: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|TableInfo]] (struct: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|TimescaleDBCap]] (struct: belongs_to) — *TimescaleDBCap matches the timescale_db capability structure*
- [[web-interface/web-interface/backup_cleaned_assets/src/postgres_browser/postgres_browser.go.md|TimescaleStatsResponse]] (struct: belongs_to) — *TimescaleStatsResponse defines the statistical overview of TimescaleDB hypertables, chunks, and activity.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
