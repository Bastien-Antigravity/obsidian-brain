---
source: obsidian-brain/08-Squad-Agent/src/core/controller.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-20 18:09:59.713538
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: controller.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/core/controller.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/main.py.md|COMMANDS_MAP]] (constant: calls) — *Commands map (CLI alias -> themed python module namespace relative to src)*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/main.py.md|main.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|set_enabled]] (function: calls) — *Enables or disables autonomous AutoRepair incident triage dynamically on the fly.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/agents/autorepair.py.md|unfreeze_service]] (function: calls) — *Resets 3-strike circuit breaker freeze for a service and closes stale FROZEN signature locks.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/switch_mode.py.md|MODES]] (constant: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/switch_mode.py.md|apply_mode_protocol]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/switch_mode.py.md|switch_mode.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/switch_mode.py.md|switch_mode.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/interfaces/command.py.md|Command]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|DualLayerMemoryStore]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|PostgresMemoryStore]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|RAGMemoryStore]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|ShortTermMemory]] (class: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|add]] (function: calls) — *Appends a new turn to the in-memory buffer, capping size.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|memory.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|retrieve]] (function: calls) — *Retrieves active conversation history buffer.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|ensure_fleet_error_schema]] (function: calls) — *Ensures Option B schema 'watchdog_agent' and triage tables exist in obsidiandb.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|list_fleet_incidents]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|pg_pool.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|resolve_schema_name]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|rebuild_menu]] (function: calls) — *Pulls status, modes, and commands to rebuild the Telegram menu.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|discord_client.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/clients/discord_client.py.md|discord_client.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|CommandController]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|_load_version]] (function: belongs_to) — *Loads version dynamically from AppConfig / VERSION.txt (fail-fast).*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|_setup_memory]] (function: belongs_to) — *Sets up the dynamic dual-layer memory layers.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|_setup_notification_client]] (function: belongs_to) — *Dynamically initializes NotificationClient from microservice-toolbox.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|_task]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|approve_incident]] (function: belongs_to) — *Applies an approved AutoRepair proposal and triggers Watchdog service restart.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|attach_telegram_menu]] (function: belongs_to) — *Registers the active Telegram MenuManager for reactive incident menu rebuilds.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|db_insert]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|db_query]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|dispatch_alert]] (function: belongs_to) — *Dispatches operational alerts to notif-server via NotificationClient.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|dispatch_alert_sync]] (function: belongs_to) — *Synchronously dispatches operational alerts to notif-server via NotificationClient.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|execute]] (function: belongs_to) — *Implements Command interface to run a quick mock verification check.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|get_active_mode]] (function: belongs_to) — *Reads active mode from the orchestration manual.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|get_autorepair_status]] (function: belongs_to) — *Returns runtime AutoRepair enable/disable status, capabilities, and metrics.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|get_chat_history]] (function: belongs_to) — *Retrieves squad chat logs from Postgres or in-memory memory store as fallback.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|get_incident]] (function: belongs_to) — *Retrieves a single fleet incident record by ID.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|get_mode_details]] (function: belongs_to) — *Returns name and description for a mode.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|get_status]] (function: belongs_to) — *Checks Squad daemon layer health.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|list_commands]] (function: belongs_to) — *Returns a list of available subcommands and their descriptions.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|list_incidents]] (function: belongs_to) — *Lists recent fleet incidents tracked by AutoRepairCoordinator or TimescaleDB.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|main]] (function: belongs_to) — *Entry point for mock verification command run.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|process_message]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|publish_user_message]] (function: belongs_to) — *Saves a user message and publishes it to EventBus to trigger agents.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|refresh_telegram_menu]] (function: belongs_to) — *Triggers a live Telegram inline menu rebuild when fleet incidents change.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|reject_incident]] (function: belongs_to) — *Marks an AutoRepair incident proposal as rejected.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|resolve_incident]] (function: belongs_to) — *Marks an AutoRepair incident manually resolved without restarting services.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|run_subcommand]] (function: belongs_to) — *Runs a direct sub-command script dynamically routing via controller.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|run_subcommand_async]] (function: belongs_to) — *Triggers a subcommand in a non-blocking background task.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|set_autorepair_enabled]] (function: belongs_to) — *Enables or disables AutoRepair real-time triage dynamically on the fly.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|switch_mode]] (function: belongs_to) — *Switches active mode in configuration files.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|unfreeze_autorepair_service]] (function: belongs_to) — *Resets 3-strike circuit breaker freeze for a service.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/grpc_control/service.py.md|service.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/rest/rest_handler.py.md|rest_handler.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|manager.py]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
