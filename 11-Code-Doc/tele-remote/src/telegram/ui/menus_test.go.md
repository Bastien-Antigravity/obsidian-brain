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
- [[tele-remote/tele-remote/src/models/ui_types.go.md|ui_types.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|Bot.OnDisconnect]] (method: calls) — *preventing a late disconnect from an older stream from deleting a newly reconnected session.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|NewBot]] (function: calls) — *NewBot registers Telebot settings, initializes memory maps, and starts the background telemetry worker.*
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|HandleDynamicText]] (function: calls) — *HandleDynamicText routes text messages from Reply buttons and user prompts back to actions.*
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|OnComponentConnected]] (function: calls) — *never wipe out an existing valid component session.*
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|RenderMenu]] (function: calls) — *RenderMenu builds and displays a CommandMenu as a Reply Keyboard.*
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|RequestEmergencyConfirmation]] (function: calls) — *RequestEmergencyConfirmation initiates a 2-step confirmation workflow for CmdPowerOff or CmdStop.*
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|ShowMainMenu]] (function: calls) — *ShowMainMenu displays the dynamic top-level menu.*
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|getMenuByPath]] (function: calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|menus.go]] (same_package)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Critical]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Debug]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Error]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Info]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Warning]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher.Close]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher.PublishCommand]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher.RequestRefresh]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|fakeUIContext.Chat]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|fakeUIContext.Message]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|fakeUIContext.Send]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|fakeUIContext.Sender]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|fakeUIContext.Text]] (method: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|mockTelegramServer.Close]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main.go]] (calls)
- [[tele-remote/tele-remote/cmd/tele-remote/main.go.md|main.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/routes/routes.go.md|routes.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/routes/routes.go.md|routes.go]] (imports)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|menus.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/ui/menus.go.md|menus.go]] (same_package)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Critical]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Debug]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Error]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Info]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger.Warning]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockLogger]] (struct: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher.Close]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher.PublishCommand]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher.RequestRefresh]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|MockPublisher]] (struct: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|TestBot_MenuRegistration]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|TestEmergencyBroadcast_PartialFailureReporting]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|TestMenu_RowAndButtonOrderingWithDuplicateTolerance]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|TestOnComponentConnected_MalformedJSONPreservesExistingMenu]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|TestOnComponentConnected_RejectsOversizedAndDeepMenus]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|TestOnComponentConnected_SameClientIDInvalidatesPendingInput]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|TestOnDisconnect_StaleStreamDoesNotDeleteNewSession]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|TestPendingInput_RoutesToOriginatingClientAndIsolatesUsers]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|TestShowMainMenu_DeterministicAlphabeticalOrder]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|TestShowMainMenu_OpenMFEPriorityAndDuplicateOrderTolerance]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|TestTwoStepConfirmation_EmergencyCommands]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|fakeUIContext.Chat]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|fakeUIContext.Message]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|fakeUIContext.Send]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|fakeUIContext.Sender]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|fakeUIContext.Text]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|fakeUIContext]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|fakeUIContext]] (struct: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|mockTelegramServer.Close]] (method: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|mockTelegramServer]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|mockTelegramServer]] (struct: defines_method)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|newFakeUIContext]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/ui/menus_test.go.md|newMockTelegramServer]] (function: belongs_to)
<!-- SYNC:END -->
