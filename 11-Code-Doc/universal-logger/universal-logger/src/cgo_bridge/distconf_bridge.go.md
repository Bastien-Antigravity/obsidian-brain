---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/src/cgo_bridge/initialize.go.md|initialize.go]] (same_package)
- [[universal-logger/universal-logger/src/cgo_bridge/initialize.go.md|sanitizeFFIString]] (function: calls) — *sanitizeFFIString cleans C strings coming across the frontier*

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_ApplyFileOverride]] (function: belongs_to) — *export DistConf_ApplyFileOverride*
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_Close]] (function: belongs_to) — *export DistConf_Close*
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_Decrypt]] (function: belongs_to) — *export DistConf_Decrypt*
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_FreeString]] (function: belongs_to) — *export DistConf_FreeString*
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_GetAddress]] (function: belongs_to) — *export DistConf_GetAddress*
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_GetCapability]] (function: belongs_to) — *export DistConf_GetCapability*
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_GetFullConfig]] (function: belongs_to) — *export DistConf_GetFullConfig*
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_GetGRPCAddress]] (function: belongs_to) — *export DistConf_GetGRPCAddress*
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_GetLastErrorCode]] (function: belongs_to) — *export DistConf_GetLastErrorCode*
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_GetLastError]] (function: belongs_to) — *export DistConf_GetLastError*
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_GetRESTAddress]] (function: belongs_to) — *export DistConf_GetRESTAddress*
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_Get]] (function: belongs_to) — *export DistConf_Get*
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_New]] (function: belongs_to) — *export DistConf_New*
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_OnLiveConfUpdate]] (function: belongs_to) — *export DistConf_OnLiveConfUpdate*
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_OnRegistryUpdate]] (function: belongs_to) — *export DistConf_OnRegistryUpdate*
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_Set]] (function: belongs_to) — *export DistConf_Set*
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_ShareConfig]] (function: belongs_to) — *export DistConf_ShareConfig*
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|DistConf_Sync]] (function: belongs_to) — *export DistConf_Sync*
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|mapErrorCode]] (function: belongs_to)
- [[universal-logger/universal-logger/src/cgo_bridge/distconf_bridge.go.md|setLastError]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (calls)
<!-- SYNC:END -->
