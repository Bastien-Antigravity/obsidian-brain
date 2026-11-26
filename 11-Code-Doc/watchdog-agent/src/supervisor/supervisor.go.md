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
Automatically generated mirror for `watchdog-agent/src/supervisor/supervisor.go`.

> **Essential Process**:
> Core supervisor engine managing lifecycle, port liveness, execution loops, process group management, stdout/stderr multiplexing, and graceful teardown for all supervised ecosystem child daemons.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/src/rest/rest_handler_test.go.md|mockWatchdogLogger.Critical]] (method: calls)
- [[watchdog-agent/src/rest/rest_handler_test.go.md|mockWatchdogLogger.Error]] (method: calls)
- [[watchdog-agent/src/rest/rest_handler_test.go.md|mockWatchdogLogger.Info]] (method: calls)
- [[watchdog-agent/src/supervisor/postgres_launcher.go.md|LaunchPostgresAttempt]] (function: calls) — *if it is not already running. It returns true if successful or if it was already running.*
- [[watchdog-agent/src/supervisor/postgres_launcher.go.md|postgres_launcher.go]] (same_package)
- [[watchdog-agent/src/supervisor/types.go.md|Service.ResolveAddr]] (method: calls) — *falling back to the service's baseline IP and Port.*
- [[watchdog-agent/src/supervisor/types.go.md|types.go]] (same_package)
- [[watchdog-agent/src/utils/lock_windows.go.md|lock_windows.go]] (imports)
- [[watchdog-agent/src/utils/utils.go.md|IsOccupantFleetService]] (function: calls) — *IsOccupantFleetService checks if the process listening on a port is a base/fleet service.*
- [[watchdog-agent/src/utils/utils.go.md|KillProcessOnPort]] (function: calls) — *KillProcessOnPort forcefully terminates any process listening on a port [WD-01]*

### 🔌 Consumers (Inbound)
- [[watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/src/config/heal.go.md|heal.go]] (calls)
- [[watchdog-agent/src/control/control_plane.go.md|control_plane.go]] (calls)
- [[watchdog-agent/src/server/controller.go.md|controller.go]] (calls)
- [[watchdog-agent/src/supervisor/postgres_launcher.go.md|postgres_launcher.go]] (calls)
- [[watchdog-agent/src/supervisor/postgres_launcher.go.md|postgres_launcher.go]] (same_package)
- [[watchdog-agent/src/supervisor/registry.go.md|registry.go]] (calls)
- [[watchdog-agent/src/supervisor/registry.go.md|registry.go]] (same_package)
- [[watchdog-agent/src/supervisor/supervisor.go.md|BuildService]] (function: belongs_to) — *BuildService executes the compilation step for a service*
- [[watchdog-agent/src/supervisor/supervisor.go.md|FindServiceByName]] (function: belongs_to) — *FindServiceByName retrieves a registered service pointer by name*
- [[watchdog-agent/src/supervisor/supervisor.go.md|IsPortListening]] (function: belongs_to) — *IsPortListening checks if TCP port listens*
- [[watchdog-agent/src/supervisor/supervisor.go.md|KillAll]] (function: belongs_to) — *KillAll kills all supervised command processes clean*
- [[watchdog-agent/src/supervisor/supervisor.go.md|LogError]] (function: belongs_to) — *LogError writes a formatted error message with watchdog prefix to stderr/logger*
- [[watchdog-agent/src/supervisor/supervisor.go.md|LogInfo]] (function: belongs_to) — *LogInfo writes a formatted message with watchdog prefix to stdout/logger*
- [[watchdog-agent/src/supervisor/supervisor.go.md|MonitorAndSupervise]] (function: belongs_to) — *MonitorAndSupervise is the supervisor runner loop*
- [[watchdog-agent/src/supervisor/supervisor.go.md|PipeOutput]] (function: belongs_to) — *PipeOutput routes logs from subprocess stdout/stderr with service prefixes*
- [[watchdog-agent/src/supervisor/supervisor.go.md|RegisterCmd]] (function: belongs_to) — *RegisterCmd adds a command to the active list*
- [[watchdog-agent/src/supervisor/supervisor.go.md|UnregisterCmd]] (function: belongs_to) — *UnregisterCmd removes a command from the active list*
- [[watchdog-agent/src/telegram/manager.go.md|manager.go]] (calls)
<!-- SYNC:END -->
