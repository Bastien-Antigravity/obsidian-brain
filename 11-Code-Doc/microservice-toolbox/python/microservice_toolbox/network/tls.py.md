---
source: microservice-toolbox/python/microservice_toolbox/network/tls.py
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-11-23 20:26:01.632643
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: tls.py

## 📝 Description
Automatically generated mirror for `microservice-toolbox/python/microservice_toolbox/network/tls.py`.

> **Essential Process**:
> Provides reusable X.509 TLS/mTLS client policy helpers and grpc.aio channel constructors mirroring the Go microservice-toolbox network/tls package.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/python/microservice_toolbox/config/local_tls.py.md|local_tls.py]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/python/microservice_toolbox/network/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/python/microservice_toolbox/network/tls.py.md|_extract_host]] (function: belongs_to)
- [[microservice-toolbox/python/microservice_toolbox/network/tls.py.md|build_client_ssl_credentials]] (function: belongs_to)
- [[microservice-toolbox/python/microservice_toolbox/network/tls.py.md|create_aio_channel]] (function: belongs_to)
- [[microservice-toolbox/python/microservice_toolbox/network/tls.py.md|is_local_address]] (function: belongs_to) — *Reports whether host represents a loopback or localhost address.*
- [[microservice-toolbox/python/microservice_toolbox/network/tls.py.md|normalize_tls_mode]] (function: belongs_to) — *Canonicalizes a TLS policy mode string, defaulting empty values to 'auto'.*
- [[microservice-toolbox/python/microservice_toolbox/network/tls.py.md|should_use_client_tls]] (function: belongs_to)
- [[microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|client.py]] (calls)
- [[microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|client.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
