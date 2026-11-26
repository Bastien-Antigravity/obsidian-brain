

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py`.

> **Essential Process**:
> Database abstraction layer for persistent storage of codebase nodes, edges, and symbol mapping in PostgreSQL.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/09-RAG-Engine/src/interfaces/codebase_db.py.md|CodebaseDB]] (class: calls)
- [[obsidian-brain/09-RAG-Engine/src/interfaces/codebase_db.py.md|codebase_db.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_schema_name]] (function: calls)
- [[obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (calls)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (imports)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (same_package)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|PostgresCodebaseDB]] (class: belongs_to) — *Manages a PostgreSQL database containing the codebase static analysis graph data.*
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|_execute_query]] (function: belongs_to) — *Helper to run queries with the thread-safe connection pool.*
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|_init_db]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|clear]] (function: belongs_to) — *Deletes codebase nodes and edges scoped to a specific brain_id (never truncates all brains).*
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|close]] (function: belongs_to) — *Closes connection resource links (shared pool closed on program exit).*
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|delete_by_brain]] (function: belongs_to) — *Removes all codebase nodes and edges belonging to a specific brain_id.*
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|find_symbols]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|get_edges]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|get_nodes]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|insert_edge]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|insert_edges_batch]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|insert_node]] (function: belongs_to)
- [[obsidian-brain/09-RAG-Engine/src/services/code_engine/postgres_db.py.md|insert_nodes_batch]] (function: belongs_to)
<!-- SYNC:END -->
