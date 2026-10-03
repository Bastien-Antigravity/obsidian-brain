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
Automatically generated mirror for `notif-server/src/notifiers/gmail.go`.

> **Essential Process**:
> Implements the Gmail notification sender via SMTP with architectural hardening. Handles both Port 587 (STARTTLS) and Port 465 (Implicit TLS). Dispatches operational and delivery messages through the ecosystem Universal Logger.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/notifiers/config.go.md|config.go]] (same_package)
- [[notif-server/notif-server/src/notifiers/config.go.md|getOption]] (function: calls) — *getOption retrieves an option from the config map trying multiple case variations.*
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.GetLogLevel]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.GetTag]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.SendMessage]] (method: defines_method) — *- source: System or notifier source tag (used to construct the email Subject).*
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.buildEmail]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.dialAndSend]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|plainAuthWithoutTLSCheck.Next]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|plainAuthWithoutTLSCheck.Start]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Close]] (method: calls)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Info]] (method: calls)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Warning]] (method: calls)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|notifiers_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/core/notifier.go.md|notifier.go]] (calls)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.GetLogLevel]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.GetTag]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.SendMessage]] (method: belongs_to) — *- source: System or notifier source tag (used to construct the email Subject).*
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.buildEmail]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender.dialAndSend]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender]] (struct: belongs_to)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|GmailSender]] (struct: defines_method)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|NewGmailSender]] (function: belongs_to)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|plainAuthWithoutTLSCheck.Next]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|plainAuthWithoutTLSCheck.Start]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|plainAuthWithoutTLSCheck]] (struct: belongs_to)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|plainAuthWithoutTLSCheck]] (struct: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|notifiers_test.go]] (calls)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|notifiers_test.go]] (same_package)
<!-- SYNC:END -->
