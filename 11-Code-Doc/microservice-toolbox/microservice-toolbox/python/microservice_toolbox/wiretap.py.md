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
> Provides a distinct, lock-free switchable real-time transport telemetry wrapper ("WireTap") for Python microservices (gRPC, FastMCP/SSE, NATS, PostgreSQL/ChromaDB). Tracks inter-service and external client connections (such as Antigravity IDE -> RAG MCP) and segregated information channels (MCP tool names, RPC methods, NATS subjects).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|client.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/init.py.md|init.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/init.py.md|init.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|_reporter_loop]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|configure_from_config]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|get_local_service]] (function: belongs_to) — *Returns the canonical service identifier for this Python process.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|is_enabled]] (function: belongs_to) — *Atomically returns whether real-time connection tracking is active.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|normalize_service_id]] (function: belongs_to) — *Normalizes arbitrary service or component names into canonical mesh IDs.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|record_event]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|record_mcp_tool_call]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|reset]] (function: belongs_to) — *Clears all recorded edges (useful for unit tests).*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|set_enabled]] (function: belongs_to) — *Atomically switches real-time connection tracking ON or OFF without locks.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|set_local_service]] (function: belongs_to) — *Sets the canonical service identifier for this Python process.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|snapshot]] (function: belongs_to) — *Returns a serializable list of EdgeReport dicts.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
