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
Automatically generated mirror for `notif-server/src/notifiers/matrix.go`.

> **Essential Process**:
> Implements the Matrix notification sender. Executes HTTP POST requests to Matrix webhook endpoints with exponential backoff. Dispatches operational and delivery messages through the ecosystem Universal Logger.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/notifiers/config.go.md|config.go]] (same_package)
- [[notif-server/notif-server/src/notifiers/config.go.md|getOption]] (function: calls) — *getOption retrieves an option from the config map trying multiple case variations.*
- [[notif-server/notif-server/src/notifiers/matrix.go.md|MatrixSender.GetLogLevel]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|MatrixSender.GetTag]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|MatrixSender.SendMessage]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Close]] (method: calls)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Debug]] (method: calls)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Error]] (method: calls)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Info]] (method: calls)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Warning]] (method: calls)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|notifiers_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/core/notifier.go.md|notifier.go]] (calls)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|MatrixSender.GetLogLevel]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|MatrixSender.GetTag]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|MatrixSender.SendMessage]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|MatrixSender]] (struct: belongs_to)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|MatrixSender]] (struct: defines_method)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|NewMatrixSender]] (function: belongs_to) — *unconfigured and returns (nil, nil) without failing.*
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|notifiers_test.go]] (calls)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|notifiers_test.go]] (same_package)
<!-- SYNC:END -->
