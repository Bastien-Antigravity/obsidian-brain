---
source: obsidian-brain/09-RAG-Engine/src/web/server.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.019813
---

# Mirror: server.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/web/server.py`.

> **Essential Process**:
> Unified FastAPI web server for RAG Dashboard and Codebase Visualizer. Pure static frontend (SPA) approach using index.html and JSON APIs.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|GLOBAL_EXCLUDES]] (constant: calls) — *Sync with RAG Engine's GLOBAL_EXCLUDES*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_db_settings]] (function: calls) — *Resolves database connection settings with decrypted credentials and target RAG database.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|RAGControllerImpl]] (class: calls) — *Standardized controller implementation for RAG operations.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|controller.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|get_brain_stats]] (function: calls) — *Calculates stats respecting active squad firewalls.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|index_directory]] (function: calls) — *Indexes directory/microservice repository.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|query]] (function: calls) — *Queries the RAG engine across partitions and returns serializable results.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/server.py.md|server.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|RAGRESTHandler]] (class: calls) — *REST API Handler mapping config and status queries to RAGController.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|register_routes]] (function: calls) — *Registers the REST routes to the FastAPI application mux.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/rest/rest_handler.py.md|rest_handler.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|mount_to_app]] (function: calls) — *Mount the SSE transport endpoints on an existing FastAPI application.*

### 🔌 Consumers (Inbound)
- [[04-Rapid-Prototyping/obsidian-brain/04-Rapid-Prototyping/src/archive.py.md|archive.py]] (calls)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/01-Fleet-Action-Plans/archive.py.md|archive.py]] (calls)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|archive.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/audit_ports.py.md|audit_ports.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|check_coherence.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|hardening_yaml.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|agent_dispatcher.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/switch_mode.py.md|switch_mode.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py.md|persona_extractor.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/convert_agents.py.md|convert_agents.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_init_update.py.md|fleet_init_update.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|sovereignty.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/init_new_brain.py.md|init_new_brain.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/install_git_hooks.py.md|install_git_hooks.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|scaffold_microservice.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|scaffold_new_brain.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|joint_audit_purger.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/knowledge_compressor.py.md|knowledge_compressor.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/maintenance_skill.py.md|maintenance_skill.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|runners.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|runners.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|synchronizer.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|seed_service.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|InterceptHandler]] (class: belongs_to) — *Custom logging handler that intercepts standard library logs and routes them to our UniLogger.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|SafeQueueWriter]] (class: belongs_to) — *Thread-safe stdout redirector that prevents recursion and strips log prefixes for the UI.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|_STATIC_DIR]] (constant: belongs_to) — *Mount static files at / using absolute path*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|_register_mfe_with_web_interface]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|_setup_uvicorn_logging]] (function: belongs_to) — *Reconfigures Uvicorn logging to use our standardized UniLogger via a Handler.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|_strip_prefix]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|catch_all]] (function: belongs_to) — *Fallback route to serve static files.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|do_register]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|emit]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|event_generator]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|flush]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|get_config]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|get_rag_stats]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|index_directory_api]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|open_in_ide]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|rag_search]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|serve_codebase_graph_json]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|serve_source]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|sse_reload_graph]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|start_async_server]] (function: belongs_to) — *Starts the uvicorn server for FastAPI with harmonized logging.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
