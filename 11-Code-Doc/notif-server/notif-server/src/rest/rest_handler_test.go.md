---
source: notif-server/src/rest/rest_handler_test.go
workspace: notif-server
type: code-mirror
status: auto-generated
last_sync: 2026-11-10T13:21:52.746258
---

# Mirror: rest_handler_test.go

## 📝 Description
Automatically generated mirror for `notif-server/src/rest/rest_handler_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (imports)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|NewRESTHandler]] (function: calls) — *NewRESTHandler creates a new RESTHandler instance*
- [[notif-server/notif-server/src/rest/rest_handler.go.md|RESTHandler.Handler]] (method: calls) — *Handler returns the REST API handler with route registration and CORS wrapping.*
- [[notif-server/notif-server/src/rest/rest_handler.go.md|rest_handler.go]] (same_package)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.AddProvider]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.GetAlertingConfig]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.GetStatus]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.GetSupportedTypes]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.ListNotifiers]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.ReloadConfig]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.RemoveProvider]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.SendTestNotification]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.SetAlertingConfig]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.AddMetadata]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Close]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Critical]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Debug]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Error]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.GetLevel]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.GetMetadata]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.GetNotifQueue]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Info]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.LogWithCaller]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Log]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Logon]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Logout]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Report]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Schedule]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.SetCallerSkip]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.SetLevel]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.SetLocalNotifQueue]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.SetMetadata]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Stream]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Trade]] (method: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Warning]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/rest/contracts.go.md|contracts.go]] (calls)
- [[notif-server/notif-server/src/rest/contracts.go.md|contracts.go]] (same_package)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|rest_handler.go]] (calls)
- [[notif-server/notif-server/src/rest/rest_handler.go.md|rest_handler.go]] (same_package)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|TestNotifHandlerContractsEndpoint]] (function: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.AddProvider]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.GetAlertingConfig]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.GetStatus]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.GetSupportedTypes]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.ListNotifiers]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.ReloadConfig]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.RemoveProvider]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.SendTestNotification]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl.SetAlertingConfig]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl]] (struct: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifControl]] (struct: defines_method)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.AddMetadata]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Close]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Critical]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Debug]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Error]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.GetLevel]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.GetMetadata]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.GetNotifQueue]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Info]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.LogWithCaller]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Log]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Logon]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Logout]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Report]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Schedule]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.SetCallerSkip]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.SetLevel]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.SetLocalNotifQueue]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.SetMetadata]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Stream]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Trade]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger.Warning]] (method: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger]] (struct: belongs_to)
- [[notif-server/notif-server/src/rest/rest_handler_test.go.md|mockNotifLogger]] (struct: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
