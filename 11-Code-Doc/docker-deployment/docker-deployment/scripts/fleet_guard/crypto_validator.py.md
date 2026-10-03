---
source: docker-deployment/scripts/fleet_guard/crypto_validator.py
workspace: docker-deployment
type: code-mirror
status: auto-generated
last_sync: 2026-10-01T01:10:01.868257
---

# Mirror: crypto_validator.py

## 📝 Description
Automatically generated mirror for `docker-deployment/scripts/fleet_guard/crypto_validator.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|run]] (function: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/models.py.md|CryptoAudit]] (class: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/models.py.md|models.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/models.py.md|models.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/__init__.py.md|__init__.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/coherence_auditor.py.md|coherence_auditor.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/coherence_auditor.py.md|coherence_auditor.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/coherence_auditor.py.md|coherence_auditor.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|IS_WINDOWS]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|audit_cryptography]] (function: belongs_to) — *Perform comprehensive audit of RSA keypair and canary decryption.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|decrypt_rsa]] (function: belongs_to) — *Decrypt an ENC(...) ciphertext string using the RSA private key.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|encrypt_rsa]] (function: belongs_to) — *Encrypt a secret string with RSA public key into ENC(...) format.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|generate_rsa_keypair]] (function: belongs_to) — *Generate sovereign RSA 2048-bit keypair strictly outside Git.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|get_openssl_binary]] (function: belongs_to) — *Locate OpenSSL binary across Linux, macOS, and Windows.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|is_git_tracked_or_unsafe]] (function: belongs_to) — *Ensure cryptographic keys are strictly outside workspace and outside any Git repository.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|resolve_keys_paths]] (function: belongs_to) — *Resolve active private and public key paths respecting precedence.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|guided_wizard.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|guided_wizard.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/guided_wizard.py.md|guided_wizard.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/param_inspector.py.md|param_inspector.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/param_inspector.py.md|param_inspector.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/param_inspector.py.md|param_inspector.py]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
