---
source: notif-server/src/core/controller_test.go
workspace: notif-server
type: code-mirror
status: auto-generated
last_sync: 2026-09-19 00:02:00.606595
microservice: 08-Base-Scripts
tags:
- '#service/08-Base-Scripts'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: controller_test.go

## 📝 Description
Automatically generated mirror for `notif-server/src/core/controller_test.go`.

> **Essential Process**:
> Unit tests for NotifController implementation. Validates dynamic provider addition, removal, configuration updates, deep-copy immutability, and template generation for all supported provider types.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/core/controller.go.md|Controller.AddProvider]] (method: calls) — *AddProvider initializes a new provider section with default template.*
- [[notif-server/notif-server/src/core/controller.go.md|Controller.GetAlertingConfig]] (method: calls) — *GetAlertingConfig returns a deep copy of the current internal configuration of notification providers.*
- [[notif-server/notif-server/src/core/controller.go.md|Controller.RemoveProvider]] (method: calls) — *RemoveProvider deletes a provider section.*
- [[notif-server/notif-server/src/core/controller.go.md|Controller.SetAlertingConfig]] (method: calls) — *SetAlertingConfig updates a specific setting for a notification provider.*
- [[notif-server/notif-server/src/core/controller.go.md|NewController]] (function: calls) — *NewController creates a new Controller instance.*
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (same_package)
- [[notif-server/notif-server/src/core/notifier.go.md|NewNotifier]] (function: calls) — *NewNotifier creates a new instance of the notification service.*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.GetActiveNotifiers]] (method: calls) — *GetActiveNotifiers returns information about all currently active notification senders.*
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.Stop]] (method: calls) — *Stop shuts down the notifier and all active workers.*
- [[notif-server/notif-server/src/core/notifier.go.md|notifier.go]] (same_package)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Error]] (method: calls)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|test_logger_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/core/controller_test.go.md|TestControllerAddProviderDetectsChange]] (function: belongs_to)
- [[notif-server/notif-server/src/core/controller_test.go.md|TestControllerDeepCopyImmutability]] (function: belongs_to)
- [[notif-server/notif-server/src/core/controller_test.go.md|TestControllerProviderTemplates]] (function: belongs_to)
- [[notif-server/notif-server/src/core/controller_test.go.md|TestControllerRemoveProvider]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
