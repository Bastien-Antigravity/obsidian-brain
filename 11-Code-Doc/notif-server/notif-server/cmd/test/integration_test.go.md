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
Automatically generated mirror for `notif-server/cmd/test/integration_test.go`.

> **Essential Process**:
> Full End-to-End integration test for the notification ecosystem. Verifies the complete flow from TCP ingestion to platform delivery.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.AddMetadata]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Close]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Critical]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Debug]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Error]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.GetLevel]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Info]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.LogWithCaller]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Log]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Logon]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Logout]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Report]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Schedule]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.SetCallerSkip]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.SetLevel]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Stream]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Trade]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Warning]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockSender.GetLogLevel]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockSender.GetTag]] (method: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockSender.SendMessage]] (method: defines_method)
- [[notif-server/notif-server/src/core/controller.go.md|NewController]] (function: calls) — *NewController creates a new Controller instance.*
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (imports)
- [[notif-server/notif-server/src/core/notifier.go.md|NewNotifier]] (function: calls) — *NewNotifier creates a new instance of the notification service.*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.RegisterSender]] (method: calls) — *RegisterSender registers a custom or programmatic notification sender with its dedicated worker pool.*
- [[notif-server/notif-server/src/core/request_handler.go.md|NewNotifHandler]] (function: calls)
- [[notif-server/notif-server/src/core/request_handler.go.md|NotifNcapHandler.NotifNcapSerialize]] (method: calls)
- [[notif-server/notif-server/src/server/server.go.md|NewServer]] (function: calls) — *NewServer creates a new Notification Server.*
- [[notif-server/notif-server/src/server/server.go.md|Server.Start]] (method: calls) — *Start listens for incoming TCP and gRPC connections.*
- [[notif-server/notif-server/src/server/server.go.md|Server.Stop]] (method: calls) — *Stop shuts down the server.*
- [[notif-server/notif-server/src/server/server.go.md|server.go]] (imports)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|TestE2EFlow]] (function: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.AddMetadata]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Close]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Critical]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Debug]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Error]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.GetLevel]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Info]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.LogWithCaller]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Log]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Logon]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Logout]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Report]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Schedule]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.SetCallerSkip]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.SetLevel]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Stream]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Trade]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger.Warning]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger]] (struct: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockLogger]] (struct: defines_method)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockSender.GetLogLevel]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockSender.GetTag]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockSender.SendMessage]] (method: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockSender]] (struct: belongs_to)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|mockSender]] (struct: defines_method)
<!-- SYNC:END -->
