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
Automatically generated mirror for `watchdog-agent/src/utils/sys_windows.go`.

> **Essential Process**:
> Windows-specific process tree management and taskkill termination.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/src/utils/sys_windows.go.md|KillProcessGroupByID]] (function: belongs_to) — *KillProcessGroupByID forcefully terminates a process group using its PID*
- [[watchdog-agent/watchdog-agent/src/utils/sys_windows.go.md|KillProcessGroup]] (function: belongs_to) — *KillProcessGroup forcefully terminates a process and all of its subprocesses (process tree)*
- [[watchdog-agent/watchdog-agent/src/utils/sys_windows.go.md|SetSysProcAttrGroup]] (function: belongs_to) — *SetSysProcAttrGroup sets the process group attributes for Windows systems*
<!-- SYNC:END -->
