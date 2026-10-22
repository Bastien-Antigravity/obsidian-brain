---
source: obsidian-brain/08-Squad-Agent/src/telegram/manager.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.644504
---

# Mirror: manager.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/telegram/manager.py`.

> **Essential Process**:
> Provides the dynamic Telegram TeleClient controller for Squad Control. Exposes submenus to switch active modes and execute subcommands.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|get_mode_details]] (function: calls) — *Returns name and description for a mode.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|list_commands]] (function: calls) — *Returns a list of available subcommands and their descriptions.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|run_subcommand_async]] (function: calls) — *Triggers a subcommand in a non-blocking background task.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/switch_mode.py.md|MODES]] (constant: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/switch_mode.py.md|switch_mode.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|MenuManager]] (class: belongs_to) — *Orchestrates dynamic rebuild operations for the Squad Control Telegram menu.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|SetupTelegram]] (function: belongs_to) — *Initializes dynamic Tele-Remote client, binds updates, and registers exit handlers.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|cmd_cb]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|handle_status]] (function: belongs_to) — *1. Status Check Action*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|make_cmd_callback]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|make_mode_callback]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|mode_cb]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|push]] (function: belongs_to) — *Trigger background transmission of the updated UI menu state*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|rebuild_menu]] (function: belongs_to) — *Pulls status, modes, and commands to rebuild the Telegram menu.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|start_tc]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
