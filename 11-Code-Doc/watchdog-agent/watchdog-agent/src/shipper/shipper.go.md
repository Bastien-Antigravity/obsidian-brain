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
> Autonomous fleet log tailer and shipper. Continuously monitors local log files across native host paths or container volume mounts, parses operational failures, and guarantees at-least-once insertion into TimescaleDB.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.GetOffset]] (method: calls) — *GetOffset retrieves the last committed offset and inode for a file.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.Save]] (method: calls) — *Save atomically writes the current state to disk.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.SetOffset]] (method: calls) — *SetOffset updates the file cursor.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|NewCheckpointManager]] (function: calls) — *NewCheckpointManager creates and loads a checkpoint manager.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|checkpoint.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient.Close]] (method: calls) — *Close closes the underlying database pool.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient.InsertBatch]] (method: calls) — *InsertBatch inserts a batch of parsed error logs in a single transaction.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|NewDBClient]] (function: calls) — *NewDBClient establishes a connection to TimescaleDB.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|db.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|BuildIncidentEvent]] (function: calls) — *BuildIncidentEvent creates a structured IncidentEvent from a ParsedErrorLog.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|IncidentThrottler.ShouldDispatch]] (method: calls) — *Returns (shouldDispatch, suppressedCount).*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|LocalIncidentNotifier.PublishIncident]] (method: calls) — *PublishIncident records the incident locally.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|NewIncidentThrottler]] (function: calls) — *NewIncidentThrottler creates a throttler with a specified suppression window.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|incident.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/parser.go.md|ParseLogLine]] (function: calls) — *ParseLogLine attempts to parse a standardized log line. Returns (log, true) if level >= ERROR.*
- [[watchdog-agent/watchdog-agent/src/shipper/parser.go.md|parser.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.DiscoverFiles]] (method: defines_method) — *DiscoverFiles finds all *.log files in Docker volumes or native workspace trees.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.ScanAndShip]] (method: defines_method) — *ScanAndShip executes one synchronization pass across all monitored log files.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.Start]] (method: defines_method) — *Start launches the continuous log shipper background loop.*

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|Config]] (struct: belongs_to) — *Config configures the LogShipper engine.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.DiscoverFiles]] (method: belongs_to) — *DiscoverFiles finds all *.log files in Docker volumes or native workspace trees.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.ScanAndShip]] (method: belongs_to) — *ScanAndShip executes one synchronization pass across all monitored log files.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.Start]] (method: belongs_to) — *Start launches the continuous log shipper background loop.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper]] (struct: belongs_to) — *LogShipper coordinates multi-file tailing and database syncing.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper]] (struct: defines_method) — *LogShipper coordinates multi-file tailing and database syncing.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|NewLogShipper]] (function: belongs_to) — *NewLogShipper initializes the shipper with state persistence.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|dirExists]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|getFileInode]] (function: belongs_to) — *getFileInode extracts the OS inode number on Unix-like platforms.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|shipper_test.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|shipper_test.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|supervisor.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|manager.go]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
