---
source: docker-deployment/scripts/fleet_guard/guided_wizard.py
workspace: docker-deployment
type: code-mirror
status: auto-generated
last_sync: 2026-10-01T01:10:01.851802
---

# Mirror: guided_wizard.py

## 📝 Description
Automatically generated mirror for `docker-deployment/scripts/fleet_guard/guided_wizard.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/docker-deployment/scripts/common.py.md|common.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/common.py.md|flush_stdin]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|crypto_validator.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|crypto_validator.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|encrypt_rsa]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|generate_rsa_keypair]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|resolve_keys_paths]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/link_healer.py.md|heal_all_ecosystem_links]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/link_healer.py.md|link_healer.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/link_healer.py.md|link_healer.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/models.py.md|models.py]] (imports)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|Colors]] (class: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|IS_WINDOWS]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|run_guided_setup]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|set_os_environment_variable]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|update_yaml_field]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
