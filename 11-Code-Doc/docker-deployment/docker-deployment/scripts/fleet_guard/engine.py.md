---
source: docker-deployment/scripts/fleet_guard/engine.py
workspace: docker-deployment
type: code-mirror
status: auto-generated
last_sync: 2026-10-01T01:10:01.857233
---

# Mirror: engine.py

## 📝 Description
Automatically generated mirror for `docker-deployment/scripts/fleet_guard/engine.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/docker-deployment/scripts/common.py.md|WORKSPACE_ROOT]] (constant: calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|common.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/common.py.md|flush_stdin]] (function: calls) — *Flush pending input characters from console and sys.stdin buffer.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/coherence_auditor.py.md|audit_coherence]] (function: calls) — *Audit cross-service parameter consistency and port conflicts.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/coherence_auditor.py.md|coherence_auditor.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/coherence_auditor.py.md|coherence_auditor.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|audit_cryptography]] (function: calls) — *Perform comprehensive audit of RSA keypair and canary decryption.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|crypto_validator.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|crypto_validator.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/git_verifier.py.md|audit_all_repositories]] (function: calls) — *Audit all repositories defined for the specified deployment mode.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/git_verifier.py.md|clone_missing_repositories]] (function: calls) — *Clone missing repositories from GitHub into workspace root.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/git_verifier.py.md|git_verifier.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/git_verifier.py.md|git_verifier.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|guided_wizard.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|guided_wizard.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|run_guided_setup]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/link_healer.py.md|audit_ecosystem_links]] (function: calls) — *Audit all standalone.yaml and inventory.json links across the workspace.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/link_healer.py.md|heal_all_ecosystem_links]] (function: calls) — *Repair all standalone.yaml and inventory.json links across the workspace.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/link_healer.py.md|link_healer.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/link_healer.py.md|link_healer.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/models.py.md|AuditReport]] (class: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/models.py.md|PreflightOptions]] (class: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/models.py.md|models.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/models.py.md|models.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/param_inspector.py.md|audit_parameters]] (function: calls) — *Audit all sensitive and required ecosystem parameters.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/param_inspector.py.md|param_inspector.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/param_inspector.py.md|param_inspector.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/modes/docker/run.py.md|run.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/branch.py.md|branch.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/ghcr/auth.py.md|auth.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/ghcr/publisher.py.md|publisher.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/ide/setup_ide.py.md|setup_ide.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/infra.py.md|infra.py]] (calls)
- [[docker-deployment/docker-deployment/modes/local/run.py.md|run.py]] (calls)
- [[docker-deployment/docker-deployment/modes/production/run.py.md|run.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/common.py.md|common.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet.py.md|fleet.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/__init__.py.md|__init__.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|crypto_validator.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|crypto_validator.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|PreflightEngine]] (class: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|__init__]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|display_report]] (function: belongs_to) — *Render a clean, structured visual report in the terminal.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|run]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|run_preflight]] (function: belongs_to) — *Convenience functional entry point for mode runners.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/git_verifier.py.md|git_verifier.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/git_verifier.py.md|git_verifier.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|guided_wizard.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|guided_wizard.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|operations.py]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
