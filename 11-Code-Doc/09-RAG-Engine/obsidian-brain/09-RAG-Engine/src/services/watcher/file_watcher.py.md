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
> Background file system watcher that monitors all registered workspaces for changes and triggers re-indexing. Ensures the RAG index remains synchronized across primary and domain workspace roots.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|GLOBAL_EXCLUDES]] (constant: calls) — *Sync with RAG Engine's GLOBAL_EXCLUDES*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_watch_settings]] (function: calls) — *Resolves filesystem watcher configuration.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|get_workspace_registry]] (function: calls) — *Returns the process-wide WorkspaceRegistry singleton.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|list_workspaces]] (function: calls) — *Returns all registered workspaces serialized as string path dictionaries.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|resolve_brain_for_path]] (function: calls) — *Resolves the owning brain_id for an absolute filesystem path via deepest prefix match.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|resolve_workspace_root]] (function: calls) — *Resolves the workspace root directory for the given brain_id (defaults to primary).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|workspace_registry.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/watcher.py.md|Watcher]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/watcher.py.md|watcher.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|rest_handler.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|UnifiedWatcher]] (class: belongs_to) — *Observer-based file watcher that monitors all registered workspaces.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|_accepts_brain_id]] (function: belongs_to) — *Checks whether a callback explicitly declares a 'brain_id' keyword parameter.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|_debounced_runner]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|_handle_delete_event]] (function: belongs_to) — *Filters and dispatches file deletion events to the delete callback.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|_handle_event]] (function: belongs_to) — *Filters and dispatches file system events to the callback with 500ms debouncing.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|_invoke_sync_callback]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|_resolve_event_context]] (function: belongs_to) — *Resolves owning brain_id and workspace-relative path parts for a filesystem event.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|on_created]] (function: belongs_to) — *Triggered when a file is created.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|on_deleted]] (function: belongs_to) — *Triggered when a file is deleted.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|on_modified]] (function: belongs_to) — *Triggered when a file is modified.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|on_moved]] (function: belongs_to) — *Triggered when a file is moved or renamed.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|start]] (function: belongs_to) — *Starts the background file watch loop across all registered workspaces.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|stop]] (function: belongs_to) — *Stops the background file watch loop.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|unwatch_workspace]] (function: belongs_to) — *Detaches the watchdog observer for a domain workspace.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|watch_workspace]] (function: belongs_to) — *Schedules a recursive watchdog observer on the given workspace root.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
