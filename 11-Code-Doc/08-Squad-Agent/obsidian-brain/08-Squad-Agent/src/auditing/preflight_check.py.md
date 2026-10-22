---
source: obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.741481
---

# Mirror: preflight_check.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py`.

> **Essential Process**:
> Cross-platform Preflight Check that runs before every squad startup. Detects and auto-repairs common drift issues across the brain ecosystem.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/audit_ports.py.md|audit_ports.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/audit_ports.py.md|audit_ports.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/audit_ports.py.md|audit_ports]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|WORKSPACE_ROOT]] (constant: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|hardening_yaml.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|ComplianceAuditor]] (class: calls) — *Mechanical compliance scanner for code files.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|audit_path]] (function: calls) — *Audits a path (file or recursive directory).*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|validate_compliance.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|validate_compliance.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_version.py.md|fleet_version.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_version.py.md|inspect_repo_version]] (function: calls) — *Inspects VERSION.txt and AI-Project-DNA.md within a repository directory.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_version.py.md|resolve_target_repos]] (function: calls) — *Resolves target repositories to operate on.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls) — *Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|walk]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|SUBMODULE_MAP]] (constant: belongs_to) — *Submodule mapping: folder name inside vault -> sibling repo name*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|_check_ecosystem_tooling_parity]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|_check_essential_files]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|_check_inventory_portability]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|_check_manifest_elements]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|_check_mode_consistency]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|_check_ports_and_capabilities]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|_check_spec_parity]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|_check_submodules]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|_check_versioning_integrity]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|main]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|run_preflight]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
