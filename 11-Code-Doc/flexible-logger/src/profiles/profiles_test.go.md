---
microservice: flexible-logger
type: note
status: active
tags:
- '#service/flexible-logger'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/src/engine/log_engine.go.md|LogEngine.Error]] (method: calls)
- [[flexible-logger/src/engine/log_engine.go.md|LogEngine.Info]] (method: calls)
- [[flexible-logger/src/engine/log_engine_test.go.md|log_engine_test.go]] (imports)
- [[flexible-logger/src/interfaces/sink.go.md|sink.go]] (imports)
- [[flexible-logger/src/models/entry.go.md|LogEntry.Release]] (method: calls) — *Release decrements the reference count and returns the entry to the pool if 0.*
- [[flexible-logger/src/models/level.go.md|Level.String]] (method: calls)
- [[flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/src/profiles/audit.go.md|NewAuditLogger]] (function: calls) — *- Notif (Async)*
- [[flexible-logger/src/profiles/audit.go.md|audit.go]] (same_package)
- [[flexible-logger/src/profiles/devel.go.md|NewDevelLogger]] (function: calls) — *- Local file (Sync) - Path derived from executable or defaults*
- [[flexible-logger/src/profiles/devel.go.md|devel.go]] (same_package)
- [[flexible-logger/src/profiles/minimal.go.md|NewMinimalLogger]] (function: calls) — *- Console output (Async)*
- [[flexible-logger/src/profiles/minimal.go.md|minimal.go]] (same_package)
- [[flexible-logger/src/profiles/notif_logger.go.md|NewNotifLogger]] (function: calls) — *NewNotifLogger creates a logger similar to NoLockLogger but with LocalNotifier.*
- [[flexible-logger/src/profiles/notif_logger.go.md|NotifLoggerWrapper.SetLocalNotifQueue]] (method: calls)
- [[flexible-logger/src/profiles/notif_logger.go.md|notif_logger.go]] (same_package)
- [[flexible-logger/src/profiles/profiles_test.go.md|SlowSink.Close]] (method: defines_method)
- [[flexible-logger/src/profiles/profiles_test.go.md|SlowSink.Write]] (method: defines_method)
- [[flexible-logger/src/profiles/standard.go.md|NewStandardLogger]] (function: calls) — *- Notif (Async) - Address from Config*
- [[flexible-logger/src/profiles/standard.go.md|standard.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[flexible-logger/src/profiles/profiles_test.go.md|SlowSink.Close]] (method: belongs_to)
- [[flexible-logger/src/profiles/profiles_test.go.md|SlowSink.Write]] (method: belongs_to)
- [[flexible-logger/src/profiles/profiles_test.go.md|SlowSink]] (struct: belongs_to) — *SlowSink for testing Audit blocking*
- [[flexible-logger/src/profiles/profiles_test.go.md|SlowSink]] (struct: defines_method) — *SlowSink for testing Audit blocking*
- [[flexible-logger/src/profiles/profiles_test.go.md|TestAllProfiles]] (function: belongs_to) — *TestAllProfiles verifies that basic standalone profiles boot up and log correctly.*
- [[flexible-logger/src/profiles/profiles_test.go.md|TestAuditLogger_Blocking]] (function: belongs_to)
- [[flexible-logger/src/profiles/profiles_test.go.md|TestAuditLogger_EmergencyFileFallback]] (function: belongs_to)
- [[flexible-logger/src/profiles/profiles_test.go.md|TestAuditLogger_MissingConfig_WarnsAndDoesNotPanic]] (function: belongs_to)
- [[flexible-logger/src/profiles/profiles_test.go.md|TestNotifLogger_LocalQueue]] (function: belongs_to)
- [[flexible-logger/src/profiles/profiles_test.go.md|TestProfile_AppNamePropagation]] (function: belongs_to)
- [[flexible-logger/src/profiles/profiles_test.go.md|probeLoopback]] (function: belongs_to) — *in the test execution environment without polluting any test listener's backlog.*
- [[flexible-logger/src/profiles/profiles_test.go.md|startTestServer]] (function: belongs_to) — *tested using "Integration Tests" with a local mock server.*
<!-- SYNC:END -->
