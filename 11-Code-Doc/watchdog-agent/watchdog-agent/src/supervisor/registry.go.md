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
Automatically generated mirror for `watchdog-agent/src/supervisor/registry.go`.

> **Essential Process**:
> Topologies registry and dependency graph validator for managed ecosystem services. Configures executable paths, build steps, dynamic capability addresses, and inter-service dependency ordering for native host supervisor runs.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|FindServiceByName]] (function: calls) — *FindServiceByName retrieves a registered service pointer by name*
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|supervisor.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/utils/lock_windows.go.md|lock_windows.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|FindPythonCmd]] (function: calls) — *FindPythonCmd locates python3 or python command in virtual environment or system fallback*

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/registry.go.md|RegisterServices]] (function: belongs_to) — *RegisterServices initializes the topology registry slice of managed services*
- [[watchdog-agent/watchdog-agent/src/supervisor/registry.go.md|ValidateRegistry]] (function: belongs_to) — *ValidateRegistry checks for missing dependencies and dependency cycles*
- [[watchdog-agent/watchdog-agent/src/supervisor/registry.go.md|resolveServiceAddr]] (function: belongs_to)
<!-- SYNC:END -->
