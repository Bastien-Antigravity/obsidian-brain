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
Automatically generated mirror for `tele-remote/src/interfaces/subscriber.go`.

> **Essential Process**:
> Defines the inbound transport listener and callback contracts bridging connected microservice streams to the Tele-Remote bot core.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[tele-remote/cmd/tele-remote/main.go.md|main.go]] (imports)
- [[tele-remote/src/interfaces/subscriber.go.md|ISubscriberCallbacks]] (struct: belongs_to) — *ISubscriberCallbacks defines the triggers from any transport layer to the Bot context*
- [[tele-remote/src/interfaces/subscriber.go.md|ISubscriber]] (interface: belongs_to) — *ISubscriber abstracts an incoming connection listener (gRPC server, NATS loop, etc)*
- [[tele-remote/src/publishers/grpc.go.md|grpc.go]] (imports)
- [[tele-remote/src/subscribers/grpc.go.md|grpc.go]] (imports)
- [[tele-remote/src/subscribers/grpc_test.go.md|grpc_test.go]] (imports)
- [[tele-remote/src/telegram/core/bot.go.md|bot.go]] (imports)
- [[tele-remote/src/telegram/ui/menus.go.md|menus.go]] (imports)
<!-- SYNC:END -->
