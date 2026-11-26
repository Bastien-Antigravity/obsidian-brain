---
source: web-interface/backup_cleaned_assets/web/static/js/realtime-common.js
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 19:46:58.499753
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: realtime-common.js

## 📝 Description
Automatically generated mirror for `web-interface/backup_cleaned_assets/web/static/js/realtime-common.js`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|gridstack-all.js]] (same_package)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|i.cloneNode]] (method: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.fetchAnalystConfig]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.fetchTimeframes]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.formatDateUTC]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.initCollapsible]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.initDuplicateView]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.setupEventListeners]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.showLogModal]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.updateStatus]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.date]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/BrainGraph.html.md|BrainGraph.html]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserver.html]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/OrderbookAggregator_OptionB.html.md|OrderbookAggregator_OptionB.html]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/charts.js.md|charts.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/test.js.md|test.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/websocket.js.md|websocket.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/WebSocketClient.js.md|WebSocketClient.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/WebSocketClient.js.md|WebSocketClient.js]] (same_package)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/app.js.md|app.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/app.js.md|app.js]] (same_package)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|gridstack-all.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|gridstack-all.js]] (same_package)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/market-observer.js.md|market-observer.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/market-observer.js.md|market-observer.js]] (same_package)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.fetchAnalystConfig]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.fetchTimeframes]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.formatDateUTC]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.initCollapsible]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.initDuplicateView]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.setupEventListeners]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.showLogModal]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.updateStatus]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager]] (class: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager]] (class: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|analyst_config]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|changeDatasource]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|infos_connection]] (function: belongs_to) — *Legacy compatibility aliases*
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|load_timeframes]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|onclose]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|onerror]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|onopen]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|updateConnectionStatus]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|updateTitle]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/ta-indicators.js.md|ta-indicators.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/ta-indicators.js.md|ta-indicators.js]] (same_package)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/traded-volume.js.md|traded-volume.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/traded-volume.js.md|traded-volume.js]] (same_package)
- [[web-interface/web-interface/web/static/js/brain_graph.js.md|brain_graph.js]] (calls)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|cose-base.js]] (calls)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|mfe-loader.js]] (calls)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|nats-monitor.js]] (calls)
- [[web-interface/web-interface/web/static/lib/layout/LayoutManager.js.md|LayoutManager.js]] (calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|Logger.js]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
