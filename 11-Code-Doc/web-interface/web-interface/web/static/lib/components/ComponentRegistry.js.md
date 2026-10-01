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
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|EventEmitter.emit]] (method: calls)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|BaseComponent.#readDataAttrs]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|BaseComponent._subscribe]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|BaseComponent.mount]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|BaseComponent.onThemeChange]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|BaseComponent.unmount]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.autoInit]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.create]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.destroy]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.getFromElement]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.getInstance]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.registerAll]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.register]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/html/CV.html.md|CV.html]] (calls)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|cose-base.js]] (calls)
- [[web-interface/web-interface/web/static/js/cytoscape-cose-bilkent.js.md|cytoscape-cose-bilkent.js]] (calls)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|market-observer.js]] (calls)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|bastien-ui.js]] (calls)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|bastien-ui.js]] (imports)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|BaseComponent.#readDataAttrs]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|BaseComponent._subscribe]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|BaseComponent.mount]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|BaseComponent.onThemeChange]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|BaseComponent.unmount]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|BaseComponent]] (class: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|BaseComponent]] (class: defines_method)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.autoInit]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.create]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.destroy]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.getFromElement]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.getInstance]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.registerAll]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.register]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry]] (class: belongs_to)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry]] (class: defines_method)
- [[web-interface/web-interface/web/static/lib/components/molecules/Card.js.md|Card.js]] (calls)
<!-- SYNC:END -->
