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
Automatically generated mirror for `distributed-config/distconf/python/distconf/__init__.py`.

> **Essential Process**:
> Python wrapper for libdistconf. Provides native access to the distributed configuration ecosystem.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_Close]] (function: calls) — *export DistConf_Close*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_Decrypt]] (function: calls) — *export DistConf_Decrypt*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_FreeString]] (function: calls) — *export DistConf_FreeString*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_GetAddress]] (function: calls) — *export DistConf_GetAddress*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_GetCapability]] (function: calls) — *export DistConf_GetCapability*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_GetFullConfig]] (function: calls) — *export DistConf_GetFullConfig*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_GetGRPCAddress]] (function: calls) — *export DistConf_GetGRPCAddress*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_GetLastErrorCode]] (function: calls) — *export DistConf_GetLastErrorCode*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_GetLastError]] (function: calls) — *export DistConf_GetLastError*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_Get]] (function: calls) — *export DistConf_Get*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_New]] (function: calls) — *export DistConf_New*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_OnLiveConfUpdate]] (function: calls) — *export DistConf_OnLiveConfUpdate*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_OnRegistryUpdate]] (function: calls) — *export DistConf_OnRegistryUpdate*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_Set]] (function: calls) — *export DistConf_Set*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_ShareConfig]] (function: calls) — *export DistConf_ShareConfig*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_Sync]] (function: calls) — *export DistConf_Sync*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_ValidateMandatoryServices]] (function: calls) — *export DistConf_ValidateMandatoryServices*

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|CALLBACK_TYPE]] (constant: belongs_to) — *Callback type: void (*config_update_cb)(uintptr_t handle, const char* json_data)*
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|DISTCONF_ERR_DECRYPTION_FAILED]] (constant: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|DISTCONF_ERR_GENERIC]] (constant: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|DISTCONF_ERR_INVALID_HANDLE]] (constant: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|DISTCONF_ERR_INVALID_INPUT]] (constant: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|DISTCONF_ERR_KEY_NOT_FOUND]] (constant: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|DISTCONF_ERR_NETWORK_FAILURE]] (constant: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|DISTCONF_ERR_VALIDATION_FAILED]] (constant: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|DISTCONF_SUCCESS]] (constant: belongs_to) — *Standardized Error Codes (must match helpers.h)*
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|DistConfError]] (class: belongs_to) — *Base exception for all DistConf errors.*
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|DistConfig]] (class: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|__del__]] (function: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|__init__]] (function: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|_load_lib]] (function: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|_raise_last_error]] (function: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|_wrapper]] (function: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|close]] (function: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|decrypt]] (function: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|get]] (function: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|get_address]] (function: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|get_capability]] (function: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|get_full_config]] (function: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|get_grpc_address]] (function: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|on_live_conf_update]] (function: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|on_registry_update]] (function: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|set]] (function: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|share_config]] (function: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|sync]] (function: belongs_to)
- [[distributed-config/distributed-config/distconf/python/distconf/__init__.py.md|validate_mandatory_services]] (function: belongs_to)
- [[distributed-config/distributed-config/distconf/python/examples/basic_usage.py.md|basic_usage.py]] (calls)
- [[distributed-config/distributed-config/distconf/python/examples/basic_usage.py.md|basic_usage.py]] (imports)
<!-- SYNC:END -->
