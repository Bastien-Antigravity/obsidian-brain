---
source: microservice-toolbox/python/microservice_toolbox/spec.py
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-11-01T13:13:18.046051
---

# Mirror: spec.py

## 📝 Description
Automatically generated mirror for `microservice-toolbox/python/microservice_toolbox/spec.py`.

> **Essential Process**:
> Standardizes self-describing service specifications and dynamic registration with web-interface for Python microservices (rag-engine, squad-agent). Auto-resolves runtime listen/REST addresses, dynamic semver, active profile, and documentation links from AppConfig. FAIL-FAST PRINCIPLE: Zero silent fallbacks, zero default values, and zero dummy placeholders. Microservices must explicitly declare their own specification metadata (name, tag, layer, category, description, doc_link, protocol, framing). Configuration addresses (including web_interface) must resolve strictly; missing capabilities, missing ports, or missing metadata FAIL FAST immediately.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|get_grpc_listen_addr]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|get_listen_addr]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/loader.py.md|get_rest_addr]] (function: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/spec.py.md|ProtocolSpec]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/spec.py.md|ServiceSpec]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/spec.py.md|_canonical_hub_name]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/spec.py.md|_extract_port]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/spec.py.md|_format_title]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/spec.py.md|_worker]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/spec.py.md|build_spec_from_config]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/spec.py.md|publish_service_spec]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/spec.py.md|to_dict]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
