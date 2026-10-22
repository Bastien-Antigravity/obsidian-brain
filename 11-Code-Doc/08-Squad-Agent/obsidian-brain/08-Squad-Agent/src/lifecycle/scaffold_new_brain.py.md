---
source: obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-20T19:59:12.317061
---

# Mirror: scaffold_new_brain.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py`.

> **Essential Process**:
> Scaffolds a new Bastien-Antigravity ecosystem directory by creating the standard folder structure, mandatory governance files, standalone.yaml symlink, and baking the AI Squad DNA into .agents/skills.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls) — *Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|create_file]] (function: belongs_to) — *Creates a file with parent directory creation, respecting dry-run mode.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|create_symlink]] (function: belongs_to) — *Creates a symbolic link, respecting dry-run mode.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|get_allocated_ecosystem_ports]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|is_port_in_use]] (function: belongs_to) — *Checks whether a port is currently open and accepting connections.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|launch_satellite_docker]] (function: belongs_to) — *Launches the newly scaffolded satellite brain squad-agent in Docker.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|main]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|resolve_available_ports]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|scaffold_brain]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
