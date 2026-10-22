---
source: obsidian-brain/08-Squad-Agent/src/auditing/ensure_frontmatter.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.747887
---

# Mirror: ensure_frontmatter.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/auditing/ensure_frontmatter.py`.

> **Essential Process**:
> Enforces YAML front-matter standards and tag taxonomy across Obsidian Brain RAG human documentation. Designed to run as a git pre-commit hook or standalone validator.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/knowledge_compressor.py.md|run]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/ensure_frontmatter.py.md|FRONT_MATTER_PATTERN]] (constant: belongs_to) — *Patterns*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/ensure_frontmatter.py.md|get_all_documentation_files]] (function: belongs_to) — *Scans for all human documentation markdown files in quick-overview and 06-Microservices.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/ensure_frontmatter.py.md|get_modified_files]] (function: belongs_to) — *Retrieves list of modified and cached markdown files using git.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/ensure_frontmatter.py.md|is_documentation_file]] (function: belongs_to) — *Determines whether a markdown file is human documentation subject to frontmatter checks.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/ensure_frontmatter.py.md|main]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/ensure_frontmatter.py.md|normalize_frontmatter]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
