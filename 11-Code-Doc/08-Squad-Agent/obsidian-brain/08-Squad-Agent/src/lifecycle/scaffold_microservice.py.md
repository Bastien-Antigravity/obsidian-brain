

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|create_file]] (function: belongs_to) — *Creates a file with parent directory creation, respecting dry-run mode.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|create_symlink]] (function: belongs_to) — *Creates a symbolic link, respecting dry-run mode.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|generate_bdd_spec]] (function: belongs_to) — *Generates the initial BDD behavior specification note in 02-Business-BDD.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|generate_common_files]] (function: belongs_to) — *Generates files mandatory across all languages: Dockerfile, compose, AGENTS.md, etc.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|generate_go_scaffold]] (function: belongs_to) — *Generates the Go microservice skeleton and source files.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|generate_python_scaffold]] (function: belongs_to) — *Generates the Python microservice skeleton and architecture folders.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|generate_rust_scaffold]] (function: belongs_to) — *Generates the Rust microservice skeleton and source files.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|main]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|resolve_workspace_root]] (function: belongs_to) — *Resolves the Bastien-Antigravity workspace root dynamically.*
<!-- SYNC:END -->
