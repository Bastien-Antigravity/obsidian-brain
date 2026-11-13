---
microservice: watchdog-agent
type: note
status: active
tags:
- '#service/watchdog-agent'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/telegram/manager.go`.

> **Essential Process**:
> Telegram bot UI integration and menu management for watchdog-agent. Dynamically constructs and binds interactive buttons, node telemetry status, and process restart callbacks into the tele-remote bot interface.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/core/controller.go.md|controller.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler_test.go.md|mockWatchdogLogger.Error]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler_test.go.md|mockWatchdogLogger.Info]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler_test.go.md|mockWatchdogLogger.Warning]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|LogShipper.Start]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|MenuManager.RebuildMenu]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|MenuManager.RebuildMenu]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|MenuManager]] (struct: belongs_to) — *MenuManager orchestrates the rebuild operations of the Telegram interactive menus.*
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|MenuManager]] (struct: defines_method) — *MenuManager orchestrates the rebuild operations of the Telegram interactive menus.*
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|NewMenuManager]] (function: belongs_to) — *NewMenuManager creates a new MenuManager.*
- [[watchdog-agent/watchdog-agent/src/telegram/manager.go.md|SetupTelegram]] (function: belongs_to) — *SetupTelegram initializes the Tele-Remote client, binds dynamic updates, and registers with Lifecycle Manager.*
<!-- SYNC:END -->
