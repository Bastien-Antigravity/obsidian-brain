---
source: obsidian-brain/08-Base-Scripts/src/fleet/fleet_refresh.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-09-17T06:24:01.675666
---

# Mirror: fleet_refresh.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Base-Scripts/src/fleet/fleet_refresh.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|get_config]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_refresh.py.md|DEFAULT_USER]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_refresh.py.md|FleetRefresher]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_refresh.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_refresh.py.md|_handle_remove_readonly]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_refresh.py.md|_is_repo_dirty]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_refresh.py.md|get_github_repos]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_refresh.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_refresh.py.md|refresh_repos]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/fleet/fleet_refresh.py.md|run_refresh]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
