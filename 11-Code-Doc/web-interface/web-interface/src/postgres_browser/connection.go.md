---
source: web-interface/src/postgres_browser/connection.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 19:46:58.629118
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: connection.go

## 📝 Description
Automatically generated mirror for `web-interface/src/postgres_browser/connection.go`.

> **Essential Process**:
> Manages database connection resolution, encrypted secret decryption, dynamic capability parsing, and cached connection pooling for Postgres/TimescaleDB.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|BrowserHandler.getDatabase]] (method: defines_method) — *getDatabase resolves connection settings from config and caches/returns the active pool.*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|BrowserHandler.resolveDBConfig]] (method: defines_method) — *resolveDBConfig dynamically extracts pre-validated connection parameters from AppConfig.*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|BrowserHandler.resolveTimescaleConfig]] (method: defines_method) — *resolveTimescaleConfig dynamically extracts connection settings and returns individual parameters.*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|BrowserHandler.switchDatabase]] (method: defines_method) — *switchDatabase connects to an alternate database on the same host configuration.*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|DBConfig.FormatDSN]] (method: defines_method) — *FormatDSN formats a lib/pq PostgreSQL connection string with URL encoding [WI-02].*
- [[web-interface/web-interface/src/postgres_browser/connection_test.go.md|connection_test.go]] (same_package)
- [[web-interface/web-interface/src/postgres_browser/connection_test.go.md|noopLogger.Close]] (method: calls)
- [[web-interface/web-interface/src/postgres_browser/connection_test.go.md|noopLogger.Info]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|BrowserHandler.getDatabase]] (method: belongs_to) — *getDatabase resolves connection settings from config and caches/returns the active pool.*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|BrowserHandler.resolveDBConfig]] (method: belongs_to) — *resolveDBConfig dynamically extracts pre-validated connection parameters from AppConfig.*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|BrowserHandler.resolveTimescaleConfig]] (method: belongs_to) — *resolveTimescaleConfig dynamically extracts connection settings and returns individual parameters.*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|BrowserHandler.switchDatabase]] (method: belongs_to) — *switchDatabase connects to an alternate database on the same host configuration.*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|BrowserHandler]] (struct: defines_method) — *resolveDBConfig dynamically extracts pre-validated connection parameters from AppConfig.*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|DBConfig.FormatDSN]] (method: belongs_to) — *FormatDSN formats a lib/pq PostgreSQL connection string with URL encoding [WI-02].*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|DBConfig]] (struct: belongs_to) — *DBConfig encapsulates resolved, validated PostgreSQL/TimescaleDB connection parameters.*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|DBConfig]] (struct: defines_method) — *DBConfig encapsulates resolved, validated PostgreSQL/TimescaleDB connection parameters.*
- [[web-interface/web-interface/src/postgres_browser/connection_test.go.md|connection_test.go]] (calls)
- [[web-interface/web-interface/src/postgres_browser/connection_test.go.md|connection_test.go]] (same_package)
- [[web-interface/web-interface/src/postgres_browser/explorer.go.md|explorer.go]] (calls)
- [[web-interface/web-interface/src/postgres_browser/explorer.go.md|explorer.go]] (same_package)
- [[web-interface/web-interface/src/postgres_browser/handler.go.md|handler.go]] (calls)
- [[web-interface/web-interface/src/postgres_browser/handler.go.md|handler.go]] (same_package)
- [[web-interface/web-interface/src/postgres_browser/query_runner.go.md|query_runner.go]] (calls)
- [[web-interface/web-interface/src/postgres_browser/query_runner.go.md|query_runner.go]] (same_package)
- [[web-interface/web-interface/src/postgres_browser/timescale_stats.go.md|timescale_stats.go]] (calls)
- [[web-interface/web-interface/src/postgres_browser/timescale_stats.go.md|timescale_stats.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
