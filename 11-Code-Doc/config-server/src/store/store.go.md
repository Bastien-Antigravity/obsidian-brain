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
Automatically generated mirror for `config-server/src/store/store.go`.

> **Essential Process**:
> Implements the high-concurrency, thread-safe in-memory configuration store using Copy-On-Write (COW) semantics protected by sync.RWMutex.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/src/store/persistence.go.md|PersistenceManager.Load]] (method: calls)
- [[config-server/src/store/persistence.go.md|persistence.go]] (same_package)
- [[config-server/src/store/store.go.md|Store.GetSection]] (method: defines_method) — *GetSection returns a copy of a specific section lock-free.*
- [[config-server/src/store/store.go.md|Store.GetVersion]] (method: defines_method) — *GetVersion returns the current monotonic configuration version lock-free.*
- [[config-server/src/store/store.go.md|Store.Get]] (method: defines_method) — *Callers MUST treat the returned map as immutable.*
- [[config-server/src/store/store.go.md|Store.Replace]] (method: defines_method) — *the matching monotonic version under a consistent lock.*
- [[config-server/src/store/store.go.md|Store.SetVersion]] (method: defines_method) — *SetVersion sets the monotonic version counter (e.g. during initial restore).*
- [[config-server/src/store/store.go.md|Store.UpdateAtomicWithOCC]] (method: defines_method) — *than the current store version, the version advances to explicitVersion;*
- [[config-server/src/store/store.go.md|Store.UpdateAtomic]] (method: defines_method)
- [[config-server/src/store/store.go.md|Store.UpdateSection]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[config-server/cmd/config-server/main.go.md|main.go]] (calls)
- [[config-server/src/core/request_handler.go.md|request_handler.go]] (calls)
- [[config-server/src/core/request_handler_test.go.md|request_handler_test.go]] (calls)
- [[config-server/src/rest/contracts.go.md|contracts.go]] (calls)
- [[config-server/src/rest/rest_handler.go.md|rest_handler.go]] (calls)
- [[config-server/src/rest/rest_handler_test.go.md|rest_handler_test.go]] (calls)
- [[config-server/src/server/controller.go.md|controller.go]] (calls)
- [[config-server/src/server/server.go.md|server.go]] (calls)
- [[config-server/src/server/server_test.go.md|server_test.go]] (calls)
- [[config-server/src/store/store.go.md|ConfigMap]] (struct: belongs_to) — *ConfigMap represents the configuration data structure (Section -> Key -> Value)*
- [[config-server/src/store/store.go.md|DeepCopy]] (function: belongs_to) — *Helper to deep copy the map (used for COW updates)*
- [[config-server/src/store/store.go.md|NewStore]] (function: belongs_to) — *NewStore initializes a new Store with an empty config.*
- [[config-server/src/store/store.go.md|Store.GetSection]] (method: belongs_to) — *GetSection returns a copy of a specific section lock-free.*
- [[config-server/src/store/store.go.md|Store.GetVersion]] (method: belongs_to) — *GetVersion returns the current monotonic configuration version lock-free.*
- [[config-server/src/store/store.go.md|Store.Get]] (method: belongs_to) — *Callers MUST treat the returned map as immutable.*
- [[config-server/src/store/store.go.md|Store.Replace]] (method: belongs_to) — *the matching monotonic version under a consistent lock.*
- [[config-server/src/store/store.go.md|Store.SetVersion]] (method: belongs_to) — *SetVersion sets the monotonic version counter (e.g. during initial restore).*
- [[config-server/src/store/store.go.md|Store.UpdateAtomicWithOCC]] (method: belongs_to) — *than the current store version, the version advances to explicitVersion;*
- [[config-server/src/store/store.go.md|Store.UpdateAtomic]] (method: belongs_to)
- [[config-server/src/store/store.go.md|Store.UpdateSection]] (method: belongs_to)
- [[config-server/src/store/store.go.md|Store]] (struct: belongs_to) — *100% lock-free reads while maintaining atomic, side-effect-free updates.*
- [[config-server/src/store/store.go.md|Store]] (struct: defines_method) — *100% lock-free reads while maintaining atomic, side-effect-free updates.*
- [[config-server/src/store/store_test.go.md|store_test.go]] (calls)
- [[config-server/src/store/store_test.go.md|store_test.go]] (same_package)
<!-- SYNC:END -->
