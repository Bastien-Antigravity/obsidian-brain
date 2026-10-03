---
source: config-server/src/telegram/manager_test.go
workspace: config-server
type: code-mirror
status: auto-generated
last_sync: 2026-10-01T01:10:01.546996
---

# Mirror: manager_test.go

## 📝 Description
Automatically generated mirror for `config-server/src/telegram/manager_test.go`.

> **Essential Process**:
> Unit tests for MenuManager, verifying dynamic menu tree building, action hierarchy construction, and callback wiring against mock controllers.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[config-server/config-server/src/core/controller.go.md|controller.go]] (imports)
- [[config-server/config-server/src/store/persistence.go.md|persistence.go]] (imports)
- [[config-server/config-server/src/telegram/manager.go.md|MenuManager.RebuildMenu]] (method: calls) — *RebuildMenu dynamically pulls the configuration map and registers it with the TeleClient.*
- [[config-server/config-server/src/telegram/manager.go.md|NewMenuManager]] (function: calls) — *NewMenuManager creates a new MenuManager.*
- [[config-server/config-server/src/telegram/manager.go.md|manager.go]] (same_package)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockController.DeleteConfig]] (method: defines_method)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockController.GetConfig]] (method: defines_method)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockController.GetStatus]] (method: defines_method)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockController.ListConfig]] (method: defines_method)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockController.PersistConfig]] (method: defines_method)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockController.ReloadConfig]] (method: defines_method)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockController.SetConfig]] (method: defines_method)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockLogger.Critical]] (method: defines_method)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockLogger.Debug]] (method: defines_method)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockLogger.Error]] (method: defines_method)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockLogger.Info]] (method: defines_method)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockLogger.Warning]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[config-server/config-server/cmd/config-server/main.go.md|main.go]] (calls)
- [[config-server/config-server/cmd/config-server/main.go.md|main.go]] (imports)
- [[config-server/config-server/src/telegram/manager.go.md|manager.go]] (calls)
- [[config-server/config-server/src/telegram/manager.go.md|manager.go]] (same_package)
- [[config-server/config-server/src/telegram/manager_test.go.md|TestMenuManager_RebuildMenu]] (function: belongs_to)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockController.DeleteConfig]] (method: belongs_to)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockController.GetConfig]] (method: belongs_to)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockController.GetStatus]] (method: belongs_to)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockController.ListConfig]] (method: belongs_to)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockController.PersistConfig]] (method: belongs_to)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockController.ReloadConfig]] (method: belongs_to)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockController.SetConfig]] (method: belongs_to)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockController]] (struct: belongs_to)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockController]] (struct: defines_method)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockLogger.Critical]] (method: belongs_to)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockLogger.Debug]] (method: belongs_to)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockLogger.Error]] (method: belongs_to)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockLogger.Info]] (method: belongs_to)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockLogger.Warning]] (method: belongs_to)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockLogger]] (struct: belongs_to)
- [[config-server/config-server/src/telegram/manager_test.go.md|mockLogger]] (struct: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
