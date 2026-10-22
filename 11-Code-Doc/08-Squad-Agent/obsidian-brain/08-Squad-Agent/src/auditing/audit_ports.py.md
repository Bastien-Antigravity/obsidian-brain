---
source: obsidian-brain/08-Squad-Agent/src/auditing/audit_ports.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.758306
---

# Mirror: audit_ports.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/auditing/audit_ports.py`.

> **Essential Process**:
> 4-Layer Port and Capability Drift Auditor and Auto-Synchronizer. Guarantees that ports and capability mappings across all 4 architectural layers: Layer 1: native.yaml (Authoritative Source of Truth) Layer 2: docker-compose.yaml (Container Manifests & Environment Variables) Layer 3: service-registry.json (Fleet Data Registry) Layer 4: Documentation (12-Docker-Deployment-Standards.md & Ecosystem-Onboarding-Guide.md) remain in 100% mechanical alignment without manual drift.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|VAULT_ROOT]] (constant: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|WORKSPACE_ROOT]] (constant: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|hardening_yaml.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|setup_terminal]] (function: calls) — *Standardizes stdout terminal output encoding to UTF-8 on Windows and POSIX systems.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/audit_ports.py.md|audit_ports]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/audit_ports.py.md|load_compose_ports]] (function: belongs_to) — *Loads port bindings and env defaults from docker-compose.yaml.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/audit_ports.py.md|load_registry_ports]] (function: belongs_to) — *Loads services from service-registry.json.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/audit_ports.py.md|load_ssot_capabilities]] (function: belongs_to) — *Loads authoritative port mappings from native.yaml.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/audit_ports.py.md|main]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/audit_ports.py.md|parse_env_default]] (function: belongs_to) — *Extracts numeric port default from '${VAR:DEFAULT}', '${VAR:-DEFAULT}' or raw int/str.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|preflight_check.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|preflight_check.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|preflight_check.py]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
