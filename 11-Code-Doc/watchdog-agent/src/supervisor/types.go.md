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
Automatically generated mirror for `watchdog-agent/src/supervisor/types.go`.

> **Essential Process**:
> Core domain types, shared supervisor state, and ANSI terminal color definitions for watchdog-agent service orchestration.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/src/supervisor/registry.go.md|registry.go]] (same_package)
- [[watchdog-agent/src/supervisor/registry.go.md|resolveServiceAddr]] (function: calls)
- [[watchdog-agent/src/supervisor/types.go.md|Service.ResolveAddr]] (method: defines_method) — *falling back to the service's baseline IP and Port.*

### 🔌 Consumers (Inbound)
- [[watchdog-agent/main.go.md|main.go]] (imports)
- [[watchdog-agent/src/config/heal.go.md|heal.go]] (imports)
- [[watchdog-agent/src/control/control_plane.go.md|control_plane.go]] (calls)
- [[watchdog-agent/src/control/control_plane.go.md|control_plane.go]] (imports)
- [[watchdog-agent/src/rest/rest_handler.go.md|rest_handler.go]] (imports)
- [[watchdog-agent/src/server/controller.go.md|controller.go]] (imports)
- [[watchdog-agent/src/server/controller_test.go.md|controller_test.go]] (imports)
- [[watchdog-agent/src/supervisor/registry.go.md|registry.go]] (calls)
- [[watchdog-agent/src/supervisor/registry.go.md|registry.go]] (same_package)
- [[watchdog-agent/src/supervisor/supervisor.go.md|supervisor.go]] (calls)
- [[watchdog-agent/src/supervisor/supervisor.go.md|supervisor.go]] (same_package)
- [[watchdog-agent/src/supervisor/types.go.md|ColorConfigServer]] (constant: belongs_to)
- [[watchdog-agent/src/supervisor/types.go.md|ColorLogServer]] (constant: belongs_to)
- [[watchdog-agent/src/supervisor/types.go.md|ColorNotifServer]] (constant: belongs_to)
- [[watchdog-agent/src/supervisor/types.go.md|ColorRagDashboard]] (constant: belongs_to)
- [[watchdog-agent/src/supervisor/types.go.md|ColorRagEngine]] (constant: belongs_to)
- [[watchdog-agent/src/supervisor/types.go.md|ColorRed]] (constant: belongs_to)
- [[watchdog-agent/src/supervisor/types.go.md|ColorReset]] (constant: belongs_to)
- [[watchdog-agent/src/supervisor/types.go.md|ColorSquadAgent]] (constant: belongs_to)
- [[watchdog-agent/src/supervisor/types.go.md|ColorTeleRemote]] (constant: belongs_to)
- [[watchdog-agent/src/supervisor/types.go.md|ColorWatchdog]] (constant: belongs_to)
- [[watchdog-agent/src/supervisor/types.go.md|ColorWebInterface]] (constant: belongs_to)
- [[watchdog-agent/src/supervisor/types.go.md|Service.ResolveAddr]] (method: belongs_to) — *falling back to the service's baseline IP and Port.*
- [[watchdog-agent/src/supervisor/types.go.md|Service]] (struct: belongs_to) — *Service represents a managed service configurations*
- [[watchdog-agent/src/supervisor/types.go.md|Service]] (struct: defines_method) — *Service represents a managed service configurations*
- [[watchdog-agent/src/telegram/manager.go.md|manager.go]] (imports)
<!-- SYNC:END -->
