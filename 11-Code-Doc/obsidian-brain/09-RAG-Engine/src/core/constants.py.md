

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/core/constants.py`.

> **Essential Process**:
> Shared constants and configuration anchors for the 09-RAG-Engine module. Provides the single source of truth for workspace path resolution, firewall exclusion rules, supported file extensions, and the access control matrix.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/09-RAG-Engine/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/access_matrix.py.md|access_matrix.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|get_workspace_registry]] (function: calls) — *Returns the process-wide WorkspaceRegistry singleton.*
- [[obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|list_workspaces]] (function: calls) — *Returns all registered workspaces serialized as string path dictionaries.*
- [[obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|workspace_registry.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|workspace_registry.py]] (same_package)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/constants.py.md|has_meaningful_codedoc_notes]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/core/constants.py.md|is_path_excluded]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|workspace_registry.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|postgres_alignment.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|synchronizer.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|seed_service.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|file_watcher.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|file_watcher.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->
