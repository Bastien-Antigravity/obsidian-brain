---
source: obsidian-brain/08-Squad-Agent/src/maintenance/maintenance_skill.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:34.686212
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: maintenance_skill.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/maintenance/maintenance_skill.py`.

> **Essential Process**:
> Performs routine maintenance tasks across the ecosystem, specifically compacting stale AI-Session-State.md files in-place to prevent context bloat without deleting mandatory repository governance files.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/maintenance/maintenance_skill.py.md|WORKSPACE_DIR]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/maintenance/maintenance_skill.py.md|compact_session_state_file]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/maintenance/maintenance_skill.py.md|main]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/maintenance/maintenance_skill.py.md|purge_stale_state]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
