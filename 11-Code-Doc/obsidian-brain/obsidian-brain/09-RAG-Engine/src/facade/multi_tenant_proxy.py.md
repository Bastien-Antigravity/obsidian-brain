

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py`.

> **Essential Process**:
> Multi-tenant storage proxies that dynamically route indexing, querying, and deletion requests to repository-specific database schemas in PostgreSQL mode.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/alignment.py.md|AlignmentService]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/alignment.py.md|alignment.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/graph_db.py.md|GraphDB]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/graph_db.py.md|graph_db.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/lexical_store.py.md|LexicalStore]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/lexical_store.py.md|lexical_store.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/parent_store.py.md|ParentStore]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/parent_store.py.md|parent_store.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|VectorStore]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|vector_store.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/models/metadata.py.md|metadata.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (same_package)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|MultiTenantAlignmentServiceProxy]] (class: belongs_to) — *Routes self-healing alignment operations to schema-specific PostgresAlignmentService instances.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|MultiTenantGraphDBProxy]] (class: belongs_to) — *Routes relational graph schema mappings to schema-specific PostgresGraphDB instances.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|MultiTenantLexicalStoreProxy]] (class: belongs_to) — *Routes lexical store operations to schema-specific PostgresLexicalStore instances.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|MultiTenantParentStoreProxy]] (class: belongs_to) — *Routes parent raw content storage operations to schema-specific PostgresParentStore instances.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|MultiTenantVectorStoreProxy]] (class: belongs_to) — *Routes vector store operations to schema-specific PgVectorStore instances.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|_get_active_schemas]] (function: belongs_to) — *Retrieves all active database schemas with 30s TTL caching.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|_get_db]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|_get_service]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|_get_store]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|_resolve_schema]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|_resolve_schema_from_id]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|add_documents]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|check_alignment]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|clear]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|close]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|delete_by_source]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|export_unified_graph]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|find_path]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|get_all]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|get_all_drifted]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|get_all_file_hashes]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|get_cached_active_schemas]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|get_dead_links]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|get_drift_details]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|get_linked_code]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|get_linked_docs]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|get_parent]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|insert_edge]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|insert_node]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|is_file_changed]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|query]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|register_active_schema]] (function: belongs_to) — *Dynamically register a newly accessed or created schema in the active schema cache.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|register_link]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|register_links_batch]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|remove_edges_by_source_or_type]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|remove_node]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|reset_registry]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|reset_store]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|set_bulk_mode]] (function: belongs_to) — *Propagates bulk ingestion mode across active schema stores.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|store_parent]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|store_parents_batch]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|traverse_neighborhood]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|update_file_hash]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (same_package)
<!-- SYNC:END -->
