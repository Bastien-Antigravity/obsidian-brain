---
source: watchdog-agent/src/shipper/db.go
workspace: watchdog-agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-08T15:50:57.977007
---

# Mirror: db.go

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/shipper/db.go`.

> **Essential Process**:
> TimescaleDB error sink management. Resolves connection credentials, ensures hypertable schema availability, and executes atomic batch inserts.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient.Close]] (method: defines_method) — *Close closes the underlying database pool.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient.EnsureSchema]] (method: defines_method) — *EnsureSchema creates the fleet_error_logs table and hypertable if missing at startup.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient.InsertBatch]] (method: defines_method) — *InsertBatch inserts a batch of parsed error logs in a single transaction.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBConfig.DSN]] (method: defines_method) — *DSN returns the formatted PostgreSQL connection string.*

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient.Close]] (method: belongs_to) — *Close closes the underlying database pool.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient.EnsureSchema]] (method: belongs_to) — *EnsureSchema creates the fleet_error_logs table and hypertable if missing at startup.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient.InsertBatch]] (method: belongs_to) — *InsertBatch inserts a batch of parsed error logs in a single transaction.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient]] (struct: belongs_to) — *DBClient manages the TimescaleDB connection and batch insertions.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient]] (struct: defines_method) — *DBClient manages the TimescaleDB connection and batch insertions.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBConfig.DSN]] (method: belongs_to) — *DSN returns the formatted PostgreSQL connection string.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBConfig]] (struct: belongs_to) — *DBConfig encapsulates PostgreSQL connection options.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBConfig]] (struct: defines_method) — *DBConfig encapsulates PostgreSQL connection options.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|FleetErrorLogsSchemaSQL]] (constant: belongs_to) — *FleetErrorLogsSchemaSQL defines the canonical DDL for the watchdog TimescaleDB sink.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|NewDBClient]] (function: belongs_to) — *NewDBClient establishes a connection to TimescaleDB.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|ResolveDBConfigWithAppConfig]] (function: belongs_to) — *3. Resilient ecosystem fallback defaults.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|ResolveDBConfig]] (function: belongs_to) — *ResolveDBConfig extracts configuration from environment variables with standard defaults.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|TimescaleDBCap]] (struct: belongs_to) — *TimescaleDBCap represents the capability structure in distributed configuration.*
- [[watchdog-agent/watchdog-agent/src/shipper/db_test.go.md|db_test.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/db_test.go.md|db_test.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|shipper.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|shipper.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|shipper_test.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|shipper_test.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
