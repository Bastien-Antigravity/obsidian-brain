---
source: obsidian-brain/08-Squad-Agent/src/core/start_squad.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:37.709121
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: start_squad.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/core/start_squad.py`.

> **Essential Process**:
> Initializes the Bastien-Antigravity AI Squad Command Center. Handles MCP binding, pre-session audits, role synchronization, and launches the selected AI client.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/agents/architect.py.md|ArchitectAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/architect.py.md|architect.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|AutoRepairCoordinator]] (class: calls) — *Real-time Watchdog incident consumer and capability-aware Tiered Auto-Repair coordinator.*
- [[obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|autorepair.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|BaseAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|base_agent.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|discover_registered_domain_workspaces]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/base_agent.py.md|slugify_role_name]] (function: calls) — *Normalizes a prompt stem or role label into a canonical lowercase slug.*
- [[obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|CodeIndexerAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|codeindexer.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/debloatsentinel.py.md|DebloatSentinelAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/debloatsentinel.py.md|debloatsentinel.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|DeveloperAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|developer.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|DocIndexerAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|docindexer.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|DocMaintainerAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|docmaintainer.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/fleetarchitect.py.md|FleetArchitectAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/fleetarchitect.py.md|fleetarchitect.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/fleetcommander.py.md|FleetCommanderAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/fleetcommander.py.md|fleetcommander.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|OracleAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|oracle.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|OrchestratorAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|orchestrator.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/patternsentinel.py.md|PatternSentinelAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/patternsentinel.py.md|patternsentinel.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/prototyper.py.md|PrototyperAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/prototyper.py.md|prototyper.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/purger.py.md|PurgerAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/purger.py.md|purger.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|QAAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|qa.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/agents/sentinel.py.md|SentinelAgent]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/agents/sentinel.py.md|sentinel.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|DiscordClient]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|HAS_DISCORD]] (constant: calls)
- [[obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|discord_client.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|start]] (function: calls) — *Establishes connection to the Gateway.*
- [[obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|start_async]] (function: calls) — *Asynchronously establishes connection to the Discord Gateway.*
- [[obsidian-brain/08-Squad-Agent/src/core/controller.py.md|CommandController]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/core/controller.py.md|dispatch_alert_sync]] (function: calls) — *Synchronously dispatches operational alerts to notif-server via NotificationClient.*
- [[obsidian-brain/08-Squad-Agent/src/core/controller.py.md|get_active_mode]] (function: calls) — *Reads active mode from the orchestration manual.*
- [[obsidian-brain/08-Squad-Agent/src/core/controller.py.md|refresh_telegram_menu]] (function: calls) — *Triggers a live Telegram inline menu rebuild when fleet incidents change.*
- [[obsidian-brain/08-Squad-Agent/src/core/controller.py.md|register_background_task]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/core/controller.py.md|start_and_supervise_agents]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/core/mission_help.py.md|mission_help.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/core/switch_mode.py.md|switch_mode.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/fleet/convert_agents.py.md|convert_agents.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/grpc_control/service.py.md|service.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/grpc_control/service.py.md|start_grpc_server]] (function: calls) — *Initializes and starts the asynchronous Squad Control gRPC server.*
- [[obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|DualSquadEventBus]] (class: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_config]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|SetupTelegram]] (function: calls) — *Initializes dynamic Tele-Remote client, binds updates, and registers exit handlers.*
- [[obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|manager.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/web/server.py.md|server.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/web/server.py.md|start_async_server]] (function: calls) — *Launches the uvicorn web server and starts the auto-registration daemon thread.*

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|C_BOLD]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|C_GREEN]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|C_RED]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|C_RESET]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|EXCLUSIONS]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|_CORE_SQUAD_ROLES]] (constant: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|_check_single_repo]] (function: belongs_to) — *Worker function for parallel git status checks.*
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|_strip_frontmatter]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|archive_strat_files]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|check_environment]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|check_rag_attached]] (function: belongs_to) — *Returns True if the 09-RAG-Engine exists and a valid server entrypoint is available.*
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|check_session_health]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|discover_domain_agents]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|ensure_background_services]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|generate_active_rituals]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|get_vault_python]] (function: belongs_to) — *Return the vault virtualenv Python when available, otherwise current Python.*
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|log_session_event]] (function: belongs_to) — *Logs a message with timestamp to the session log file.*
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|main]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|print_process_manifest_summary]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|protect_core_kms]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|regenerate_agents]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|run_preflight]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|setup_mcp]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_engine]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|unlock_core_kms]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
