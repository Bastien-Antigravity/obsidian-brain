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
Automatically generated mirror for `watchdog-agent/src/utils/utils.go`.

> **Essential Process**:
> System utilities and network inspection helpers for watchdog-agent. Provides workspace root resolution, local IP detection, port listener tests, cross-platform process tree cleanup, and python virtualenv discovery.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/registry.go.md|registry.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|supervisor.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|FindPythonCmd]] (function: belongs_to) — *FindPythonCmd locates python3 or python command in virtual environment or system fallback*
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|FindWorkspaceRoot]] (function: belongs_to) — *FindWorkspaceRoot locates the workspace root containing docker-deployment*
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|GetLocalIPs]] (function: belongs_to) — *GetLocalIPs returns a set of local IP addresses for this machine*
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|IsLocalIP]] (function: belongs_to) — *IsLocalIP is an alias for IsLocal*
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|IsLocal]] (function: belongs_to) — *IsLocal checks if an IP belongs to the local machine*
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|IsOccupantFleetService]] (function: belongs_to) — *IsOccupantFleetService checks if the process listening on a port is a base/fleet service.*
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|KillProcessOnPort]] (function: belongs_to) — *KillProcessOnPort forcefully terminates any process listening on a port*
<!-- SYNC:END -->
