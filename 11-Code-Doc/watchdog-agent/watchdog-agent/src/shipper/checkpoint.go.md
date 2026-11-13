---
source: watchdog-agent/src/shipper/checkpoint.go
workspace: watchdog-agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-08T15:50:35.205772
---

# Mirror: checkpoint.go

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/shipper/checkpoint.go`.

> **Essential Process**:
> Checkpoint manager tracking persistent file byte offsets and inodes. Guarantees at-least-once delivery with zero duplicate replay across shipper restarts, crashes, or log file rotations.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.GetOffset]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.Save]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.SetOffset]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.load]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/rest/contracts.go.md|contracts.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.GetOffset]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.Save]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.SetOffset]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager.load]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager]] (struct: belongs_to) — *CheckpointManager coordinates thread-safe file cursor persistence.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|CheckpointManager]] (struct: defines_method) — *CheckpointManager coordinates thread-safe file cursor persistence.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|FileOffset]] (struct: belongs_to) — *FileOffset records the read progression for a single log file.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|NewCheckpointManager]] (function: belongs_to) — *NewCheckpointManager creates and loads a checkpoint manager.*
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint_test.go.md|checkpoint_test.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint_test.go.md|checkpoint_test.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|shipper.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|shipper.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|shipper_test.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper_test.go.md|shipper_test.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
