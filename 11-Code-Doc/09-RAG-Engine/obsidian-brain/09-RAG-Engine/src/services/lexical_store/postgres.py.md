---
source: obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.284576
---

# Mirror: postgres.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py`.

> **Essential Process**:
> Lexical search store implementation using PostgreSQL Full Text Search (FTS). Provides keyword-based retrieval with Postgres persistence for the RAG engine.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/lexical_store.py.md|LexicalStore]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/lexical_store.py.md|lexical_store.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/models/metadata.py.md|metadata.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_schema_name]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (imports)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|HAS_POSTGRES]] (constant: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|PostgresLexicalStore]] (class: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|_delete]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|_execute_query]] (function: belongs_to) — *Helper to run queries with the thread-safe connection pool.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|_init_db]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|_read]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|_reset]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|_write]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|add_documents]] (function: belongs_to) — *Adds or updates lexical entries in Postgres (Upsert).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|close]] (function: belongs_to) — *Closes connection resource links (shared pool closed on program exit).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|delete_by_brain]] (function: belongs_to) — *Removes all lexical entries belonging to a specific brain partition.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|delete_by_source]] (function: belongs_to) — *Removes all lexical entries belonging to a specific source file.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|query]] (function: belongs_to) — *Performs a lexical search query using Postgres Full Text Search (FTS).*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|reset_store]] (function: belongs_to) — *Deletes all documents from the store.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/lexical_store/postgres.py.md|set_bulk_mode]] (function: belongs_to) — *Enables or disables bulk ingestion mode.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
