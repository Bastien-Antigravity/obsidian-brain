---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/config/heal.go`.

> **Essential Process**:
> Automated configuration symlink self-healing subsystem. Audits, verifies, and repairs all base ecosystem standalone.yaml symlinks across 35 targets pointing to the authoritative native.yaml template.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|LogInfo]] (function: calls) — *LogInfo writes a formatted message with watchdog prefix to stdout/logger*
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|types.go]] (imports)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/config/heal.go.md|HealSymlinks]] (function: belongs_to) — *HealSymlinks heals ecosystem configuration symlinks pointing to the central standalone.yaml*
- [[watchdog-agent/watchdog-agent/src/config/heal.go.md|SymlinkTarget]] (struct: belongs_to)
- [[watchdog-agent/watchdog-agent/src/config/heal.go.md|safeLinkOrCopy]] (function: belongs_to)
<!-- SYNC:END -->
