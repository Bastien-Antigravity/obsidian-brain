---
microservice: tele-remote
type: note
status: active
tags:
- '#service/tele-remote'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `tele-remote/src/telegram/core/bot.go`.

> **Essential Process**:
> Manages the Telegram Bot lifecycle, ChatID authorization middleware, non-blocking telemetry broadcast worker, and session-safe in-memory state registry for connected microservices.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[tele-remote/tele-remote/src/interfaces/subscriber.go.md|subscriber.go]] (imports)
- [[tele-remote/tele-remote/src/models/ui_types.go.md|ui_types.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.AuthMiddleware]] (method: defines_method) — *AuthMiddleware silently drops any Telegram update from an unauthorized ChatID/Sender without replying.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Broadcast]] (method: defines_method) — *Broadcast sends a plain text message to all pre-configured ChatIDs.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.IsAuthorized]] (method: defines_method) — *IsAuthorized checks whether the incoming Telegram context matches any configured ChatID or AllowedUsers.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.LoggingMiddleware]] (method: defines_method) — *LoggingMiddleware intercepts all incoming messages for auditing.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.OnDisconnect]] (method: defines_method) — *preventing a late disconnect from an older stream from deleting a newly reconnected session.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.OnTelemetry]] (method: defines_method) — *OnTelemetry enqueues incoming logs or events non-blockingly for asynchronous delivery to the admin chat.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Send]] (method: defines_method) — *Send wraps tb.Context.Send to intercept and log all outgoing responses.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.SetBurstLimit]] (method: defines_method) — *SetBurstLimit dynamically updates the RateLimiter's maximum burst threshold.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Start]] (method: defines_method) — *Start begins polling and shuts down cleanly when ctx is cancelled.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.runTelemetryWorker]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Error]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Info]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Warning]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (same_package)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext.Callback]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext.Chat]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext.Message]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext.Sender]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext.Text]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|NewRateLimiter]] (function: calls) — *NewRateLimiter instantiates a sliding-window rate limiter with sensible defaults.*
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|rate_limiter.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main.go]] (calls)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|grpc.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.AuthMiddleware]] (method: belongs_to) — *AuthMiddleware silently drops any Telegram update from an unauthorized ChatID/Sender without replying.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Broadcast]] (method: belongs_to) — *Broadcast sends a plain text message to all pre-configured ChatIDs.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.IsAuthorized]] (method: belongs_to) — *IsAuthorized checks whether the incoming Telegram context matches any configured ChatID or AllowedUsers.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.LoggingMiddleware]] (method: belongs_to) — *LoggingMiddleware intercepts all incoming messages for auditing.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.OnDisconnect]] (method: belongs_to) — *preventing a late disconnect from an older stream from deleting a newly reconnected session.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.OnTelemetry]] (method: belongs_to) — *OnTelemetry enqueues incoming logs or events non-blockingly for asynchronous delivery to the admin chat.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Send]] (method: belongs_to) — *Send wraps tb.Context.Send to intercept and log all outgoing responses.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.SetBurstLimit]] (method: belongs_to) — *SetBurstLimit dynamically updates the RateLimiter's maximum burst threshold.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Start]] (method: belongs_to) — *Start begins polling and shuts down cleanly when ctx is cancelled.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.runTelemetryWorker]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot]] (struct: belongs_to) — *Bot holds the Telegram connection, config, non-blocking telemetry queue, and live state registry.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot]] (struct: defines_method) — *Bot holds the Telegram connection, config, non-blocking telemetry queue, and live state registry.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Config]] (struct: belongs_to) — *Config holds the Telegram bot connection and authorization settings.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|GetConvKey]] (function: belongs_to) — *falling back to UserID: 0 when c.Sender() is nil.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|NewBot]] (function: belongs_to) — *NewBot registers Telebot settings, initializes memory maps, and starts the background telemetry worker.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|parseAuthorizedIDs]] (function: belongs_to) — *parseAuthorizedIDs extracts unique numeric IDs from chatID and allowedUsers inputs on the cold path.*
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (same_package)
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|rate_limiter.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|rate_limiter.go]] (same_package)
- [[tele-remote/tele-remote/src/telegram/routes/routes.go.md|routes.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|menus.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|menus_test.go]] (calls)
<!-- SYNC:END -->
