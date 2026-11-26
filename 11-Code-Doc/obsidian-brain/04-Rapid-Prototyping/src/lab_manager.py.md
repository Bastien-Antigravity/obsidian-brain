---
microservice: 04-Rapid-Prototyping
type: note
status: active
tags:
- '#service/04-Rapid-Prototyping'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py`.

> **Essential Process**:
> 🧪 Lab Manager utility for Level 04 Rapid Prototyping Sandbox. Automates sandbox directory creation, repository cloning, stub extraction, and archiving.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[obsidian-brain/04-Rapid-Prototyping/lab_manager.py.md|lab_manager.py]] (calls)
- [[obsidian-brain/04-Rapid-Prototyping/lab_manager.py.md|lab_manager.py]] (imports)
- [[obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py.md|clone_repo]] (function: belongs_to) — *Clones a microservice repository into the sandbox folder's clones directory.*
- [[obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py.md|create_sandbox]] (function: belongs_to) — *Creates a dedicated sandbox workspace folder at the root of L04.*
- [[obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py.md|extract_file]] (function: belongs_to) — *Extracts a specific file from a clone into the sandbox stubs folder.*
- [[obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py.md|get_repo_url]] (function: belongs_to) — *Resolves repo name to Git URL using the fleet inventory.*
- [[obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py.md|load_inventory]] (function: belongs_to) — *Attempts to load the repository inventory from Level 05.*
- [[obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py.md|main]] (function: belongs_to)
- [[obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py.md|print_help]] (function: belongs_to)
<!-- SYNC:END -->
