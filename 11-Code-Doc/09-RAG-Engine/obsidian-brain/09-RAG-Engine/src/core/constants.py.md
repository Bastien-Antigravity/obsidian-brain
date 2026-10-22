---
source: obsidian-brain/09-RAG-Engine/src/core/constants.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-13T19:05:46.292390
---

# Mirror: constants.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/core/constants.py`.

> **Essential Process**:
> Shared constants and configuration anchors for the 09-RAG-Engine module. Provides the single source of truth for workspace path resolution, firewall exclusion rules, supported file extensions, and the access control matrix.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|GLOBAL_EXCLUDES]] (constant: calls) — *Sync with RAG Engine's GLOBAL_EXCLUDES*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/access_matrix.py.md|access_matrix.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|is_path_excluded]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|postgres_alignment.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|synchronizer.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|seed_service.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|file_watcher.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
