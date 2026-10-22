---
source: obsidian-brain/08-Squad-Agent/src/lifecycle/unlock_vault.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.533643
---

# Mirror: unlock_vault.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/lifecycle/unlock_vault.py`.

> **Essential Process**:
> Restores read/write permissions (chmod 0755/0644) to role prompts in Tech Stack and Core KMS, enabling AI adapters and templates to be synchronized and edited across the fleet.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls) — *Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|walk]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/unlock_vault.py.md|main]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/unlock_vault.py.md|unlock_role_prompts]] (function: belongs_to) — *Recursively restores permissions to Role-Prompts directories.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
