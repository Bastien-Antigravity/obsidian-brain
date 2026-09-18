

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/ensure_frontmatter.py.md|FRONT_MATTER_PATTERN]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/ensure_frontmatter.py.md|get_all_documentation_files]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/ensure_frontmatter.py.md|get_modified_files]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/ensure_frontmatter.py.md|is_documentation_file]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/ensure_frontmatter.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/ensure_frontmatter.py.md|normalize_frontmatter]] (function: belongs_to)
<!-- SYNC:END -->
