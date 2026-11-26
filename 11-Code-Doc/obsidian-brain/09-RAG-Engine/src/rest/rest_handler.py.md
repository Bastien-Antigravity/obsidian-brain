

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py`.

> **Essential Process**:
> Provides the REST API endpoints wrapping the RAGController. Supports querying/updating config variables and checking system health via HTTP.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|get_drifted_documents]] (function: calls) — *Retrieves drifted code-to-documentation alignment links.*
- [[obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|get_workspace_registry]] (function: calls) — *Returns the process-wide WorkspaceRegistry singleton.*
- [[obsidian-brain/09-RAG-Engine/src/core/workspace_registry.py.md|workspace_registry.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|index_workspace]] (function: calls) — *Walks and indexes all supported files in a registered domain workspace.*
- [[obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|build_rag_engine_contracts]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|contracts.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|contracts.py]] (same_package)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|unwatch_workspace]] (function: calls) — *Detaches the watchdog observer for a domain workspace.*
- [[obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|watch_workspace]] (function: calls) — *Schedules a recursive watchdog observer on the given workspace root.*

### 🔌 Consumers (Inbound)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|RAGRESTHandler]] (class: belongs_to) — *REST API Handler mapping config and status queries to RAGController.*
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|get_code_dependencies]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|get_config]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|get_contracts]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|get_status]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|index_document]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|list_config]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|list_drifted_documents]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|list_workspaces]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|purge_vault]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|query_rag]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|register_routes]] (function: belongs_to) — *Registers the REST routes to the FastAPI application mux.*
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|register_workspace]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|search_code_symbols]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|set_config]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|sync_code_docs]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|unregister_workspace]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->
