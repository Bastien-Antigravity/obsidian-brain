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

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/main.py.md|COMMANDS_MAP]] (constant: calls) — *Commands map (CLI alias -> themed python module namespace relative to src)*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/main.py.md|main.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/switch_mode.py.md|MODES]] (constant: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/switch_mode.py.md|apply_mode_protocol]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/switch_mode.py.md|switch_mode.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/switch_mode.py.md|switch_mode.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/interfaces/command.py.md|Command]] (class: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|DualLayerMemoryStore]] (class: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|PostgresMemoryStore]] (class: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|RAGMemoryStore]] (class: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|ShortTermMemory]] (class: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|add]] (function: calls) — *Appends a new turn to the in-memory buffer, capping size.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|memory.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/memory.py.md|retrieve]] (function: calls) — *Retrieves active conversation history buffer.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/pg_pool.py.md|pg_pool.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/pg_pool.py.md|resolve_schema_name]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/clients/discord_client.py.md|discord_client.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/clients/discord_client.py.md|discord_client.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|CommandController]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|_setup_memory]] (function: belongs_to) — *Sets up the dynamic dual-layer memory layers.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|_task]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|db_insert]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|db_query]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|execute]] (function: belongs_to) — *Implements Command interface to run a quick mock verification check.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|get_active_mode]] (function: belongs_to) — *Reads active mode from the orchestration manual.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|get_chat_history]] (function: belongs_to) — *Retrieves squad chat logs from Postgres or in-memory memory store as fallback.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|get_mode_details]] (function: belongs_to) — *Returns name and description for a mode.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|get_status]] (function: belongs_to) — *Checks Squad daemon layer health.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|list_commands]] (function: belongs_to) — *Returns a list of available subcommands and their descriptions.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|main]] (function: belongs_to) — *Entry point for mock verification command run.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|process_message]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|publish_user_message]] (function: belongs_to) — *Saves a user message and publishes it to EventBus to trigger agents.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|run_subcommand]] (function: belongs_to) — *Runs a direct sub-command script dynamically routing via controller.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|run_subcommand_async]] (function: belongs_to) — *Triggers a subcommand in a non-blocking background task.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|switch_mode]] (function: belongs_to) — *Switches active mode in configuration files.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/grpc_control/service.py.md|service.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/rest/rest_handler.py.md|rest_handler.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|manager.py]] (calls)
<!-- SYNC:END -->
