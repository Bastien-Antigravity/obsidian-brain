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

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/core/controller.go.md|Controller.AddProvider]] (method: calls)
- [[notif-server/notif-server/src/core/controller.go.md|Controller.GetAlertingConfig]] (method: calls)
- [[notif-server/notif-server/src/core/controller.go.md|Controller.RemoveProvider]] (method: calls)
- [[notif-server/notif-server/src/core/controller.go.md|Controller.SetAlertingConfig]] (method: calls)
- [[notif-server/notif-server/src/core/controller.go.md|NewController]] (function: calls)
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (same_package)
- [[notif-server/notif-server/src/core/notifier.go.md|NewNotifier]] (function: calls)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.GetActiveNotifiers]] (method: calls)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.Stop]] (method: calls)
- [[notif-server/notif-server/src/core/notifier.go.md|notifier.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/core/controller_test.go.md|TestControllerAddProviderDetectsChange]] (function: belongs_to)
- [[notif-server/notif-server/src/core/controller_test.go.md|TestControllerDeepCopyImmutability]] (function: belongs_to)
- [[notif-server/notif-server/src/core/controller_test.go.md|TestControllerProviderTemplates]] (function: belongs_to)
- [[notif-server/notif-server/src/core/controller_test.go.md|TestControllerRemoveProvider]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
