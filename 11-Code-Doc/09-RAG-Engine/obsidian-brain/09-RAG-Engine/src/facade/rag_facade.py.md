---
source: obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.150709
---

# Mirror: rag_facade.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py`.

> **Essential Process**:
> Unified orchestrator for indexing and hybrid querying in the RAG Engine. Acts as the central point of contact for external consumers (CLI, MCP, Web).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|GLOBAL_EXCLUDES]] (constant: calls) — *Sync with RAG Engine's GLOBAL_EXCLUDES*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|is_path_excluded]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|add_documents]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|check_alignment]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|clear]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|get_all]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|get_linked_docs]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|get_parent]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|multi_tenant_proxy.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|reset_registry]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|reset_store]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/alignment.py.md|alignment.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|enrich_pending]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|enricher.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|start_background_loop]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/enricher.py.md|stop_background_loop]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/indexing_pipeline.py.md|build_full_index]] (function: calls) — *Scans the entire workspace and performs a comprehensive re-index.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/indexing_pipeline.py.md|indexing_pipeline.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/indexing_pipeline.py.md|process_file]] (function: calls) — *Processes and indexes a single file based on its path.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/parent_store.py.md|parent_store.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/query_engine.py.md|query_engine.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/query_expander.py.md|expand_query]] (function: calls) — *Expands a given query into multiple semantic variants.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/query_expander.py.md|query_expander.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|vector_store.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/watcher.py.md|start]] (function: calls) — *Starts the background file watch loop.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/watcher.py.md|stop]] (function: calls) — *Stops the background file watch loop.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/watcher.py.md|watcher.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/models/metadata.py.md|MChunkMetadata]] (class: calls) — *Normalized metadata for a logical chunk.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/models/metadata.py.md|metadata.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/models/request.py.md|MQueryRequest]] (class: calls) — *Encapsulates search parameters.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/models/request.py.md|request.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/models/result.py.md|result.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/markdown_analyzer.py.md|MarkdownAnalyzer]] (class: calls) — *Hierarchical header-based chunker for Markdown.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/markdown_analyzer.py.md|analyze]] (function: calls) — *Analyzes markdown files and splits them into logical chunks by headers.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/markdown_analyzer.py.md|markdown_analyzer.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|load_pending_from_store]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|set_stores]] (function: calls) — *Late-bind stores (called by the facade factory after construction).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|_batch_flusher_loop]] (function: calls) — *Background task that aggregates FileResults and flushes them in batches.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|_load_inventory_and_map_notes]] (function: calls) — *Loads inventory.json and builds a mapping of note stem names to file paths.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|SeedService]] (class: calls) — *Manages exporting and importing sanitized seed data for the RAG Engine.*
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|debug]] (function: calls)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|RAGFacade]] (class: belongs_to) — *Main entry point and orchestrator for the RAG engine.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|_hydrate_chunk]] (function: belongs_to) — *Internal helper for concurrent hydration.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|analyzer]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|build_index]] (function: belongs_to) — *Builds full index asynchronously.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|delete_by_brain]] (function: belongs_to) — *Atomic unmerge/purge of all embeddings, lexical entries, and parent records for a brain partition.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|delete_file]] (function: belongs_to) — *Orchestrates real-time removal of deleted file records asynchronously.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|enrich_now]] (function: belongs_to) — *Triggers an immediate enrichment pass on all pending chunks.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|enrich_pending_records]] (function: belongs_to) — *Standalone run to enrich pending/unenriched records loaded from database.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|export_seed]] (function: belongs_to) — *Exports database tables in schema to a sanitized seed package.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|get_brain_stats]] (function: belongs_to) — *Calculates metadata stats while respecting squad firewalls.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|get_web_root]] (function: belongs_to) — *Returns path to the dashboard static files.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|import_seed]] (function: belongs_to) — *Imports seed datasets from JSONL.gz into PostgreSQL schema.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|index_directory]] (function: belongs_to) — *Walks and indexes a specific directory or microservice repository path.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|index_document_content]] (function: belongs_to) — *Ingests and embeds a document directly into the specified brain partition.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|index_file]] (function: belongs_to) — *Orchestrates file processing asynchronously.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|is_database_empty]] (function: belongs_to) — *Checks whether database has 0 indexed records.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|lexical_store]] (function: belongs_to) — *Provides direct access to lexical store (delegates to query_engine or pipeline).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|query]] (function: belongs_to) — *Hybrid search with context hydration asynchronously.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|reset_index]] (function: belongs_to) — *Resets all storage layers for a clean rebuild.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|sem_process]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|start_enricher_loop]] (function: belongs_to) — *Starts the background LLM enrichment loop. Safe to call at server start.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|start_watcher]] (function: belongs_to) — *Starts background file monitoring.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|stop_enricher_loop]] (function: belongs_to) — *Stops the background LLM enrichment loop gracefully.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|stop_watcher]] (function: belongs_to) — *Stops background file monitoring.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|sync_docs]] (function: belongs_to) — *Orchestrates the synchronization of code-derived documentation.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|workspaces_root]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
