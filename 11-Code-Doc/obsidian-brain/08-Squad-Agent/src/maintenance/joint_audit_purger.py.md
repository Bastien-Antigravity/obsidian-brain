---
source: obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py
workspace: obsidian-brain
type: code-mirror
status: auto-generated
last_sync: 2026-10-13 02:56:34.689853
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: joint_audit_purger.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py`.

> **Essential Process**:
> Dark Matter Scanner and Purger for the obsidian-brain knowledge base. Scans markdown files in the vault to identify orphan documents without incoming Obsidian wikilinks. Supports generating review checklists and executing authorized deletions.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|GLOBAL_EXCLUDES]] (constant: belongs_to) — *Sync with RAG Engine's GLOBAL_EXCLUDES*
- [[obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|_find_vault_root]] (function: belongs_to) — *Finds the obsidian-brain directory relative to the script.*
- [[obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|execute_purge]] (function: belongs_to) — *Reads the approval checklist and deletes files marked for deletion.*
- [[obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|generate_purge_approval_request]] (function: belongs_to) — *Generates the Markdown approval checklist for human or agent review.*
- [[obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|is_ignored_by_firewall]] (function: belongs_to) — *Checks if a path is ignored by context firewalls (.aiignore etc) or carries the #ai/ignore tag.*
- [[obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|joint_audit]] (function: belongs_to) — *Scans the vault for orphaned markdown files and records purge candidates.*
- [[obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|main]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
