---
source: obsidian-brain/09-RAG-Engine/main.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-13T19:05:45.425202
---

# Mirror: main.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/main.py`.

> **Essential Process**:
> Main CLI entrypoint for the Obsidian Brain RAG Engine. Coordinates workspace indexing, semantic search (FastMCP SSE), background file watching, interactive visualizer dashboard, documentation synchronization, and database seed tooling.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[04-Rapid-Prototyping/obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py.md|print_help]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|RAGControllerImpl]] (class: calls) — *Standardized controller implementation for RAG operations.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|build_index]] (function: calls) — *Triggers index rebuild.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|controller.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|index_directory]] (function: calls) — *Indexes directory/microservice repository.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|index_file]] (function: calls) — *Indexes a single file.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|reset_index]] (function: calls) — *Resets all database layers.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/controller.py.md|sync_docs]] (function: calls) — *Syncs codebase documentation mirrors.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|runners.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|start_visualizer]] (function: calls) — *Helper to start visualizer.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/server.py.md|server.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|get_rag_facade]] (function: calls) — *Factory to construct and return a singleton RAGFacade instance.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|enrich_pending_records]] (function: calls) — *Standalone run to enrich pending/unenriched records loaded from database.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|start_enricher_loop]] (function: calls) — *Starts the background LLM enrichment loop. Safe to call at server start.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|start_watcher]] (function: calls) — *Starts background file monitoring.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|stop_enricher_loop]] (function: calls) — *Stops the background LLM enrichment loop gracefully.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|stop_watcher]] (function: calls) — *Stops background file monitoring.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|service.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/grpc_control/service.py.md|start_grpc_server]] (function: calls) — *Initializes and starts the asynchronous RAG Control gRPC server.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|SetupTelegram]] (function: calls) — *Initializes dynamic Tele-Remote client, binds updates, and registers exit handlers.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|manager.py]] (imports)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/brain_health_audit.py.md|brain_health_audit.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|check_coherence.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/ensure_frontmatter.py.md|ensure_frontmatter.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|validate_compliance.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py.md|persona_extractor.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/build_inventory.py.md|build_inventory.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|fleet_commander.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_refresh.py.md|fleet_refresh.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|improved_transformer.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|scaffold_microservice.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|scaffold_new_brain.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/knowledge_compressor.py.md|knowledge_compressor.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|_init_facade_threadsafe]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|_run_server]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|_target]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|run]] (function: belongs_to) — *Dispatch execution based on parsed CLI arguments.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
