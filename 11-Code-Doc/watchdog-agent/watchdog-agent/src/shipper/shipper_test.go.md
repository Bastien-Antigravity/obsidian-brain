---
source: watchdog-agent/src/shipper/shipper_test.go
workspace: watchdog-agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-08T15:51:27.503776
---

# Mirror: shipper_test.go

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/shipper/shipper_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.GetOffset]] (method: calls) — *GetOffset retrieves the last committed offset and inode for a file.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.Save]] (method: calls) — *Save atomically writes the current state to disk.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.SetOffset]] (method: calls) — *SetOffset updates the file cursor.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|NewCheckpointManager]] (function: calls) — *NewCheckpointManager creates and loads a checkpoint manager.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|checkpoint.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBClient.Close]] (method: calls) — *Close closes the underlying database pool.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|db.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.DiscoverFiles]] (method: calls) — *DiscoverFiles finds all *.log files in Docker volumes or native workspace trees.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.ScanAndShip]] (method: calls) — *ScanAndShip executes one bounded synchronization pass across monitored log files.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.tailSingleFile]] (method: calls) — *tailSingleFile reads complete newline-terminated lines from lastOffset up to maxRemaining errors.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|NewLogShipper]] (function: calls) — *NewLogShipper initializes the shipper with persistent cursor state.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|getFileInode]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|shipper.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|TestShipper_DiscoverFilesAndCheckpoint]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|TestShipper_OfflineDB_OffsetsFreeze]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|TestShipper_RotationDetection]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|TestShipper_SkipsForwardedEntriesInMainLog]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|TestShipper_TailSingleFile_BoundedBatchChunking]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|TestShipper_TailSingleFile_SkipsIncompleteEOFLine]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|testDummyDBConfig]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|testLogger]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
