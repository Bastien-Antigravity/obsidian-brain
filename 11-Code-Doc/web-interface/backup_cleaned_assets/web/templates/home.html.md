---
source: web-interface/backup_cleaned_assets/web/templates/home.html
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 19:46:58.547990
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: home.html

## 📝 Description
Automatically generated mirror for `web-interface/backup_cleaned_assets/web/templates/home.html`.

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
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#anim-icon (i)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#anim-text (span)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#arrow-config (marker)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#arrow-grpc (marker)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#arrow-nats (marker)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#arrow-safesocket (marker)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#arrow-sql (marker)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#btn-anim-toggle (button)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#card-agent_squad (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#card-config_server (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#card-log_server (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#card-nats (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#card-notif_server (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#card-rag_engine (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#card-rag_mcp (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#card-tele_remote (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#card-timescale_db (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#card-watchdog_agent (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#card-web_interface (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#dynamic-tiers-container (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#exchange-canvas-box (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#exchange-svg (svg)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#fleet-summary-text (span)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#inspector-actions-box (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#inspector-addr (td)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#inspector-cap (td)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#inspector-data-code (code)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#inspector-desc (p)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#inspector-flow-list (ul)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#inspector-framing (td)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#inspector-link-graph (a)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#inspector-link-mfe (a)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#inspector-name (h3)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#inspector-protocol (td)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#inspector-sdk-code (code)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#inspector-sdks (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#inspector-status (td)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#mesh-messages-group (g)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#mesh-nodes-group (g)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#mesh-particles-group (g)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#mesh-tracks-group (g)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#pane-code (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#pane-data (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#pane-flow (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#pane-specs (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#row-addr (tr)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#row-cap (tr)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#row-framing (tr)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#row-proto (tr)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#row-status (tr)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#section-sdks (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#service-inspector (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#specs-overview-title (span)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#status-agent_squad (span)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#status-config_server (span)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#status-log_server (span)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#status-nats (span)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#status-notif_server (span)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#status-rag_engine (span)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#status-rag_mcp (span)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#status-tele_remote (span)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#status-timescale_db (span)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#status-watchdog_agent (span)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#status-web_interface (span)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#tab-code-title (span)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|#tab-data-title (span)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|DEFAULT_NODES]] (constant: belongs_to) — *11 Core Ecosystem Services Initial Positions*
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|ECOSYSTEM_BASE_SERVICES]] (constant: belongs_to) — *Dynamically discover and render any NEW microservices outside the base ecosystem*
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|EXCHANGES]] (constant: belongs_to) — *Authoritative Interservice Message Exchange Definitions (Clickable Messages)*
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|MESH_LINKS]] (constant: belongs_to) — *Authoritative Interservice Links & Clickable Message Exchanges*
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|PARTICLE_STREAMS]] (constant: belongs_to) — *Particle Streams (Subset of key links for animated moving dots)*
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|SERVICE_METADATA]] (constant: belongs_to) — *Complete Service Metadata dynamically populated from /api/v1/system/service-registry*
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|applyProtocolFilter]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|attachNodeDragListeners]] (function: belongs_to) — *Particle Streams (Subset of key links for animated moving dots)*
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|closeInspector]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|filterProtocol]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|getPathAndMid]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|getProtoColor]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|openExchangeInspector]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|openInspector]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|pollFleetServices]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|renderMesh]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|resetNodeLayout]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|switchInspectorTab]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|toggleExchangeAnimation]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|toggleInspectorExpand]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|triggerPrismHighlight]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
