---
source: obsidian-brain/09-RAG-Engine/src/facade/__init__.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.175740
---

# Mirror: __init__.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/facade/__init__.py`.

> **Essential Process**:
> Factory and entrypoint for the RAG facade layer of the Obsidian Brain RAG Engine. Coordinates the initialization of all internal services (VectorStore, LexicalStore, Pipeline, etc.).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|MultiTenantAlignmentServiceProxy]] (class: calls) — *Routes self-healing alignment operations to schema-specific PostgresAlignmentService instances.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|MultiTenantGraphDBProxy]] (class: calls) — *Routes relational graph schema mappings to schema-specific PostgresGraphDB instances.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|MultiTenantLexicalStoreProxy]] (class: calls) — *Routes lexical store operations to schema-specific PostgresLexicalStore instances.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|MultiTenantParentStoreProxy]] (class: calls) — *Routes parent raw content storage operations to schema-specific PostgresParentStore instances.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|MultiTenantVectorStoreProxy]] (class: calls) — *Routes vector store operations to schema-specific PgVectorStore instances.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|multi_tenant_proxy.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|multi_tenant_proxy.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|RAGFacade]] (class: calls) — *Main entry point and orchestrator for the RAG engine.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|PostgresAlignmentService]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|postgres_alignment.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|CodeDocSynchronizer]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|synchronizer.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|CodeEngineAnalyzerBridge]] (class: calls) — *Bridge analyzer that uses CodeEngine's AST-based parsers for structural chunking.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/code_analyzer.py.md|code_analyzer.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/markdown_analyzer.py.md|MarkdownAnalyzer]] (class: calls) — *Hierarchical header-based chunker for Markdown.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/markdown_analyzer.py.md|markdown_analyzer.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/text_analyzer.py.md|TextAnalyzer]] (class: calls) — *Handles chunking for generic text and configuration files.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/text_analyzer.py.md|text_analyzer.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|CodebaseAnalyzer]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|LLMEnricher]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/enricher/llm_enricher.py.md|llm_enricher.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|PostgresGraphDB]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|postgres_db.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|StandardIndexingPipeline]] (class: calls) — *Coordinates the multi-stage indexing process for files.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|PostgresLexicalStore]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|postgres.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/llm/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/llm/__init__.py.md|get_llm_client]] (function: calls) — *Factory to retrieve configured LLMClient.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|PostgresParentStore]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|postgres.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|GraphRAGQueryEngine]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/graph_rag.py.md|graph_rag.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_engine/hybrid.py.md|hybrid.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|LLMQueryExpander]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/query_expander/llm_expander.py.md|llm_expander.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|PgVectorStore]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|pgvector.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|UnifiedWatcher]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|file_watcher.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (imports)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|runners.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/runners.py.md|runners.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|get_rag_facade]] (function: belongs_to) — *Factory to construct and return a singleton RAGFacade instance.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|patched_get_language]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|patched_get_parser]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
