---
source: obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.909620
---

# Mirror: fleet_commander.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py`.

> **Essential Process**:
> Fleet Commander - Unified Fleet Git, Synchronization, and Architectural Compliance. Native first-class Engine Room orchestrator in 08-Squad-Agent.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_active_workspaces]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls) — *Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|Sovereignty]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|audit_file]] (function: calls) — *Runs the full suite against a single file.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|get_report]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|sovereignty.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|validate_isolation_zone]] (function: calls) — *Checks for the presence and structure of the isolation zone.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/knowledge_compressor.py.md|run]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|FleetCommander]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|_load_inventory]] (function: belongs_to) — *Loads repository paths from inventory.json and populates compliance exclusions.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|_log]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|_resolve_active_workspaces]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|_run_command]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|_step]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|audit_docs]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|audit_isolation_zone]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|execute_fleet_push]] (function: belongs_to) — *Main execution loop for mass git operations with Sovereignty compliance audits.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|execute_fleet_status]] (function: belongs_to) — *Audits git status, active branch, and working tree purity across repos.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|execute_fleet_sync]] (function: belongs_to) — *Pulls latest changes on develop branch and pushes if ahead, strictly skipping dirty repos.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|execute_vault_sync]] (function: belongs_to) — *Performs atomic synchronization across all obsidian-brain submodules and parent pointer.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|main]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|validate_architecture]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
