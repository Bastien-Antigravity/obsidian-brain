---
source: config-server/src/rest/contracts.go
workspace: config-server
type: code-mirror
status: auto-generated
last_sync: 2026-11-10T13:21:50.574497
---

# Mirror: contracts.go

## 📝 Description
Automatically generated mirror for `config-server/src/rest/contracts.go`.

> **Essential Process**:
> Builds exhaustive, microservice-authored Exchange Contracts for config-server across HTTP/REST, gRPC Control, SafeSocket TCP (ConfigMsg Protobuf), and outbound Tele-Remote streaming.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/config-server/src/grpc_control/service.go.md|service.go]] (imports)
- [[config-server/config-server/src/rest/contracts.go.md|RESTHandler.handleContracts]] (method: defines_method)
- [[config-server/config-server/src/rest/rest_handler.go.md|RESTHandler.sendJSON]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler.go.md|rest_handler.go]] (same_package)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockControl.GetStatus]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|mockLogger.Error]] (method: calls)
- [[config-server/config-server/src/rest/rest_handler_test.go.md|rest_handler_test.go]] (same_package)
- [[config-server/config-server/src/store/store.go.md|Store.Get]] (method: calls) — *Callers MUST treat the returned map as immutable.*

### 🔌 Consumers (Inbound)
- [[config-server/config-server/cmd/config-server/main.go.md|main.go]] (calls)
- [[config-server/config-server/src/rest/contracts.go.md|BuildExchangeContracts]] (function: belongs_to) — *BuildExchangeContracts constructs the exhaustive contract catalog from live config-server sources.*
- [[config-server/config-server/src/rest/contracts.go.md|RESTHandler.handleContracts]] (method: belongs_to)
- [[config-server/config-server/src/rest/contracts.go.md|RESTHandler]] (struct: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
