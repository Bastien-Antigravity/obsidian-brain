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
Automatically generated mirror for `universal-logger/unilog/python/test_unified_callback.py`.

> **Essential Process**:
> Validation test suite for CGO callback dispatching, testing configuration updates and notification callbacks from Go to Python runtimes.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[universal-logger/universal-logger/unilog/python/unilog/__init__.py.md|__init__.py]] (imports)

### 🔌 Consumers (Inbound)
- [[universal-logger/universal-logger/unilog/python/test_unified_callback.py.md|TestUnifiedCallback]] (class: belongs_to) — *Unified Callback verification (Sync & Async)*
- [[universal-logger/universal-logger/unilog/python/test_unified_callback.py.md|listen_task]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/test_unified_callback.py.md|my_cb]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/test_unified_callback.py.md|notif_cb]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/test_unified_callback.py.md|run_test]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/test_unified_callback.py.md|sync_cb]] (function: belongs_to)
- [[universal-logger/universal-logger/unilog/python/test_unified_callback.py.md|test_async_iterator]] (function: belongs_to) — *Verify that the async iterator correctly marshals data using call_soon_threadsafe*
- [[universal-logger/universal-logger/unilog/python/test_unified_callback.py.md|test_dual_mode]] (function: belongs_to) — *Verify that both sync and async systems can coexist on the same logger session*
- [[universal-logger/universal-logger/unilog/python/test_unified_callback.py.md|test_notification_callback]] (function: belongs_to) — *Verify that local alert notifications triggered from Go reach Python callbacks*
- [[universal-logger/universal-logger/unilog/python/test_unified_callback.py.md|test_sync_callback]] (function: belongs_to) — *Verify that traditional sync callbacks triggered from Go reach Python*
<!-- SYNC:END -->
