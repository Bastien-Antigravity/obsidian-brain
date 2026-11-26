---
source: obsidian-brain/08-Squad-Agent/src/agents/developer.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:34.632307
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: developer.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/agents/developer.py`.

> **Essential Process**:
> Lead Developer agent daemon specialized in reading/writing source files, scaffolding compliant L3/L4/L5 microservices, compiling code, and implementing logic changes across both the central workspace and registered external domain workspaces.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|BaseAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_resolve_active_workspace_root]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/models/build_spec.py.md|allocate_domain_port]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/models/build_spec.py.md|build_spec.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|DeveloperAgent]] (class: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|_ALLOWED_FLEET_MODES]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|_ALLOWED_LANGS]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|_ALLOWED_LAYERS]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|_load_system_prompt]] (function: belongs_to) — *Scopes specialist prompts dynamically when task_context specifies a target language.*
- [[obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|execute_tool]] (function: belongs_to) — *Executes DeveloperAgent tools, delegating standard workspace/RAG tools to BaseAgent.*
- [[obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|scaffold_microservice]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
