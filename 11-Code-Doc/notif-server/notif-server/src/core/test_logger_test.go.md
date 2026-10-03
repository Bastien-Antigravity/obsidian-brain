---
source: notif-server/src/core/test_logger_test.go
workspace: notif-server
type: code-mirror
status: auto-generated
last_sync: 2026-10-01T01:10:02.656316
---

# Mirror: test_logger_test.go

## 📝 Description
Automatically generated mirror for `notif-server/src/core/test_logger_test.go`.

> **Essential Process**:
> Test logger fixture implementing log_interfaces.Logger for core unit tests. Isolated to test builds (_test.go).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.AddMetadata]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Close]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Critical]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Debug]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Error]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.GetLevel]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.GetMetadata]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.GetNotifQueue]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Info]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.LogWithCaller]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Log]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Logon]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Logout]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Report]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Schedule]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.SetCallerSkip]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.SetLevel]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.SetLocalNotifQueue]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.SetMetadata]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Stream]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Trade]] (method: defines_method)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Warning]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (calls)
- [[notif-server/notif-server/src/core/controller.go.md|controller.go]] (same_package)
- [[notif-server/notif-server/src/core/controller_test.go.md|controller_test.go]] (calls)
- [[notif-server/notif-server/src/core/controller_test.go.md|controller_test.go]] (same_package)
- [[notif-server/notif-server/src/core/notifier.go.md|notifier.go]] (calls)
- [[notif-server/notif-server/src/core/notifier.go.md|notifier.go]] (same_package)
- [[notif-server/notif-server/src/core/request_handler.go.md|request_handler.go]] (calls)
- [[notif-server/notif-server/src/core/request_handler.go.md|request_handler.go]] (same_package)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.AddMetadata]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Close]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Critical]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Debug]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Error]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.GetLevel]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.GetMetadata]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.GetNotifQueue]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Info]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.LogWithCaller]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Log]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Logon]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Logout]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Report]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Schedule]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.SetCallerSkip]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.SetLevel]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.SetLocalNotifQueue]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.SetMetadata]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Stream]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Trade]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger.Warning]] (method: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger]] (struct: belongs_to)
- [[notif-server/notif-server/src/core/test_logger_test.go.md|testNotifierLogger]] (struct: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
