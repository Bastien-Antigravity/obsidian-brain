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
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|EventEmitter.emit]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|EventEmitter.on]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|WebSocketClient.connect]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|WebSocketClient.disconnect]] (method: defines_method)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|onclose]] (function: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|onerror]] (function: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|onopen]] (function: calls)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|realtime-common.js]] (same_package)
- [[web-interface/web-interface/web/static/js/traded-volume.js.md|onmessage]] (function: calls)
- [[web-interface/web-interface/web/static/js/traded-volume.js.md|traded-volume.js]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|EventEmitter.emit]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|EventEmitter.on]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|EventEmitter]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|EventEmitter]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|WebSocketClient.connect]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|WebSocketClient.disconnect]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|WebSocketClient]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|WebSocketClient]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/app.js.md|app.js]] (calls)
- [[web-interface/web-interface/web/static/js/app.js.md|app.js]] (same_package)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|cose-base.js]] (calls)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|cose-base.js]] (same_package)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|gridstack-all.js]] (calls)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|gridstack-all.js]] (same_package)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|bastien-ui.js]] (calls)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.js]] (calls)
- [[web-interface/web-interface/web/static/lib/layout/LayoutManager.js.md|LayoutManager.js]] (calls)
- [[web-interface/web-interface/web/static/lib/theme/ThemeEngine.js.md|ThemeEngine.js]] (calls)
<!-- SYNC:END -->
