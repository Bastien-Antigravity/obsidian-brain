---
source: microservice-toolbox/python/microservice_toolbox/config/local_tls.py
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-11-23T20:26:01.584935
---

# Mirror: local_tls.py

## 📝 Description
Automatically generated mirror for `microservice-toolbox/python/microservice_toolbox/config/local_tls.py`.

> **Essential Process**:
> Defines the LocalTLSConfig model and extraction helpers for service-private X.509 TLS/mTLS paths. Strictly reads from the 'local:' configuration namespace and never from shared 'capabilities:'.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|loader.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|loader.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|loader.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/local_tls.py.md|LocalTLSConfig]] (class: belongs_to) — *Service-private X.509 TLS/mTLS file paths from the local: configuration section.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/local_tls.py.md|_extract_local_tls_from_map]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/local_tls.py.md|_extract_trimmed_string]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/local_tls.py.md|extract_local_tls_config]] (function: belongs_to) — *Normalizes a raw dict or LocalTLSConfig instance into a trimmed LocalTLSConfig.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/local_tls.py.md|is_empty]] (function: belongs_to) — *Returns True when all path fields are empty and verify_client is unset.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/local_tls.py.md|should_verify_client]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/network/tls.py.md|tls.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|client.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|client.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
