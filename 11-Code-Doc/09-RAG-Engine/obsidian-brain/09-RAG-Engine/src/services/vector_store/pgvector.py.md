---
source: obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-13T19:05:46.096918
---

# Mirror: pgvector.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py`.

> **Essential Process**:
> Vector store implementation using pgvector in PostgreSQL for semantic search. Handles document embedding, upserting, and cosine distance queries.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|VectorStore]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/vector_store.py.md|vector_store.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/models/metadata.py.md|metadata.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_schema_name]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (imports)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|HAS_DEPENDENCIES]] (constant: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|PgVectorStore]] (class: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|_delete]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|_execute_query]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|_init_db]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|_read]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|_reset]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|_write]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|add_documents]] (function: belongs_to) — *Adds or updates embeddings in pgvector (Upsert).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|close]] (function: belongs_to) — *Closes connection resource links (shared pool closed on program exit).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|delete_by_source]] (function: belongs_to) — *Removes all vectors belonging to a specific source file.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|get_all]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|get_all_source_paths]] (function: belongs_to) — *Retrieves distinct source file paths stored in the vector collection.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|model]] (function: belongs_to) — *Lazily loads and caches the shared BGE-M3 SentenceTransformer model instance.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|query]] (function: belongs_to) — *Performs semantic similarity search using pgvector cosine similarity (<=>).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/vector_store/pgvector.py.md|reset_store]] (function: belongs_to) — *Deletes and re-initializes the entire database.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
