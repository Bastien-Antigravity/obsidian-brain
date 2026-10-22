---
source: obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-13T19:05:46.100280
---

# Mirror: seed_service.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py`.

> **Essential Process**:
> Seed Exporter and Importer Service for PostgreSQL + pgvector database tables. Provides reproducible dataset backup, sanitization, and restoration for CI, GitHub, and local fleet development environments.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|get_schema_name]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/utils/pg_pool.py.md|pg_pool.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/interfaces.py.md|debug]] (function: calls)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|SeedService]] (class: belongs_to) — *Manages exporting and importing sanitized seed data for the RAG Engine.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|_get_pool]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|_get_schema]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|_sanitize_dict]] (function: belongs_to) — *Recursively sanitizes dictionary strings and metadata.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|_sanitize_string]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|export_seed]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|import_seed]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|is_database_empty]] (function: belongs_to) — *Checks whether the database tables in schema currently have 0 records.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|json_dumps]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/seed/seed_service.py.md|json_loads]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
