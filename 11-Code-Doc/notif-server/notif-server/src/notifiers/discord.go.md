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

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/core/notifier.go.md|Notifier.EnsureSafeLogger]] (method: calls)
- [[notif-server/notif-server/src/notifiers/discord.go.md|DiscordSender.GetLogLevel]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/discord.go.md|DiscordSender.GetTag]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/discord.go.md|DiscordSender.SendMessage]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Close]] (method: calls)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Debug]] (method: calls)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Error]] (method: calls)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Info]] (method: calls)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Warning]] (method: calls)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|notifiers_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/core/notifier.go.md|notifier.go]] (calls)
- [[notif-server/notif-server/src/notifiers/discord.go.md|DiscordSender.GetLogLevel]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/discord.go.md|DiscordSender.GetTag]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/discord.go.md|DiscordSender.SendMessage]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/discord.go.md|DiscordSender]] (struct: belongs_to)
- [[notif-server/notif-server/src/notifiers/discord.go.md|DiscordSender]] (struct: defines_method)
- [[notif-server/notif-server/src/notifiers/discord.go.md|NewDiscordSender]] (function: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|notifiers_test.go]] (calls)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|notifiers_test.go]] (same_package)
<!-- SYNC:END -->
