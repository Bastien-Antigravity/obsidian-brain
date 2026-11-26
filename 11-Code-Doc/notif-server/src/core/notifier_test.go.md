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
Automatically generated mirror for `notif-server/src/core/notifier_test.go`.

> **Essential Process**:
> Unit tests for the Notifier core logic. Verifies asynchronous message flow, worker pool dispatch, and queue capacity handling.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/src/core/controller.go.md|Controller.GetStatus]] (method: calls) — *GetStatus returns server health and real-time delivery/backpressure telemetry.*
- [[notif-server/src/core/controller.go.md|Controller.SetAlertingConfig]] (method: calls) — *SetAlertingConfig updates a specific setting for a notification provider.*
- [[notif-server/src/core/controller.go.md|NewController]] (function: calls) — *NewController creates a new Controller instance.*
- [[notif-server/src/core/controller.go.md|controller.go]] (same_package)
- [[notif-server/src/core/notifier.go.md|NewNotifier]] (function: calls) — *NewNotifier creates a new instance of the notification service.*
- [[notif-server/src/core/notifier.go.md|Notifier.GetActiveNotifiers]] (method: calls) — *GetActiveNotifiers returns dynamic health and telemetry about all active notification senders.*
- [[notif-server/src/core/notifier.go.md|Notifier.GetDroppedIngestionCount]] (method: calls) — *GetDroppedIngestionCount returns the total number of notifications dropped because NotifChan was full.*
- [[notif-server/src/core/notifier.go.md|Notifier.InitDefaultProviders]] (method: calls) — *if no dynamic providers have been registered for them.*
- [[notif-server/src/core/notifier.go.md|Notifier.Notify]] (method: calls) — *Notify sends a structured notification message.*
- [[notif-server/src/core/notifier.go.md|Notifier.RegisterSender]] (method: calls) — *RegisterSender registers a custom or programmatic notification sender with its dedicated worker.*
- [[notif-server/src/core/notifier.go.md|Notifier.Reload]] (method: calls) — *senders that have changed or were added/removed.*
- [[notif-server/src/core/notifier.go.md|Notifier.SendRaw]] (method: calls) — *SendRaw deserializes a binary Cap'n Proto notification frame and queues it.*
- [[notif-server/src/core/notifier.go.md|Notifier.Stop]] (method: calls) — *It is fully idempotent and safe to call multiple times.*
- [[notif-server/src/core/notifier.go.md|notifier.go]] (same_package)
- [[notif-server/src/core/notifier_test.go.md|blockingMockSender.GetLogLevel]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|blockingMockSender.GetTag]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|blockingMockSender.SendMessage]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|channelBlockingMockSender.GetLogLevel]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|channelBlockingMockSender.GetTag]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|channelBlockingMockSender.SendMessage]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|collectingMockSender.GetLogLevel]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|collectingMockSender.GetTag]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|collectingMockSender.SendMessage]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|collectingMockSender.getMessages]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|ctxCheckingFallbackSender.GetLogLevel]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|ctxCheckingFallbackSender.GetTag]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|ctxCheckingFallbackSender.SendMessage]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|failingMockSender.GetLogLevel]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|failingMockSender.GetTag]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|failingMockSender.SendMessage]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|mockSender.GetLogLevel]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|mockSender.GetTag]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|mockSender.SendMessage]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|mockSender.getLastMsg]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|mockSender.getLastSub]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|mockSender.isCalled]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|mockSender.setCalled]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|timeoutPrimarySender.GetLogLevel]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|timeoutPrimarySender.GetTag]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|timeoutPrimarySender.SendMessage]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|toggleMockSender.GetLogLevel]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|toggleMockSender.GetTag]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|toggleMockSender.SendMessage]] (method: defines_method)
- [[notif-server/src/core/notifier_test.go.md|toggleMockSender.setError]] (method: defines_method)
- [[notif-server/src/core/request_handler.go.md|NewNotifHandler]] (function: calls)
- [[notif-server/src/core/request_handler.go.md|NotifNcapHandler.NotifNcapSerialize]] (method: calls) — *Allocates a fresh message arena per call to avoid unbounded memory leaks and data races [NS-6].*
- [[notif-server/src/core/request_handler.go.md|request_handler.go]] (same_package)
- [[notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Close]] (method: calls)
- [[notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Error]] (method: calls)
- [[notif-server/src/core/test_logger_test.go.md|test_logger_test.go]] (same_package)
- [[notif-server/src/server/server.go.md|NewServer]] (function: calls) — *NewServer creates a new Notification Server.*

