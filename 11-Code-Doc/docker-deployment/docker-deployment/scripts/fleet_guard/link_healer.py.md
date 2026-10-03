---
source: docker-deployment/scripts/fleet_guard/link_healer.py
workspace: docker-deployment
type: code-mirror
status: auto-generated
last_sync: 2026-10-01T01:10:01.862821
---

# Mirror: link_healer.py

## 📝 Description
Automatically generated mirror for `docker-deployment/scripts/fleet_guard/link_healer.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/models.py.md|LinkAudit]] (class: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/models.py.md|models.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/models.py.md|models.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/__init__.py.md|__init__.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|guided_wizard.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|guided_wizard.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|guided_wizard.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/link_healer.py.md|INVENTORY_SOURCE_REL]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/link_healer.py.md|IS_WINDOWS]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/link_healer.py.md|TARGET_CONFIG_REL]] (constant: belongs_to) — *Canonical base targets relative to workspace root*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/link_healer.py.md|audit_ecosystem_links]] (function: belongs_to) — *Audit all standalone.yaml and inventory.json links across the workspace.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/link_healer.py.md|heal_all_ecosystem_links]] (function: belongs_to) — *Repair all standalone.yaml and inventory.json links across the workspace.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/link_healer.py.md|heal_ecosystem_link]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
