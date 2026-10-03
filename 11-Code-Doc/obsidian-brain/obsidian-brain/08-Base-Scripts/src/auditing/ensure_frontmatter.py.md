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
Automatically generated mirror for `obsidian-brain/08-Base-Scripts/src/auditing/ensure_frontmatter.py`.

> **Essential Process**:
> Enforces YAML front-matter standards and tag taxonomy across Obsidian Brain RAG human documentation. Designed to run as a git pre-commit hook or standalone validator.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/maintenance/knowledge_compressor.py.md|run]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/ensure_frontmatter.py.md|FRONT_MATTER_PATTERN]] (constant: belongs_to) — *Patterns*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/ensure_frontmatter.py.md|get_all_documentation_files]] (function: belongs_to) — *Scans for all human documentation markdown files in quick-overview and 06-Microservices.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/ensure_frontmatter.py.md|get_modified_files]] (function: belongs_to) — *Retrieves list of modified and cached markdown files using git.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/ensure_frontmatter.py.md|is_documentation_file]] (function: belongs_to) — *Determines whether a markdown file is human documentation subject to frontmatter checks.*
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/ensure_frontmatter.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/ensure_frontmatter.py.md|normalize_frontmatter]] (function: belongs_to)
<!-- SYNC:END -->
