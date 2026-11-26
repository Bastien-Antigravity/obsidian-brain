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
- [[watchdog-agent/src/core/controller.go.md|controller.go]] (imports)
- [[watchdog-agent/src/server/controller.go.md|Controller.GetStatus]] (method: defines_method) — *GetStatus retrieves the status metadata of all supervised services*
- [[watchdog-agent/src/server/controller.go.md|Controller.PauseService]] (method: defines_method) — *PauseService suspends auto-restart supervision for a service and terminates any running process*
- [[watchdog-agent/src/server/controller.go.md|Controller.RestartAll]] (method: defines_method) — *RestartAll kills all running processes so they all restart sequentially*
- [[watchdog-agent/src/server/controller.go.md|Controller.RestartService]] (method: defines_method) — *RestartService forcefully terminates the process group of a service to let it auto-restart*
- [[watchdog-agent/src/server/controller.go.md|Controller.ResumeService]] (method: defines_method) — *ResumeService re-enables supervision for a service, clears crash history, and allows supervisor to relaunch*
- [[watchdog-agent/src/supervisor/supervisor.go.md|FindServiceByName]] (function: calls) — *FindServiceByName retrieves a registered service pointer by name*
- [[watchdog-agent/src/supervisor/supervisor.go.md|IsPortListening]] (function: calls) — *IsPortListening checks if TCP port listens*
- [[watchdog-agent/src/supervisor/supervisor.go.md|KillAll]] (function: calls) — *KillAll kills all supervised command processes clean*
- [[watchdog-agent/src/supervisor/supervisor.go.md|LogInfo]] (function: calls) — *LogInfo writes a formatted message with watchdog prefix to stdout/logger*
- [[watchdog-agent/src/supervisor/types.go.md|types.go]] (imports)
- [[watchdog-agent/src/utils/lock_windows.go.md|lock_windows.go]] (imports)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/main.go.md|main.go]] (imports)
- [[watchdog-agent/src/rest/contracts.go.md|contracts.go]] (imports)
- [[watchdog-agent/src/server/controller.go.md|Controller.GetStatus]] (method: belongs_to) — *GetStatus retrieves the status metadata of all supervised services*
- [[watchdog-agent/src/server/controller.go.md|Controller.PauseService]] (method: belongs_to) — *PauseService suspends auto-restart supervision for a service and terminates any running process*
- [[watchdog-agent/src/server/controller.go.md|Controller.RestartAll]] (method: belongs_to) — *RestartAll kills all running processes so they all restart sequentially*
- [[watchdog-agent/src/server/controller.go.md|Controller.RestartService]] (method: belongs_to) — *RestartService forcefully terminates the process group of a service to let it auto-restart*
- [[watchdog-agent/src/server/controller.go.md|Controller.ResumeService]] (method: belongs_to) — *ResumeService re-enables supervision for a service, clears crash history, and allows supervisor to relaunch*
- [[watchdog-agent/src/server/controller.go.md|Controller]] (struct: belongs_to) — *Controller implements core.WatchdogController interface*
- [[watchdog-agent/src/server/controller.go.md|Controller]] (struct: defines_method) — *Controller implements core.WatchdogController interface*
- [[watchdog-agent/src/server/controller.go.md|NewController]] (function: belongs_to) — *NewController creates a new Controller instance*
- [[watchdog-agent/src/server/controller_test.go.md|controller_test.go]] (calls)
- [[watchdog-agent/src/server/controller_test.go.md|controller_test.go]] (same_package)
<!-- SYNC:END -->
