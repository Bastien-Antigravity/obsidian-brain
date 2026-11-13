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
Automatically generated mirror for `watchdog-agent/src/server/controller.go`.

> **Essential Process**:
> Concrete implementation of core.WatchdogController interface. Aggregates live process tree statuses, evaluates database/RAG connection liveness, and triggers graceful or forced child process group restarts.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/core/controller.go.md|controller.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.GetStatus]] (method: defines_method) — *GetStatus retrieves the status metadata of all supervised services*
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.RestartAll]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.RestartService]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|FindServiceByName]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|IsPortListening]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|KillAll]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|LogInfo]] (function: calls)
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|types.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/utils/lock_windows.go.md|lock_windows.go]] (imports)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/rest/contracts.go.md|contracts.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.GetStatus]] (method: belongs_to) — *GetStatus retrieves the status metadata of all supervised services*
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.RestartAll]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.RestartService]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller]] (struct: belongs_to) — *Controller implements core.WatchdogController interface*
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller]] (struct: defines_method) — *Controller implements core.WatchdogController interface*
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|NewController]] (function: belongs_to) — *NewController creates a new Controller instance*
<!-- SYNC:END -->
