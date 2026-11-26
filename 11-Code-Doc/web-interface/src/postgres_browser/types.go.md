---
source: web-interface/src/postgres_browser/types.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 19:46:58.612582
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: types.go

## 📝 Description
Automatically generated mirror for `web-interface/src/postgres_browser/types.go`.

> **Essential Process**:
> Data Transfer Objects (DTOs) and struct definitions for PostgreSQL and TimescaleDB browser metadata inspection and SQL execution.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/postgres_browser/types.go.md|BrowserHandler]] (struct: belongs_to) — *BrowserHandler handles Postgres HTTP browser API operations.*
- [[web-interface/web-interface/src/postgres_browser/types.go.md|ColumnInfo]] (struct: belongs_to) — *ColumnInfo describes column schema attributes.*
- [[web-interface/web-interface/src/postgres_browser/types.go.md|QueryRequest]] (struct: belongs_to) — *QueryRequest defines the payload for ad-hoc read-only SQL queries.*
- [[web-interface/web-interface/src/postgres_browser/types.go.md|QueryResponse]] (struct: belongs_to) — *QueryResponse represents the tabulated result of an executed SQL query.*
- [[web-interface/web-interface/src/postgres_browser/types.go.md|TableData]] (struct: belongs_to) — *TableData represents paginated rows and total record counts for a table.*
- [[web-interface/web-interface/src/postgres_browser/types.go.md|TableInfo]] (struct: belongs_to) — *TableInfo encapsulates basic table identification.*
- [[web-interface/web-interface/src/postgres_browser/types.go.md|TimescaleDBCap]] (struct: belongs_to) — *TimescaleDBCap matches the timescale_db capability structure in configuration.*
- [[web-interface/web-interface/src/postgres_browser/types.go.md|TimescaleStatsResponse]] (struct: belongs_to) — *TimescaleStatsResponse defines the statistical overview of TimescaleDB hypertables, chunks, and activity.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
