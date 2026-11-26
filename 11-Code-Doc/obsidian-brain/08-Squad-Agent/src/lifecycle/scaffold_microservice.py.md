---
source: obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:34.567014
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: scaffold_microservice.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py`.

> **Essential Process**:
> CLI entrypoint and orchestration facade for scaffolding Bastien-Antigravity microservices, delegating language-specific code generation to modular single-concern generators under src.lifecycle.scaffolder.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|_is_external_domain_workspace]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|generate_bdd_spec]] (function: calls) — *Generates the initial BDD behavior specification note in 02-Business-BDD and service spec in 06-Microservices.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|generate_common_files]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|register_sandbox_service]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|resolve_workspace_root]] (function: calls) — *Resolves the active workspace root dynamically without hardcoded folder names.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/cpp_generator.py.md|generate_cpp_scaffold]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/go_generator.py.md|generate_go_scaffold]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/python_generator.py.md|generate_python_scaffold]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/rust_generator.py.md|generate_rust_scaffold]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/models/build_spec.py.md|allocate_domain_port]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/models/build_spec.py.md|build_spec.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|main]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
