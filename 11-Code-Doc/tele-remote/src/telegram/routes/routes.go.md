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
Automatically generated mirror for `tele-remote/src/telegram/routes/routes.go`.

> **Essential Process**:
> Registers global Telebot middlewares (LoggingMiddleware and AuthMiddleware) and wires top-level Telegram command and reply-keyboard handlers.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[tele-remote/src/models/ui_types.go.md|ui_types.go]] (imports)
- [[tele-remote/src/telegram/core/bot.go.md|Bot.AuthMiddleware]] (method: calls) — *AuthMiddleware rejects any Telegram update from an unauthorized ChatID/Sender.*
- [[tele-remote/src/telegram/core/bot.go.md|Bot.LoggingMiddleware]] (method: calls) — *LoggingMiddleware intercepts all incoming messages for auditing.*
- [[tele-remote/src/telegram/core/bot.go.md|GetConvKey]] (function: calls) — *falling back to UserID: 0 when c.Sender() is nil.*
- [[tele-remote/src/telegram/core/bot.go.md|MaskChatID]] (function: calls) — *(e.g. "...3982") to prevent plaintext credential leakage in logs and telemetry.*
- [[tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (imports)
- [[tele-remote/src/telegram/core/rate_limiter.go.md|Bot.RateLimitMiddleware]] (method: calls) — *RateLimitMiddleware drops rapid updates per ConversationKey before executing handlers.*
- [[tele-remote/src/telegram/ui/menus.go.md|HandleDynamicText]] (function: calls) — *HandleDynamicText routes text messages from Reply buttons and user prompts back to actions.*
- [[tele-remote/src/telegram/ui/menus.go.md|RequestEmergencyConfirmation]] (function: calls) — *RequestEmergencyConfirmation initiates a 2-step confirmation workflow for CmdPowerOff or CmdStop.*
- [[tele-remote/src/telegram/ui/menus.go.md|ShowMainMenu]] (function: calls) — *ShowMainMenu displays the dynamic top-level menu.*
- [[tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Info]] (method: calls)
- [[tele-remote/src/telegram/ui/menus_test.go.md|fakeUIContext.Send]] (method: calls)
- [[tele-remote/src/telegram/ui/menus_test.go.md|fakeUIContext.Text]] (method: calls)
- [[tele-remote/src/telegram/ui/menus_test.go.md|menus_test.go]] (imports)

### 🔌 Consumers (Inbound)
- [[tele-remote/cmd/tele-remote/main.go.md|main.go]] (calls)
- [[tele-remote/cmd/tele-remote/main.go.md|main.go]] (imports)
- [[tele-remote/src/telegram/routes/routes.go.md|SetupRoutes]] (function: belongs_to) — *SetupRoutes initializes global middlewares, static handlers, and dynamic reply-keyboard routing.*
<!-- SYNC:END -->
