---
source: docker-deployment/scripts/ghcr_cleaner.py
workspace: docker-deployment
type: code-mirror
status: auto-generated
last_sync: 2026-10-23T13:14:29.516475
---

# Mirror: ghcr_cleaner.py

## 📝 Description
Automatically generated mirror for `docker-deployment/scripts/ghcr_cleaner.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/docker-deployment/scripts/common.py.md|common.py]] (imports)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/ghcr_cleaner.py.md|CONTAINER_PACKAGES]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/ghcr_cleaner.py.md|DEPLOY_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/ghcr_cleaner.py.md|MODES_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/ghcr_cleaner.py.md|SCRIPTS_DIR]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/ghcr_cleaner.py.md|check_token_scopes]] (function: belongs_to) — *Verify GitHub Token and return authenticated username and scopes.*
- [[docker-deployment/docker-deployment/scripts/ghcr_cleaner.py.md|delete_package_version]] (function: belongs_to) — *Delete a specific package version on GHCR.*
- [[docker-deployment/docker-deployment/scripts/ghcr_cleaner.py.md|fetch_package_versions]] (function: belongs_to) — *Fetch all versions of a container package.*
- [[docker-deployment/docker-deployment/scripts/ghcr_cleaner.py.md|get_token_and_user]] (function: belongs_to) — *Retrieve GitHub user and token from environment.*
- [[docker-deployment/docker-deployment/scripts/ghcr_cleaner.py.md|run_cleaner]] (function: belongs_to) — *Audit and optionally purge untagged / orphaned container versions.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
