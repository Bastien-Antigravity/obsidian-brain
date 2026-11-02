---
microservice: web-interface
type: note
status: active
tags:
- '#service/web-interface'
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
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|EventEmitter.emit]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|EventEmitter.on]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|EventEmitter]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|EventEmitter]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|WebSocketClient.connect]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|WebSocketClient.disconnect]] (method: belongs_to)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|WebSocketClient]] (class: belongs_to)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|WebSocketClient]] (class: defines_method)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|cose-base.js]] (calls)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|cose-base.js]] (same_package)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|bastien-ui.js]] (calls)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.js]] (calls)
- [[web-interface/web-interface/web/static/lib/layout/LayoutManager.js.md|LayoutManager.js]] (calls)
- [[web-interface/web-interface/web/static/lib/theme/ThemeEngine.js.md|ThemeEngine.js]] (calls)
<!-- SYNC:END -->
