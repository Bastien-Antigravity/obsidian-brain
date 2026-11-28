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
Automatically generated mirror for `config-server/src/core/request_handler.go`.

> **Essential Process**:
> Decodes incoming Protobuf ConfigMsg frames, executes the corresponding configuration command against Store, and returns response frames.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/src/helpers/config_updates.go.md|ApplyUpdates]] (function: calls) — *It also supports key deletions via the "__DELETED__" sentinel value.*
- [[config-server/src/helpers/config_updates_test.go.md|config_updates_test.go]] (imports)
- [[config-server/src/store/persistence.go.md|persistence.go]] (imports)
- [[config-server/src/store/store.go.md|Store.Get]] (method: calls) — *Callers MUST treat the returned map as immutable.*
- [[config-server/src/store/store.go.md|Store.UpdateAtomicWithOCC]] (method: calls) — *than the current store version, the version advances to explicitVersion;*
- [[config-server/src/store/store.go.md|Store.UpdateAtomic]] (method: calls)

### 🔌 Consumers (Inbound)
- [[config-server/src/core/request_handler.go.md|ProcessRequest]] (function: belongs_to) — *It delegates to ProcessRequestWithVersion for atomic version-stamped execution.*
- [[config-server/src/core/request_handler_test.go.md|request_handler_test.go]] (calls)
- [[config-server/src/core/request_handler_test.go.md|request_handler_test.go]] (same_package)
- [[config-server/src/server/connection.go.md|connection.go]] (calls)
<!-- SYNC:END -->
