---
source: obsidian-brain/08-Squad-Agent/src/fleet/convert_agents.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:37.794417
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: convert_agents.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/fleet/convert_agents.py`.

> **Essential Process**:
> Converts the human-readable Role-Prompts from the core-kms-brain into compatible Gemini CLI agent definitions in the obsidian-brain vault.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|check_coherence.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|check_coherence.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/fleet/convert_agents.py.md|_write_compiled_skill]] (function: belongs_to) — *Compiles a raw Role-Prompt markdown file and writes <target_dir>/<skill_name>/SKILL.md.*
- [[obsidian-brain/08-Squad-Agent/src/fleet/convert_agents.py.md|build_skill_markdown]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/fleet/convert_agents.py.md|compile_skills]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/fleet/convert_agents.py.md|main]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|scaffold_new_brain.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|scaffold_new_brain.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
