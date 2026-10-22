---
source: obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.695518
---

# Mirror: orchestration_lib.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py`.

> **Essential Process**:
> Provides shared orchestration utility functions for path resolution, mode retrieval, dynamic inventory querying, and structured logging.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|add]] (function: calls) — *Appends a new turn to the in-memory buffer, capping size.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|memory.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/audit_ports.py.md|audit_ports.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/audit_ports.py.md|audit_ports.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/brain_health_audit.py.md|brain_health_audit.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/brain_health_audit.py.md|brain_health_audit.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|check_coherence.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|check_coherence.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/ensure_frontmatter.py.md|ensure_frontmatter.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/ensure_frontmatter.py.md|ensure_frontmatter.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|preflight_check.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|preflight_check.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|agent_dispatcher.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/agent_dispatcher.py.md|agent_dispatcher.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/mission_help.py.md|mission_help.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/mission_help.py.md|mission_help.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/switch_mode.py.md|switch_mode.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/switch_mode.py.md|switch_mode.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py.md|persona_extractor.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py.md|persona_extractor.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/build_inventory.py.md|build_inventory.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/build_inventory.py.md|build_inventory.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/close_mission.py.md|close_mission.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/close_mission.py.md|close_mission.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/convert_agents.py.md|convert_agents.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/convert_agents.py.md|convert_agents.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fix_feats.py.md|fix_feats.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fix_feats.py.md|fix_feats.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|fleet_commander.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|fleet_commander.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_init_update.py.md|fleet_init_update.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_init_update.py.md|fleet_init_update.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_refresh.py.md|fleet_refresh.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_refresh.py.md|fleet_refresh.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_version.py.md|fleet_version.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_version.py.md|fleet_version.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/map_feats.py.md|map_feats.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/map_feats.py.md|map_feats.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|C_BOLD]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|C_CYAN]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|C_DIM]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|C_GREEN]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|C_RED]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|C_RESET]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|C_YELLOW]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_active_mode]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_config]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_fleet_repositories]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_logger]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_active_workspaces]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|setup_terminal]] (function: belongs_to) — *Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/init_new_brain.py.md|init_new_brain.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/init_new_brain.py.md|init_new_brain.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/install_git_hooks.py.md|install_git_hooks.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/install_git_hooks.py.md|install_git_hooks.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|scaffold_new_brain.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|scaffold_new_brain.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/unlock_vault.py.md|unlock_vault.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/unlock_vault.py.md|unlock_vault.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/knowledge_compressor.py.md|knowledge_compressor.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/knowledge_compressor.py.md|knowledge_compressor.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/maintenance_skill.py.md|maintenance_skill.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/maintenance_skill.py.md|maintenance_skill.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
