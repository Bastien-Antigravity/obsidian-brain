---
source: config-server/src/core/request_handler_test.go
workspace: config-server
type: code-mirror
status: auto-generated
last_sync: 2026-09-17 06:23:59.674589
microservice: 08-Base-Scripts
tags:
- '#service/08-Base-Scripts'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: request_handler_test.go

## 📝 Description
Automatically generated mirror for `config-server/src/core/request_handler_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/config-server/src/core/request_handler.go.md|ProcessRequest]] (function: calls)
- [[config-server/config-server/src/core/request_handler.go.md|request_handler.go]] (same_package)
- [[config-server/config-server/src/store/persistence.go.md|persistence.go]] (imports)
- [[config-server/config-server/src/store/store.go.md|NewStore]] (function: calls)
- [[config-server/config-server/src/store/store.go.md|Store.Get]] (method: calls)
- [[config-server/config-server/src/store/store.go.md|Store.Replace]] (method: calls)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/src/core/request_handler_test.go.md|TestProcessRequest_GetSyncAndFullRefresh]] (function: belongs_to)
- [[config-server/config-server/src/core/request_handler_test.go.md|TestProcessRequest_MalformedProtobuf]] (function: belongs_to)
- [[config-server/config-server/src/core/request_handler_test.go.md|TestProcessRequest_PutSync_InvalidJSON]] (function: belongs_to)
- [[config-server/config-server/src/core/request_handler_test.go.md|TestProcessRequest_PutSync_Success]] (function: belongs_to)
- [[config-server/config-server/src/core/request_handler_test.go.md|TestProcessRequest_UnknownCommand]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
