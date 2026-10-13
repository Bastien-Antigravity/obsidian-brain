---
source: obsidian-brain/08-Squad-Agent/src/fleet/fleet_refresh.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13T02:56:34.741909
---

# Mirror: fleet_refresh.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/fleet/fleet_refresh.py`.

> **Essential Process**:
> Safely refreshes, synchronizes, or clones repositories across the fleet. Enforces strict anti-data-loss verification to ensure uncommitted work is NEVER lost.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_config]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls) — *Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/maintenance/knowledge_compressor.py.md|run]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls) — *Resolves public key PEM string from AppConfig or standard file paths.*

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/fleet/fleet_refresh.py.md|DEFAULT_USER]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/fleet/fleet_refresh.py.md|FleetRefresher]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/fleet/fleet_refresh.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/fleet/fleet_refresh.py.md|_handle_remove_readonly]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/fleet/fleet_refresh.py.md|_is_repo_dirty]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/fleet/fleet_refresh.py.md|get_github_repos]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/fleet/fleet_refresh.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/fleet/fleet_refresh.py.md|refresh_repos]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/fleet/fleet_refresh.py.md|run_refresh]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
