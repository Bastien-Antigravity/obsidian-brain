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
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.GetOffset]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.Save]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.SetOffset]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|NewCheckpointManager]] (function: calls) — *NewCheckpointManager creates and loads a checkpoint manager.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|checkpoint.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|ResolveDBConfig]] (function: calls) — *targeting Option B (base ecosystem 'obsidiandb') and fails fast on missing values.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|db.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.DiscoverFiles]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.ScanAndShip]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|NewLogShipper]] (function: calls) — *NewLogShipper initializes the shipper with persistent cursor state.*
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|getFileInode]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|shipper.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|TestShipper_DiscoverFilesAndCheckpoint]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|TestShipper_OfflineDB_OffsetsFreeze]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|TestShipper_RotationDetection]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
