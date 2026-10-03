---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Base-Scripts/src/core/agent_dispatcher.py`.

> **Essential Process**:
> Monitors the Obsidian Vault recursively for pending tasks and automates the handover to specific AI Agent personas.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/agent_dispatcher.py.md|OBSIDIAN_DIR]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/agent_dispatcher.py.md|ROLE_MAP]] (constant: belongs_to) — *Role to Prompt Filename Mapping*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/agent_dispatcher.py.md|ROLE_PROMPT_SOURCES]] (constant: belongs_to) — *Source of Truth Precedence*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/agent_dispatcher.py.md|SEMANTIC_KEYWORDS]] (constant: belongs_to) — *Semantic Keywords for Fallback Scoring*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/agent_dispatcher.py.md|WORKSPACE_ROOT]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/agent_dispatcher.py.md|get_role_prompt_path]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/agent_dispatcher.py.md|is_ignored_by_firewall]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/agent_dispatcher.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/agent_dispatcher.py.md|parse_frontmatter]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/agent_dispatcher.py.md|process_vault_tasks]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/agent_dispatcher.py.md|route_task_semantically]] (function: belongs_to)
<!-- SYNC:END -->
