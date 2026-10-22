---
source: microservice-toolbox/cpp/include/microservice_toolbox/version/Version.hpp
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:59.227384
---

# Mirror: Version.hpp

## 📝 Description
Automatically generated mirror for `microservice-toolbox/cpp/include/microservice_toolbox/version/Version.hpp`.

> **Essential Process**:
> Standardized dynamic version resolution engine for C++ services and tools. Reads dynamic semver strictly from VERSION.txt single source of truth, environment variable overrides, compile-time LDFLAGS/macros, and caches in memory.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/version/Version.hpp.md|GetCachedVersionRef]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/version/Version.hpp.md|GetVersionMutex]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/version/Version.hpp.md|GetVersion]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/version/Version.hpp.md|MICROSERVICE_TOOLBOX_VERSION_HPP]] (macro: belongs_to) — *ifndef MICROSERVICE_TOOLBOX_VERSION_HPP*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/version/Version.hpp.md|ResetVersion]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/version/Version.hpp.md|ResolveVersion]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/version/Version.hpp.md|SetVersion]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/version/Version.hpp.md|Trim]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/version/Version.hpp.md|appVer]] (constant: belongs_to) — *2. Check environment variables*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/version/Version.hpp.md|svcVer]] (constant: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/conn_manager/manager.go.md|manager.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/connectivity/resolver.go.md|resolver.go]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
