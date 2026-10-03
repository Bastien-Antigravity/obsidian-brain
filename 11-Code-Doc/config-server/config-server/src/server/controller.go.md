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
Automatically generated mirror for `config-server/src/server/controller.go`.

> **Essential Process**:
> Implements the core.ConfigController interface on Server, providing atomic configuration accessors, mutators, dynamic listing, and health status reporting.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/config-server/src/core/controller.go.md|controller.go]] (imports)
- [[config-server/config-server/src/server/controller.go.md|Server.DeleteConfig]] (method: defines_method) — *DeleteConfig deletes a configuration key atomically and broadcasts the change.*
- [[config-server/config-server/src/server/controller.go.md|Server.GetConfig]] (method: defines_method) — *GetConfig returns a specific configuration value from the dynamic store.*
- [[config-server/config-server/src/server/controller.go.md|Server.GetStatus]] (method: defines_method) — *GetStatus returns the health status, active client counts, and client names.*
- [[config-server/config-server/src/server/controller.go.md|Server.ListConfig]] (method: defines_method) — *ListConfig returns the full current configuration state, merging static base configurations with dynamic overrides.*
- [[config-server/config-server/src/server/controller.go.md|Server.PersistConfig]] (method: defines_method) — *PersistConfig manually triggers a save of the configuration state.*
- [[config-server/config-server/src/server/controller.go.md|Server.SetConfig]] (method: defines_method) — *SetConfig updates a configuration value atomically and broadcasts the change.*
- [[config-server/config-server/src/server/server.go.md|Server.BroadcastConfig]] (method: calls) — *BroadcastConfig sends a full configuration update to all connected clients.*
- [[config-server/config-server/src/server/server.go.md|Server.GetActiveClients]] (method: calls) — *GetActiveClients returns the current number of connected clients.*
- [[config-server/config-server/src/server/server.go.md|Server.GetClientNames]] (method: calls) — *GetClientNames returns the names of all currently connected clients.*
- [[config-server/config-server/src/server/server.go.md|Server.TriggerSave]] (method: calls) — *TriggerSave marks the state as dirty to trigger background persistence.*
- [[config-server/config-server/src/server/server.go.md|server.go]] (same_package)
- [[config-server/config-server/src/server/server_test.go.md|mockLogger.Debug]] (method: calls)
- [[config-server/config-server/src/server/server_test.go.md|mockLogger.Info]] (method: calls)
- [[config-server/config-server/src/server/server_test.go.md|server_test.go]] (same_package)
- [[config-server/config-server/src/store/persistence.go.md|persistence.go]] (imports)
- [[config-server/config-server/src/store/store.go.md|DeepCopy]] (function: calls) — *Helper to deep copy the map (used for COW updates)*
- [[config-server/config-server/src/store/store.go.md|Store.Get]] (method: calls) — *Callers MUST treat the returned map as immutable.*
- [[config-server/config-server/src/store/store.go.md|Store.UpdateAtomic]] (method: calls) — *remains untouched (Atomicity/Rollback).*

### 🔌 Consumers (Inbound)
- [[config-server/config-server/cmd/config-server/main.go.md|main.go]] (imports)
- [[config-server/config-server/src/grpc_control/grpc_service.go.md|grpc_service.go]] (imports)
- [[config-server/config-server/src/server/controller.go.md|Server.DeleteConfig]] (method: belongs_to) — *DeleteConfig deletes a configuration key atomically and broadcasts the change.*
- [[config-server/config-server/src/server/controller.go.md|Server.GetConfig]] (method: belongs_to) — *GetConfig returns a specific configuration value from the dynamic store.*
- [[config-server/config-server/src/server/controller.go.md|Server.GetStatus]] (method: belongs_to) — *GetStatus returns the health status, active client counts, and client names.*
- [[config-server/config-server/src/server/controller.go.md|Server.ListConfig]] (method: belongs_to) — *ListConfig returns the full current configuration state, merging static base configurations with dynamic overrides.*
- [[config-server/config-server/src/server/controller.go.md|Server.PersistConfig]] (method: belongs_to) — *PersistConfig manually triggers a save of the configuration state.*
- [[config-server/config-server/src/server/controller.go.md|Server.SetConfig]] (method: belongs_to) — *SetConfig updates a configuration value atomically and broadcasts the change.*
- [[config-server/config-server/src/server/controller.go.md|Server]] (struct: defines_method) — *GetStatus returns the health status, active client counts, and client names.*
- [[config-server/config-server/src/server/controller.go.md|init]] (function: belongs_to)
- [[config-server/config-server/src/server/server_test.go.md|server_test.go]] (calls)
- [[config-server/config-server/src/server/server_test.go.md|server_test.go]] (same_package)
<!-- SYNC:END -->
