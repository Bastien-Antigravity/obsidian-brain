---
source: web-interface/web/static/lib/mfe/OpenMFEContracts.js
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-10T13:21:54.075218
---

# Mirror: OpenMFEContracts.js

## 📝 Description
Automatically generated mirror for `web-interface/web/static/lib/mfe/OpenMFEContracts.js`.

> **Essential Process**:
> Shared OpenMFE utility for fetching microservice-authored exchange contracts (REST APIs, gRPC/Protobuf IDLs, Cap'n Proto schemas, SafeSocket wire specs, NATS JetStream subjects, TimescaleDB SQL schemas, FastMCP JSON-RPC/SSE) and mounting one tab per contract type inside an MFE's .openmfe-tabs-bar (div[3]).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.escapeHTML]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.fetchContracts]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.mountContractTabs]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.renderContractPanelInner]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.renderDirectionBadge]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.renderKindBadge]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.renderUnavailableNotice]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.tabIdForContract]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|log-server-inspector.js]] (calls)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|nats-monitor.js]] (calls)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|rag-mcp-inspector.js]] (calls)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|tele-remote-inspector.js]] (calls)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|timescaledb-inspector.js]] (calls)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|bastien-ui.js]] (imports)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.escapeHTML]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.fetchContracts]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.mountContractTabs]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.renderContractPanelInner]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.renderDirectionBadge]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.renderKindBadge]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.renderUnavailableNotice]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts.tabIdForContract]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts]] (class: belongs_to)
- [[web-interface/web-interface/web/static/lib/mfe/OpenMFEContracts.js.md|OpenMFEContracts]] (class: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
