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
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|g]] (function: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|m]] (function: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|n]] (function: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|p]] (function: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|y]] (class: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.get]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|    if (!topoData]] (function: belongs_to) — *Ingest Authoritative Server Mesh Topology (Phase 2 Server-Hydrated Graph)*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md| const tra]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md| {
    document.qu]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|BASE_MESH_LINKS]] (constant: belongs_to) — *Authoritative Interservice Links & Clickable Message Exchanges (Base Fleet)*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|BASE_PARTICLE_STREAMS]] (constant: belongs_to) — *Particle Streams (Subset of key links for animated moving dots)*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|DEFAULT_NODES]] (constant: belongs_to) — *11 Core Ecosystem Services Initial Positions*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|DYNAMIC_SLOT_CANDIDATES]] (constant: belongs_to) — *Canonical candidate slots for dynamic microservices (avoiding overlap with 11 base nodes)*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|EXCHANGES]] (constant: belongs_to) — *Authoritative Interservice Message Exchange Definitions (Clickable Messages)*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|InspectorType ]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|addLink]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|ation() {
    const svg]] (function: belongs_to) — *Animation Toggle*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|calculateDynamicNodePosition]] (function: belongs_to) — *Calculate non-colliding coordinates for dynamically discovered microservices*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|document.getElementBy]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|document.hidden) ]] (function: belongs_to) — *Live Fleet Status Poller & Dynamic Microservice Discovery*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|eners() {
    const svg]] (function: belongs_to) — *Node Dragging Engine (like CodebaseVisualizer & easyDoc)*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|ensureDynamicServiceLinks]] (function: belongs_to) — *plus any declared dependencies for dynamically discovered microservices.*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|ers() {
    const con]] (function: belongs_to) — *Dynamic Protocol Filter Button Renderer*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|geId) {
    const ex ]] (function: belongs_to) — *Open Inspector for a Clicked Message Exchange*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|ght() {
    if (windo]] (function: belongs_to) — *Inspector Functions (Service Nodes & Clickable Messages)*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|h();
    ren]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|iceKey, keepT]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|ndow.__fleetPol]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|o) {
    swit]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|p2, curveOffs]] (function: belongs_to) — *Calculate Curved Path & Midpoint between two nodes*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|r() {
    const tra]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|t btn = document.]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|to, btn) {
   ]] (function: belongs_to) — *Protocol Filter*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|{
    nodePosit]] (function: belongs_to) — *Reset Node Layout to Default Architectural Positions*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
