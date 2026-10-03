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
Automatically generated mirror for `microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp`.

> **Essential Process**:
> C++ wrapper for libdistconf CGO shared library exports.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.ApplyFileOverride]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Decrypt]] (method: defines_method) — *Decrypt a secret*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.DistConfig]] (method: defines_method) — *Disable copy*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetAddress]] (method: defines_method) — *Get an address (host:port) for a capability*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetCapability]] (method: defines_method) — *Get a capability configuration as JSON*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetFullConfig]] (method: defines_method) — *Get full configuration as JSON*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetGRPCAddress]] (method: defines_method) — *Get a gRPC address for a capability*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetLastError]] (method: defines_method) — *Get the last error from the underlying engine*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetRESTAddress]] (method: defines_method) — *Get a REST address for a capability*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetRegistryMutex]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetRegistry]] (method: defines_method) — *Meyer's Singleton for header-only static registry without C++17 inline variables*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Get]] (method: defines_method) — *Get a configuration value*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.OnLiveConfUpdate]] (method: defines_method) — *Register a live update listener*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.OnRegistryUpdate]] (method: defines_method) — *Register a registry update listener*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Set]] (method: defines_method) — *Set a configuration value*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.ShareConfig]] (method: defines_method) — *Broadcast state to the ecosystem*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.StaticCallbackBridge]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.StaticRegistryBridge]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Sync]] (method: defines_method) — *Synchronize with the Config Server*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.ValidateMandatoryServices]] (method: defines_method) — *Validate mandatory services*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/libdistconf.h.md|libdistconf.h]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.hpp]] (calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.hpp]] (same_package)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DISTCONF_HPP]] (macro: belongs_to) — *ifndef DISTCONF_HPP*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.ApplyFileOverride]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Decrypt]] (method: belongs_to) — *Decrypt a secret*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.DistConfig]] (method: belongs_to) — *Disable copy*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetAddress]] (method: belongs_to) — *Get an address (host:port) for a capability*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetCapability]] (method: belongs_to) — *Get a capability configuration as JSON*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetFullConfig]] (method: belongs_to) — *Get full configuration as JSON*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetGRPCAddress]] (method: belongs_to) — *Get a gRPC address for a capability*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetLastError]] (method: belongs_to) — *Get the last error from the underlying engine*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetRESTAddress]] (method: belongs_to) — *Get a REST address for a capability*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetRegistryMutex]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetRegistry]] (method: belongs_to) — *Meyer's Singleton for header-only static registry without C++17 inline variables*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Get]] (method: belongs_to) — *Get a configuration value*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.OnLiveConfUpdate]] (method: belongs_to) — *Register a live update listener*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.OnRegistryUpdate]] (method: belongs_to) — *Register a registry update listener*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Set]] (method: belongs_to) — *Set a configuration value*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.ShareConfig]] (method: belongs_to) — *Broadcast state to the ecosystem*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.StaticCallbackBridge]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.StaticRegistryBridge]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Sync]] (method: belongs_to) — *Synchronize with the Config Server*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.ValidateMandatoryServices]] (method: belongs_to) — *Validate mandatory services*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig]] (class: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|loader.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/integration/rust_con.rs.md|rust_con.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/integration/rust_gen.rs.md|rust_gen.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/process_lock.py.md|process_lock.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|manager.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/connectivity/resolver.rs.md|resolver.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/lifecycle/manager.rs.md|manager.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/grpc_server.rs.md|grpc_server.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/providers.rs.md|providers.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/serializers/serializer.rs.md|serializer.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|client.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|logger.rs]] (calls)
<!-- SYNC:END -->
