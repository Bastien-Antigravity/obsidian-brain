

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py`.

> **Essential Process**:
> Background file system watcher that monitors for changes and triggers re-indexing. Ensures the RAG index remains synchronized with the workspace state.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/joint_audit_purger.py.md|GLOBAL_EXCLUDES]] (constant: calls) — *Sync with RAG Engine's GLOBAL_EXCLUDES*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_watch_settings]] (function: calls) — *Resolves filesystem watcher configuration.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/watcher.py.md|Watcher]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/watcher.py.md|watcher.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|UnifiedWatcher]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|_debounced_runner]] (function: belongs_to) — *Runner coroutine that sleeps for 500ms before triggering the index pipeline*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|_handle_event]] (function: belongs_to) — *Filters and dispatches file system events to the callback with 500ms debouncing.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|on_created]] (function: belongs_to) — *Triggered when a file is created.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|on_modified]] (function: belongs_to) — *Triggered when a file is modified.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|start]] (function: belongs_to) — *Starts the background file watch loop.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|stop]] (function: belongs_to) — *Stops the background file watch loop.*
<!-- SYNC:END -->
