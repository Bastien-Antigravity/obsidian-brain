---
source: obsidian-brain/08-Squad-Agent/src/maintenance/maintenance_skill.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13T02:56:34.686212
---

# Mirror: maintenance_skill.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/maintenance/maintenance_skill.py`.

> **Essential Process**:
> Performs routine maintenance tasks across the ecosystem, specifically purging stale AI-Session-State.md files to prevent context bloat.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/maintenance/maintenance_skill.py.md|WORKSPACE_DIR]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/maintenance/maintenance_skill.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/maintenance/maintenance_skill.py.md|purge_stale_state]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
