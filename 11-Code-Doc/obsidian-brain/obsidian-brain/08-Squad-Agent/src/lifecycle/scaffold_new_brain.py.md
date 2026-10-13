---
source: obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13T02:56:37.724952
---

# Mirror: scaffold_new_brain.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py`.

> **Essential Process**:
> Scaffolds a new Bastien-Antigravity ecosystem directory by creating the standard folder structure, mandatory governance files, standalone.yaml symlink, and baking the AI Squad DNA into .agents/skills.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls) — *Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|create_file]] (function: belongs_to) — *Creates a file with parent directory creation, respecting dry-run mode.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|create_symlink]] (function: belongs_to) — *Creates a symbolic link, respecting dry-run mode.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|scaffold_brain]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
