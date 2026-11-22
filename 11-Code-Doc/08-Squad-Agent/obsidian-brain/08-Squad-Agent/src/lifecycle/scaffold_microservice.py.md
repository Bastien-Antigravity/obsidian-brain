---
microservice: 08-Squad-Agent
type: note
status: active
tags:
- '#service/08-Squad-Agent'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py`.

> **Essential Process**:
> Scaffolds a new Bastien-Antigravity microservice adhering to canonical repository structure, mandatory root files, Docker standards, and BDD specifications.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|_is_core_workspace]] (function: belongs_to) — *Returns True when target_dir resides inside the local core Bastien-Antigravity workspace.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|_is_external_domain_workspace]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|_is_valid_workspace]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|_register_in_go_work]] (function: belongs_to) — *Ensures a newly scaffolded Go microservice is registered in the workspace go.work file.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|_resolve_brain_name]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|_to_pascal_case]] (function: belongs_to) — *Converts a kebab/snake identifier into PascalCase.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|create_file]] (function: belongs_to) — *Creates a file with parent directory creation, respecting dry-run mode.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|create_symlink]] (function: belongs_to) — *Creates a symbolic link, respecting dry-run mode.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|generate_bdd_spec]] (function: belongs_to) — *Generates the initial BDD behavior specification note in 02-Business-BDD and service spec in 06-Microservices.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|generate_common_files]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|generate_cpp_scaffold]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|generate_go_scaffold]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|generate_openmfe_component_js]] (function: belongs_to) — *Generates a standardized BastienMFEElement Web Component with dynamic Exchange Contract tabs.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|generate_python_scaffold]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|generate_rust_scaffold]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|main]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|register_sandbox_service]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|resolve_workspace_root]] (function: belongs_to) — *Resolves the Bastien-Antigravity workspace root dynamically.*
<!-- SYNC:END -->
