---
source: obsidian-brain/08-Base-Scripts/src/auditing/audit_ports.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-01T01:10:02.915785
---

# Mirror: audit_ports.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Base-Scripts/src/auditing/audit_ports.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/hardening_yaml.py.md|VAULT_ROOT]] (constant: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/hardening_yaml.py.md|WORKSPACE_ROOT]] (constant: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/hardening_yaml.py.md|hardening_yaml.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/audit_ports.py.md|audit_ports]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/audit_ports.py.md|load_compose_ports]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/audit_ports.py.md|load_registry_ports]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/audit_ports.py.md|load_ssot_capabilities]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/audit_ports.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/audit_ports.py.md|parse_env_default]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/preflight_check.py.md|preflight_check.py]] (calls)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/preflight_check.py.md|preflight_check.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Base-Scripts/src/auditing/preflight_check.py.md|preflight_check.py]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
