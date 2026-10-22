---
source: obsidian-brain/08-Squad-Agent/src/core/start_squad.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.479547
---

# Mirror: start_squad.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/core/start_squad.py`.

> **Essential Process**:
> Initializes the Bastien-Antigravity AI Squad Command Center. Handles MCP binding, pre-session audits, role synchronization, and launches the selected AI client.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/architect.py.md|ArchitectAgent]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/architect.py.md|architect.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|CodeIndexerAgent]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/codeindexer.py.md|codeindexer.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|DeveloperAgent]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/developer.py.md|developer.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|DocIndexerAgent]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docindexer.py.md|docindexer.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|DocMaintainerAgent]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/docmaintainer.py.md|docmaintainer.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/fleetarchitect.py.md|FleetArchitectAgent]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/fleetarchitect.py.md|fleetarchitect.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/fleetcommander.py.md|FleetCommanderAgent]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/fleetcommander.py.md|fleetcommander.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|OracleAgent]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/oracle.py.md|oracle.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|OrchestratorAgent]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/orchestrator.py.md|orchestrator.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/patternsentinel.py.md|PatternSentinelAgent]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/patternsentinel.py.md|patternsentinel.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/prototyper.py.md|PrototyperAgent]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/prototyper.py.md|prototyper.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/purger.py.md|PurgerAgent]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/purger.py.md|purger.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|QAAgent]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/qa.py.md|qa.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/sentinel.py.md|SentinelAgent]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/sentinel.py.md|sentinel.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|DiscordClient]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|HAS_DISCORD]] (constant: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|discord_client.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|start]] (function: calls) — *Establishes connection to the Gateway.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|start_async]] (function: calls) — *Asynchronously establishes connection to the Discord Gateway.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|CommandController]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|dispatch_alert_sync]] (function: calls) — *Synchronously dispatches operational alerts to notif-server via NotificationClient.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|get_active_mode]] (function: calls) — *Reads active mode from the orchestration manual.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/mission_help.py.md|mission_help.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/switch_mode.py.md|switch_mode.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/convert_agents.py.md|convert_agents.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/grpc_control/service.py.md|service.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/grpc_control/service.py.md|start_grpc_server]] (function: calls) — *Initializes and starts the asynchronous Squad Control gRPC server.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/interfaces.py.md|DualSquadEventBus]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_config]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|SetupTelegram]] (function: calls) — *Initializes dynamic Tele-Remote client, binds updates, and registers exit handlers.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|manager.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/server.py.md|server.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/server.py.md|start_async_server]] (function: calls) — *Launches the uvicorn web server and starts the auto-registration daemon thread.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|C_BOLD]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|C_GREEN]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|C_RED]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|C_RESET]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|EXCLUSIONS]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|_check_single_repo]] (function: belongs_to) — *Worker function for parallel git status checks.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|_strip_frontmatter]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|archive_strat_files]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|check_environment]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|check_rag_attached]] (function: belongs_to) — *Returns True if the 09-RAG-Engine exists and a valid server entrypoint is available.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|check_session_health]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|ensure_background_services]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|generate_active_rituals]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|get_vault_python]] (function: belongs_to) — *Return the vault virtualenv Python when available, otherwise current Python.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|log_session_event]] (function: belongs_to) — *Logs a message with timestamp to the session log file.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|main]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|print_process_manifest_summary]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|protect_core_kms]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|regenerate_agents]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|run_preflight]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|setup_mcp]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_engine]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|unlock_core_kms]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
