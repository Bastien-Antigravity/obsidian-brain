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
Automatically generated mirror for `notif-server/src/core/notifier.go`.

> **Essential Process**:
> Manages the core notification dispatch logic, worker pools, and asynchronous queuing. Ensures that slow external APIs do not block the ingestion layer.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.ConsumeRawMessages]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.GetActiveNotifiers]] (method: defines_method) — *GetActiveNotifiers returns information about all currently active notification senders.*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.InitDefaultProviders]] (method: defines_method) — *if no dynamic providers have been registered for them.*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.LoadNotifSender]] (method: defines_method) — *but essentially Reload is the new standard.*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.Notify]] (method: defines_method) — *Notify sends a structured notification message.*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.RegisterSender]] (method: defines_method) — *RegisterSender registers a custom or programmatic notification sender with its dedicated worker pool.*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.Reload]] (method: defines_method) — *senders that have changed or were added/removed.*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.SendNotification]] (method: defines_method) — *SendNotification implements proto_msg.NotifServiceServer (gRPC)*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.SendRaw]] (method: defines_method) — *SendRaw sends a raw byte message (serialized).*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.Stop]] (method: defines_method) — *Stop shuts down the notifier and all active workers.*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.processMessage]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.startSenderWorker]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.startSender]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.stopSender]] (method: defines_method)
- [[notif-server/notif-server/src/core/notifier_test.go.md|mockSender.GetTag]] (method: calls)
- [[notif-server/notif-server/src/core/notifier_test.go.md|mockSender.SendMessage]] (method: calls)
- [[notif-server/notif-server/src/core/notifier_test.go.md|notifier_test.go]] (same_package)
- [[notif-server/notif-server/src/core/request_handler.go.md|DeserializeNotifMsg]] (function: calls) — *This helper is exposed for servers or other components using this library.*
- [[notif-server/notif-server/src/core/request_handler.go.md|request_handler.go]] (same_package)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.AddMetadata]] (method: calls)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Debug]] (method: calls)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Error]] (method: calls)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Info]] (method: calls)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Warning]] (method: calls)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|test_logger_test.go]] (same_package)
- [[notif-server/notif-server/src/interfaces/notifier.go.md|notifier.go]] (imports)
- [[notif-server/notif-server/src/notifiers/config.go.md|config.go]] (imports)
- [[notif-server/notif-server/src/notifiers/discord.go.md|NewDiscordSender]] (function: calls) — *unconfigured and returns (nil, nil) without failing.*
- [[notif-server/notif-server/src/notifiers/gmail.go.md|NewGmailSender]] (function: calls)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|NewMatrixSender]] (function: calls) — *unconfigured and returns (nil, nil) without failing.*
- [[notif-server/notif-server/src/notifiers/telegram.go.md|NewTelegramSender]] (function: calls) — *is considered unconfigured and returns (nil, nil) without failing.*
- [[notif-server/notif-server/src/schemas/protobuf/notif_service.pb.go.md|NotifRequest.String]] (method: calls)
- [[notif-server/notif-server/src/schemas/protobuf/notif_service.pb.go.md|notif_service.pb.go]] (imports)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/cmd/notif-server/main.go.md|main.go]] (calls)
- [[notif-server/notif-server/cmd/test/integration_test.go.md|integration_test.go]] (calls)
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (calls)
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (same_package)
- [[notif-server/notif-server/src/core/controller_test.go.md|controller_test.go]] (calls)
- [[notif-server/notif-server/src/core/controller_test.go.md|controller_test.go]] (same_package)
- [[notif-server/notif-server/src/core/notifier.go.md|NewNotifier]] (function: belongs_to) — *NewNotifier creates a new instance of the notification service.*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.ConsumeRawMessages]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.GetActiveNotifiers]] (method: belongs_to) — *GetActiveNotifiers returns information about all currently active notification senders.*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.InitDefaultProviders]] (method: belongs_to) — *if no dynamic providers have been registered for them.*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.LoadNotifSender]] (method: belongs_to) — *but essentially Reload is the new standard.*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.Notify]] (method: belongs_to) — *Notify sends a structured notification message.*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.RegisterSender]] (method: belongs_to) — *RegisterSender registers a custom or programmatic notification sender with its dedicated worker pool.*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.Reload]] (method: belongs_to) — *senders that have changed or were added/removed.*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.SendNotification]] (method: belongs_to) — *SendNotification implements proto_msg.NotifServiceServer (gRPC)*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.SendRaw]] (method: belongs_to) — *SendRaw sends a raw byte message (serialized).*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.Stop]] (method: belongs_to) — *Stop shuts down the notifier and all active workers.*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.processMessage]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.startSenderWorker]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.startSender]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.stopSender]] (method: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|NotifierStatus]] (struct: belongs_to) — *NotifierStatus contains basic info about an active provider*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier]] (struct: belongs_to)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier]] (struct: defines_method)
- [[notif-server/notif-server/src/core/notifier_test.go.md|notifier_test.go]] (calls)
- [[notif-server/notif-server/src/core/notifier_test.go.md|notifier_test.go]] (same_package)
- [[notif-server/notif-server/src/core/worker_pool_test.go.md|worker_pool_test.go]] (calls)
- [[notif-server/notif-server/src/core/worker_pool_test.go.md|worker_pool_test.go]] (same_package)
- [[notif-server/notif-server/src/server/server_test.go.md|server_test.go]] (calls)
- [[notif-server/notif-server/src/server/timeout_test.go.md|timeout_test.go]] (calls)
<!-- SYNC:END -->
