---
source: watchdog-agent/src/shipper/shipper.go
workspace: watchdog-agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-08 15:51:19.714693
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: shipper.go

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/shipper/shipper.go`.

> **Essential Process**:
> Autonomous fleet log tailer and shipper. Continuously monitors local log files across native host paths or container volume mounts, parses operational failures, guarantees idempotent at-least-once insertion into obsidiandb, and dispatches throttled incident events to Squad Agent over NATS.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler_test.go.md|mockWatchdogLogger.Info]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler_test.go.md|mockWatchdogLogger.Warning]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.GetOffset]] (method: calls) — *GetOffset retrieves the last committed offset and inode for a file.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.PruneMissingFiles]] (method: calls) — *PruneMissingFiles removes stale offsets whose log files no longer exist on disk.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.Save]] (method: calls) — *Save atomically writes the current state to disk.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.SetOffset]] (method: calls) — *SetOffset updates the file cursor.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|NewCheckpointManager]] (function: calls) — *NewCheckpointManager creates and loads a checkpoint manager.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|checkpoint.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient.Close]] (method: calls) — *Close closes the underlying database pool.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient.InsertBatch]] (method: calls) — *InsertBatch idempotently inserts parsed error logs inside an atomic bounded transaction.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|NewDBClient]] (function: calls) — *NewDBClient establishes a connection pool to the configured base database.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|db.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|BuildIncidentEvent]] (function: calls) — *BuildIncidentEvent creates a structured IncidentEvent from a ParsedErrorLog.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|IncidentThrottler.ShouldDispatch]] (method: calls) — *Returns (shouldDispatch, accumulatedCount).*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|LocalIncidentNotifier.PublishIncident]] (method: calls) — *PublishIncident records the incident locally.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|NewIncidentThrottler]] (function: calls) — *NewIncidentThrottler creates a throttler with a specified suppression window.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|incident.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/parser.go.md|ComputeEventHash]] (function: calls) — *brain, file path, byte offset, and timestamp so crash replays are idempotent.*
- [[watchdog-agent/watchdog-agent/src/shipper/parser.go.md|ParseLogLine]] (function: calls) — *Returns (log, true) strictly for canonical ERROR (10) and CRITICAL (11) entries.*
- [[watchdog-agent/watchdog-agent/src/shipper/parser.go.md|parser.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.DiscoverFiles]] (method: defines_method) — *DiscoverFiles finds all *.log files in Docker volumes or native workspace trees.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.ScanAndShip]] (method: defines_method) — *ScanAndShip executes one bounded synchronization pass across monitored log files.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.ScanDir]] (method: defines_method) — *ScanDir returns the resolved external log scan directory (empty if scanning workspace RootDir).*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.Start]] (method: defines_method) — *Start launches the continuous log shipper background loop.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.ensureConnected]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.tailSingleFile]] (method: defines_method) — *tailSingleFile reads complete newline-terminated lines from lastOffset up to maxRemaining errors.*

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|Config]] (struct: belongs_to) — *Config configures the LogShipper engine.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|DirExists]] (function: belongs_to) — *DirExists reports whether path exists and is a directory.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.DiscoverFiles]] (method: belongs_to) — *DiscoverFiles finds all *.log files in Docker volumes or native workspace trees.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.ScanAndShip]] (method: belongs_to) — *ScanAndShip executes one bounded synchronization pass across monitored log files.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.ScanDir]] (method: belongs_to) — *ScanDir returns the resolved external log scan directory (empty if scanning workspace RootDir).*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.Start]] (method: belongs_to) — *Start launches the continuous log shipper background loop.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.ensureConnected]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.tailSingleFile]] (method: belongs_to) — *tailSingleFile reads complete newline-terminated lines from lastOffset up to maxRemaining errors.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper]] (struct: belongs_to) — *LogShipper coordinates multi-file tailing, checkpointing, and database syncing.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper]] (struct: defines_method) — *LogShipper coordinates multi-file tailing, checkpointing, and database syncing.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|NewLogShipper]] (function: belongs_to) — *NewLogShipper initializes the shipper with persistent cursor state.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|defaultMaxBatchSize]] (constant: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|getFileInode]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|isAggregatedMainLog]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|isOwnLogServerEntry]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|pendingOffset]] (struct: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|shipper_test.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|shipper_test.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
