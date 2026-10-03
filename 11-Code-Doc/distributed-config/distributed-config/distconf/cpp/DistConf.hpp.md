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
Automatically generated mirror for `distributed-config/distconf/cpp/DistConf.hpp`.

> **Essential Process**:
> C++ RAII facade and header-only wrapper for the distributed-config library, binding the libdistconf CGO shared object.

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
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_GetLastError]] (function: calls) — *export DistConf_GetLastError*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_Get]] (function: calls) — *export DistConf_Get*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_New]] (function: calls) — *export DistConf_New*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_OnLiveConfUpdate]] (function: calls) — *export DistConf_OnLiveConfUpdate*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_OnRegistryUpdate]] (function: calls) — *export DistConf_OnRegistryUpdate*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_Set]] (function: calls) — *export DistConf_Set*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_ShareConfig]] (function: calls) — *export DistConf_ShareConfig*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_Sync]] (function: calls) — *export DistConf_Sync*
- [[distributed-config/distributed-config/cmd/libdistconf/main.go.md|DistConf_ValidateMandatoryServices]] (function: calls) — *export DistConf_ValidateMandatoryServices*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.Decrypt]] (method: defines_method) — *Decrypt a secret*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.DistConfig]] (method: defines_method) — *Disable copy*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.GetAddress]] (method: defines_method) — *Get an address (host:port) for a capability*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.GetCapability]] (method: defines_method) — *Get a capability configuration as JSON*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.GetFullConfig]] (method: defines_method) — *Get full configuration as JSON*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.GetGRPCAddress]] (method: defines_method) — *Get a gRPC address for a capability*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.GetLastError]] (method: defines_method) — *Get the last error from the underlying engine*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.GetRegistryMutex]] (method: defines_method)
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.GetRegistry]] (method: defines_method) — *Meyer's Singleton for header-only static registry without C++17 inline variables*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.Get]] (method: defines_method) — *Get a configuration value*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.OnLiveConfUpdate]] (method: defines_method) — *Register a live update listener*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.OnRegistryUpdate]] (method: defines_method) — *Register a registry update listener*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.Set]] (method: defines_method) — *Set a configuration value*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.ShareConfig]] (method: defines_method) — *Broadcast state to the ecosystem*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.StaticCallbackBridge]] (method: defines_method)
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.StaticRegistryBridge]] (method: defines_method)
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.Sync]] (method: defines_method) — *Synchronize with the Config Server*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.ValidateMandatoryServices]] (method: defines_method) — *Validate mandatory services*
- [[distributed-config/distributed-config/distconf/libdistconf/libdistconf.h.md|libdistconf.h]] (imports)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DISTCONF_HPP]] (macro: belongs_to) — *ifndef DISTCONF_HPP*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.Decrypt]] (method: belongs_to) — *Decrypt a secret*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.DistConfig]] (method: belongs_to) — *Disable copy*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.GetAddress]] (method: belongs_to) — *Get an address (host:port) for a capability*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.GetCapability]] (method: belongs_to) — *Get a capability configuration as JSON*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.GetFullConfig]] (method: belongs_to) — *Get full configuration as JSON*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.GetGRPCAddress]] (method: belongs_to) — *Get a gRPC address for a capability*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.GetLastError]] (method: belongs_to) — *Get the last error from the underlying engine*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.GetRegistryMutex]] (method: belongs_to)
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.GetRegistry]] (method: belongs_to) — *Meyer's Singleton for header-only static registry without C++17 inline variables*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.Get]] (method: belongs_to) — *Get a configuration value*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.OnLiveConfUpdate]] (method: belongs_to) — *Register a live update listener*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.OnRegistryUpdate]] (method: belongs_to) — *Register a registry update listener*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.Set]] (method: belongs_to) — *Set a configuration value*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.ShareConfig]] (method: belongs_to) — *Broadcast state to the ecosystem*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.StaticCallbackBridge]] (method: belongs_to)
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.StaticRegistryBridge]] (method: belongs_to)
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.Sync]] (method: belongs_to) — *Synchronize with the Config Server*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig.ValidateMandatoryServices]] (method: belongs_to) — *Validate mandatory services*
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig]] (class: belongs_to)
- [[distributed-config/distributed-config/distconf/cpp/DistConf.hpp.md|DistConfig]] (class: defines_method)
- [[distributed-config/distributed-config/distconf/cpp/examples/basic_usage.cpp.md|basic_usage.cpp]] (calls)
- [[distributed-config/distributed-config/distconf/cpp/examples/basic_usage.cpp.md|basic_usage.cpp]] (imports)
<!-- SYNC:END -->
