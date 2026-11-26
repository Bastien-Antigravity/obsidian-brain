---
source: microservice-toolbox/python/microservice_toolbox/trace.py
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-11-26T19:45:06.061295
---

# Mirror: trace.py

## 📝 Description
Automatically generated mirror for `microservice-toolbox/python/microservice_toolbox/trace.py`.

> **Essential Process**:
> Cross-service and cross-brain mission trace correlation (X-Bastien-Mission-ID) for Python microservices. Sanitizes, extracts, injects, and binds mission_id across ASGI/FastAPI requests, NATS headers, ContextVar task state, and UniLog structured metadata.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/python/microservice_toolbox/wiretap.py.md|reset]] (function: calls) — *Clears all recorded edges (useful for unit tests).*
- [[microservice-toolbox/python/microservice_toolbox/wiretap.py.md|wiretap.py]] (same_package)
- [[microservice-toolbox/rust/src/business/models.rs.md|decode]] (function: calls)
- [[microservice-toolbox/rust/src/business/models.rs.md|encode]] (function: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/python/microservice_toolbox/trace.py.md|ENV_MISSION_ID]] (constant: belongs_to)
- [[microservice-toolbox/python/microservice_toolbox/trace.py.md|HEADER_MISSION_ID]] (constant: belongs_to)
- [[microservice-toolbox/python/microservice_toolbox/trace.py.md|METADATA_KEY]] (constant: belongs_to)
- [[microservice-toolbox/python/microservice_toolbox/trace.py.md|MissionIDMiddleware]] (class: belongs_to) — *Zero-dependency ASGI middleware propagating X-Bastien-Mission-ID on HTTP requests.*
- [[microservice-toolbox/python/microservice_toolbox/trace.py.md|_MAX_MISSION_ID_LEN]] (constant: belongs_to)
- [[microservice-toolbox/python/microservice_toolbox/trace.py.md|__call__]] (function: belongs_to)
- [[microservice-toolbox/python/microservice_toolbox/trace.py.md|__init__]] (function: belongs_to)
- [[microservice-toolbox/python/microservice_toolbox/trace.py.md|bind_from_env]] (function: belongs_to) — *Binds X_BASTIEN_MISSION_ID to logger metadata during cold bootstrap if present.*
- [[microservice-toolbox/python/microservice_toolbox/trace.py.md|extract_from_headers]] (function: belongs_to)
- [[microservice-toolbox/python/microservice_toolbox/trace.py.md|get_mission_id]] (function: belongs_to) — *Returns the active task-scoped mission ID or falls back to X_BASTIEN_MISSION_ID.*
- [[microservice-toolbox/python/microservice_toolbox/trace.py.md|inject_headers]] (function: belongs_to) — *Injects the active X-Bastien-Mission-ID into an outbound HTTP/NATS header dictionary.*
- [[microservice-toolbox/python/microservice_toolbox/trace.py.md|sanitize_mission_id]] (function: belongs_to) — *Validates and trims a raw mission ID, rejecting whitespace or control characters.*
- [[microservice-toolbox/python/microservice_toolbox/trace.py.md|send_with_header]] (function: belongs_to)
- [[microservice-toolbox/python/microservice_toolbox/trace.py.md|set_mission_id]] (function: belongs_to) — *Sets the active task-scoped mission ID and optionally binds UniLog metadata.*
- [[microservice-toolbox/python/microservice_toolbox/utils/init.py.md|init.py]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
