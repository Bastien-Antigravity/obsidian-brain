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
- [[watchdog-agent/src/control/control_plane.go.md|BusClient.Publish]] (method: defines_method) — *Publish sends a payload over NATS using the lock-free active connection pointer.*
- [[watchdog-agent/src/control/control_plane.go.md|BusClient.Start]] (method: defines_method) — *publishes periodic node heartbeats until ctx is canceled.*
- [[watchdog-agent/src/control/control_plane.go.md|BusClient.SubjectPrefix]] (method: defines_method) — *SubjectPrefix returns the resolved NATS subject prefix.*
- [[watchdog-agent/src/supervisor/supervisor.go.md|LogError]] (function: calls) — *LogError writes a formatted error message with watchdog prefix to stderr/logger*
- [[watchdog-agent/src/supervisor/supervisor.go.md|LogInfo]] (function: calls) — *LogInfo writes a formatted message with watchdog prefix to stdout/logger*
- [[watchdog-agent/src/supervisor/types.go.md|Service.ResolveAddr]] (method: calls) — *falling back to the service's baseline IP and Port.*
- [[watchdog-agent/src/supervisor/types.go.md|types.go]] (imports)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/main.go.md|main.go]] (imports)
- [[watchdog-agent/src/control/control_plane.go.md|BusClient.Publish]] (method: belongs_to) — *Publish sends a payload over NATS using the lock-free active connection pointer.*
- [[watchdog-agent/src/control/control_plane.go.md|BusClient.Start]] (method: belongs_to) — *publishes periodic node heartbeats until ctx is canceled.*
- [[watchdog-agent/src/control/control_plane.go.md|BusClient.SubjectPrefix]] (method: belongs_to) — *SubjectPrefix returns the resolved NATS subject prefix.*
- [[watchdog-agent/src/control/control_plane.go.md|BusClient]] (struct: belongs_to) — *BusClient manages the shared NATS connection for heartbeats and fleet incidents.*
- [[watchdog-agent/src/control/control_plane.go.md|BusClient]] (struct: defines_method) — *BusClient manages the shared NATS connection for heartbeats and fleet incidents.*
- [[watchdog-agent/src/control/control_plane.go.md|NewBusClient]] (function: belongs_to) — *NewBusClient resolves NATS configuration from validated AppConfig on cold startup.*
- [[watchdog-agent/src/control/control_plane.go.md|NodeStatus]] (struct: belongs_to)
- [[watchdog-agent/src/control/control_plane.go.md|ServiceStatus]] (struct: belongs_to)
- [[watchdog-agent/src/control/control_plane.go.md|collectServicesStatus]] (function: belongs_to)
<!-- SYNC:END -->
