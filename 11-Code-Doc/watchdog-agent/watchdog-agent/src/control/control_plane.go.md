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
Automatically generated mirror for `watchdog-agent/src/control/control_plane.go`.

> **Essential Process**:
> NATS control plane telemetry publisher for watchdog-agent. Publishes periodic node heartbeats, health statuses, and dynamic supervised process states over the ecosystem NATS messaging bus.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|LogError]] (function: calls) — *LogError writes a formatted error message with watchdog prefix to stderr/logger*
- [[watchdog-agent/watchdog-agent/src/supervisor/supervisor.go.md|LogInfo]] (function: calls) — *LogInfo writes a formatted message with watchdog prefix to stdout/logger*
- [[watchdog-agent/watchdog-agent/src/supervisor/types.go.md|types.go]] (imports)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/control/control_plane.go.md|NodeStatus]] (struct: belongs_to)
- [[watchdog-agent/watchdog-agent/src/control/control_plane.go.md|ServiceStatus]] (struct: belongs_to)
- [[watchdog-agent/watchdog-agent/src/control/control_plane.go.md|StartNATSControlPlane]] (function: belongs_to) — *StartNATSControlPlane connects to the NATS event bus and publishes node heartbeats*
- [[watchdog-agent/watchdog-agent/src/control/control_plane.go.md|collectServicesStatus]] (function: belongs_to)
<!-- SYNC:END -->
