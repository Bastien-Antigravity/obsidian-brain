---
source: obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-26T19:45:04.169413
---

# Mirror: common.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py`.

> **Essential Process**:
> Shared filesystem helpers, workspace/Cargo/Go-work registration utilities, OpenMFE Web Component bundle builder, multi-stage Docker/CI/Makefile common file generator, and BDD specification emitter for Bastien-Antigravity microservice scaffolding.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|scaffold_microservice.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|_discover_rust_library_crates]] (function: belongs_to) — *Scans workspace_root for local Rust library crates (Cargo.toml + src/lib.rs).*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|_is_core_workspace]] (function: belongs_to) — *Returns True when target_dir resides inside the local core Bastien-Antigravity workspace.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|_is_external_domain_workspace]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|_is_valid_workspace]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|_register_in_cargo_config]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|_register_in_go_work]] (function: belongs_to) — *Ensures a newly scaffolded Go microservice is registered in the workspace go.work file.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|_resolve_brain_name]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|_to_pascal_case]] (function: belongs_to) — *Converts a kebab/snake identifier into PascalCase.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|create_file]] (function: belongs_to) — *Creates a file with parent directory creation, respecting dry-run mode.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|create_symlink]] (function: belongs_to) — *Creates a symbolic link, respecting dry-run mode.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|generate_bdd_spec]] (function: belongs_to) — *Generates the initial BDD behavior specification note in 02-Business-BDD and service spec in 06-Microservices.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|generate_common_files]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|generate_openmfe_component_js]] (function: belongs_to) — *Generates a standardized BastienMFEElement Web Component with dynamic Exchange Contract tabs.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|register_sandbox_service]] (function: belongs_to)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|resolve_workspace_root]] (function: belongs_to) — *Resolves the active workspace root dynamically without hardcoded folder names.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/cpp_generator.py.md|cpp_generator.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/cpp_generator.py.md|cpp_generator.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/cpp_generator.py.md|cpp_generator.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/go_generator.py.md|go_generator.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/go_generator.py.md|go_generator.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/go_generator.py.md|go_generator.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/python_generator.py.md|python_generator.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/python_generator.py.md|python_generator.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/python_generator.py.md|python_generator.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/rust_generator.py.md|rust_generator.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/rust_generator.py.md|rust_generator.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/rust_generator.py.md|rust_generator.py]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
