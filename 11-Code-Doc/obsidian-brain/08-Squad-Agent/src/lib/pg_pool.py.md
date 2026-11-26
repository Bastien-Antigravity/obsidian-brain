---
source: obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:34.673147
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
- [[obsidian-brain/08-Squad-Agent/src/auditing/audit_secret_leakage.py.md|decrypt_secret]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|autorepair.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|autorepair.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|FLEET_ERROR_DDL]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|HAS_POSTGRES]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|_borrow_conn]] (function: belongs_to) — *Borrows a connection from pg_pool, rolling back cleanly on failure.*
- [[obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|close_pg_pool]] (function: belongs_to) — *Closes all active connections in the pool on shutdown.*
- [[obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|ensure_fleet_error_schema]] (function: belongs_to) — *Ensures Option B schema 'watchdog_agent' and triage tables exist in obsidiandb.*
- [[obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|get_pg_pool]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|list_fleet_incidents]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|query_recent_fleet_errors]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|resolve_schema_name]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|upsert_fleet_incident]] (function: belongs_to) — *Persists or updates an AutoRepair triage incident record in PostgreSQL.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|scaffold_new_brain.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|scaffold_new_brain.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
