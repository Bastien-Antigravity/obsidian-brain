---
microservice: 08-Squad-Agent
type: note
status: active
tags:
- '#service/08-Squad-Agent'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `notif-server/src/core/notifier.go`.

> **Essential Process**:
> Manages the core notification dispatch logic, worker queues, and asynchronous delivery. Ensures that slow external APIs do not block the ingestion layer.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/src/core/controller.go.md|cloneConfig]] (function: calls)
- [[notif-server/src/core/controller.go.md|controller.go]] (same_package)
- [[notif-server/src/core/notifier.go.md|Notifier.GetActiveNotifiers]] (method: defines_method) — *GetActiveNotifiers returns dynamic health and telemetry about all active notification senders.*
- [[notif-server/src/core/notifier.go.md|Notifier.GetDefaultSender]] (method: defines_method) — *GetDefaultSender returns the primary/default notification sender.*
- [[notif-server/src/core/notifier.go.md|Notifier.GetDefaultTag]] (method: defines_method) — *GetDefaultTag returns the tag of the primary/default notification sender.*
- [[notif-server/src/core/notifier.go.md|Notifier.GetDroppedIngestionCount]] (method: defines_method) — *GetDroppedIngestionCount returns the total number of notifications dropped because NotifChan was full.*
- [[notif-server/src/core/notifier.go.md|Notifier.GetIngestionQueueDepth]] (method: defines_method) — *GetIngestionQueueDepth returns the current number of pending notifications in NotifChan.*
- [[notif-server/src/core/notifier.go.md|Notifier.InitDefaultProviders]] (method: defines_method) — *if no dynamic providers have been registered for them.*
- [[notif-server/src/core/notifier.go.md|Notifier.LoadNotifSender]] (method: defines_method) — *LoadNotifSender is a wrapper around Reload for backward compatibility.*
- [[notif-server/src/core/notifier.go.md|Notifier.Notify]] (method: defines_method) — *Notify sends a structured notification message.*
- [[notif-server/src/core/notifier.go.md|Notifier.RegisterSender]] (method: defines_method) — *RegisterSender registers a custom or programmatic notification sender with its dedicated worker.*
- [[notif-server/src/core/notifier.go.md|Notifier.Reload]] (method: defines_method) — *senders that have changed or were added/removed.*
- [[notif-server/src/core/notifier.go.md|Notifier.SendNotification]] (method: defines_method) — *SendNotification implements proto_msg.NotifServiceServer (gRPC)*
- [[notif-server/src/core/notifier.go.md|Notifier.SendRaw]] (method: defines_method) — *SendRaw deserializes a binary Cap'n Proto notification frame and queues it.*
- [[notif-server/src/core/notifier.go.md|Notifier.Stop]] (method: defines_method) — *It is fully idempotent and safe to call multiple times.*
- [[notif-server/src/core/notifier.go.md|Notifier.addLevelTagLocked]] (method: defines_method)
- [[notif-server/src/core/notifier.go.md|Notifier.dispatchMessage]] (method: defines_method)
- [[notif-server/src/core/notifier.go.md|Notifier.processMessage]] (method: defines_method)
- [[notif-server/src/core/notifier.go.md|Notifier.startSenderLocked]] (method: defines_method)
- [[notif-server/src/core/notifier.go.md|Notifier.startSenderWorkerLocked]] (method: defines_method)
- [[notif-server/src/core/notifier.go.md|Notifier.startSenderWorker]] (method: defines_method)
- [[notif-server/src/core/notifier.go.md|Notifier.stopSenderLocked]] (method: defines_method)
- [[notif-server/src/core/notifier.go.md|senderMetrics.recordDrop]] (method: defines_method)
- [[notif-server/src/core/notifier.go.md|senderMetrics.recordFailure]] (method: defines_method)
- [[notif-server/src/core/notifier.go.md|senderMetrics.recordSuccess]] (method: defines_method)
- [[notif-server/src/core/notifier.go.md|senderMetrics.snapshot]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|mockSender.GetLogLevel]] (method: calls)
- [[notif-server/src/core/notifier_test.go.md|mockSender.GetTag]] (method: calls)
- [[notif-server/src/core/notifier_test.go.md|mockSender.SendMessage]] (method: calls)
- [[notif-server/src/core/notifier_test.go.md|notifier_test.go]] (same_package)
- [[notif-server/src/core/request_handler.go.md|DeserializeNotifMsg]] (function: calls) — *This helper is exposed for servers or other components using this library.*
- [[notif-server/src/core/request_handler.go.md|request_handler.go]] (same_package)
- [[notif-server/src/core/test_logger_test.go.md|testNotifierLogger.AddMetadata]] (method: calls)
- [[notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Debug]] (method: calls)
- [[notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Error]] (method: calls)
- [[notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Info]] (method: calls)
- [[notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Warning]] (method: calls)
- [[notif-server/src/core/test_logger_test.go.md|test_logger_test.go]] (same_package)
- [[notif-server/src/interfaces/notifier.go.md|notifier.go]] (imports)
- [[notif-server/src/notifiers/config.go.md|config.go]] (imports)
- [[notif-server/src/notifiers/discord.go.md|NewDiscordSender]] (function: calls) — *or (nil, error) if decryption fails.*
- [[notif-server/src/notifiers/gmail.go.md|NewGmailSender]] (function: calls)
- [[notif-server/src/notifiers/matrix.go.md|NewMatrixSender]] (function: calls) — *or (nil, error) if decryption fails.*
- [[notif-server/src/notifiers/telegram.go.md|NewTelegramSender]] (function: calls) — *or (nil, error) if decryption fails.*
- [[notif-server/src/schemas/protobuf/notif_service.pb.go.md|NotifRequest.String]] (method: calls)
- [[notif-server/src/schemas/protobuf/notif_service.pb.go.md|notif_service.pb.go]] (imports)

