---
source: obsidian-brain/08-Squad-Agent/src/lifecycle/install_git_hooks.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.537872
---

# Mirror: install_git_hooks.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/lifecycle/install_git_hooks.py`.

> **Essential Process**:
> Installs background post-commit and post-merge git hooks inside the vault's .git/ directory. This automates the synchronization of RAG indexing and AI coding personas on Git events.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/pkg/mod/github.com/!bastien-!antigravity/microservice-toolbox@v0.0.1/python/microservice_toolbox/utils/bootstrap.py.md|ensure_import_paths]] (function: calls) — *Ensure the script directory and vault root are available on sys.path.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/pkg/mod/github.com/!bastien-!antigravity/microservice-toolbox@v0.0.1/python/microservice_toolbox/utils/bootstrap.py.md|ensure_virtualenv]] (function: calls) — *Re-launch the current script using the nearest virtualenv Python if available.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/pkg/mod/github.com/!bastien-!antigravity/microservice-toolbox@v0.0.1/python/microservice_toolbox/utils/bootstrap.py.md|prepend_venv_bin]] (function: calls) — *Ensure the vault virtualenv bin/Scripts directory is on PATH.*

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/install_git_hooks.py.md|install_hooks]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/install_git_hooks.py.md|main]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
