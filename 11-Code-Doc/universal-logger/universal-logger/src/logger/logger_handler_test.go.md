---
source: universal-logger/src/logger/logger_handler_test.go
workspace: universal-logger
type: code-mirror
status: auto-generated
last_sync: 2026-09-17 19:14:20.810813
microservice: 08-Base-Scripts
tags:
- '#service/08-Base-Scripts'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: logger_handler_test.go

## 📝 Description
Automatically generated mirror for `universal-logger/src/logger/logger_handler_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/src/interfaces/models.go.md|models.go]] (imports)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|NewUniLog]] (function: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.AddMetadata]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.GetMetadata]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|UniLog.SetMetadata]] (method: calls)
- [[universal-logger/universal-logger/src/logger/logger_handler.go.md|logger_handler.go]] (same_package)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|capturingSink.Close]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|capturingSink.Write]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|capturingSink.clear]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|capturingSink.getEntries]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Close]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Critical]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Debug]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Error]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.GetLevel]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Info]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.LogWithCaller]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Log]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Logon]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Logout]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Report]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Schedule]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.SetCallerSkip]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.SetLevel]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Stream]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Trade]] (method: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Warning]] (method: defines_method)
- [[universal-logger/universal-logger/src/utils/logger_utils.go.md|LogWithMetadata]] (function: calls)
- [[universal-logger/universal-logger/src/utils/notif_message.go.md|notif_message.go]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|unilog.go]] (calls)
- [[universal-logger/universal-logger/src/bootstrap/unilog.go.md|unilog.go]] (imports)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|TestUniLog_DynamicLevelFiltering_Unit]] (function: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|TestUniLog_LogWithCaller_ModuleFallback]] (function: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|TestUniLog_LogWithCaller_PreservesDetails]] (function: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|TestUniLog_MetadataConcurrency]] (function: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|TestUniLog_MetadataFormatting]] (function: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|TestUniLog_NotificationThresholds_Unit]] (function: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|capturedRecord]] (struct: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|capturingSink.Close]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|capturingSink.Write]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|capturingSink.clear]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|capturingSink.getEntries]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|capturingSink]] (struct: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|capturingSink]] (struct: defines_method)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Close]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Critical]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Debug]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Error]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.GetLevel]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Info]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.LogWithCaller]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Log]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Logon]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Logout]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Report]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Schedule]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.SetCallerSkip]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.SetLevel]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Stream]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Trade]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger.Warning]] (method: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger]] (struct: belongs_to)
- [[universal-logger/universal-logger/src/logger/logger_handler_test.go.md|mockFlexLogger]] (struct: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
