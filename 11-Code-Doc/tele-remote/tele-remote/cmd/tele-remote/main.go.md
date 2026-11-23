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
- [[tele-remote/tele-remote/cmd/tele-remote/contracts.go.md|buildTeleRemoteContracts]] (function: calls)
- [[tele-remote/tele-remote/cmd/tele-remote/contracts.go.md|contracts.go]] (same_package)
- [[tele-remote/tele-remote/src/interfaces/subscriber.go.md|subscriber.go]] (imports)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|GrpcSubscriber.StartListen]] (method: calls) — *StartListen binds the TCP socket and serves incoming gRPC component streams.*
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|NewGrpcSubscriber]] (function: calls) — *NewGrpcSubscriber instantiates a gRPC transport listener bound to ip:port.*
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|grpc.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.SetBurstLimit]] (method: calls) — *SetBurstLimit dynamically updates the RateLimiter's maximum burst threshold.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.Start]] (method: calls) — *Start begins polling and shuts down cleanly when ctx is cancelled.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|NewBot]] (function: calls) — *NewBot registers Telebot settings, initializes memory maps, and starts the background telemetry worker.*
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/routes/routes.go.md|SetupRoutes]] (function: calls) — *SetupRoutes initializes global middlewares, static handlers, and dynamic reply-keyboard routing.*
- [[tele-remote/tele-remote/src/telegram/routes/routes.go.md|routes.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|OnComponentConnected]] (function: calls) — *never wipe out an existing valid component session.*
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Critical]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Error]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Info]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Warning]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|menus_test.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|mockTelegramServer.Close]] (method: calls)

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|TeleRemoteCap]] (struct: belongs_to) — *TeleRemoteCap matches the specific capability for this service*
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main]] (function: belongs_to)
<!-- SYNC:END -->
