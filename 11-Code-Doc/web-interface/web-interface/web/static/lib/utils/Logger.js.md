---
source: web-interface/web/static/lib/utils/Logger.js
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:54:01.725669
---

# Mirror: Logger.js

## 📝 Description
Automatically generated mirror for `web-interface/web/static/lib/utils/Logger.js`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger._dispatchRemote]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger._log]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.captureGlobalErrors]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.critical]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.debug]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.enqueueOffline]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.error]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.flushOfflineQueue]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.getLogger]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.get]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.info]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.initOfflineListener]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.warn]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.warning]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/html/CommonToolbox.html.md|CommonToolbox.html]] (calls)
- [[web-interface/web-interface/web/html/MarketObserver.html.md|MarketObserver.html]] (calls)
- [[web-interface/web-interface/web/html/OrderbookAggregator_OptionB.html.md|OrderbookAggregator_OptionB.html]] (calls)
- [[web-interface/web-interface/web/html/RtTaAnalyst.html.md|RtTaAnalyst.html]] (calls)
- [[web-interface/web-interface/web/html/TAIndicatorsAll.html.md|TAIndicatorsAll.html]] (calls)
- [[web-interface/web-interface/web/html/TradedVolume.html.md|TradedVolume.html]] (calls)
- [[web-interface/web-interface/web/static/js/ChartManager.js.md|ChartManager.js]] (calls)
- [[web-interface/web-interface/web/static/js/DOMRenderer.js.md|DOMRenderer.js]] (calls)
- [[web-interface/web-interface/web/static/js/WebSocketClient.js.md|WebSocketClient.js]] (calls)
- [[web-interface/web-interface/web/static/js/app.js.md|app.js]] (calls)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|cose-base.js]] (calls)
- [[web-interface/web-interface/web/static/js/database-explorer.js.md|database-explorer.js]] (calls)
- [[web-interface/web-interface/web/static/js/gridstack-all.js.md|gridstack-all.js]] (calls)
- [[web-interface/web-interface/web/static/js/market-observer.js.md|market-observer.js]] (calls)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|mfe-loader.js]] (calls)
- [[web-interface/web-interface/web/static/js/ta-indicators.js.md|ta-indicators.js]] (calls)
- [[web-interface/web-interface/web/static/js/traded-volume.js.md|traded-volume.js]] (calls)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|bastien-ui.js]] (calls)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|bastien-ui.js]] (imports)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.js]] (calls)
- [[web-interface/web-interface/web/static/lib/components/organisms/DataGrid.js.md|DataGrid.js]] (calls)
- [[web-interface/web-interface/web/static/lib/utils/EventBus.js.md|EventBus.js]] (calls)
- [[web-interface/web-interface/web/static/lib/utils/EventBus.js.md|EventBus.js]] (same_package)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger._dispatchRemote]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger._log]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.captureGlobalErrors]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.critical]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.debug]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.enqueueOffline]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.error]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.flushOfflineQueue]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.getLogger]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.get]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.info]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.initOfflineListener]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.warn]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.warning]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger]] (class: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger]] (class: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
