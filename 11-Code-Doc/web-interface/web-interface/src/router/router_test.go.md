---
source: web-interface/src/router/router_test.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-09-13T14:08:57.891667
---

# Mirror: router_test.go

## 📝 Description
Automatically generated mirror for `web-interface/src/router/router_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/router/dynamic.go.md|RegisterDynamicRoutes]] (function: calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.AddMetadata]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Close]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Critical]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Debug]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Error]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.GetLevel]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.GetNotifQueue]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Info]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Log]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Logon]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Logout]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Report]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Schedule]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.SetCallerSkip]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.SetLevel]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.SetLocalNotifQueue]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.SetMetadata]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Stream]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Trade]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Warning]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (imports)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|main_test.go]] (imports)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (same_package)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (calls)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|TestDecryptionEndpointRemoved]] (function: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.AddMetadata]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Close]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Critical]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Debug]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Error]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.GetLevel]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.GetNotifQueue]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Info]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Log]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Logon]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Logout]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Report]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Schedule]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.SetCallerSkip]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.SetLevel]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.SetLocalNotifQueue]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.SetMetadata]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Stream]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Trade]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Warning]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger]] (struct: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger]] (struct: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
