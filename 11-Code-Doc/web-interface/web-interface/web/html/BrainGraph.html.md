---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/html/BrainGraph.html.md|#cy (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/BrainGraph.html.md|#filter-microservice (select)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/BrainGraph.html.md|#filter-type (select)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/BrainGraph.html.md|#info-label (h4)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/BrainGraph.html.md|#info-type (span)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/BrainGraph.html.md|#layout-select (select)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/BrainGraph.html.md|#loading-overlay (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/BrainGraph.html.md|#node-info (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/BrainGraph.html.md|#stat-edges (b)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/BrainGraph.html.md|#stat-missing (b)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/BrainGraph.html.md|#stat-nodes (b)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/BrainGraph.html.md|#stat-orphans (b)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/BrainGraph.html.md|#toggle-labels (input)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/BrainGraph.html.md|#toggle-missing (input)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/BrainGraph.html.md|#toggle-orphans (input)]] (element: belongs_to)
- [[web-interface/web-interface/web/static/js/cytoscape-cose-bilkent.js.md|cytoscape-cose-bilkent.js]] (calls)
<!-- SYNC:END -->
