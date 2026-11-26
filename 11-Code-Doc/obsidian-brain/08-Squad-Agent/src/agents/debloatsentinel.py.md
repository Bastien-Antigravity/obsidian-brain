---
source: obsidian-brain/08-Squad-Agent/src/agents/debloatsentinel.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-11-04 23:07:16.438337
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: debloatsentinel.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/agents/debloatsentinel.py`.

> **Essential Process**:
> DebloatSentinel agent daemon specialized in identifying over-engineering, redundant checks, useless synchronization, and simplifying source code.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|BaseAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|_resolve_active_workspace_root]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|debloat_audit.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|generate_safe_by_design_markdown]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/auditing/debloat_audit.py.md|run_debloat_audit]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/agents/debloatsentinel.py.md|DebloatSentinelAgent]] (class: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/debloatsentinel.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/debloatsentinel.py.md|audit_codebase_bloat]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/debloatsentinel.py.md|execute_tool]] (function: belongs_to) — *Executes a function call requested by the model.*
- [[obsidian-brain/08-Squad-Agent/src/agents/debloatsentinel.py.md|generate_safe_by_design_spec]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/agents/debloatsentinel.py.md|propose_code_simplification]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
