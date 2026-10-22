---
source: obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.469254
---

# Mirror: agent_dispatcher.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py`.

> **Essential Process**:
> Monitors the Obsidian Vault recursively for pending tasks and automates the handover to specific AI Agent personas.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|OBSIDIAN_DIR]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|ROLE_MAP]] (constant: belongs_to) — *Role to Prompt Filename Mapping (21 Ecosystem Squad Personas)*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|ROLE_PROMPT_SOURCES]] (constant: belongs_to) — *Source of Truth Precedence*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|SEMANTIC_KEYWORDS]] (constant: belongs_to) — *Semantic Keywords for Fallback Scoring*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|WORKSPACE_ROOT]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|get_role_prompt_path]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|is_ignored_by_firewall]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|main]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|parse_frontmatter]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|process_vault_tasks]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|route_task_semantically]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
