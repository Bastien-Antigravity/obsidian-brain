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
Automatically generated mirror for `notif-server/src/telegram/manager.go`.

> **Essential Process**:
> Orchestrates dynamic interactive Telegram menus and telemetry streaming for notif-server via Tele-Remote. Allows operators to trigger test alerts, reload senders, and configure alerting providers remotely.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (imports)
- [[notif-server/notif-server/src/telegram/manager.go.md|MenuManager.RebuildMenu]] (method: defines_method) — *RebuildMenu dynamically pulls the configuration map and registers it with the TeleClient.*

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/cmd/notif-server/main.go.md|main.go]] (imports)
- [[notif-server/notif-server/src/telegram/manager.go.md|MenuManager.RebuildMenu]] (method: belongs_to) — *RebuildMenu dynamically pulls the configuration map and registers it with the TeleClient.*
- [[notif-server/notif-server/src/telegram/manager.go.md|MenuManager]] (struct: belongs_to) — *RebuildMenu dynamically pulls the configuration map and registers it with the TeleClient.*
- [[notif-server/notif-server/src/telegram/manager.go.md|MenuManager]] (struct: defines_method) — *RebuildMenu dynamically pulls the configuration map and registers it with the TeleClient.*
- [[notif-server/notif-server/src/telegram/manager.go.md|NewMenuManager]] (function: belongs_to) — *NewMenuManager creates a new MenuManager.*
- [[notif-server/notif-server/src/telegram/manager.go.md|config.AppCon]] (function: belongs_to) — *SetupTelegram initializes the Tele-Remote client, binds dynamic updates, and registers with Lifecycle Manager.*
<!-- SYNC:END -->
