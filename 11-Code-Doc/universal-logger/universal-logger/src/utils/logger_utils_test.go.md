---
source: universal-logger/src/utils/logger_utils_test.go
workspace: universal-logger
type: code-mirror
status: auto-generated
last_sync: 2026-09-17 19:14:20.932318
microservice: 08-Base-Scripts
tags:
- '#service/08-Base-Scripts'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: logger_utils_test.go

## 📝 Description
Automatically generated mirror for `universal-logger/src/utils/logger_utils_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/src/interfaces/models.go.md|models.go]] (imports)
- [[universal-logger/universal-logger/src/utils/logger_utils.go.md|LogWithMetadata]] (function: calls)
- [[universal-logger/universal-logger/src/utils/logger_utils.go.md|logger_utils.go]] (same_package)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.AddMetadata]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Close]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Critical]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Debug]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Error]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.GetLevel]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.GetMetadata]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.GetNotifQueue]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Info]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.LogWithCaller]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Log]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Logon]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Logout]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Report]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Schedule]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.SetCallerSkip]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.SetLevel]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.SetLocalNotifQueue]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.SetMetadata]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Stream]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Trade]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Warning]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockWrapper.Unwrap]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/notif_message.go.md|notif_message.go]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/utils/logger_utils.go.md|logger_utils.go]] (calls)
- [[universal-logger/universal-logger/src/utils/logger_utils.go.md|logger_utils.go]] (same_package)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|TestLogWithMetadata_DelegatesToLogWithCaller]] (function: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|TestLogWithMetadata_NilLogger]] (function: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|TestLogWithMetadata_UnwrapsTarget]] (function: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.AddMetadata]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Close]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Critical]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Debug]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Error]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.GetLevel]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.GetMetadata]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.GetNotifQueue]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Info]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.LogWithCaller]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Log]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Logon]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Logout]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Report]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Schedule]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.SetCallerSkip]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.SetLevel]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.SetLocalNotifQueue]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.SetMetadata]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Stream]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Trade]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller.Warning]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller]] (struct: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockLoggerWithCaller]] (struct: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockWrapper.Unwrap]] (method: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockWrapper]] (struct: belongs_to)
- [[universal-logger/universal-logger/src/utils/logger_utils_test.go.md|mockWrapper]] (struct: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
