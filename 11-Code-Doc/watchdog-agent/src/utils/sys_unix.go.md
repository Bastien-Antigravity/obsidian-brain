---
microservice: watchdog-agent
type: note
status: active
tags:
- '#service/watchdog-agent'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/utils/sys_unix.go`.

> **Essential Process**:
> Unix-specific process group management and signal dispatching for clean process tree termination.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/src/utils/sys_unix.go.md|KillProcessGroupByID]] (function: belongs_to) — *KillProcessGroupByID terminates a process group using its PID, trying SIGTERM before SIGKILL*
- [[watchdog-agent/watchdog-agent/src/utils/sys_unix.go.md|KillProcessGroup]] (function: belongs_to) — *attempting graceful SIGTERM first before sending SIGKILL [WD-04].*
- [[watchdog-agent/watchdog-agent/src/utils/sys_unix.go.md|SetSysProcAttrGroup]] (function: belongs_to) — *SetSysProcAttrGroup sets the process group attributes for Unix-like systems*
<!-- SYNC:END -->
