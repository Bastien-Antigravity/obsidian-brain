---
source: web-interface/src/postgres_browser/contracts.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-10T13:21:54.555635
---

# Mirror: contracts.go

## 📝 Description
Automatically generated mirror for `web-interface/src/postgres_browser/contracts.go`.

> **Essential Process**:
> Introspects PostgreSQL and TimescaleDB system catalogs directly from the live database instance to produce authoritative, exhaustive SQL, Hypertable, Wire v3, and REST Browser Exchange Contracts.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.Get]] (method: calls) — *Get looks up a registered service by name or tag (case-insensitive, flexible with hyphens/underscores/spaces).*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|BrowserHandler.resolveDBConfig]] (method: calls) — *resolveDBConfig dynamically extracts pre-validated connection parameters from AppConfig.*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|BrowserHandler.switchDatabase]] (method: calls) — *switchDatabase connects to an alternate database on the same host configuration.*
- [[web-interface/web-interface/src/postgres_browser/connection.go.md|connection.go]] (same_package)
- [[web-interface/web-interface/src/postgres_browser/connection_test.go.md|connection_test.go]] (same_package)
- [[web-interface/web-interface/src/postgres_browser/connection_test.go.md|noopLogger.Close]] (method: calls)
- [[web-interface/web-interface/src/postgres_browser/contracts.go.md|BrowserHandler.GetTimescaleContracts]] (method: defines_method) — *GetTimescaleContracts queries live PostgreSQL/TimescaleDB catalogs and returns exhaustive exchange contracts.*

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/postgres_browser/contracts.go.md|BrowserHandler.GetTimescaleContracts]] (method: belongs_to) — *GetTimescaleContracts queries live PostgreSQL/TimescaleDB catalogs and returns exhaustive exchange contracts.*
- [[web-interface/web-interface/src/postgres_browser/contracts.go.md|BrowserHandler]] (struct: defines_method) — *GetTimescaleContracts queries live PostgreSQL/TimescaleDB catalogs and returns exhaustive exchange contracts.*
- [[web-interface/web-interface/src/postgres_browser/contracts.go.md|buildTimescaleContractsFromDB]] (function: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/contracts.go.md|introspectedColumn]] (struct: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/contracts.go.md|introspectedHypertable]] (struct: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/contracts.go.md|introspectedTableKey]] (struct: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/contracts.go.md|synthesizeTimescaleEnvelope]] (function: belongs_to)
- [[web-interface/web-interface/src/postgres_browser/contracts_test.go.md|contracts_test.go]] (calls)
- [[web-interface/web-interface/src/postgres_browser/contracts_test.go.md|contracts_test.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
