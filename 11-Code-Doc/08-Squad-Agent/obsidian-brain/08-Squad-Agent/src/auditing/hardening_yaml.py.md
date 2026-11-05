---
source: obsidian-brain/08-Squad-Agent/src/auditing/hardening_yaml.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22 16:53:55.718491
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
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
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/pkg/mod/github.com/!bastien-!antigravity/microservice-toolbox@v0.0.1/python/microservice_toolbox/utils/bootstrap.py.md|ensure_import_paths]] (function: calls) — *Ensure the script directory and vault root are available on sys.path.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/pkg/mod/github.com/!bastien-!antigravity/microservice-toolbox@v0.0.1/python/microservice_toolbox/utils/bootstrap.py.md|ensure_virtualenv]] (function: calls) — *Re-launch the current script using the nearest virtualenv Python if available.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/pkg/mod/github.com/!bastien-!antigravity/microservice-toolbox@v0.0.1/python/microservice_toolbox/utils/bootstrap.py.md|prepend_venv_bin]] (function: calls) — *Ensure the vault virtualenv bin/Scripts directory is on PATH.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

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
