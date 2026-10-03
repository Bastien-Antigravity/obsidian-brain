

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py`.

> **Essential Process**:
> Unified orchestrator for indexing and hybrid querying in the RAG Engine. Acts as the central point of contact for external consumers (CLI, MCP, Web).

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/joint_audit_purger.py.md|GLOBAL_EXCLUDES]] (constant: calls) — *Sync with RAG Engine's GLOBAL_EXCLUDES*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|is_path_excluded]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|check_alignment]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|clear]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|get_all]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|get_linked_docs]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|get_parent]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|multi_tenant_proxy.py]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|reset_registry]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|reset_store]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/alignment.py.md|alignment.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|enrich_pending]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|enricher.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|start_background_loop]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|stop_background_loop]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/indexing_pipeline.py.md|build_full_index]] (function: calls) — *Scans the entire workspace and performs a comprehensive re-index.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/indexing_pipeline.py.md|indexing_pipeline.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/indexing_pipeline.py.md|process_file]] (function: calls) — *Processes and indexes a single file based on its path.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/parent_store.py.md|parent_store.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/query_engine.py.md|query_engine.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/query_expander.py.md|expand_query]] (function: calls) — *Expands a given query into multiple semantic variants.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/query_expander.py.md|query_expander.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|vector_store.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/watcher.py.md|start]] (function: calls) — *Starts the background file watch loop.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/watcher.py.md|stop]] (function: calls) — *Stops the background file watch loop.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/watcher.py.md|watcher.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/request.py.md|MQueryRequest]] (class: calls) — *Encapsulates search parameters.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/request.py.md|request.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/result.py.md|result.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|load_pending_from_store]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|set_stores]] (function: calls) — *Late-bind stores (called by the facade factory after construction).*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|_batch_flusher_loop]] (function: calls) — *Background task that aggregates FileResults and flushes them in batches.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|_load_inventory_and_map_notes]] (function: calls) — *Loads inventory.json and builds a mapping of note stem names to file paths.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/seed/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|SeedService]] (class: calls) — *Manages exporting and importing sanitized seed data for the RAG Engine.*

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|runners.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|RAGFacade]] (class: belongs_to) — *Main entry point and orchestrator for the RAG engine.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|_hydrate_chunk]] (function: belongs_to) — *Internal helper for concurrent hydration.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|analyzer]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|build_index]] (function: belongs_to) — *Builds full index asynchronously.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|enrich_now]] (function: belongs_to) — *Triggers an immediate enrichment pass on all pending chunks.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|enrich_pending_records]] (function: belongs_to) — *Standalone run to enrich pending/unenriched records loaded from database.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|export_seed]] (function: belongs_to) — *Exports database tables in schema to a sanitized seed package.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|get_brain_stats]] (function: belongs_to) — *Calculates metadata stats while respecting squad firewalls.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|get_web_root]] (function: belongs_to) — *Returns path to the dashboard static files.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|import_seed]] (function: belongs_to) — *Imports seed datasets from JSONL.gz into PostgreSQL schema.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|index_directory]] (function: belongs_to) — *Walks and indexes a specific directory or microservice repository path.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|index_file]] (function: belongs_to) — *Orchestrates file processing asynchronously.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|is_database_empty]] (function: belongs_to) — *Checks whether database has 0 indexed records.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|lexical_store]] (function: belongs_to) — *Provides direct access to lexical store (delegates to query_engine or pipeline).*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|query]] (function: belongs_to) — *Hybrid search with context hydration asynchronously.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|reset_index]] (function: belongs_to) — *Resets all storage layers for a clean rebuild.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|sem_process]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|start_enricher_loop]] (function: belongs_to) — *Starts the background LLM enrichment loop. Safe to call at server start.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|start_watcher]] (function: belongs_to) — *Starts background file monitoring.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|stop_enricher_loop]] (function: belongs_to) — *Stops the background LLM enrichment loop gracefully.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|stop_watcher]] (function: belongs_to) — *Stops background file monitoring.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|sync_docs]] (function: belongs_to) — *Orchestrates the synchronization of code-derived documentation.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|workspaces_root]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (calls)
<!-- SYNC:END -->
