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
Automatically generated mirror for `microservice-toolbox/python/microservice_toolbox/utils/process_lock.py`.

> **Essential Process**:
> Provides cross-platform process locking using file locking to prevent multiple instances of the same service/command from running concurrently.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetLastError]] (method: calls) — *Get the last error from the underlying engine*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/terminal_ui.py.md|terminal_ui.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/terminal_ui.py.md|truncate]] (function: calls) — *Helper to truncate strings to a maximum length.*

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/conn_manager/connection.py.md|connection.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/process_lock.py.md|ERROR_ACCESS_DENIED]] (constant: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/process_lock.py.md|ProcessLock]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/process_lock.py.md|__init__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/process_lock.py.md|acquire]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/process_lock.py.md|is_pid_alive]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/process_lock.py.md|is_process_running]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/process_lock.py.md|prevent_double_start]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/process_lock.py.md|release]] (function: belongs_to)
<!-- SYNC:END -->
