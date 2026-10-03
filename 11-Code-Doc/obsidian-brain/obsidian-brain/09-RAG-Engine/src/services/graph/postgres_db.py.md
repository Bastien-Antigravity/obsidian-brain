

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py`.

> **Essential Process**:
> Graph database utility class for the Unified Knowledge Graph in PostgreSQL. Manages kms_nodes and kms_edges, initializes unified views across codebase and alignment tables, and runs recursive SQL Common Table Expression (CTE) queries for Graph-RAG.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/graph_db.py.md|graph_db.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_schema_name]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|HAS_POSTGRES]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|PostgresGraphDB]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|_execute_query]] (function: belongs_to) — *Helper to run queries with the thread-safe connection pool.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|_init_db]] (function: belongs_to) — *Initializes connection pool, tables, indexes, and views in PostgreSQL.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|clear]] (function: belongs_to) — *Clears local KMS nodes and edges.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|close]] (function: belongs_to) — *Closes connection resource links (shared pool closed on program exit).*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|export_unified_graph]] (function: belongs_to) — *Exports the combined view of nodes and edges from all tables to a JSON file.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|find_path]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|insert_edge]] (function: belongs_to) — *Inserts a relationship edge in the local KMS database.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|insert_node]] (function: belongs_to) — *Inserts or updates a node in the local KMS database.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|remove_edges_by_source_or_type]] (function: belongs_to) — *Removes local KMS edges by source and optional type.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|remove_node]] (function: belongs_to) — *Removes a local KMS node and all edges connected to it.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/graph/postgres_db.py.md|traverse_neighborhood]] (function: belongs_to)
<!-- SYNC:END -->
