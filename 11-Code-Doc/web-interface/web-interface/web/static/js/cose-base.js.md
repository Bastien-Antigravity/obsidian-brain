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
- [[web-interface/web-interface/web/html/CV.html.md|transform]] (function: calls)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|EventEmitter.emit]] (method: calls)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|WebSocketClient.js]] (same_package)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|gridstack-all.js]] (same_package)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|i.sort]] (method: calls)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|y]] (class: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|realtime-common.js]] (same_package)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.create]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|CoSEConstants]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|CoSEEdge]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|CoSEGraphManager]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|CoSEGraph]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|CoSELayout]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|CoSENode]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|ConstraintHandler]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|__webpack_require__]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|_toConsumableArray]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|setUnion]] (function: belongs_to) — *find union of two sets*
- [[web-interface/web-interface/web/static/js/cytoscape-cose-bilkent.js.md|cytoscape-cose-bilkent.js]] (calls)
- [[web-interface/web-interface/web/static/js/cytoscape-cose-bilkent.js.md|cytoscape-cose-bilkent.js]] (same_package)
<!-- SYNC:END -->
