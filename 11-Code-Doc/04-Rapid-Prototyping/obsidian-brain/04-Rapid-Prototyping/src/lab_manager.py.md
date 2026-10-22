---
source: obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py
workspace: 04-Rapid-Prototyping
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.423749
---

# Mirror: lab_manager.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py`.

> **Essential Process**:
> 🧪 Lab Manager utility for Level 04 Rapid Prototyping Sandbox. Automates sandbox directory creation, repository cloning, stub extraction, and archiving.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[04-Rapid-Prototyping/obsidian-brain/04-Rapid-Prototyping/lab_manager.py.md|lab_manager.py]] (calls)
- [[04-Rapid-Prototyping/obsidian-brain/04-Rapid-Prototyping/lab_manager.py.md|lab_manager.py]] (imports)
- [[04-Rapid-Prototyping/obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py.md|clone_repo]] (function: belongs_to) — *Clones a microservice repository into the sandbox folder's clones directory.*
- [[04-Rapid-Prototyping/obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py.md|create_sandbox]] (function: belongs_to) — *Creates a dedicated sandbox workspace folder at the root of L04.*
- [[04-Rapid-Prototyping/obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py.md|extract_file]] (function: belongs_to) — *Extracts a specific file from a clone into the sandbox stubs folder.*
- [[04-Rapid-Prototyping/obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py.md|get_repo_url]] (function: belongs_to) — *Resolves repo name to Git URL using the fleet inventory.*
- [[04-Rapid-Prototyping/obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py.md|load_inventory]] (function: belongs_to) — *Attempts to load the repository inventory from Level 05.*
- [[04-Rapid-Prototyping/obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py.md|main]] (function: belongs_to)
- [[04-Rapid-Prototyping/obsidian-brain/04-Rapid-Prototyping/src/lab_manager.py.md|print_help]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|main.py]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
