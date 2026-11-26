---
source: obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/go_generator.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-26T19:45:04.160780
---

# Mirror: go_generator.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/go_generator.py`.

> **Essential Process**:
> Generates a compliant Go 1.25 microservice repository skeleton wired to microservice-toolbox (BootstrapService, OnLiveConfUpdate, PublishWithLifecycle, ExchangeContracts, OpenMFE, and standalone Zone-1 unit tests).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|_is_core_workspace]] (function: calls) — *Returns True when target_dir resides inside the local core Bastien-Antigravity workspace.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|_register_in_go_work]] (function: calls) — *Ensures a newly scaffolded Go microservice is registered in the workspace go.work file.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|_resolve_brain_name]] (function: calls)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|common.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|common.py]] (same_package)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|create_file]] (function: calls) — *Creates a file with parent directory creation, respecting dry-run mode.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|generate_openmfe_component_js]] (function: calls) — *Generates a standardized BastienMFEElement Web Component with dynamic Exchange Contract tabs.*
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/common.py.md|resolve_workspace_root]] (function: calls) — *Resolves the active workspace root dynamically without hardcoded folder names.*

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffold_microservice.py.md|scaffold_microservice.py]] (calls)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/08-Squad-Agent/src/lifecycle/scaffolder/go_generator.py.md|generate_go_scaffold]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
