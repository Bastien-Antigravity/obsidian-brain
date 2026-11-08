---
source: web-interface/web/static/js/home-transport-mesh.js
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 19:46:57.974570
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: home-transport-mesh.js

## 📝 Description
Automatically generated mirror for `web-interface/web/static/js/home-transport-mesh.js`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|a]] (function: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|d]] (function: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|i.find]] (method: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|i.sort]] (method: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|y]] (class: calls)
- [[web-interface/web-interface/src/logclient/log_service.pb.go.md|x]] (struct: calls)
- [[web-interface/web-interface/web/static/lib/prism/prism-module.js.md|highlightElement]] (function: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.warn]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/router/mesh_topology.go.md|mesh_topology.go]] (calls)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|BASE_MESH_LINKS]] (constant: belongs_to) — *Authoritative Interservice Links & Clickable Message Exchanges (Base Fleet)*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|BASE_PARTICLE_STREAMS]] (constant: belongs_to) — *Particle Streams (Subset of key links for animated moving dots)*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|DEFAULT_NODES]] (constant: belongs_to) — *11 Core Ecosystem Services Initial Positions*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|DYNAMIC_SLOT_CANDIDATES]] (constant: belongs_to) — *Canonical candidate slots for dynamic microservices (avoiding overlap with 11 base nodes)*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|ECOSYSTEM_BASE_SERVICES]] (constant: belongs_to) — *Dynamically discover and render any NEW microservices outside the base ecosystem*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|EXCHANGES]] (constant: belongs_to) — *Authoritative Interservice Message Exchange Definitions (Clickable Messages)*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|PROTOCOL_CATALOG]] (constant: belongs_to) — *Canonical Protocol Catalog*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|SERVICE_METADATA]] (constant: belongs_to) — *Complete Service Metadata dynamically populated from /api/v1/system/service-registry*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|addLink]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|applyMeshTopology]] (function: belongs_to) — *Ingest Authoritative Server Mesh Topology (Phase 2 Server-Hydrated Graph)*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|applyProtocolFilter]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|attachNodeDragListeners]] (function: belongs_to) — *Node Dragging Engine (like CodebaseVisualizer & easyDoc)*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|calculateDynamicNodePosition]] (function: belongs_to) — *Calculate non-colliding coordinates for dynamically discovered microservices*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|cleanupHomePage]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|closeInspector]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|ensureDynamicServiceLinks]] (function: belongs_to) — *plus any declared dependencies for dynamically discovered microservices.*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|filterProtocol]] (function: belongs_to) — *Protocol Filter*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|getPathAndMid]] (function: belongs_to) — *Calculate Curved Path & Midpoint between two nodes*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|getProtoColor]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|initHomePage]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|initRefreshButton]] (function: belongs_to) — *Standardized Tactile Refresh Button with Loading Spin & Debounce*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|openExchangeInspector]] (function: belongs_to) — *Open Inspector for a Clicked Message Exchange*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|openInspector]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|pollFleetServices]] (function: belongs_to) — *Live Fleet Status Poller & Dynamic Microservice Discovery*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|renderMesh]] (function: belongs_to) — *Render Transport Mesh*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|renderProtocolFilters]] (function: belongs_to) — *Dynamic Protocol Filter Button Renderer*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|renderSegregatedChannels]] (function: belongs_to) — *Render Segregated Channels Table in Inspector*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|resetNodeLayout]] (function: belongs_to) — *Reset Node Layout to Default Architectural Positions*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|switchInspectorTab]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|syncWireTapButtonUI]] (function: belongs_to) — *WireTap Lock-Free Telemetry Switch*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|toggleExchangeAnimation]] (function: belongs_to) — *Animation Toggle*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|toggleInspectorExpand]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|toggleWireTap]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|triggerPrismHighlight]] (function: belongs_to) — *Inspector Functions (Service Nodes & Clickable Messages)*
- [[web-interface/web-interface/web/static/lib/router/PageRouter.js.md|PageRouter.js]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
