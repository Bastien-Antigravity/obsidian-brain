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

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.AuthMiddleware]] (method: calls) — *AuthMiddleware silently drops any Telegram update from an unauthorized ChatID/Sender without replying.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Broadcast]] (method: calls) — *Broadcast sends a plain text message to all pre-configured ChatIDs.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.OnTelemetry]] (method: calls) — *OnTelemetry enqueues incoming logs or events non-blockingly for asynchronous delivery to the admin chat.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|NewBot]] (function: calls) — *NewBot registers Telebot settings, initializes memory maps, and starts the background telemetry worker.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|bot.go]] (same_package)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Critical]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Debug]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Error]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Info]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Warning]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockPublisher.Close]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockPublisher.PublishCommand]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockPublisher.RequestRefresh]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext.Callback]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext.Chat]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext.Message]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext.Send]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext.Sender]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext.Text]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|mockTelegramServer.Close]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|mockTelegramServer.lastMessage]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|Bot.RateLimitMiddleware]] (method: calls) — *RateLimitMiddleware drops rapid updates per ConversationKey before executing handlers.*
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|NewRateLimiter]] (function: calls) — *NewRateLimiter instantiates a sliding-window rate limiter with sensible defaults.*
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|rate_limiter.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|bot.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|bot.go]] (same_package)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Critical]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Debug]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Error]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Info]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Warning]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger]] (struct: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockPublisher.Close]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockPublisher.PublishCommand]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockPublisher.RequestRefresh]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockPublisher]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockPublisher]] (struct: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|TestBot_AuthMiddlewareRejectsUnauthorizedChatID]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|TestBot_Broadcast]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|TestBot_OnTelemetryNonBlocking]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|TestBot_RateLimitMiddleware]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext.Callback]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext.Chat]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext.Message]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext.Send]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext.Sender]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext.Text]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext]] (struct: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|mockTelegramServer.Close]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|mockTelegramServer.lastMessage]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|mockTelegramServer]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|mockTelegramServer]] (struct: defines_method)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|newFakeContext]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|newMockTelegramServer]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|rate_limiter.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|rate_limiter.go]] (same_package)
- [[tele-remote/tele-remote/src/telegram/routes/routes.go.md|routes.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|menus.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|menus_test.go]] (imports)
<!-- SYNC:END -->
