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
Automatically generated mirror for `distributed-config/src/network/sync_logic_test.go`.

> **Essential Process**:
> Regression and sync logic test suite verifying that broadcast synchronization deep-merges delta updates into LiveConfig without dropping untouched sections.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/src/core/config.go.md|Config.Get]] (method: calls) — *Returns an empty string if not found.*
- [[distributed-config/distributed-config/src/core/config.go.md|config.go]] (imports)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.HandleIncoming]] (method: calls)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|NewConfigHandler]] (function: calls)
- [[distributed-config/distributed-config/src/network/proto_handler.go.md|proto_handler.go]] (same_package)
- [[distributed-config/distributed-config/src/schemas/config.pb.go.md|config.pb.go]] (imports)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/network/sync_logic_test.go.md|TestMergeBugReproduction]] (function: belongs_to)
<!-- SYNC:END -->
