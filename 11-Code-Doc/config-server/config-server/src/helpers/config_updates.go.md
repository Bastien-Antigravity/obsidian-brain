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
Automatically generated mirror for `config-server/src/helpers/config_updates.go`.

> **Essential Process**:
> Performs deep merge updates between current configuration map state and incoming delta key-value updates.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/config-server/src/store/persistence.go.md|persistence.go]] (imports)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/src/core/request_handler.go.md|request_handler.go]] (calls)
- [[config-server/config-server/src/helpers/config_updates.go.md|ApplyUpdates]] (function: belongs_to) — *It also supports key deletions via the "__DELETED__" sentinel value.*
- [[config-server/config-server/src/helpers/config_updates_test.go.md|config_updates_test.go]] (calls)
- [[config-server/config-server/src/helpers/config_updates_test.go.md|config_updates_test.go]] (same_package)
<!-- SYNC:END -->
