---
source: docker-deployment/scripts/fleet_guard/git_verifier.py
workspace: docker-deployment
type: code-mirror
status: auto-generated
last_sync: 2026-10-01T01:10:01.848448
---

# Mirror: git_verifier.py

## 📝 Description
Automatically generated mirror for `docker-deployment/scripts/fleet_guard/git_verifier.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|run]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/models.py.md|RepoAudit]] (class: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/models.py.md|models.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/models.py.md|models.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/__init__.py.md|__init__.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/git_verifier.py.md|CANONICAL_BRANCH]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/git_verifier.py.md|DEFAULT_GITHUB_ORG]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/git_verifier.py.md|WORKSPACE_REPOSITORIES]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/git_verifier.py.md|audit_all_repositories]] (function: belongs_to) — *Audit all repositories defined for the specified deployment mode.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/git_verifier.py.md|audit_repository]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/git_verifier.py.md|clone_missing_repositories]] (function: belongs_to) — *Clone missing repositories from GitHub into workspace root.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/git_verifier.py.md|load_mode_repositories]] (function: belongs_to) — *Load ecosystem repository manifest for the targeted execution mode.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
