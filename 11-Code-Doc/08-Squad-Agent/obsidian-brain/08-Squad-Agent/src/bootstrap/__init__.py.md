---
source: obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.499058
---

# Mirror: __init__.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py`.

> **Essential Process**:
> Root-level environment bootstrapper and singleton manager for 08-Squad-Agent. Sets up system path, redirects virtualenv execution, and instantiates the application configuration loader and the UniLog logging engine exactly once.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|PostgresMemoryStore]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|memory.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|pg_pool.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|resolve_schema_name]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/main.py.md|main.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|preflight_check.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|discord_client.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/improved_transformer.py.md|improved_transformer.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|scaffold_new_brain.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/unlock_vault.py.md|unlock_vault.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|joint_audit_purger.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/knowledge_compressor.py.md|knowledge_compressor.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
