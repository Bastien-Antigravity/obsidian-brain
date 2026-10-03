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
- None detected

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main.go]] (imports)
- [[tele-remote/tele-remote/src/interfaces/subscriber.go.md|ISubscriberCallbacks]] (struct: belongs_to) — *ISubscriberCallbacks defines the triggers from any transport layer to the Bot context*
- [[tele-remote/tele-remote/src/interfaces/subscriber.go.md|ISubscriber]] (interface: belongs_to) — *ISubscriber abstracts an incoming connection listener (gRPC server, NATS loop, etc)*
- [[tele-remote/tele-remote/src/publishers/grpc.go.md|grpc.go]] (imports)
- [[tele-remote/tele-remote/src/subscribers/grpc.go.md|grpc.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|bot.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|menus.go]] (imports)
<!-- SYNC:END -->
