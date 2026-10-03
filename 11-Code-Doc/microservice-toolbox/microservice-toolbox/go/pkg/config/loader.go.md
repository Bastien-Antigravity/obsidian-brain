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
Automatically generated mirror for `microservice-toolbox/go/pkg/config/loader.go`.

> **Essential Process**:
> Loads layered configuration from local YAML, environment variables, and distributed config server.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Decrypt]] (method: calls) — *Decrypt a secret*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetAddress]] (method: calls) — *Get an address (host:port) for a capability*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetGRPCAddress]] (method: calls) — *Get a gRPC address for a capability*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetRESTAddress]] (method: calls) — *Get a REST address for a capability*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args.go.md|AppConfig.ParseCLIArgs]] (method: calls) — *It implements a "Docker Guard": if DOCKER_ENV=true, --host and --port are ignored.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args.go.md|args.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.DecryptSecret]] (method: defines_method) — *If it is an ENC(...) block but decryption fails, an error is returned.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetGRPCListenAddr]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetListenAddr]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetLocal]] (method: defines_method) — *Supports nested lookups using dot notation (e.g., "database.host").*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetRESTAddr]] (method: defines_method) — *GetRESTAddr returns the address for the REST management interface.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetServiceName]] (method: defines_method) — *GetServiceName returns the standardized program name.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.OnLiveConfUpdate]] (method: defines_method) — *OnLiveConfUpdate registers a callback for live configuration updates.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.OnRegistryUpdate]] (method: defines_method) — *OnRegistryUpdate registers a callback for service registry changes.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.SetLogger]] (method: defines_method) — *SetLogger updates the logger after instantiation.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.ShareConfig]] (method: defines_method) — *ShareConfig shares service configuration with the ecosystem.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.UnmarshalLocal]] (method: defines_method) — *UnmarshalLocal maps the 'local' configuration section into a target struct.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.ValidateUniquePorts]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.applyCLIGRPCOverrides]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.applyCLIOverrides]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.applyFileOverride]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.ensurePath]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.loadPublicKey]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/merger.go.md|DeepMerge]] (function: calls) — *If a key exists in both and the source is not a map, the source value overwrites the destination.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/merger.go.md|merger.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|NewResolver]] (function: calls) — *NewResolver creates a new network resolver.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver_test.go.md|resolver_test.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|EnsureSafeLogger]] (function: calls) — *production microservices from silently running dark without operational logs.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|logger.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Info]] (method: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args_test.go.md|args_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args_test.go.md|args_test.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.DecryptSecret]] (method: belongs_to) — *If it is an ENC(...) block but decryption fails, an error is returned.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetGRPCListenAddr]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetListenAddr]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetLocal]] (method: belongs_to) — *Supports nested lookups using dot notation (e.g., "database.host").*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetRESTAddr]] (method: belongs_to) — *GetRESTAddr returns the address for the REST management interface.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetServiceName]] (method: belongs_to) — *GetServiceName returns the standardized program name.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.OnLiveConfUpdate]] (method: belongs_to) — *OnLiveConfUpdate registers a callback for live configuration updates.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.OnRegistryUpdate]] (method: belongs_to) — *OnRegistryUpdate registers a callback for service registry changes.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.SetLogger]] (method: belongs_to) — *SetLogger updates the logger after instantiation.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.ShareConfig]] (method: belongs_to) — *ShareConfig shares service configuration with the ecosystem.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.UnmarshalLocal]] (method: belongs_to) — *UnmarshalLocal maps the 'local' configuration section into a target struct.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.ValidateUniquePorts]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.applyCLIGRPCOverrides]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.applyCLIOverrides]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.applyFileOverride]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.ensurePath]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.loadPublicKey]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|LoadConfigWithLogger]] (function: belongs_to) — *LoadConfigWithLogger loads the configuration with an explicit logger and layered priority.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|LoadConfig]] (function: belongs_to) — *LoadConfig loads the configuration with layered priority.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|endpointKey]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|getIP]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|getPort]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|normalizeIP]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|loader_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|loader_test.go]] (same_package)
<!-- SYNC:END -->
