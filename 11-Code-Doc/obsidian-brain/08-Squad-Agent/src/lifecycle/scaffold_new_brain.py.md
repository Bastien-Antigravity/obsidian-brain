---
source: obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:37.724952
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: scaffold_new_brain.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py`.

> **Essential Process**:
> Scaffolds a new Bastien-Antigravity ecosystem directory by creating the standard folder structure, mandatory governance files, standalone.yaml symlink, and baking the AI Squad DNA into .agents/skills.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/fleet/convert_agents.py.md|compile_skills]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/fleet/convert_agents.py.md|convert_agents.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls) — *Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems.*
- [[obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|get_pg_pool]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|pg_pool.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lib/pg_pool.py.md|resolve_schema_name]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|_build_full_capabilities_yaml]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|_register_workspace_with_rag]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|_resolve_rag_base_url]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|_resolve_rag_purge_url]] (function: belongs_to) — *Resolves the 09-RAG-Engine REST purge URL.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|_scan_root_for_crates]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|_seed_workspace_cargo_config]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|_seed_workspace_go_work]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|create_file]] (function: belongs_to) — *Creates a file with parent directory creation, respecting dry-run mode.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|create_symlink]] (function: belongs_to) — *Creates a symbolic link, respecting dry-run mode.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|destroy_sandbox_brain]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|generate_sandbox_standalone_yaml]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|get_allocated_ecosystem_ports]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|is_port_in_use]] (function: belongs_to) — *Checks whether a port is currently open and accepting connections.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|launch_satellite_docker]] (function: belongs_to) — *Launches the newly scaffolded satellite brain squad-agent in Docker.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|main]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|resolve_active_fleet_host]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|resolve_available_ports]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|scaffold_brain]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|scaffold_workspace]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|seed_domain_repo_control]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_new_brain.py.md|seed_sandbox_repo_control]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
