---
microservice: 03-Tech-Stack
type: note
status: active
tags:
- '#service/03-Tech-Stack'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `obsidian-brain/03-Tech-Stack/05-Project-Scripts/Multi-Repo-Validator.py`.

> **Essential Process**:
> Ecosystem orchestrator that discovers all microservice repositories (including selected obsidian-brain services) and triggers their build, test, or lint cycles.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[obsidian-brain/03-Tech-Stack/05-Project-Scripts/Multi-Repo-Validator.py.md|OBSIDIAN_SERVICE_REPOS]] (constant: belongs_to)
- [[obsidian-brain/03-Tech-Stack/05-Project-Scripts/Multi-Repo-Validator.py.md|_has_language_marker]] (function: belongs_to) — *Returns True if the directory contains a supported Go, Rust, or Python marker.*
- [[obsidian-brain/03-Tech-Stack/05-Project-Scripts/Multi-Repo-Validator.py.md|get_repos]] (function: belongs_to)
- [[obsidian-brain/03-Tech-Stack/05-Project-Scripts/Multi-Repo-Validator.py.md|run_all]] (function: belongs_to)
<!-- SYNC:END -->
