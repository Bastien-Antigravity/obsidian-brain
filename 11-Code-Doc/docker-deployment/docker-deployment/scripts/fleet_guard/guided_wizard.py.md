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
- [[docker-deployment/docker-deployment/scripts/common.py.md|flush_stdin]] (function: calls) — *Flush pending input characters from console and sys.stdin buffer.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|crypto_validator.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|crypto_validator.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|encrypt_rsa]] (function: calls) — *Encrypt a secret string with RSA public key into ENC(...) format.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|generate_rsa_keypair]] (function: calls) — *Generate sovereign RSA 2048-bit keypair strictly outside Git.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|is_git_tracked_or_unsafe]] (function: calls) — *Ensure cryptographic keys are strictly outside workspace and outside any Git repository.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|resolve_keys_paths]] (function: calls) — *Resolve active private and public key paths respecting precedence.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|run]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/link_healer.py.md|heal_all_ecosystem_links]] (function: calls) — *Repair all standalone.yaml and inventory.json links across the workspace.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/link_healer.py.md|link_healer.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/link_healer.py.md|link_healer.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/models.py.md|models.py]] (imports)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|Colors]] (class: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|IS_WINDOWS]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|_make_ssl_context]] (function: belongs_to) — *Create a resilient SSL context using certifi if present, falling back to default.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|run_guided_setup]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|set_os_environment_variable]] (function: belongs_to) — *Set variable in current process and guide user to persist in OS environment (shell / registry).*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|update_yaml_field]] (function: belongs_to) — *Safely replace or update a field under a section in a YAML file while preserving comments.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|verify_github_token]] (function: belongs_to) — *Verify GitHub Personal Access Token against GitHub API (/user) with resilient SSL fallbacks.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|verify_telegram_token]] (function: belongs_to) — *Verify Telegram bot token against Telegram Bot API (getMe) with resilient SSL fallbacks.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
