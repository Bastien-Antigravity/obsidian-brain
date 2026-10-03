

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/alignment.py.md|AlignmentService]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/alignment.py.md|alignment.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_schema_name]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|HAS_POSTGRES]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|PostgresAlignmentService]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|_compute_hash]] (function: belongs_to) — *Computes a SHA-256 hash of the given text.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|_execute_query]] (function: belongs_to) — *Helper to run queries with the thread-safe connection pool.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|_init_db]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|_read]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|_read_links_and_parents]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|_reset]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|_write]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|_write_drifts]] (function: belongs_to) — *Truncate and insert new drifts to the documentation_drift_registry table in Postgres*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|check_alignment]] (function: belongs_to) — *Compares the current code content against the hash stored to detect drift.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|close]] (function: belongs_to) — *Closes connection resource links (shared pool closed on program exit).*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|get_all_drifted]] (function: belongs_to) — *Returns a list of all documentation notes that are currently out of sync with code.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|get_dead_links]] (function: belongs_to) — *Identifies links where the code chunk ID no longer exists in the system.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|get_drift_details]] (function: belongs_to) — *Returns details needed for a rewrite: current hash vs stored hash and linked docs.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|get_linked_code]] (function: belongs_to) — *Retrieves all code chunks linked to a specific Obsidian note.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|get_linked_docs]] (function: belongs_to) — *Retrieves all Obsidian documentation notes linked to a specific code chunk.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|register_link]] (function: belongs_to) — *Registers a link between a code chunk and doc, writing to PG.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|register_links_batch]] (function: belongs_to) — *Registers multiple links in a single PG batch.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/postgres_alignment.py.md|reset_registry]] (function: belongs_to) — *Clears the alignment registry in PG.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|synchronizer.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|synchronizer.py]] (same_package)
<!-- SYNC:END -->