### 🔌 Consumers (Inbound)
- [[notif-server/cmd/notif-server/main.go.md|main.go]] (calls)
- [[notif-server/cmd/test/integration_test.go.md|integration_test.go]] (calls)
- [[notif-server/src/core/controller.go.md|controller.go]] (calls)
- [[notif-server/src/core/controller.go.md|controller.go]] (same_package)
- [[notif-server/src/core/controller_test.go.md|controller_test.go]] (calls)
- [[notif-server/src/core/controller_test.go.md|controller_test.go]] (same_package)
- [[notif-server/src/core/notifier.go.md|NewNotifier]] (function: belongs_to) — *NewNotifier creates a new instance of the notification service.*
- [[notif-server/src/core/notifier.go.md|Notifier.GetActiveNotifiers]] (method: belongs_to) — *GetActiveNotifiers returns dynamic health and telemetry about all active notification senders.*
- [[notif-server/src/core/notifier.go.md|Notifier.GetDefaultSender]] (method: belongs_to) — *GetDefaultSender returns the primary/default notification sender.*
- [[notif-server/src/core/notifier.go.md|Notifier.GetDefaultTag]] (method: belongs_to) — *GetDefaultTag returns the tag of the primary/default notification sender.*
- [[notif-server/src/core/notifier.go.md|Notifier.GetDroppedIngestionCount]] (method: belongs_to) — *GetDroppedIngestionCount returns the total number of notifications dropped because NotifChan was full.*
- [[notif-server/src/core/notifier.go.md|Notifier.GetIngestionQueueDepth]] (method: belongs_to) — *GetIngestionQueueDepth returns the current number of pending notifications in NotifChan.*
- [[notif-server/src/core/notifier.go.md|Notifier.InitDefaultProviders]] (method: belongs_to) — *if no dynamic providers have been registered for them.*
- [[notif-server/src/core/notifier.go.md|Notifier.LoadNotifSender]] (method: belongs_to) — *LoadNotifSender is a wrapper around Reload for backward compatibility.*
- [[notif-server/src/core/notifier.go.md|Notifier.Notify]] (method: belongs_to) — *Notify sends a structured notification message.*
- [[notif-server/src/core/notifier.go.md|Notifier.RegisterSender]] (method: belongs_to) — *RegisterSender registers a custom or programmatic notification sender with its dedicated worker.*
- [[notif-server/src/core/notifier.go.md|Notifier.Reload]] (method: belongs_to) — *senders that have changed or were added/removed.*
- [[notif-server/src/core/notifier.go.md|Notifier.SendNotification]] (method: belongs_to) — *SendNotification implements proto_msg.NotifServiceServer (gRPC)*
- [[notif-server/src/core/notifier.go.md|Notifier.SendRaw]] (method: belongs_to) — *SendRaw deserializes a binary Cap'n Proto notification frame and queues it.*
- [[notif-server/src/core/notifier.go.md|Notifier.Stop]] (method: belongs_to) — *It is fully idempotent and safe to call multiple times.*
- [[notif-server/src/core/notifier.go.md|Notifier.addLevelTagLocked]] (method: belongs_to)
- [[notif-server/src/core/notifier.go.md|Notifier.dispatchMessage]] (method: belongs_to)
- [[notif-server/src/core/notifier.go.md|Notifier.processMessage]] (method: belongs_to)
- [[notif-server/src/core/notifier.go.md|Notifier.startSenderLocked]] (method: belongs_to)
- [[notif-server/src/core/notifier.go.md|Notifier.startSenderWorkerLocked]] (method: belongs_to)
- [[notif-server/src/core/notifier.go.md|Notifier.startSenderWorker]] (method: belongs_to)
- [[notif-server/src/core/notifier.go.md|Notifier.stopSenderLocked]] (method: belongs_to)
- [[notif-server/src/core/notifier.go.md|NotifierStatus]] (struct: belongs_to) — *NotifierStatus contains health and telemetry info about an active provider.*
- [[notif-server/src/core/notifier.go.md|Notifier]] (struct: belongs_to) — *Notifier is the concrete implementation of the notification service.*
- [[notif-server/src/core/notifier.go.md|Notifier]] (struct: defines_method) — *Notifier is the concrete implementation of the notification service.*
- [[notif-server/src/core/notifier.go.md|isNilSender]] (function: belongs_to)
- [[notif-server/src/core/notifier.go.md|senderMetrics.recordDrop]] (method: belongs_to)
- [[notif-server/src/core/notifier.go.md|senderMetrics.recordFailure]] (method: belongs_to)
- [[notif-server/src/core/notifier.go.md|senderMetrics.recordSuccess]] (method: belongs_to)
- [[notif-server/src/core/notifier.go.md|senderMetrics.snapshot]] (method: belongs_to)
- [[notif-server/src/core/notifier.go.md|senderMetrics]] (struct: belongs_to) — *senderMetrics tracks delivery health and backpressure telemetry for a single provider.*
- [[notif-server/src/core/notifier.go.md|senderMetrics]] (struct: defines_method) — *senderMetrics tracks delivery health and backpressure telemetry for a single provider.*
- [[notif-server/src/core/notifier_test.go.md|notifier_test.go]] (calls)
- [[notif-server/src/core/notifier_test.go.md|notifier_test.go]] (same_package)
- [[notif-server/src/core/worker_pool_test.go.md|worker_pool_test.go]] (calls)
- [[notif-server/src/core/worker_pool_test.go.md|worker_pool_test.go]] (same_package)
- [[notif-server/src/server/connection.go.md|connection.go]] (calls)
- [[notif-server/src/server/server_test.go.md|server_test.go]] (calls)
<!-- SYNC:END -->
