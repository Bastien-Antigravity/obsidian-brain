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
Automatically generated mirror for `universal-logger/unilog/python/unilog/listeners.py`.

> **Essential Process**:
> Asynchronous event listeners and subscription streams for configuration updates and telemetry notifications in the Python UniLog client.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (calls)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (imports)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (same_package)
- [[universal-logger/universal-logger/unilog/python/unilog/listeners.py.md|ConfigUpdateListener]] (class: belongs_to) — *Async config listener*
- [[universal-logger/universal-logger/unilog/python/unilog/listeners.py.md|__aiter__]] (function: belongs_to) — *Async Iterator protocol*
- [[universal-logger/universal-logger/unilog/python/unilog/listeners.py.md|__anext__]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/unilog/listeners.py.md|__del__]] (function: belongs_to) — *Destruction guard to prevent memory leaks by unhooking from parent*
- [[universal-logger/universal-logger/unilog/python/unilog/listeners.py.md|__init__]] (function: belongs_to) — *Initialization*
- [[universal-logger/universal-logger/unilog/python/unilog/listeners.py.md|_put]] (function: belongs_to) — *Internal thread-safe bridge to push data from Go into the Python event loop*
<!-- SYNC:END -->
