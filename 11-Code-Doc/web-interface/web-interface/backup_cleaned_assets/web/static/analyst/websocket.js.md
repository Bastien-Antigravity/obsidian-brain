---
source: web-interface/backup_cleaned_assets/web/static/analyst/websocket.js
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 19:46:58.421755
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: websocket.js

## 📝 Description
Automatically generated mirror for `web-interface/backup_cleaned_assets/web/static/analyst/websocket.js`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/charts.js.md|TA_WebSocketBindingManager.onclose]] (method: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/charts.js.md|TA_WebSocketBindingManager.onerror]] (method: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/charts.js.md|TA_WebSocketBindingManager.onmessage]] (method: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/charts.js.md|TA_WebSocketBindingManager.onopen]] (method: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/charts.js.md|charts.js]] (same_package)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/websocket.js.md|WebSocketClient.connect]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/websocket.js.md|WebSocketClient.reconnect]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/websocket.js.md|WebSocketClient.sendMessage]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/charts.js.md|charts.js]] (imports)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/searchBar.js.md|searchBar.js]] (imports)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/websocket.js.md|WebSocketClient.connect]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/websocket.js.md|WebSocketClient.reconnect]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/websocket.js.md|WebSocketClient.sendMessage]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/websocket.js.md|WebSocketClient]] (class: belongs_to) — *websocket.js*
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/websocket.js.md|WebSocketClient]] (class: defines_method) — *websocket.js*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
