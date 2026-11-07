---
microservice: web-interface
type: note
status: active
tags:
- '#service/web-interface'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `web-interface/src/telegram/manager.go`.

> **Essential Process**:
> Manages the telegram bot integration and interactive control menu for the web-interface microservice.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/core/controller.go.md|Controller.CheckDatabase]] (method: calls) — *CheckDatabase checks database availability dynamically by querying the current appConfig.*
- [[web-interface/web-interface/src/core/controller.go.md|Controller.GetStatus]] (method: calls) — *GetStatus returns metadata about the web-interface runtime.*
- [[web-interface/web-interface/src/core/controller.go.md|controller.go]] (imports)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.Register]] (method: calls) — *Register adds or updates a microfrontend service in the registry with automatic deduplication.*
- [[web-interface/web-interface/src/server/facade.go.md|ServerFacade.Start]] (method: calls)
- [[web-interface/web-interface/src/telegram/manager.go.md|MenuManager.BuildMenu]] (method: defines_method) — *BuildMenu dynamically updates actions with custom callbacks for the Telegram bot*

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (imports)
- [[web-interface/web-interface/src/telegram/manager.go.md|MenuManager.BuildMenu]] (method: belongs_to) — *BuildMenu dynamically updates actions with custom callbacks for the Telegram bot*
- [[web-interface/web-interface/src/telegram/manager.go.md|MenuManager]] (struct: belongs_to) — *MenuManager orchestrates telegram interactive menus for the web-interface*
- [[web-interface/web-interface/src/telegram/manager.go.md|MenuManager]] (struct: defines_method) — *MenuManager orchestrates telegram interactive menus for the web-interface*
- [[web-interface/web-interface/src/telegram/manager.go.md|NewMenuManager]] (function: belongs_to) — *NewMenuManager creates a new MenuManager*
- [[web-interface/web-interface/src/telegram/manager.go.md|SetupTelegram]] (function: belongs_to) — *SetupTelegram initializes the Tele-Remote client, registers callbacks, and hooks into lifecycle*
<!-- SYNC:END -->
