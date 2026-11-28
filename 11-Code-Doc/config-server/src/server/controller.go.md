---
microservice: config-server
type: note
status: active
tags:
- '#service/config-server'
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
- [[config-server/src/core/controller.go.md|controller.go]] (imports)
- [[config-server/src/server/controller.go.md|Server.DeleteConfig]] (method: defines_method)
- [[config-server/src/server/controller.go.md|Server.GetConfig]] (method: defines_method)
- [[config-server/src/server/controller.go.md|Server.GetStatus]] (method: defines_method)
- [[config-server/src/server/controller.go.md|Server.GetStoreVersion]] (method: defines_method)
- [[config-server/src/server/controller.go.md|Server.ListConfig]] (method: defines_method)
- [[config-server/src/server/controller.go.md|Server.PersistConfig]] (method: defines_method)
- [[config-server/src/server/controller.go.md|Server.SetConfigWithOCC]] (method: defines_method)
- [[config-server/src/server/controller.go.md|Server.SetConfig]] (method: defines_method)
- [[config-server/src/server/server.go.md|Server.BroadcastConfig]] (method: calls)
- [[config-server/src/server/server.go.md|Server.BroadcastFullRefresh]] (method: calls)
- [[config-server/src/server/server.go.md|Server.GetActiveClients]] (method: calls)
- [[config-server/src/server/server.go.md|Server.GetClientNames]] (method: calls)
- [[config-server/src/server/server.go.md|Server.TriggerSave]] (method: calls)
- [[config-server/src/server/server.go.md|server.go]] (same_package)
- [[config-server/src/server/server_test.go.md|mockLogger.Debug]] (method: calls)
- [[config-server/src/server/server_test.go.md|mockLogger.Info]] (method: calls)
- [[config-server/src/server/server_test.go.md|server_test.go]] (same_package)
- [[config-server/src/store/persistence.go.md|persistence.go]] (imports)
- [[config-server/src/store/store.go.md|DeepCopy]] (function: calls) — *Helper to deep copy the map (used for COW updates)*
- [[config-server/src/store/store.go.md|Store.Get]] (method: calls) — *Callers MUST treat the returned map as immutable.*
- [[config-server/src/store/store.go.md|Store.UpdateAtomicWithOCC]] (method: calls) — *than the current store version, the version advances to explicitVersion;*
- [[config-server/src/store/store.go.md|Store.UpdateSection]] (method: calls)

### 🔌 Consumers (Inbound)
- [[config-server/cmd/config-server/main.go.md|main.go]] (imports)
- [[config-server/src/grpc_control/grpc_service.go.md|grpc_service.go]] (imports)
- [[config-server/src/server/controller.go.md|Server.DeleteConfig]] (method: belongs_to)
- [[config-server/src/server/controller.go.md|Server.GetConfig]] (method: belongs_to)
- [[config-server/src/server/controller.go.md|Server.GetStatus]] (method: belongs_to)
- [[config-server/src/server/controller.go.md|Server.GetStoreVersion]] (method: belongs_to)
- [[config-server/src/server/controller.go.md|Server.ListConfig]] (method: belongs_to)
- [[config-server/src/server/controller.go.md|Server.PersistConfig]] (method: belongs_to)
- [[config-server/src/server/controller.go.md|Server.SetConfigWithOCC]] (method: belongs_to)
- [[config-server/src/server/controller.go.md|Server.SetConfig]] (method: belongs_to)
- [[config-server/src/server/controller.go.md|Server]] (struct: defines_method) — *ESSENTIAL PROCESS:*
- [[config-server/src/server/server_test.go.md|server_test.go]] (calls)
- [[config-server/src/server/server_test.go.md|server_test.go]] (same_package)
<!-- SYNC:END -->
