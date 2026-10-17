---
source: obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-13T19:05:46.107195
---

# Mirror: pg_pool.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py`.

> **Essential Process**:
> Shared PostgreSQL connection pooling and schema name resolver for RAG Engine services. Ensures single-instance connection pooling to prevent DB port exhaustion.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_db_settings]] (function: calls) — *Resolves database connection settings with decrypted credentials and target RAG database.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|multi_tenant_proxy.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/multi_tenant_proxy.py.md|multi_tenant_proxy.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|postgres_alignment.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|postgres_alignment.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|postgres_db.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|postgres_db.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|db_config.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|db_config.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|postgres_db.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|postgres_db.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|postgres.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|postgres.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/fastmcp.py.md|fastmcp.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|postgres.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|postgres.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|seed_service.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|seed_service.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|pgvector.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|pgvector.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|HAS_POSTGRES]] (constant: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|close_pg_pool]] (function: belongs_to) — *Closes all connections in the shared pool.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_pg_pool]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_schema_name]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
