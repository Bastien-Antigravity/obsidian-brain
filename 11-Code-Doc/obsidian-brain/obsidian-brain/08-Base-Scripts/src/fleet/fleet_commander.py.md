---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py`.

> **Essential Process**:
> Fleet Commander - Unified Fleet Git, Synchronization, and Architectural Compliance. Native first-class Engine Room orchestrator in 08-Base-Scripts.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|resolve_active_workspaces]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls) — *Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|Sovereignty]] (class: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|audit_file]] (function: calls) — *Runs the full suite against a single file.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|get_report]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|sovereignty.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/sovereignty.py.md|validate_isolation_zone]] (function: calls) — *Checks for the presence and structure of the isolation zone.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/knowledge_compressor.py.md|run]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|FleetCommander]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|_load_inventory]] (function: belongs_to) — *Loads repository paths from inventory.json and populates compliance exclusions.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|_log]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|_resolve_active_workspaces]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|_run_command]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|_step]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|audit_docs]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|audit_isolation_zone]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|execute_fleet_push]] (function: belongs_to) — *Main execution loop for mass git operations with Sovereignty compliance audits.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|execute_fleet_status]] (function: belongs_to) — *Audits git status, active branch, and working tree purity across repos.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|execute_fleet_sync]] (function: belongs_to) — *Pulls latest changes on develop branch and pushes if ahead, strictly skipping dirty repos.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|execute_vault_sync]] (function: belongs_to) — *Performs atomic synchronization across all obsidian-brain submodules and parent pointer.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_commander.py.md|validate_architecture]] (function: belongs_to)
<!-- SYNC:END -->
