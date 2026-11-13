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
Automatically generated mirror for `watchdog-agent/src/control/control_plane.go`.

> **Essential Process**:
> NATS control plane client and telemetry publisher for watchdog-agent. Connects asynchronously with exponential backoff, publishes periodic node heartbeats, and exposes lock-free Publish for real-time fleet incidents.

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
- [[watchdog-agent/watchdog-agent/src/control/control_plane.go.md|StartNATSControlPlane]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/control/control_plane.go.md|collectServicesStatus]] (function: belongs_to)
<!-- SYNC:END -->
