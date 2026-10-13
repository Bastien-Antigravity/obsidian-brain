---
source: obsidian-brain/08-Squad-Agent/src/auditing/brain_health_audit.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13T02:56:34.722531
---

# Mirror: brain_health_audit.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/auditing/brain_health_audit.py`.

> **Essential Process**:
> Audits the Obsidian vault for structural integrity, YAML compliance, and link health.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|VAULT_ROOT]] (constant: calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|WORKSPACE_ROOT]] (constant: calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|hardening_yaml.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|audit_file]] (function: calls) — *Audits a single source file and returns a list of detected violations.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/auditing/validate_compliance.py.md|validate_compliance.py]] (same_package)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/interfaces/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/interfaces/auditor.py.md|Auditor]] (class: calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|Sovereignty]] (class: calls)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|auto_fix_file]] (function: calls) — *Fixes taxonomy issues, enforces YAML frontmatter schema, and automatically converts absolute links to relative ones.*
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|get_report]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/auditing/brain_health_audit.py.md|BrainSentinel]] (class: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/auditing/brain_health_audit.py.md|IGNORE_DIRS]] (constant: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/auditing/brain_health_audit.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/auditing/brain_health_audit.py.md|audit]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/auditing/brain_health_audit.py.md|auto_fix]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/auditing/brain_health_audit.py.md|main]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/auditing/brain_health_audit.py.md|report]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/08-Squad-Agent/src/auditing/brain_health_audit.py.md|scan]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
