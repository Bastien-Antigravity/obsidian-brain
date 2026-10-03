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
Automatically generated mirror for `watchdog-agent/main.go`.

> **Essential Process**:
> Bastien-Antigravity Watchdog Agent main entry point. Orchestrates native host microservices, heals ecosystem configuration symlinks, manages node single-instance locking, publishes NATS telemetry, and exposes the HTTP REST / OpenMFE management portal.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/config/heal.go.md|HealSymlinks]] (function: calls) — *HealSymlinks heals ecosystem configuration symlinks pointing to the central standalone.yaml*
- [[watchdog-agent/watchdog-agent/src/config/heal.go.md|heal.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/control/control_plane.go.md|StartNATSControlPlane]] (function: calls) — *StartNATSControlPlane connects to the NATS event bus and publishes node heartbeats*
- [[watchdog-agent/watchdog-agent/src/control/control_plane.go.md|control_plane.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/rest/mfe.js.md|mfe.js]] (imports)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|NewRESTHandler]] (function: calls) — *NewRESTHandler creates a new RESTHandler instance*
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler.StartServer]] (method: calls) — *StartServer launches HTTP REST API server*
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|NewController]] (function: calls) — *NewController creates a new Controller instance*
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|controller.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/supervisor/registry.go.md|RegisterServices]] (function: calls) — *RegisterServices initializes the topology registry slice of managed services*
- [[watchdog-agent/watchdog-agent/src/supervisor/registry.go.md|ValidateRegistry]] (function: calls) — *ValidateRegistry checks for missing dependencies and dependency cycles*
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|LogError]] (function: calls) — *LogError writes a formatted error message with watchdog prefix to stderr/logger*
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|LogInfo]] (function: calls) — *LogInfo writes a formatted message with watchdog prefix to stdout/logger*
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|MonitorAndSupervise]] (function: calls) — *MonitorAndSupervise is the supervisor runner loop*
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|types.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|manager.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/utils/lock_windows.go.md|AcquireLock]] (function: calls) — *AcquireLock opens and locks the lock file exclusively on Windows using CreateFile.*
- [[watchdog-agent/watchdog-agent/src/utils/lock_windows.go.md|lock_windows.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|FindWorkspaceRoot]] (function: calls) — *FindWorkspaceRoot locates the workspace root containing docker-deployment*
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|GetLocalIPs]] (function: calls) — *GetLocalIPs returns a set of local IP addresses for this machine*
- [[watchdog-agent/watchdog-agent/src/utils/utils.go.md|IsLocal]] (function: calls) — *IsLocal checks if an IP belongs to the local machine*

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->
