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

## 📝 Description
Automatically generated mirror for `distributed-config/cmd/libdistconf/main.go`.

> **Essential Process**:
> CGO entrypoint compiling into the shared library libdistconf (so/dylib), exposing a stable C ABI for polyglot consumers (Python, Rust, C++, VBA).

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/distconf/libdistconf/libdistconf.h.md|call_config_update_cb]] (function: calls) — *Helper to safely execute a C callback from Go*
- [[distributed-config/distributed-config/src/cgo_bridge/errors.c.md|set_last_error]] (function: calls)
- [[distributed-config/distributed-config/src/cgo_bridge/initialize.go.md|Close]] (function: calls) — *Close is a Go-native wrapper for DistConf_Close.*
- [[distributed-config/distributed-config/src/cgo_bridge/initialize.go.md|New]] (function: calls) — *New is a Go-native wrapper for DistConf_New.*
- [[distributed-config/distributed-config/src/cgo_bridge/initialize.go.md|initialize.go]] (imports)
- [[distributed-config/distributed-config/src/cgo_bridge/validation.go.md|IsValid]] (function: calls) — *IsValid is a Go-native wrapper for checking handle validity.*
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_ApplyFileOverride]] (function: belongs_to) — *export DistConf_ApplyFileOverride*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_Close]] (function: belongs_to) — *export DistConf_Close*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_Decrypt]] (function: belongs_to) — *export DistConf_Decrypt*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_FreeString]] (function: belongs_to) — *export DistConf_FreeString*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_GetAddress]] (function: belongs_to) — *export DistConf_GetAddress*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_GetCapability]] (function: belongs_to) — *export DistConf_GetCapability*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_GetFullConfig]] (function: belongs_to) — *export DistConf_GetFullConfig*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_GetGRPCAddress]] (function: belongs_to) — *export DistConf_GetGRPCAddress*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_GetLastErrorCode]] (function: belongs_to) — *export DistConf_GetLastErrorCode*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_GetLastError]] (function: belongs_to) — *export DistConf_GetLastError*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_GetRESTAddress]] (function: belongs_to) — *export DistConf_GetRESTAddress*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_Get]] (function: belongs_to) — *export DistConf_Get*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_IsValid]] (function: belongs_to) — *export DistConf_IsValid*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_New]] (function: belongs_to) — *export DistConf_New*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_OnLiveConfUpdate]] (function: belongs_to) — *export DistConf_OnLiveConfUpdate*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_OnRegistryUpdate]] (function: belongs_to) — *export DistConf_OnRegistryUpdate*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_Set]] (function: belongs_to) — *export DistConf_Set*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_ShareConfig]] (function: belongs_to) — *export DistConf_ShareConfig*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_Sync]] (function: belongs_to) — *export DistConf_Sync*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_ValidateMandatoryServices]] (function: belongs_to) — *export DistConf_ValidateMandatoryServices*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|main]] (function: belongs_to)
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|mapErrorCode]] (function: belongs_to)
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|setLastError]] (function: belongs_to)
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConf.hpp]] (calls)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|__init__.py]] (calls)
- [[distributed-config/distributed-config/distconf/python/ffi_validation.py.md|ffi_validation.py]] (calls)
<!-- SYNC:END -->
