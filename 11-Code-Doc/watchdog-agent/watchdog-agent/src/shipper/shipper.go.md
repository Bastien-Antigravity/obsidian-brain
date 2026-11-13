---
source: watchdog-agent/src/shipper/shipper.go
workspace: watchdog-agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-08T15:51:19.714693
---

# Mirror: shipper.go

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/shipper/shipper.go`.

> **Essential Process**:
> Autonomous fleet log tailer and shipper. Continuously monitors local log files across native host paths or container volume mounts, parses operational failures, guarantees idempotent at-least-once insertion into obsidiandb, and dispatches throttled incident events to Squad Agent over NATS.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.GetOffset]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.Save]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.SetOffset]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|NewCheckpointManager]] (function: calls) — *NewCheckpointManager creates and loads a checkpoint manager.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|checkpoint.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient.Close]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient.InsertBatch]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|NewDBClient]] (function: calls) — *NewDBClient establishes a connection pool to the configured base database.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|db.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|BuildIncidentEvent]] (function: calls) — *BuildIncidentEvent creates a structured IncidentEvent from a ParsedErrorLog.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|IncidentThrottler.ShouldDispatch]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|LocalIncidentNotifier.PublishIncident]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|NewIncidentThrottler]] (function: calls) — *NewIncidentThrottler creates a throttler with a specified suppression window.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|incident.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/parser.go.md|ParseLogLine]] (function: calls) — *Returns (log, true) strictly for canonical ERROR (10) and CRITICAL (11) entries.*
- [[watchdog-agent/watchdog-agent/src/shipper/parser.go.md|parser.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.DiscoverFiles]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.ScanAndShip]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.Start]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|Config]] (struct: belongs_to) — *Config configures the LogShipper engine.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.DiscoverFiles]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.ScanAndShip]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.Start]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper]] (struct: belongs_to) — *LogShipper coordinates multi-file tailing, checkpointing, and database syncing.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper]] (struct: defines_method) — *LogShipper coordinates multi-file tailing, checkpointing, and database syncing.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|NewLogShipper]] (function: belongs_to) — *NewLogShipper initializes the shipper with persistent cursor state.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|dirExists]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|getFileInode]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|shipper_test.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|shipper_test.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|supervisor.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|manager.go]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
