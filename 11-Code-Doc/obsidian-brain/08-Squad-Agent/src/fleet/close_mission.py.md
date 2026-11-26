---
source: obsidian-brain/08-Squad-Agent/src/fleet/close_mission.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:37.801093
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: close_mission.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/fleet/close_mission.py`.

> **Essential Process**:
> Mission Sign-off Ritual and Governance Gate for Bastien-Antigravity. Finalizes active AI sessions by verifying Git branch status, dirty working trees, uncommitted files, and knowledge base documentation sovereignty before conclusion.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_active_mode]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_fleet_repositories]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls) — *Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems.*
- [[obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|Sovereignty]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|audit_file]] (function: calls) — *Runs the full suite against a single file.*
- [[obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|auto_fix_file]] (function: calls) — *Fixes taxonomy issues, enforces YAML frontmatter schema, and automatically converts absolute links to relative ones.*
- [[obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|get_report]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|is_ignored_by_firewall]] (function: calls) — *Checks if a path is ignored by context firewalls (.aiignore etc) or carries the #ai/ignore tag.*
- [[obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|log_error]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|sovereignty.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/fleet/close_mission.py.md|EXCLUSIONS]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/fleet/close_mission.py.md|confirm_step]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/fleet/close_mission.py.md|get_current_branch]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/fleet/close_mission.py.md|main]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
