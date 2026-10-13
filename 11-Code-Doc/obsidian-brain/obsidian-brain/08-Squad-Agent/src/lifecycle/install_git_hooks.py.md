---
source: obsidian-brain/08-Squad-Agent/src/lifecycle/install_git_hooks.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13T02:56:37.736009
---

# Mirror: install_git_hooks.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/lifecycle/install_git_hooks.py`.

> **Essential Process**:
> Installs background post-commit and post-merge git hooks inside the vault's .git/ directory. This automates the synchronization of RAG indexing and AI coding personas on Git events.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lifecycle/install_git_hooks.py.md|install_hooks]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lifecycle/install_git_hooks.py.md|main]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
