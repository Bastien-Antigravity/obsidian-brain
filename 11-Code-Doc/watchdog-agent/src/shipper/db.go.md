---
source: watchdog-agent/src/shipper/db.go
workspace: watchdog-agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-08 15:50:57.977007
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: db.go

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/shipper/db.go`.

> **Essential Process**:
> TimescaleDB / PostgreSQL error sink management for watchdog-agent. Resolves validated connection credentials from AppConfig capabilities, verifies schema "watchdog_agent".fleet_error_logs, and commits idempotent batch inserts.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient.Close]] (method: defines_method) — *Close closes the underlying database pool.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient.EnsureSchema]] (method: defines_method) — *EnsureSchema creates schema 'watchdog_agent', table 'fleet_error_logs', hypertable, and retention if missing.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient.InsertBatch]] (method: defines_method) — *InsertBatch idempotently inserts parsed error logs inside an atomic bounded transaction.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBConfig.DSN]] (method: defines_method) — *DSN returns the formatted PostgreSQL connection URI.*

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/rest/contracts.go.md|contracts.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient.Close]] (method: belongs_to) — *Close closes the underlying database pool.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient.EnsureSchema]] (method: belongs_to) — *EnsureSchema creates schema 'watchdog_agent', table 'fleet_error_logs', hypertable, and retention if missing.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient.InsertBatch]] (method: belongs_to) — *InsertBatch idempotently inserts parsed error logs inside an atomic bounded transaction.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient]] (struct: belongs_to) — *DBClient manages the TimescaleDB connection pool and idempotent batch writes.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient]] (struct: defines_method) — *DBClient manages the TimescaleDB connection pool and idempotent batch writes.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBConfig.DSN]] (method: belongs_to) — *DSN returns the formatted PostgreSQL connection URI.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBConfig]] (struct: belongs_to) — *DBConfig encapsulates validated PostgreSQL connection parameters.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBConfig]] (struct: defines_method) — *DBConfig encapsulates validated PostgreSQL connection parameters.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|FleetErrorLogsSchemaSQL]] (constant: belongs_to) — *FleetErrorLogsSchemaSQL defines the canonical Option B DDL inside obsidiandb schema 'watchdog_agent'.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|NewDBClient]] (function: belongs_to) — *NewDBClient establishes a connection pool to the configured base database.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|ResolveBrainID]] (function: belongs_to) — *documented in Multi-Brain Partitioning Standard: AppConfig -> env -> obsidian-brain.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|ResolveDBConfigWithAppConfig]] (function: belongs_to) — *targeting Option B (base ecosystem 'obsidiandb') and fails fast on missing values.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|TimescaleDBCap]] (struct: belongs_to) — *TimescaleDBCap mirrors the validated capabilities.timescale_db YAML structure.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|WatchdogErrorDBCap]] (struct: belongs_to) — *WatchdogErrorDBCap captures optional watchdog_agent error log settings in AppConfig.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|resolveErrorDBName]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/db_test.go.md|db_test.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/db_test.go.md|db_test.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|shipper.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|shipper.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|shipper_test.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|shipper_test.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
