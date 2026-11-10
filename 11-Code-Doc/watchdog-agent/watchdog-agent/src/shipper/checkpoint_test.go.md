---
source: watchdog-agent/src/shipper/checkpoint_test.go
workspace: watchdog-agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-09T14:40:54.514711
---

# Mirror: checkpoint_test.go

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/shipper/checkpoint_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler_test.go.md|mockWatchdogLogger.Error]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.GetOffset]] (method: calls) — *GetOffset retrieves the last committed offset and inode for a file.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.Save]] (method: calls) — *Save atomically writes the current state to disk.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.SetOffset]] (method: calls) — *SetOffset updates the file cursor.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|NewCheckpointManager]] (function: calls) — *NewCheckpointManager creates and loads a checkpoint manager.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|checkpoint.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint_test.go.md|TestCheckpointManager_CorruptedFileRecovery]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint_test.go.md|TestCheckpointManager_NonExistentFile]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint_test.go.md|TestCheckpointManager_SaveAndReload]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
