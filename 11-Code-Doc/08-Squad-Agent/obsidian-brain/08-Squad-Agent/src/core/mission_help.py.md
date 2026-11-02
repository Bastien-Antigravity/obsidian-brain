---
source: obsidian-brain/08-Squad-Agent/src/core/mission_help.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.488849
---

# Mirror: mission_help.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/core/mission_help.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls) — *Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/pkg/mod/github.com/!bastien-!antigravity/microservice-toolbox@v0.0.1/python/microservice_toolbox/utils/bootstrap.py.md|ensure_import_paths]] (function: calls) — *Ensure the script directory and vault root are available on sys.path.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/pkg/mod/github.com/!bastien-!antigravity/microservice-toolbox@v0.0.1/python/microservice_toolbox/utils/bootstrap.py.md|ensure_virtualenv]] (function: calls) — *Re-launch the current script using the nearest virtualenv Python if available.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/pkg/mod/github.com/!bastien-!antigravity/microservice-toolbox@v0.0.1/python/microservice_toolbox/utils/bootstrap.py.md|prepend_venv_bin]] (function: calls) — *Ensure the vault virtualenv bin/Scripts directory is on PATH.*

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/mission_help.py.md|MissionHelper]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/mission_help.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/mission_help.py.md|main]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/mission_help.py.md|print_cheat_sheet]] (function: belongs_to) — *Prints the formatted help content to stdout.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/core/start_squad.py.md|start_squad.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
