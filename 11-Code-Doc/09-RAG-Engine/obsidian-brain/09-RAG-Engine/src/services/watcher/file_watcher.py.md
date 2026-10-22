---
source: obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.247164
---

# Mirror: file_watcher.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py`.

> **Essential Process**:
> Background file system watcher that monitors for changes and triggers re-indexing. Ensures the RAG index remains synchronized with the workspace state.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|GLOBAL_EXCLUDES]] (constant: calls) — *Sync with RAG Engine's GLOBAL_EXCLUDES*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_watch_settings]] (function: calls) — *Resolves filesystem watcher configuration.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/watcher.py.md|Watcher]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/watcher.py.md|watcher.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|UnifiedWatcher]] (class: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|_debounced_runner]] (function: belongs_to) — *Runner coroutine that sleeps for 500ms before triggering the index pipeline*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|_handle_delete_event]] (function: belongs_to) — *Filters and dispatches file deletion events to the delete callback.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|_handle_event]] (function: belongs_to) — *Filters and dispatches file system events to the callback with 500ms debouncing.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|on_created]] (function: belongs_to) — *Triggered when a file is created.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|on_deleted]] (function: belongs_to) — *Triggered when a file is deleted.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|on_modified]] (function: belongs_to) — *Triggered when a file is modified.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|on_moved]] (function: belongs_to) — *Triggered when a file is moved or renamed.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|start]] (function: belongs_to) — *Starts the background file watch loop.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|stop]] (function: belongs_to) — *Stops the background file watch loop.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
