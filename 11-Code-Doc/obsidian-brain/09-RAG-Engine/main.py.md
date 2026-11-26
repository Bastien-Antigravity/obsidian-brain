

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/main.py`.

> **Essential Process**:
> Main CLI entrypoint for the Obsidian Brain RAG Engine. Coordinates workspace indexing, semantic search (FastMCP SSE), background file watching, interactive visualizer dashboard, documentation synchronization, and database seed tooling.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/09-RAG-Engine/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|RAGControllerImpl]] (class: calls) — *Standardized controller implementation for RAG operations.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|build_index]] (function: calls) — *Triggers index rebuild.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|controller.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|index_directory]] (function: calls) — *Indexes directory/microservice repository.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|index_file]] (function: calls) — *Indexes a single file.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|reset_index]] (function: calls) — *Resets all database layers.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|sync_docs]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/core/runners.py.md|runners.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/runners.py.md|start_visualizer]] (function: calls) — *Helper to start visualizer.*
- [[obsidian-brain/09-RAG-Engine/src/core/server.py.md|server.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|get_rag_facade]] (function: calls) — *Factory to construct and return a singleton RAGFacade instance.*
- [[obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|enrich_pending_records]] (function: calls) — *Standalone run to enrich pending/unenriched records loaded from database.*
- [[obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|start_enricher_loop]] (function: calls) — *Starts the background LLM enrichment loop. Safe to call at server start.*
- [[obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|start_watcher]] (function: calls) — *Starts background file monitoring.*
- [[obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|stop_enricher_loop]] (function: calls) — *Stops the background LLM enrichment loop gracefully.*
- [[obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|stop_watcher]] (function: calls) — *Stops background file monitoring.*
- [[obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|service.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|start_grpc_server]] (function: calls) — *Initializes and starts the asynchronous RAG Control gRPC server.*
- [[obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|build_rag_mcp_contracts]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|contracts.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|SetupTelegram]] (function: calls) — *Initializes dynamic Tele-Remote client, binds updates, and registers exit handlers.*
- [[obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|manager.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/09-RAG-Engine/main.py.md|_init_facade_threadsafe]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/main.py.md|_run_server]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/main.py.md|_safe_stop_enricher]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/main.py.md|_target]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/main.py.md|run]] (function: belongs_to) — *Dispatch execution based on parsed CLI arguments.*
<!-- SYNC:END -->
