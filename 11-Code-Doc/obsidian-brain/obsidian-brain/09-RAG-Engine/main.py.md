

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/main.py`.

> **Essential Process**:
> Main CLI entrypoint for the Obsidian Brain RAG Engine. Coordinates indexing, semantic search (MCP), background watching, and visualizer dashboard. This file acts as a transparent dashboard containing the CLI parameter definitions and dispatcher handlers for visibility.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py.md|print_help]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|RAGControllerImpl]] (class: calls) — *Standardized controller implementation for RAG operations.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|build_index]] (function: calls) — *Triggers index rebuild.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|controller.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|index_directory]] (function: calls) — *Indexes directory/microservice repository.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|index_file]] (function: calls) — *Indexes a single file.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|reset_index]] (function: calls) — *Resets all database layers.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|sync_docs]] (function: calls) — *Syncs codebase documentation mirrors.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|runners.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|start_visualizer]] (function: calls) — *Helper to start visualizer.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|start_watcher]] (function: calls) — *Helper to start watcher.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/server.py.md|server.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|get_rag_facade]] (function: calls) — *Factory to construct and return a singleton RAGFacade instance.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|enrich_pending_records]] (function: calls) — *Standalone run to enrich pending/unenriched records loaded from database.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|start_enricher_loop]] (function: calls) — *Starts the background LLM enrichment loop. Safe to call at server start.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|stop_enricher_loop]] (function: calls) — *Stops the background LLM enrichment loop gracefully.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|stop_watcher]] (function: calls) — *Stops background file monitoring.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|service.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|start_grpc_server]] (function: calls) — *Initializes and starts the asynchronous RAG Control gRPC server.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|SetupTelegram]] (function: calls) — *Initializes dynamic Tele-Remote client, binds updates, and registers exit handlers.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|manager.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/brain_health_audit.py.md|brain_health_audit.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/check_coherence.py.md|check_coherence.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/ensure_frontmatter.py.md|ensure_frontmatter.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/validate_compliance.py.md|validate_compliance.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/extraction/persona_extractor.py.md|persona_extractor.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/build_inventory.py.md|build_inventory.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|fleet_commander.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_refresh.py.md|fleet_refresh.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/improved_transformer.py.md|improved_transformer.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lifecycle/scaffold_microservice.py.md|scaffold_microservice.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lifecycle/scaffold_new_brain.py.md|scaffold_new_brain.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/knowledge_compressor.py.md|knowledge_compressor.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|_init_facade_threadsafe]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|_run_server]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|_target]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|run]] (function: belongs_to) — *Dispatch execution based on parsed CLI arguments.*
<!-- SYNC:END -->
