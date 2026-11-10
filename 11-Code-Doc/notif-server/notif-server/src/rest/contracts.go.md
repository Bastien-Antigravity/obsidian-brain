---
source: notif-server/src/rest/contracts.go
workspace: notif-server
type: code-mirror
status: auto-generated
last_sync: 2026-11-10T13:21:52.751706
---

# Mirror: contracts.go

## 📝 Description
Automatically generated mirror for `notif-server/src/rest/contracts.go`.

> **Essential Process**:
> Constructs exhaustive, microservice-authored Exchange Contracts for notif-server across HTTP/REST, gRPC (NotifService + NotifControlService), SafeSocket TCP with Cap'n Proto (NotifierMsg), and outbound Tele-Remote / Alerting providers.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (imports)
- [[notif-server/notif-server/src/grpc_control/service.go.md|service.go]] (imports)
- [[notif-server/notif-server/src/rest/contracts.go.md|RESTHandler.handleContracts]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.sendJSON]] (method: calls)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|rest_handler.go]] (same_package)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.GetStatus]] (method: calls)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.GetSupportedTypes]] (method: calls)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.ListNotifiers]] (method: calls)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Error]] (method: calls)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|rest_handler_test.go]] (same_package)
- [[notif-server/notif-server/src/schemas/capnp/notifier.go.md|notifier.go]] (imports)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service.pb.go.md|notif_service.pb.go]] (imports)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/cmd/notif-server/main.go.md|main.go]] (calls)
- [[notif-server/notif-server/src/rest/contracts.go.md|BuildExchangeContracts]] (function: belongs_to) — *BuildExchangeContracts constructs the exhaustive contract catalog from notif-server sources.*
- [[notif-server/notif-server/src/rest/contracts.go.md|RESTHandler.handleContracts]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/contracts.go.md|RESTHandler]] (struct: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
