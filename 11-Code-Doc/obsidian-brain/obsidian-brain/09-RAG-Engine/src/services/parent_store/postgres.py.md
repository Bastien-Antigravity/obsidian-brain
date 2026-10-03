

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py`.

> **Essential Process**:
> PostgreSQL implementation of the Parent Store for the RAG engine. Persists full raw content of document chunks to enable reconstruction and drift detection.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/parent_store.py.md|ParentStore]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/parent_store.py.md|parent_store.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_schema_name]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|HAS_POSTGRES]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|PostgresParentStore]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|_check]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|_delete]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|_execute_query]] (function: belongs_to) — *Helper to run queries with the thread-safe connection pool.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|_init_db]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|_read]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|_reset]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|_update]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|_write]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|close]] (function: belongs_to) — *Closes connection resource links (shared pool closed on program exit).*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|delete_by_source]] (function: belongs_to) — *Deletes all parent content associated with a source path in PostgreSQL.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|get_all_file_hashes]] (function: belongs_to) — *Retrieves all stored file hashes from the database as a dictionary {source_path: file_hash}.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|get_parent]] (function: belongs_to) — *Retrieves the raw content for a specific chunk ID from PostgreSQL.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|is_file_changed]] (function: belongs_to) — *Checks if a file's hash differs from the stored version (Differential Indexing).*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|reset_store]] (function: belongs_to) — *Resets the parent store in PostgreSQL by dropping table records.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|store_parent]] (function: belongs_to) — *Stores the raw content associated with a chunk ID in PostgreSQL.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|store_parents_batch]] (function: belongs_to) — *Stores a batch of chunk objects in a single transaction in PostgreSQL.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/parent_store/postgres.py.md|update_file_hash]] (function: belongs_to) — *Updates the stored hash for a file after successful indexing.*
<!-- SYNC:END -->
