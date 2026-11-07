---
source: notif-server/cmd/notif-server/main_test.go
workspace: notif-server
type: code-mirror
status: auto-generated
last_sync: 2026-10-11 13:58:55.361505
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: main_test.go

## 📝 Description
Automatically generated mirror for `notif-server/cmd/notif-server/main_test.go`.

> **Essential Process**:
> Unit tests for notif-server main entrypoint helpers, including pre-flight Telegram Bot Token verification.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/cmd/notif-server/main.go.md|main.go]] (same_package)
- [[notif-server/notif-server/cmd/notif-server/main.go.md|verifyTelegramToken]] (function: calls) — *verifyTelegramToken validates a Telegram bot token against the getMe endpoint.*
- [[notif-server/notif-server/src/server/server.go.md|NewServer]] (function: calls) — *NewServer creates a new Notification Server.*

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/cmd/notif-server/main_test.go.md|TestVerifyTelegramToken]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
