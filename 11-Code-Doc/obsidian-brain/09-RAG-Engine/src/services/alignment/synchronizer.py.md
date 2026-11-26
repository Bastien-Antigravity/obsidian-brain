

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py`.

> **Essential Process**:
> Proactive synchronizer that ensures Obsidian mirror docs stay in sync with source code. Handles skeleton generation, architectural context injection, and tag extraction.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|get_workspace_registry]] (function: calls) — *Returns the process-wide WorkspaceRegistry singleton.*
- [[obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|resolve_brain_for_path]] (function: calls) — *Resolves the owning brain_id for an absolute filesystem path via deepest prefix match.*
- [[obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|resolve_codedoc_root]] (function: calls) — *Resolves the 11-Code-Doc mirror directory for the given brain_id.*
- [[obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|resolve_workspace_root]] (function: calls) — *Resolves the workspace root directory for the given brain_id (defaults to primary).*
- [[obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|workspace_registry.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/interfaces/alignment.py.md|alignment.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|get_all_drifted]] (function: calls) — *Returns a list of all documentation notes that are currently out of sync with code.*
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|postgres_alignment.py]] (same_package)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|register_links_batch]] (function: calls) — *Registers multiple links in a single PG batch.*
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|CodeDocSynchronizer]] (class: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|_cleanup]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|_cleanup_orphans]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|_cleanup_single_file_orphan]] (function: belongs_to) — *Cleans up ONLY the mirror for a specific single file if that source file has been deleted.*
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|_create_skeleton]] (function: belongs_to) — *Generates the initial mirror file structure.*
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|_extract_essential_process]] (function: belongs_to) — *Extracts the ESSENTIAL PROCESS text from a source file's Triple-Block header.*
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|_format_context_block]] (function: belongs_to) — *Generates the Markdown context section.*
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|_get_symbol_doc]] (function: belongs_to) — *Lazily extracts a 1-line doc comment or summary intent for a symbol node.*
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|_inject_context]] (function: belongs_to) — *Safely replaces the content between SYNC markers and updates Description if essential_process is provided.*
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|_process_file]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|_read]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|_read_file]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|_resolve_source_path]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|_run_sync_inner]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|_scan_notes]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|_walk_and_reconcile]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|_write]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|format_edge]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|run_sync]] (function: belongs_to)
<!-- SYNC:END -->
