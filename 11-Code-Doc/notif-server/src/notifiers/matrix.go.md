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
Automatically generated mirror for `notif-server/src/notifiers/matrix.go`.

> **Essential Process**:
> Implements the Matrix notification sender. Executes HTTP POST requests to Matrix webhook endpoints with exponential backoff. Dispatches operational and delivery messages through the ecosystem Universal Logger.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/src/notifiers/config.go.md|config.go]] (same_package)
- [[notif-server/src/notifiers/config.go.md|getOption]] (function: calls) — *getOption retrieves an option from the config map trying multiple case variations.*
- [[notif-server/src/notifiers/matrix.go.md|MatrixSender.GetLogLevel]] (method: defines_method)
- [[notif-server/src/notifiers/matrix.go.md|MatrixSender.GetTag]] (method: defines_method)
- [[notif-server/src/notifiers/matrix.go.md|MatrixSender.SendMessage]] (method: defines_method)
- [[notif-server/src/notifiers/matrix.go.md|MatrixSender.redactError]] (method: defines_method) — *redactError strips the webhook URL and any other secrets from transport errors via the standard sanitizer.*
- [[notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Close]] (method: calls)
- [[notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Debug]] (method: calls)
- [[notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Error]] (method: calls)
- [[notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Info]] (method: calls)
- [[notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Warning]] (method: calls)
- [[notif-server/src/notifiers/notifiers_test.go.md|notifiers_test.go]] (same_package)
- [[notif-server/src/sanitizer/sanitizer.go.md|RedactSecrets]] (function: calls) — *from error strings and telemetry messages.*
- [[notif-server/src/sanitizer/sanitizer.go.md|sanitizer.go]] (imports)

### 🔌 Consumers (Inbound)
- [[notif-server/src/core/notifier.go.md|notifier.go]] (calls)
- [[notif-server/src/notifiers/matrix.go.md|MatrixSender.GetLogLevel]] (method: belongs_to)
- [[notif-server/src/notifiers/matrix.go.md|MatrixSender.GetTag]] (method: belongs_to)
- [[notif-server/src/notifiers/matrix.go.md|MatrixSender.SendMessage]] (method: belongs_to)
- [[notif-server/src/notifiers/matrix.go.md|MatrixSender.redactError]] (method: belongs_to) — *redactError strips the webhook URL and any other secrets from transport errors via the standard sanitizer.*
- [[notif-server/src/notifiers/matrix.go.md|MatrixSender]] (struct: belongs_to)
- [[notif-server/src/notifiers/matrix.go.md|MatrixSender]] (struct: defines_method)
- [[notif-server/src/notifiers/matrix.go.md|NewMatrixSender]] (function: belongs_to) — *or (nil, error) if decryption fails.*
- [[notif-server/src/notifiers/notifiers_test.go.md|notifiers_test.go]] (calls)
- [[notif-server/src/notifiers/notifiers_test.go.md|notifiers_test.go]] (same_package)
<!-- SYNC:END -->
