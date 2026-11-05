---
source: web-interface/backup_cleaned_assets/web/static/js/WebSocketClient.js
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 19:46:58.526827
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: WebSocketClient.js

## 📝 Description
Automatically generated mirror for `web-interface/backup_cleaned_assets/web/static/js/WebSocketClient.js`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/WebSocketClient.js.md|EventEmitter.emit]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/WebSocketClient.js.md|EventEmitter.on]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/WebSocketClient.js.md|WebSocketClient.connect]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/WebSocketClient.js.md|WebSocketClient.disconnect]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|onclose]] (function: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|onerror]] (function: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|onopen]] (function: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|realtime-common.js]] (same_package)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/traded-volume.js.md|onmessage]] (function: calls) — *Legacy hook for WebSocket onmessage*
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/traded-volume.js.md|traded-volume.js]] (same_package)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/WebSocketClient.js.md|EventEmitter.emit]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/WebSocketClient.js.md|EventEmitter.on]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/WebSocketClient.js.md|EventEmitter]] (class: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/WebSocketClient.js.md|EventEmitter]] (class: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/WebSocketClient.js.md|WebSocketClient.connect]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/WebSocketClient.js.md|WebSocketClient.disconnect]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/WebSocketClient.js.md|WebSocketClient]] (class: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/WebSocketClient.js.md|WebSocketClient]] (class: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/app.js.md|app.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/app.js.md|app.js]] (same_package)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|gridstack-all.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|gridstack-all.js]] (same_package)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|cose-base.js]] (calls)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|bastien-ui.js]] (calls)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.js]] (calls)
- [[web-interface/web-interface/web/static/lib/layout/LayoutManager.js.md|LayoutManager.js]] (calls)
- [[web-interface/web-interface/web/static/lib/theme/ThemeEngine.js.md|ThemeEngine.js]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
