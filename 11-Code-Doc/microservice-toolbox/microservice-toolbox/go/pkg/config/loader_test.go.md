---
microservice: microservice-toolbox
type: note
status: active
tags:
- '#service/microservice-toolbox'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `microservice-toolbox/go/pkg/config/loader_test.go`.

> **Essential Process**:
> Loads layered configuration from local YAML, environment variables, and distributed config server.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args.go.md|AppConfig.ParseCLIArgs]] (method: calls) — *It implements a "Docker Guard": if DOCKER_ENV=true, --host and --port are ignored.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args.go.md|args.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.DecryptSecret]] (method: calls) — *If it is an ENC(...) block but decryption fails, an error is returned.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetGRPCListenAddr]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetListenAddr]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetLocalString]] (method: calls) — *Returns an empty string if the key does not exist or is nil.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetLocal]] (method: calls) — *Supports nested lookups using dot notation (e.g., "database.host").*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetRESTAddr]] (method: calls) — *GetRESTAddr returns the address for the REST management interface.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.SetLogger]] (method: calls) — *SetLogger updates the logger after instantiation.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.UnmarshalLocal]] (method: calls) — *UnmarshalLocal maps the 'local' configuration section into a target struct.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.ensurePath]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|LoadConfig]] (function: calls) — *LoadConfig loads the configuration with layered priority.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|loader.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/merger.go.md|DeepMerge]] (function: calls) — *If a key exists in both and the source is not a map, the source value overwrites the destination.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/merger.go.md|merger.go]] (same_package)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver_test.go.md|resolver_test.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|EnsureSafeLogger]] (function: calls) — *production microservices from silently running dark without operational logs.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|logger.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|Config]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|TestAppConfig_AddressResolution]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|TestAppConfig_AutoLoadPublicKey]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|TestAppConfig_CLIOverrideScope]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|TestAppConfig_DecryptPlaintextPassthrough]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|TestAppConfig_DuplicatePorts]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|TestAppConfig_EnsurePath]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|TestAppConfig_GRPCMissingReturnsError]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|TestAppConfig_GetLocalEmpty]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|TestAppConfig_GetLocal]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|TestAppConfig_KeyFlag]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|TestAppConfig_LoadConfigFactory]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|TestAppConfig_MissingFileReturnsError]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|TestAppConfig_Secrets]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|TestAppConfig_SetLogger]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|TestAppConfig_UnmarshalLocal]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader_test.go.md|TestDeepMerge]] (function: belongs_to)
<!-- SYNC:END -->
