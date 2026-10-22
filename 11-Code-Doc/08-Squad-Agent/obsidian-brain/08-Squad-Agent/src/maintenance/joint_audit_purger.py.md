---
source: obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.712808
---

# Mirror: joint_audit_purger.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py`.

> **Essential Process**:
> Dark Matter Scanner and Purger for the obsidian-brain knowledge base. Scans markdown files in the vault to identify orphan documents without incoming Obsidian wikilinks. Supports generating review checklists and executing authorized deletions.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/bootstrap/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|walk]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|GLOBAL_EXCLUDES]] (constant: belongs_to) — *Sync with RAG Engine's GLOBAL_EXCLUDES*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|_find_vault_root]] (function: belongs_to) — *Finds the obsidian-brain directory relative to the script.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|execute_purge]] (function: belongs_to) — *Reads the approval checklist and deletes files marked for deletion.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|generate_purge_approval_request]] (function: belongs_to) — *Generates the Markdown approval checklist for human or agent review.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|is_ignored_by_firewall]] (function: belongs_to) — *Checks if a path is ignored by context firewalls (.aiignore etc) or carries the #ai/ignore tag.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|joint_audit]] (function: belongs_to) — *Scans the vault for orphaned markdown files and records purge candidates.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/maintenance/joint_audit_purger.py.md|main]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/constants.py.md|constants.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/alignment/synchronizer.py.md|synchronizer.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/engine.py.md|engine.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|standard.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/mcp/tools.py.md|tools.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/watcher/file_watcher.py.md|file_watcher.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|server.py]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
