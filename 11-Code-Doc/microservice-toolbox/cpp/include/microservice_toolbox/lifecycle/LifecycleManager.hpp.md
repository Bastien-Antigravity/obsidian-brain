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
Automatically generated mirror for `microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp`.

> **Essential Process**:
> Core microservice-toolbox module: LifecycleManager.hpp. Captures OS signals (SIGINT, SIGTERM) and executes cleanup hooks in LIFO order.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.ExecuteCleanups]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.LifecycleManager]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.Register]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.RequestInstanceShutdown]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.RequestShutdown]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.SignalHandler]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.Wait]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.execute_cleanups]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.register_hook]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.wait]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/logger/Logger.hpp.md|Logger.hpp]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|CleanupEntry]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|GlobalShutdownFlag]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.ExecuteCleanups]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.LifecycleManager]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.Register]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.RequestInstanceShutdown]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.RequestShutdown]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.SignalHandler]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.Wait]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.execute_cleanups]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.register_hook]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.wait]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager]] (class: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|MICROSERVICE_TOOLBOX_LIFECYCLE_MANAGER_HPP]] (macro: belongs_to) — *ifndef MICROSERVICE_TOOLBOX_LIFECYCLE_MANAGER_HPP*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|NewManagerWithLogger]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|NewManager]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|PendingSignalFlag]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|new_manager]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|new_manager_with_logger]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|spec.hpp]] (calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|spec.hpp]] (imports)
<!-- SYNC:END -->
