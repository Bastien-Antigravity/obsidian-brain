---
microservice: notif-server
type: note
status: active
tags:
- '#service/notif-server'
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
- [[notif-server/notif-server/src/core/controller.go.md|Controller.AddProvider]] (method: calls) — *AddProvider initializes a new provider section with default template.*
- [[notif-server/notif-server/src/core/controller.go.md|Controller.GetAlertingConfig]] (method: calls) — *GetAlertingConfig returns a deep copy of the current internal configuration of notification providers.*
- [[notif-server/notif-server/src/core/controller.go.md|Controller.GetStatus]] (method: calls) — *GetStatus returns server health and metadata.*
- [[notif-server/notif-server/src/core/controller.go.md|Controller.GetSupportedTypes]] (method: calls) — *GetSupportedTypes returns the list of hardcoded drivers available.*
- [[notif-server/notif-server/src/core/controller.go.md|Controller.ReloadConfig]] (method: calls) — *ReloadConfig triggers a manual reload of the configuration.*
- [[notif-server/notif-server/src/core/controller.go.md|Controller.RemoveProvider]] (method: calls) — *RemoveProvider deletes a provider section.*
- [[notif-server/notif-server/src/core/controller.go.md|Controller.SendTestNotification]] (method: calls) — *SendTestNotification triggers a test notification through the engine and logger.*
- [[notif-server/notif-server/src/core/controller.go.md|Controller.SetAlertingConfig]] (method: calls) — *SetAlertingConfig updates a specific setting for a notification provider.*
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (imports)
- [[notif-server/notif-server/src/telegram/manager.go.md|MenuManager.RebuildMenu]] (method: defines_method) — *RebuildMenu dynamically pulls the configuration map and registers it with the TeleClient.*

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/cmd/notif-server/main.go.md|main.go]] (calls)
- [[notif-server/notif-server/cmd/notif-server/main.go.md|main.go]] (imports)
- [[notif-server/notif-server/src/telegram/manager.go.md|MenuManager.RebuildMenu]] (method: belongs_to) — *RebuildMenu dynamically pulls the configuration map and registers it with the TeleClient.*
- [[notif-server/notif-server/src/telegram/manager.go.md|MenuManager]] (struct: belongs_to) — *MenuManager orchestrates the rebuild operations of the Telegram interactive menus.*
- [[notif-server/notif-server/src/telegram/manager.go.md|MenuManager]] (struct: defines_method) — *MenuManager orchestrates the rebuild operations of the Telegram interactive menus.*
- [[notif-server/notif-server/src/telegram/manager.go.md|NewMenuManager]] (function: belongs_to) — *NewMenuManager creates a new MenuManager.*
- [[notif-server/notif-server/src/telegram/manager.go.md|SetupTelegram]] (function: belongs_to) — *SetupTelegram initializes the Tele-Remote client, binds dynamic updates, and registers with Lifecycle Manager.*
<!-- SYNC:END -->
