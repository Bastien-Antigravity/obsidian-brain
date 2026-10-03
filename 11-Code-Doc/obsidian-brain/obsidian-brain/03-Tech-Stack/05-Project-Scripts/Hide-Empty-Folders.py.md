---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `obsidian-brain/03-Tech-Stack/05-Project-Scripts/Hide-Empty-Folders.py`.

> **Essential Process**:
> Hides folders in Obsidian that do not contain any .md files (directly or recursively) by generating a CSS snippet for the UI.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/03-Tech-Stack/05-Project-Scripts/Hide-Empty-Folders.py.md|CSS_FILE]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/03-Tech-Stack/05-Project-Scripts/Hide-Empty-Folders.py.md|IGNORE_DIRS]] (constant: belongs_to) — *Directories to ignore completely*
- [[obsidian-brain/obsidian-brain/03-Tech-Stack/05-Project-Scripts/Hide-Empty-Folders.py.md|OBSIDIAN_DIR]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/03-Tech-Stack/05-Project-Scripts/Hide-Empty-Folders.py.md|SCRIPT_DIR]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/03-Tech-Stack/05-Project-Scripts/Hide-Empty-Folders.py.md|SNIPPETS_DIR]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/03-Tech-Stack/05-Project-Scripts/Hide-Empty-Folders.py.md|VAULT_ROOT]] (constant: belongs_to) — *tech-stack-brain/05-Project-Scripts -> parent is tech-stack-brain -> parent is obsidian-brain (VAULT_ROOT)*
- [[obsidian-brain/obsidian-brain/03-Tech-Stack/05-Project-Scripts/Hide-Empty-Folders.py.md|contains_md_recursive]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/03-Tech-Stack/05-Project-Scripts/Hide-Empty-Folders.py.md|css_escape]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/03-Tech-Stack/05-Project-Scripts/Hide-Empty-Folders.py.md|main]] (function: belongs_to)
<!-- SYNC:END -->
