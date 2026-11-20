---
source: obsidian-brain/03-Tech-Stack/05-Project-Scripts/Multi-Repo-Validator.py
workspace: 03-Tech-Stack
type: code-mirror
status: auto-generated
last_sync: 2026-10-22 16:53:55.392019
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: Multi-Repo-Validator.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/03-Tech-Stack/05-Project-Scripts/Multi-Repo-Validator.py`.

> **Essential Process**:
> Ecosystem orchestrator that discovers all microservice repositories (including selected obsidian-brain services) and triggers their build, test, or lint cycles.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)

### 🔌 Consumers (Inbound)
- [[03-Tech-Stack/obsidian-brain/03-Tech-Stack/05-Project-Scripts/Multi-Repo-Validator.py.md|OBSIDIAN_SERVICE_REPOS]] (constant: belongs_to)
- [[03-Tech-Stack/obsidian-brain/03-Tech-Stack/05-Project-Scripts/Multi-Repo-Validator.py.md|_has_language_marker]] (function: belongs_to) — *Returns True if the directory contains a supported Go, Rust, or Python marker.*
- [[03-Tech-Stack/obsidian-brain/03-Tech-Stack/05-Project-Scripts/Multi-Repo-Validator.py.md|get_repos]] (function: belongs_to)
- [[03-Tech-Stack/obsidian-brain/03-Tech-Stack/05-Project-Scripts/Multi-Repo-Validator.py.md|run_all]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
