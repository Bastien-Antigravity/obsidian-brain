---
microservice: distributed-config
type: note
status: active
tags:
- '#service/distributed-config'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `distributed-config/src/facade/config_facade_test.go`.

> **Essential Process**:
> Unit test suite verifying facade initialization, multi-profile loading, and local callback execution upon SetSingle mutations.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.DeleteKey]] (method: calls) — *DeleteKey removes a single key from a section.*
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.DeleteKeysWithOCC]] (method: calls) — *Returns ErrVersionConflict if expectedVersion does not match server version.*
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.DeleteKeys]] (method: calls) — *DeleteKeys removes specified section keys from live configuration and syncs to server.*
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.GetVersion]] (method: calls) — *GetVersion returns the last seen server configuration version.*
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.OnLiveConfUpdate]] (method: calls)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.SetSingle]] (method: calls) — *SetSingle is a helper for updating a single configuration value.*
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.SetWithOCC]] (method: calls) — *Returns ErrVersionConflict if expectedVersion does not match server version.*
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|Config.ShareConfigWithOCC]] (method: calls) — *ShareConfigWithOCC converts payload and updates configuration with optimistic concurrency control.*
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|NewConfig]] (function: calls)
- [[distributed-config/distributed-config/src/facade/config_facade.go.md|config_facade.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/distributed_config.go.md|distributed_config.go]] (imports)
- [[distributed-config/distributed-config/src/facade/config_facade_test.go.md|TestFacade_OCCAndDeletions]] (function: belongs_to)
- [[distributed-config/distributed-config/src/facade/config_facade_test.go.md|TestNewConfig]] (function: belongs_to)
<!-- SYNC:END -->
