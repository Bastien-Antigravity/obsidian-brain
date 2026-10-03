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
Automatically generated mirror for `obsidian-brain/08-Base-Scripts/src/telegram/manager.py`.

> **Essential Process**:
> Provides the dynamic Telegram TeleClient controller for Squad Control. Exposes submenus to switch active modes and execute subcommands.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|get_mode_details]] (function: calls) — *Returns name and description for a mode.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|list_commands]] (function: calls) — *Returns a list of available subcommands and their descriptions.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/controller.py.md|run_subcommand_async]] (function: calls) — *Triggers a subcommand in a non-blocking background task.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/switch_mode.py.md|MODES]] (constant: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/switch_mode.py.md|switch_mode.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|MenuManager]] (class: belongs_to) — *Orchestrates dynamic rebuild operations for the Squad Control Telegram menu.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|SetupTelegram]] (function: belongs_to) — *Initializes dynamic Tele-Remote client, binds updates, and registers exit handlers.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|cmd_cb]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|handle_status]] (function: belongs_to) — *1. Status Check Action*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|make_cmd_callback]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|make_mode_callback]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|mode_cb]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|push]] (function: belongs_to) — *Trigger background transmission of the updated UI menu state*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|rebuild_menu]] (function: belongs_to) — *Pulls status, modes, and commands to rebuild the Telegram menu.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/telegram/manager.py.md|start_tc]] (function: belongs_to)
<!-- SYNC:END -->
