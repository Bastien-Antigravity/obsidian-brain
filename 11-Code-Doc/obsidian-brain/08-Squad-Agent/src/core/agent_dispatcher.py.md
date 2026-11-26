---
source: obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:34.478302
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: agent_dispatcher.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py`.

> **Essential Process**:
> Monitors the Obsidian Vault recursively for pending tasks and automates the handover to specific AI Agent personas (central and domain-vault).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|discover_registered_domain_workspaces]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|slugify_role_name]] (function: calls) — *Normalizes a prompt stem or role label into a canonical lowercase slug.*
- [[obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|eval_agent.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/auditing/eval_agent.py.md|eval_agent.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|OBSIDIAN_DIR]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|ROLE_MAP]] (constant: belongs_to) — *Role to Prompt Filename Mapping (21 Ecosystem Squad Personas)*
- [[obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|ROLE_PROMPT_SOURCES]] (constant: belongs_to) — *Source of Truth Precedence*
- [[obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|SEMANTIC_KEYWORDS]] (constant: belongs_to) — *Semantic Keywords for Fallback Scoring*
- [[obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|WORKSPACE_ROOT]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|_role_keywords_from_prompt]] (function: belongs_to) — *Derives semantic matching keywords from a discovered domain role prompt filename.*
- [[obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|discover_vault_roles]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|get_role_prompt_path]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|is_ignored_by_firewall]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|main]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|parse_frontmatter]] (function: belongs_to) — *Parses YAML frontmatter from a markdown file using a late import.*
- [[obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|process_vault_tasks]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|route_task_semantically]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
