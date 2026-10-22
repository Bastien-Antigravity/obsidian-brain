---
source: obsidian-brain/05-Fleet-Operation/01-Fleet-Action-Plans/archive.py
workspace: 05-Fleet-Operation
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.452354
---

# Mirror: archive.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/05-Fleet-Operation/01-Fleet-Action-Plans/archive.py`.

> **Essential Process**:
> Audits the Fleet Action Plans folder and archives completed or historical plans into the 'plans/' folder (with context firewall ignore rules).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/01-Fleet-Action-Plans/archive.py.md|DefaultLogger]] (class: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/01-Fleet-Action-Plans/archive.py.md|FleetActionPlansArchiver]] (class: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/01-Fleet-Action-Plans/archive.py.md|__init__]] (function: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/01-Fleet-Action-Plans/archive.py.md|_archive_files]] (function: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/01-Fleet-Action-Plans/archive.py.md|_check_active_migrations]] (function: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/01-Fleet-Action-Plans/archive.py.md|_ensure_firewall]] (function: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/01-Fleet-Action-Plans/archive.py.md|_is_plan_completed]] (function: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/01-Fleet-Action-Plans/archive.py.md|_update_moc]] (function: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/01-Fleet-Action-Plans/archive.py.md|critical]] (function: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/01-Fleet-Action-Plans/archive.py.md|error]] (function: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/01-Fleet-Action-Plans/archive.py.md|info]] (function: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/01-Fleet-Action-Plans/archive.py.md|run_archive]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
