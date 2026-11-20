---
source: obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-11-20T08:30:16.882958
---

# Mirror: workspace_registry.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py`.

> **Essential Process**:
> Multi-workspace registry for the 09-RAG-Engine supporting primary and domain brains. Auto-discovers domain workspaces from environment variables and persisted YAML config, and resolves workspace, vault, and 11-Code-Doc mirror roots per brain_id.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|WorkspaceRegistry]] (class: belongs_to) — *Thread-safe registry mapping brain_id partitions to filesystem workspace and vault roots.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|_discover_from_extra_dir]] (function: belongs_to) — *Scans EXTRA_WORKSPACES_DIR immediate subdirectories for domain vaults.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|_discover_from_extra_env]] (function: belongs_to) — *Parses EXTRA_WORKSPACES comma- or colon-separated entries ('brain_id=/path' or '/path').*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|_discover_workspaces]] (function: belongs_to) — *Discovers domain workspaces from env vars and persisted YAML configuration.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|_infer_vault_path]] (function: belongs_to) — *Resolves the Obsidian vault root inside a domain workspace directory.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|_load_persisted_config]] (function: belongs_to) — *Loads persisted domain workspace entries from workspaces.yaml if present.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|_persist_config]] (function: belongs_to) — *Persists extra workspace registrations to workspaces.yaml when writable.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|_set_workspace_internal]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|_split_extra_workspaces]] (function: belongs_to) — *Splits EXTRA_WORKSPACES on ',' and ':' without breaking Windows drive letters (e.g. C:\).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|_translate_docker_path]] (function: belongs_to) — *Translates host-side workspace paths to container mount paths when running in Docker.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|get_workspace_registry]] (function: belongs_to) — *Returns the process-wide WorkspaceRegistry singleton.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|list_workspaces]] (function: belongs_to) — *Returns all registered workspaces serialized as string path dictionaries.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|register_workspace]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|resolve_brain_for_path]] (function: belongs_to) — *Resolves the owning brain_id for an absolute filesystem path via deepest prefix match.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|resolve_codedoc_root]] (function: belongs_to) — *Resolves the 11-Code-Doc mirror directory for the given brain_id.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|resolve_vault_root]] (function: belongs_to) — *Resolves the Obsidian vault root directory for the given brain_id (defaults to primary).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|resolve_workspace_root]] (function: belongs_to) — *Resolves the workspace root directory for the given brain_id (defaults to primary).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|unregister_workspace]] (function: belongs_to) — *Unregisters a domain workspace. Refuses to unregister primary 'obsidian-brain'.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|rest_handler.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|rest_handler.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|synchronizer.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|synchronizer.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|file_watcher.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|file_watcher.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
