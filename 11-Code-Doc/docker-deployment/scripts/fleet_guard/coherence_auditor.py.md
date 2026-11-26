---
source: docker-deployment/scripts/fleet_guard/coherence_auditor.py
workspace: docker-deployment
type: code-mirror
status: auto-generated
last_sync: 2026-10-01 01:10:01.842996
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: coherence_auditor.py

## 📝 Description
Automatically generated mirror for `docker-deployment/scripts/fleet_guard/coherence_auditor.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[docker-deployment/scripts/fleet_guard/crypto_validator.py.md|crypto_validator.py]] (imports)
- [[docker-deployment/scripts/fleet_guard/crypto_validator.py.md|crypto_validator.py]] (same_package)
- [[docker-deployment/scripts/fleet_guard/crypto_validator.py.md|decrypt_rsa]] (function: calls) — *Decrypt an ENC(...) ciphertext string using the RSA private key.*
- [[docker-deployment/scripts/fleet_guard/models.py.md|CoherenceAudit]] (class: calls)
- [[docker-deployment/scripts/fleet_guard/models.py.md|PortAudit]] (class: calls)
- [[docker-deployment/scripts/fleet_guard/models.py.md|models.py]] (imports)
- [[docker-deployment/scripts/fleet_guard/models.py.md|models.py]] (same_package)

### 🔌 Consumers (Inbound)
- [[docker-deployment/scripts/fleet_guard/__init__.py.md|__init__.py]] (imports)
- [[docker-deployment/scripts/fleet_guard/coherence_auditor.py.md|MODE_PORTS]] (constant: belongs_to) — *Canonical listening ports to verify availability before launching*
- [[docker-deployment/scripts/fleet_guard/coherence_auditor.py.md|_ENV_TEMPLATE_RE]] (constant: belongs_to)
- [[docker-deployment/scripts/fleet_guard/coherence_auditor.py.md|_INTRA_SERVICE_PORT_KEYS]] (constant: belongs_to)
- [[docker-deployment/scripts/fleet_guard/coherence_auditor.py.md|_repl]] (function: belongs_to)
- [[docker-deployment/scripts/fleet_guard/coherence_auditor.py.md|_resolve_env_template]] (function: belongs_to) — *Resolve ${VAR:default} or ${VAR:-default} templates using os.environ or fallback defaults.*
- [[docker-deployment/scripts/fleet_guard/coherence_auditor.py.md|audit_coherence]] (function: belongs_to) — *Audit cross-service parameter consistency and port conflicts.*
- [[docker-deployment/scripts/fleet_guard/coherence_auditor.py.md|audit_port_bindings]] (function: belongs_to) — *Audit port availability for the active mode.*
- [[docker-deployment/scripts/fleet_guard/coherence_auditor.py.md|audit_yaml_port_uniqueness]] (function: belongs_to) — *Audit active mode YAML configs to ensure intra-service ports are mutually distinct.*
- [[docker-deployment/scripts/fleet_guard/coherence_auditor.py.md|is_port_free_to_bind]] (function: belongs_to) — *Check if a TCP port is free to bind on the specified IP address.*
- [[docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (calls)
- [[docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (imports)
- [[docker-deployment/scripts/fleet_guard/engine.py.md|engine.py]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
