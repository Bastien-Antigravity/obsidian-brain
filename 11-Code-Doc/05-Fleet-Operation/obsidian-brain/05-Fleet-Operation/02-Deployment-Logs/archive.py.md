---
source: obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py
workspace: 05-Fleet-Operation
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:55.429869
---

# Mirror: archive.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py`.

> **Essential Process**:
> Audits the Deployment Logs folder and archives historical deployment logs into the 'deployments/' folder (with context firewall ignore rules).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/server.py.md|write]] (function: calls)

### 🔌 Consumers (Inbound)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|DefaultLogger]] (class: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|DeploymentLogsArchiver]] (class: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|__init__]] (function: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|_archive_files]] (function: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|_ensure_firewall]] (function: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|_identify_logs]] (function: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|_update_moc]] (function: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|critical]] (function: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|error]] (function: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|info]] (function: belongs_to)
- [[05-Fleet-Operation/obsidian-brain/05-Fleet-Operation/02-Deployment-Logs/archive.py.md|run_archive]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
