---
source: obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.718491
---

# Mirror: hardening_yaml.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py`.

> **Essential Process**:
> Enforces mandatory YAML frontmatter (microservice, type, status) across all markdown files in the Obsidian vault based on their directory location.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/audit_ports.py.md|audit_ports.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/audit_ports.py.md|audit_ports.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/brain_health_audit.py.md|brain_health_audit.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/brain_health_audit.py.md|brain_health_audit.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|check_coherence.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/check_coherence.py.md|check_coherence.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|VAULT_ROOT]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|WORKSPACE_ROOT]] (constant: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|ZONE_MAP]] (constant: belongs_to) — *Mapping of folder prefixes to metadata*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|_find_workspace_root]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|apply_hardening]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py.md|main]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|preflight_check.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/preflight_check.py.md|preflight_check.py]] (same_package)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fix_feats.py.md|fix_feats.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/map_feats.py.md|map_feats.py]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
