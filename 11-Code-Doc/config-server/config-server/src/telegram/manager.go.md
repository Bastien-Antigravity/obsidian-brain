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
Automatically generated mirror for `config-server/src/telegram/manager.go`.

> **Essential Process**:
> Binds config-server management operations to the tele-remote interactive Telegram bot interface, publishing hierarchical menus for browsing, editing, and persisting state.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/config-server/src/core/controller.go.md|controller.go]] (imports)
- [[config-server/config-server/src/telegram/manager.go.md|MenuManager.RebuildMenu]] (method: defines_method) — *RebuildMenu dynamically pulls the configuration map and registers it with the TeleClient.*
- [[config-server/config-server/src/telegram/manager_test.go.md|manager_test.go]] (same_package)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockController.ListConfig]] (method: calls)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockLogger.Error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/src/telegram/manager.go.md|*toolbox_conf]] (function: belongs_to) — *SetupTelegram initializes the Tele-Remote client, binds dynamic updates, and registers with Lifecycle Manager.*
- [[config-server/config-server/src/telegram/manager.go.md|MenuManager.RebuildMenu]] (method: belongs_to) — *RebuildMenu dynamically pulls the configuration map and registers it with the TeleClient.*
- [[config-server/config-server/src/telegram/manager.go.md|MenuManager]] (struct: belongs_to) — *RebuildMenu dynamically pulls the configuration map and registers it with the TeleClient.*
- [[config-server/config-server/src/telegram/manager.go.md|MenuManager]] (struct: defines_method) — *RebuildMenu dynamically pulls the configuration map and registers it with the TeleClient.*
- [[config-server/config-server/src/telegram/manager.go.md|NewMenuManager]] (function: belongs_to) — *NewMenuManager creates a new MenuManager.*
- [[config-server/config-server/src/telegram/manager_test.go.md|manager_test.go]] (calls)
- [[config-server/config-server/src/telegram/manager_test.go.md|manager_test.go]] (same_package)
<!-- SYNC:END -->
