---
source: obsidian-brain/08-Squad-Agent/src/core/switch_mode.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13T02:56:34.495462
---

# Mirror: switch_mode.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/core/switch_mode.py`.

> **Essential Process**:
> Switches the operational protocol of the AI Squad by atomically updating the MODE-MANUAL.md and all associated AI-Session-State.md files.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls) — *Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/core/controller.py.md|controller.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/core/switch_mode.py.md|MODES]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/core/switch_mode.py.md|_update_file_field]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/core/switch_mode.py.md|apply_mode_protocol]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/core/switch_mode.py.md|get_mode_choice_interactive]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/core/switch_mode.py.md|main]] (function: belongs_to) — *Entry point for standalone execution.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|manager.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|manager.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
