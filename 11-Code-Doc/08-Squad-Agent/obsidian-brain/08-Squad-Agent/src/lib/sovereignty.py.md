---
source: obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.686005
---

# Mirror: sovereignty.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py`.

> **Essential Process**:
> Sovereignty Engine and Centralized Knowledge Validation Library. Enforces YAML frontmatter schema, Obsidian tag taxonomy, and cross-reference integrity across the Bastien-Antigravity ecosystem notes.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|add]] (function: calls) — *Appends a new turn to the in-memory buffer, capping size.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/memory.py.md|memory.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/brain_health_audit.py.md|brain_health_audit.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/auditing/brain_health_audit.py.md|brain_health_audit.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/close_mission.py.md|close_mission.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/close_mission.py.md|close_mission.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|fleet_commander.py]] (calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/fleet/fleet_commander.py.md|fleet_commander.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|Sovereignty]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|_index_workspace]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|_load_taxonomy]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|audit_file]] (function: belongs_to) — *Runs the full suite against a single file.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|auto_fix_file]] (function: belongs_to) — *Fixes taxonomy issues, enforces YAML frontmatter schema, and automatically converts absolute links to relative ones.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|get_report]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|is_ignored_by_firewall]] (function: belongs_to) — *Checks if a path is ignored by context firewalls (.aiignore etc) or carries the #ai/ignore tag.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|log_error]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|log_warning]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|validate_frontmatter]] (function: belongs_to) — *Checks for mandatory YAML frontmatter fields.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|validate_hardcoded_paths]] (function: belongs_to) — *Ensures that no hardcoded absolute local paths are used in links.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|validate_isolation_zone]] (function: belongs_to) — *Checks for the presence and structure of the isolation zone.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|validate_links]] (function: belongs_to) — *Identifies broken [[Links]], ignoring those inside code blocks.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|validate_orphan_tags]] (function: belongs_to) — *Identifies tags not defined in the taxonomy, ignoring hex colors and code blocks.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|validate_placeholders]] (function: belongs_to) — *Ensures that template placeholders like {{microservice}} are resolved.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|validate_session_state]] (function: belongs_to) — *Checks for Mission-ID in session states.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|validate_taxonomy]] (function: belongs_to) — *Ensures mandatory and transversal tags are present.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|validate_telemetry]] (function: belongs_to) — *Ensures Roles have the [SCAN] block.*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/sovereignty.py.md|validate_utc_mandate]] (function: belongs_to) — *Heuristic check for prohibited local time references.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
