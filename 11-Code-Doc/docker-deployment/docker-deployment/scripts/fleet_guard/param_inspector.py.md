---
source: docker-deployment/scripts/fleet_guard/param_inspector.py
workspace: docker-deployment
type: code-mirror
status: auto-generated
last_sync: 2026-10-01T01:10:01.865648
---

# Mirror: param_inspector.py

## 📝 Description
Automatically generated mirror for `docker-deployment/scripts/fleet_guard/param_inspector.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|crypto_validator.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|crypto_validator.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/crypto_validator.py.md|decrypt_rsa]] (function: calls) — *Decrypt an ENC(...) ciphertext string using the RSA private key.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/models.py.md|ParamAudit]] (class: calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/models.py.md|models.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/models.py.md|models.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/__init__.py.md|__init__.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/fleet_guard/param_inspector.py.md|PARAM_SPECS]] (constant: belongs_to) — *Definition of critical parameters to audit*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/param_inspector.py.md|audit_parameters]] (function: belongs_to) — *Audit all sensitive and required ecosystem parameters.*
- [[docker-deployment/docker-deployment/scripts/fleet_guard/param_inspector.py.md|extract_yaml_value]] (function: belongs_to) — *Simple parser to extract a nested key from YAML content.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
