---
source: notif-server/src/notifiers/notifiers_test.go
workspace: notif-server
type: code-mirror
status: auto-generated
last_sync: 2026-09-19 00:02:00.663210
microservice: 08-Base-Scripts
tags:
- '#service/08-Base-Scripts'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: notifiers_test.go

## 📝 Description
Automatically generated mirror for `notif-server/src/notifiers/notifiers_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/notifiers/discord.go.md|NewDiscordSender]] (function: calls)
- [[notif-server/notif-server/src/notifiers/discord.go.md|discord.go]] (same_package)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|NewGmailSender]] (function: calls)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|gmail.go]] (same_package)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|MatrixSender.GetLogLevel]] (method: calls)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|MatrixSender.GetTag]] (method: calls)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|MatrixSender.SendMessage]] (method: calls)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|NewMatrixSender]] (function: calls)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|matrix.go]] (same_package)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.AddMetadata]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Close]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Critical]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Debug]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Error]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.GetLevel]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.GetMetadata]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.GetNotifQueue]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Info]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.LogWithCaller]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Log]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Logon]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Logout]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Report]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Schedule]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.SetCallerSkip]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.SetLevel]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.SetLocalNotifQueue]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.SetMetadata]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Stream]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Trade]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Warning]] (method: defines_method)
- [[notif-server/notif-server/src/notifiers/telegram.go.md|NewTelegramSender]] (function: calls)
- [[notif-server/notif-server/src/notifiers/telegram.go.md|telegram.go]] (same_package)
- [[notif-server/notif-server/src/server/server.go.md|NewServer]] (function: calls)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/cmd/notif-server/main.go.md|main.go]] (calls)
- [[notif-server/notif-server/src/notifiers/discord.go.md|discord.go]] (calls)
- [[notif-server/notif-server/src/notifiers/discord.go.md|discord.go]] (same_package)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|gmail.go]] (calls)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|gmail.go]] (same_package)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|matrix.go]] (calls)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|matrix.go]] (same_package)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|TestDiscordOnDemandDecryption]] (function: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|TestDiscordOptionalConfig]] (function: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|TestDiscordSendMessageMock]] (function: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|TestExplicitParameterValidation]] (function: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|TestGmailOptionalConfig]] (function: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|TestMatrixOptionalConfig]] (function: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|TestMatrixSendMessageMock]] (function: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|TestTelegramOnDemandDecryption]] (function: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|TestTelegramOptionalConfig]] (function: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|TestTelegramSendMessageMock]] (function: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.AddMetadata]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Close]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Critical]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Debug]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Error]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.GetLevel]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.GetMetadata]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.GetNotifQueue]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Info]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.LogWithCaller]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Log]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Logon]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Logout]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Report]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Schedule]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.SetCallerSkip]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.SetLevel]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.SetLocalNotifQueue]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.SetMetadata]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Stream]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Trade]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger.Warning]] (method: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger]] (struct: belongs_to)
- [[notif-server/notif-server/src/notifiers/notifiers_test.go.md|mockTestLogger]] (struct: defines_method)
- [[notif-server/notif-server/src/notifiers/telegram.go.md|telegram.go]] (calls)
- [[notif-server/notif-server/src/notifiers/telegram.go.md|telegram.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
