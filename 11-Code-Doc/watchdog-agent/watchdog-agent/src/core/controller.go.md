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
Automatically generated mirror for `watchdog-agent/src/core/controller.go`.

> **Essential Process**:
> Core interface and telemetry data contract definitions for watchdog-agent. Defines service statuses, overall node health metrics, and control signatures.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/src/core/controller.go.md|ServiceStatus]] (struct: belongs_to) — *ServiceStatus represents the current status of a managed process*
- [[watchdog-agent/watchdog-agent/src/core/controller.go.md|WatchdogController]] (interface: belongs_to) — *WatchdogController defines status and control interfaces for watchdog-agent*
- [[watchdog-agent/watchdog-agent/src/core/controller.go.md|WatchdogStatusInfo]] (struct: belongs_to) — *WatchdogStatusInfo represents the overall watchdog telemetry*
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|rest_handler.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|controller.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|manager.go]] (imports)
<!-- SYNC:END -->
