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
Automatically generated mirror for `universal-logger/unilog/python/unilog/models.py`.

> **Essential Process**:
> Data models, enumerations, and type definitions representing log levels, metadata containers, and FFI callback signatures for UniLog.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/unilog/python/unilog/__init__.py.md|__init__.py]] (imports)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (calls)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (imports)
- [[universal-logger/universal-logger/unilog/python/unilog/facade.py.md|facade.py]] (same_package)
- [[universal-logger/universal-logger/unilog/python/unilog/models.py.md|LogLevel]] (class: belongs_to) — *Log Levels*
- [[universal-logger/universal-logger/unilog/python/unilog/models.py.md|from_str]] (function: belongs_to) — *Helper to convert string-based levels from config to enum*
<!-- SYNC:END -->
