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
- [[tele-remote/tele-remote/src/interfaces/subscriber.go.md|subscriber.go]] (imports)
- [[tele-remote/tele-remote/src/models/ui_types.go.md|ui_types.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Broadcast]] (method: defines_method) — *Broadcast sends a plain text message to the pre-configured ChatID*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.LoggingMiddleware]] (method: defines_method) — *LoggingMiddleware intercepts all incoming messages for auditing*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.OnDisconnect]] (method: defines_method) — *OnDisconnect cleans up a component's state when it loses connection*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.OnTelemetry]] (method: defines_method) — *OnTelemetry handles incoming logs or events by broadcasting them to the admin chat*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Send]] (method: defines_method) — *Send wraps tb.Context.Send to intercept and log all outgoing responses*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Start]] (method: defines_method) — *Start begins polling*
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Error]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Info]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Warning]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main.go]] (calls)
- [[tele-remote/tele-remote/src/publishers/grpc.go.md|grpc.go]] (calls)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|grpc.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Broadcast]] (method: belongs_to) — *Broadcast sends a plain text message to the pre-configured ChatID*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.LoggingMiddleware]] (method: belongs_to) — *LoggingMiddleware intercepts all incoming messages for auditing*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.OnDisconnect]] (method: belongs_to) — *OnDisconnect cleans up a component's state when it loses connection*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.OnTelemetry]] (method: belongs_to) — *OnTelemetry handles incoming logs or events by broadcasting them to the admin chat*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Send]] (method: belongs_to) — *Send wraps tb.Context.Send to intercept and log all outgoing responses*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Start]] (method: belongs_to) — *Start begins polling*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot]] (struct: belongs_to) — *Send wraps tb.Context.Send to intercept and log all outgoing responses*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot]] (struct: defines_method) — *Send wraps tb.Context.Send to intercept and log all outgoing responses*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Config]] (struct: belongs_to) — *Config is a simple alias for the toolbox AppConfig in this context*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|NewBot]] (function: belongs_to) — *NewBot registers Telebot settings and initializes memory maps*
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (same_package)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|menus_test.go]] (calls)
<!-- SYNC:END -->
