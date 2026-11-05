---
source: web-interface/backup_cleaned_assets/web/static/js/traded-volume.js
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 19:46:58.488973
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: traded-volume.js

## 📝 Description
Automatically generated mirror for `web-interface/backup_cleaned_assets/web/static/js/traded-volume.js`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|realtime-common.js]] (same_package)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/traded-volume.js.md|TradedVolumeDashboard.onMessage]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/traded-volume.js.md|TradedVolumeDashboard.renderRow]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/WebSocketClient.js.md|WebSocketClient.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/WebSocketClient.js.md|WebSocketClient.js]] (same_package)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/market-observer.js.md|market-observer.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/market-observer.js.md|market-observer.js]] (same_package)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/prism.js.md|prism.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/prism.js.md|prism.js]] (same_package)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/traded-volume.js.md|TradedVolumeDashboard.onMessage]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/traded-volume.js.md|TradedVolumeDashboard.renderRow]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/traded-volume.js.md|TradedVolumeDashboard]] (class: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/traded-volume.js.md|TradedVolumeDashboard]] (class: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/traded-volume.js.md|onmessage]] (function: belongs_to) — *Legacy hook for WebSocket onmessage*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
