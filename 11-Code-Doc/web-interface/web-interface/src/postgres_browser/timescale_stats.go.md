---
source: web-interface/src/postgres_browser/timescale_stats.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 19:46:58.621143
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: timescale_stats.go

## 📝 Description
Automatically generated mirror for `web-interface/src/postgres_browser/timescale_stats.go`.

> **Essential Process**:
> Gathers TimescaleDB-specific operational statistics: hypertable counts, chunk distribution, compression status, total database size, and active query sessions.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.Get]] (method: calls) — *Get looks up a registered service by name or tag (case-insensitive, flexible with hyphens/underscores/spaces).*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|BrowserHandler.resolveDBConfig]] (method: calls) — *resolveDBConfig dynamically extracts pre-validated connection parameters from AppConfig.*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|BrowserHandler.switchDatabase]] (method: calls) — *switchDatabase connects to an alternate database on the same host configuration.*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|connection.go]] (same_package)
- [[web-interface/web-interface/src/postgres_browser/connection_test.go.md|connection_test.go]] (same_package)
- [[web-interface/web-interface/src/postgres_browser/connection_test.go.md|noopLogger.Close]] (method: calls)
- [[web-interface/web-interface/src/postgres_browser/timescale_stats.go.md|BrowserHandler.GetTimescaleStats]] (method: defines_method) — *GetTimescaleStats queries TimescaleDB hypertables, chunk statistics, and active connections.*

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/postgres_browser/timescale_stats.go.md|BrowserHandler.GetTimescaleStats]] (method: belongs_to) — *GetTimescaleStats queries TimescaleDB hypertables, chunk statistics, and active connections.*
- [[web-interface/web-interface/src/postgres_browser/timescale_stats.go.md|BrowserHandler]] (struct: defines_method) — *GetTimescaleStats queries TimescaleDB hypertables, chunk statistics, and active connections.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
