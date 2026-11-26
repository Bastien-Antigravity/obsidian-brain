

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/web/server.py`.

> **Essential Process**:
> Unified FastAPI web server for RAG Dashboard and Codebase Visualizer. Pure static frontend (SPA) approach using index.html and JSON APIs.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/09-RAG-Engine/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_db_settings]] (function: calls) — *Resolves database connection settings with decrypted credentials and target RAG database.*
- [[obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|RAGControllerImpl]] (class: calls) — *Standardized controller implementation for RAG operations.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|controller.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|get_brain_stats]] (function: calls) — *Calculates stats respecting active squad firewalls.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|index_directory]] (function: calls) — *Indexes directory/microservice repository.*
- [[obsidian-brain/09-RAG-Engine/src/core/controller.py.md|query]] (function: calls) — *Queries the RAG engine across partitions and returns serializable results.*
- [[obsidian-brain/09-RAG-Engine/src/core/server.py.md|server.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|get_rag_facade]] (function: calls) — *Factory to construct and return a singleton RAGFacade instance.*
- [[obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|build_rag_engine_contracts]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/rest/contracts.py.md|contracts.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|RAGRESTHandler]] (class: calls) — *REST API Handler mapping config and status queries to RAGController.*
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|register_routes]] (function: calls) — *Registers the REST routes to the FastAPI application mux.*
- [[obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|rest_handler.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|mount_to_app]] (function: calls) — *Mount the SSE transport endpoints on an existing FastAPI application.*

### 🔌 Consumers (Inbound)
- [[obsidian-brain/09-RAG-Engine/src/core/runners.py.md|runners.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/core/runners.py.md|runners.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|synchronizer.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|seed_service.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|InterceptHandler]] (class: belongs_to) — *Custom logging handler that intercepts standard library logs and routes them to our UniLogger.*
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|SafeQueueWriter]] (class: belongs_to) — *Thread-safe stdout redirector that prevents recursion and strips log prefixes for the UI.*
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|_STATIC_DIR]] (constant: belongs_to) — *Mount static files at / using absolute path*
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|_register_mfe_with_web_interface]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|_setup_uvicorn_logging]] (function: belongs_to) — *Reconfigures Uvicorn logging to use our standardized UniLogger via a Handler.*
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|_strip_prefix]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|catch_all]] (function: belongs_to) — *Fallback route to serve static files.*
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|emit]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|event_generator]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|flush]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|get_config]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|get_rag_engine_contracts]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|get_rag_stats]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|index_directory_api]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|open_in_ide]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|rag_search]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|serve_codebase_graph_json]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|serve_source]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|sse_reload_graph]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|start_async_server]] (function: belongs_to) — *Starts the uvicorn server for FastAPI with harmonized logging.*
- [[obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: belongs_to)
<!-- SYNC:END -->
