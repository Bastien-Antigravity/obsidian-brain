---
source: config-server/src/grpc_control/service_test.go
workspace: config-server
type: code-mirror
status: auto-generated
last_sync: 2026-09-17T06:23:59.699181
---

# Mirror: service_test.go

## 📝 Description
Automatically generated mirror for `config-server/src/grpc_control/service_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/config-server/src/core/controller.go.md|controller.go]] (imports)
- [[config-server/config-server/src/grpc_control/service.go.md|NewControlService]] (function: calls)
- [[config-server/config-server/src/grpc_control/service.go.md|service.go]] (same_package)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockConfigController.DeleteConfig]] (method: defines_method)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockConfigController.GetConfig]] (method: defines_method)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockConfigController.GetStatus]] (method: defines_method)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockConfigController.ListConfig]] (method: defines_method)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockConfigController.PersistConfig]] (method: defines_method)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockConfigController.ReloadConfig]] (method: defines_method)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockConfigController.SetConfig]] (method: defines_method)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockLogger.Critical]] (method: defines_method)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockLogger.Debug]] (method: defines_method)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockLogger.Error]] (method: defines_method)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockLogger.Info]] (method: defines_method)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockLogger.Warning]] (method: defines_method)
- [[config-server/config-server/src/store/persistence.go.md|persistence.go]] (imports)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/src/grpc_control/config_server_grpc.pb.go.md|config_server_grpc.pb.go]] (calls)
- [[config-server/config-server/src/grpc_control/config_server_grpc.pb.go.md|config_server_grpc.pb.go]] (same_package)
- [[config-server/config-server/src/grpc_control/grpc_service.go.md|grpc_service.go]] (calls)
- [[config-server/config-server/src/grpc_control/grpc_service.go.md|grpc_service.go]] (same_package)
- [[config-server/config-server/src/grpc_control/service.go.md|service.go]] (calls)
- [[config-server/config-server/src/grpc_control/service.go.md|service.go]] (same_package)
- [[config-server/config-server/src/grpc_control/service_test.go.md|TestControlServiceImpl_GetConfig]] (function: belongs_to)
- [[config-server/config-server/src/grpc_control/service_test.go.md|TestControlServiceImpl_GetStatus]] (function: belongs_to)
- [[config-server/config-server/src/grpc_control/service_test.go.md|TestControlServiceImpl_ListConfig]] (function: belongs_to)
- [[config-server/config-server/src/grpc_control/service_test.go.md|TestControlServiceImpl_ReloadAndPersist]] (function: belongs_to)
- [[config-server/config-server/src/grpc_control/service_test.go.md|TestControlServiceImpl_SetConfig]] (function: belongs_to)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockConfigController.DeleteConfig]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockConfigController.GetConfig]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockConfigController.GetStatus]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockConfigController.ListConfig]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockConfigController.PersistConfig]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockConfigController.ReloadConfig]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockConfigController.SetConfig]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockConfigController]] (struct: belongs_to)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockConfigController]] (struct: defines_method)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockLogger.Critical]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockLogger.Debug]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockLogger.Error]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockLogger.Info]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockLogger.Warning]] (method: belongs_to)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockLogger]] (struct: belongs_to)
- [[config-server/config-server/src/grpc_control/service_test.go.md|mockLogger]] (struct: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
