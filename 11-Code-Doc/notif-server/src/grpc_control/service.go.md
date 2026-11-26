---
microservice: notif-server
type: note
status: active
tags:
- '#service/notif-server'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `notif-server/src/grpc_control/service.go`.

> **Essential Process**:
> Provides gRPC management control service for dynamic notification provider configuration.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/src/core/controller.go.md|controller.go]] (imports)
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl.AddProvider]] (method: defines_method) — *AddProvider initializes a new notification provider*
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl.GetAlertingConfig]] (method: defines_method) — *Uses a deny-by-default allowlist (sanitizer.IsPublicField): anything not explicitly public is masked.*
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl.GetStatus]] (method: defines_method) — *GetStatus returns server health and metadata*
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl.GetSupportedTypes]] (method: defines_method) — *GetSupportedTypes returns the list of available notification drivers*
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl.ListNotifiers]] (method: defines_method) — *ListNotifiers returns the list of configured notifiers*
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl.ReloadConfig]] (method: defines_method) — *ReloadConfig triggers a manual reload of the configuration*
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl.RemoveProvider]] (method: defines_method) — *RemoveProvider deletes a notification provider*
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl.SendTestNotification]] (method: defines_method) — *SendTestNotification triggers a test notification through the engine*
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl.SetAlertingConfig]] (method: defines_method) — *SetAlertingConfig updates a specific setting for a notification platform*
- [[notif-server/src/sanitizer/sanitizer.go.md|IsPublicField]] (function: calls) — *Uses a deny-by-default allowlist: any unknown field, ENC(...) value, or embedded secret URL returns false.*
- [[notif-server/src/sanitizer/sanitizer.go.md|sanitizer.go]] (imports)

### 🔌 Consumers (Inbound)
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl.AddProvider]] (method: belongs_to) — *AddProvider initializes a new notification provider*
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl.GetAlertingConfig]] (method: belongs_to) — *Uses a deny-by-default allowlist (sanitizer.IsPublicField): anything not explicitly public is masked.*
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl.GetStatus]] (method: belongs_to) — *GetStatus returns server health and metadata*
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl.GetSupportedTypes]] (method: belongs_to) — *GetSupportedTypes returns the list of available notification drivers*
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl.ListNotifiers]] (method: belongs_to) — *ListNotifiers returns the list of configured notifiers*
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl.ReloadConfig]] (method: belongs_to) — *ReloadConfig triggers a manual reload of the configuration*
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl.RemoveProvider]] (method: belongs_to) — *RemoveProvider deletes a notification provider*
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl.SendTestNotification]] (method: belongs_to) — *SendTestNotification triggers a test notification through the engine*
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl.SetAlertingConfig]] (method: belongs_to) — *SetAlertingConfig updates a specific setting for a notification platform*
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl]] (struct: belongs_to)
- [[notif-server/src/grpc_control/service.go.md|ControlServiceImpl]] (struct: defines_method)
- [[notif-server/src/grpc_control/service.go.md|NewControlService]] (function: belongs_to) — *NewControlService creates a new ControlServiceImpl instance*
- [[notif-server/src/rest/contracts.go.md|contracts.go]] (imports)
- [[notif-server/src/rest/rest_handler.go.md|rest_handler.go]] (calls)
- [[notif-server/src/rest/rest_handler.go.md|rest_handler.go]] (imports)
- [[notif-server/src/server/server.go.md|server.go]] (calls)
- [[notif-server/src/server/server.go.md|server.go]] (imports)
<!-- SYNC:END -->
