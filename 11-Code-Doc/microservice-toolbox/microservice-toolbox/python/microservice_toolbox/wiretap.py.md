---
source: microservice-toolbox/python/microservice_toolbox/wiretap.py
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-11-07T14:41:18.172252
---

# Mirror: wiretap.py

## 📝 Description
Automatically generated mirror for `microservice-toolbox/python/microservice_toolbox/wiretap.py`.

> **Essential Process**:
> Provides a distinct, switchable real-time transport telemetry wrapper ("WireTap") for Python microservices (gRPC, FastMCP/SSE, NATS, PostgreSQL/ChromaDB). Tracks inter-service and external client connections and segregated information channels under thread-safe synchronization, with power-of-two bitmask sampling.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|decode]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/business/models.rs.md|encode]] (function: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|client.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/init.py.md|init.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/init.py.md|init.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|_reporter_loop]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|configure_from_config]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|get_local_service]] (function: belongs_to) — *Returns the canonical service identifier for this Python process.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|get_web_hub_url]] (function: belongs_to) — *Returns the configured base HTTP URL for the central WireTap ingestion hub.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|is_enabled]] (function: belongs_to) — *Returns whether real-time connection tracking is active.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|merge_remote_snapshot]] (function: belongs_to) — *Merges a batch of remote EdgeReport dicts into the local store.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|normalize_service_id]] (function: belongs_to) — *Normalizes arbitrary service or component names into canonical mesh IDs.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|record_event]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|record_mcp_tool_call]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|reset]] (function: belongs_to) — *Clears all recorded edges (useful for unit tests).*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|set_enabled]] (function: belongs_to) — *Switches real-time connection tracking ON or OFF.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|set_local_service]] (function: belongs_to) — *Sets the canonical service identifier for this Python process.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|set_web_hub_url]] (function: belongs_to) — *Sets the base HTTP URL for the central WireTap ingestion hub.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|should_sample]] (function: belongs_to) — *Power-of-two thread-local bitmask sampler (mask == 0 always returns True).*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|snapshot]] (function: belongs_to) — *Returns a serializable list of EdgeReport dicts.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