### 🔌 Consumers (Inbound)
- [[notif-server/src/core/controller.go.md|controller.go]] (calls)
- [[notif-server/src/core/controller.go.md|controller.go]] (same_package)
- [[notif-server/src/core/controller_test.go.md|controller_test.go]] (calls)
- [[notif-server/src/core/controller_test.go.md|controller_test.go]] (same_package)
- [[notif-server/src/core/notifier.go.md|notifier.go]] (calls)
- [[notif-server/src/core/notifier.go.md|notifier.go]] (same_package)
- [[notif-server/src/core/notifier_test.go.md|TestDefaultRoutingFallbackBanner]] (function: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|TestFallbackAfterPrimaryContextTimeout]] (function: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|TestFallbackToTelegramOnSenderFailure]] (function: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|TestGracefulSenderReplacementDrainsPending]] (function: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|TestImplicitRouting]] (function: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|TestLiveConfigHotReloadOnTheFlyAndMultipleSameTypeSenders]] (function: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|TestNotifierDropCountersUnderBackpressure]] (function: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|TestNotifierDynamicHealthMetricsTransitions]] (function: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|TestNotifierGracefulShutdownIdempotentAndDrains]] (function: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|TestNotifierMessageFlow]] (function: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|TestRawMessageConsumption]] (function: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|TestRegisterSenderDeduplicationNoWorkerLeak]] (function: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|TestReloadAndRegisterAfterStopAreSafe]] (function: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|TestWorkerPoolCapacity]] (function: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|blockingMockSender.GetLogLevel]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|blockingMockSender.GetTag]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|blockingMockSender.SendMessage]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|blockingMockSender]] (struct: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|blockingMockSender]] (struct: defines_method)
- [[notif-server/src/core/notifier_test.go.md|channelBlockingMockSender.GetLogLevel]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|channelBlockingMockSender.GetTag]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|channelBlockingMockSender.SendMessage]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|channelBlockingMockSender]] (struct: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|channelBlockingMockSender]] (struct: defines_method)
- [[notif-server/src/core/notifier_test.go.md|collectingMockSender.GetLogLevel]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|collectingMockSender.GetTag]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|collectingMockSender.SendMessage]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|collectingMockSender.getMessages]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|collectingMockSender]] (struct: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|collectingMockSender]] (struct: defines_method)
- [[notif-server/src/core/notifier_test.go.md|ctxCheckingFallbackSender.GetLogLevel]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|ctxCheckingFallbackSender.GetTag]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|ctxCheckingFallbackSender.SendMessage]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|ctxCheckingFallbackSender]] (struct: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|ctxCheckingFallbackSender]] (struct: defines_method)
- [[notif-server/src/core/notifier_test.go.md|failingMockSender.GetLogLevel]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|failingMockSender.GetTag]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|failingMockSender.SendMessage]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|failingMockSender]] (struct: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|failingMockSender]] (struct: defines_method)
- [[notif-server/src/core/notifier_test.go.md|findNotifierStatus]] (function: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|init]] (function: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|iterations]] (constant: belongs_to) — *1. Repeatedly register 10 senders with the same tag*
- [[notif-server/src/core/notifier_test.go.md|mockSender.GetLogLevel]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|mockSender.GetTag]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|mockSender.SendMessage]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|mockSender.getLastMsg]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|mockSender.getLastSub]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|mockSender.isCalled]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|mockSender.setCalled]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|mockSender]] (struct: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|mockSender]] (struct: defines_method)
- [[notif-server/src/core/notifier_test.go.md|timeoutPrimarySender.GetLogLevel]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|timeoutPrimarySender.GetTag]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|timeoutPrimarySender.SendMessage]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|timeoutPrimarySender]] (struct: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|timeoutPrimarySender]] (struct: defines_method)
- [[notif-server/src/core/notifier_test.go.md|toggleMockSender.GetLogLevel]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|toggleMockSender.GetTag]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|toggleMockSender.SendMessage]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|toggleMockSender.setError]] (method: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|toggleMockSender]] (struct: belongs_to)
- [[notif-server/src/core/notifier_test.go.md|toggleMockSender]] (struct: defines_method)
<!-- SYNC:END -->
