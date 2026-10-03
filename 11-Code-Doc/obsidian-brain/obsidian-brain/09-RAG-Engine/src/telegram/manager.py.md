

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/telegram/manager.py`.

> **Essential Process**:
> Provides the dynamic Telegram TeleClient controller for RAG Engine. Automatically constructs config-browsing submenus and hooks configuration update callbacks.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|MenuManager]] (class: belongs_to) — *Orchestrates dynamic rebuild operations for the RAG Telegram control menu.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|SetupTelegram]] (function: belongs_to) — *Initializes dynamic Tele-Remote client, binds updates, and registers exit handlers.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|edit_cb]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|handle_clean_sync]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|handle_index_dir]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|handle_index_file]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|handle_rebuild]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|handle_reset_rebuild]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|handle_stats]] (function: belongs_to) — *1. RAG Indexing Stats & Operations*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|handle_sync]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|make_edit_callback]] (function: belongs_to) — *Edit callback factory*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|on_update_cb]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|push]] (function: belongs_to) — *Trigger background transmission of the updated UI menu state*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|rebuild_menu]] (function: belongs_to) — *Pulls stats, capabilities, and settings configuration map to rebuild the Telegram menu.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|run_clean_sync]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|run_index_dir]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|run_index_file]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|run_rebuild]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|run_reset_rebuild]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|run_sync]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/telegram/manager.py.md|start_tc]] (function: belongs_to)
<!-- SYNC:END -->
