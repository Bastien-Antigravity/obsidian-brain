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
Automatically generated mirror for `microservice-toolbox/python/microservice_toolbox/utils/terminal_ui.py`.

> **Essential Process**:
> Formats and prints internal toolbox log messages to the terminal. Ensures consistent visual output with Go/Rust implementations.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/helpers.py.md|get_hostname]] (function: calls) — *Get system hostname (cached)*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/helpers.py.md|helpers.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/helpers.py.md|helpers.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/process_lock.py.md|process_lock.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/process_lock.py.md|process_lock.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/terminal_ui.py.md|print_internal_log]] (function: belongs_to) — *Formats and prints an internal toolbox log message*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/terminal_ui.py.md|truncate]] (function: belongs_to) — *Helper to truncate strings to a maximum length.*
<!-- SYNC:END -->
