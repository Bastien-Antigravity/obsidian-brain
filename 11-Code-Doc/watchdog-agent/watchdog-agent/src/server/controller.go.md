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
Automatically generated mirror for `watchdog-agent/src/server/controller.go`.

> **Essential Process**:
> Concrete implementation of core.WatchdogController interface. Aggregates live process tree statuses, evaluates database/RAG connection liveness, and triggers graceful or forced child process group restarts.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/core/controller.go.md|controller.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.GetStatus]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.RestartAll]] (method: defines_method) — *RestartService forcefully terminates the process group of a service to let it auto-restart*
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.RestartService]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|FindServiceByName]] (function: calls) — *FindServiceByName retrieves a registered service pointer by name*
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|IsPortListening]] (function: calls) — *IsPortListening checks if TCP port listens*
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|KillAll]] (function: calls) — *KillAll kills all supervised command processes clean*
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|LogInfo]] (function: calls) — *LogInfo writes a formatted message with watchdog prefix to stdout/logger*
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|types.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/utils/lock_windows.go.md|lock_windows.go]] (imports)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|rest_handler.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.GetStatus]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.RestartAll]] (method: belongs_to) — *RestartService forcefully terminates the process group of a service to let it auto-restart*
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller.RestartService]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller]] (struct: belongs_to) — *RestartService forcefully terminates the process group of a service to let it auto-restart*
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|Controller]] (struct: defines_method) — *RestartService forcefully terminates the process group of a service to let it auto-restart*
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|NewController]] (function: belongs_to) — *NewController creates a new Controller instance*
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|manager.go]] (calls)
<!-- SYNC:END -->
