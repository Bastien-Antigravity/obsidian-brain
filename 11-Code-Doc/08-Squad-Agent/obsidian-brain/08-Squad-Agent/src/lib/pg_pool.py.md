---
source: obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22 16:53:55.658049
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: pg_pool.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|autorepair.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|autorepair.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|FLEET_ERROR_DDL]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|HAS_POSTGRES]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|_borrow_conn]] (function: belongs_to) — *Borrows a connection from pg_pool, rolling back cleanly on failure.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|close_pg_pool]] (function: belongs_to) — *Closes all active connections in the pool on shutdown.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|ensure_fleet_error_schema]] (function: belongs_to) — *Ensures Option B schema 'watchdog_agent' and triage tables exist in obsidiandb.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|get_pg_pool]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|list_fleet_incidents]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|query_recent_fleet_errors]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|resolve_schema_name]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|upsert_fleet_incident]] (function: belongs_to) — *Persists or updates an AutoRepair triage incident record in PostgreSQL.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|scaffold_new_brain.py]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
