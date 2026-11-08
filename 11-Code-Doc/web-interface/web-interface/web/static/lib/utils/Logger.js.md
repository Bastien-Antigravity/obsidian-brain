---
source: web-interface/web/static/lib/utils/Logger.js
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-10-22 16:54:01.725669
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: Logger.js

## 📝 Description
Automatically generated mirror for `web-interface/web/static/lib/utils/Logger.js`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)
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
- [[web-interface/web-interface/backup_cleaned_assets/web/html/CommonToolbox.html.md|CommonToolbox.html]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserver.html]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/OrderbookAggregator_OptionB.html.md|OrderbookAggregator_OptionB.html]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|RtTaAnalyst.html]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/TAIndicatorsAll.html.md|TAIndicatorsAll.html]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/TradedVolume.html.md|TradedVolume.html]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/ChartManager.js.md|ChartManager.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/DOMRenderer.js.md|DOMRenderer.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/WebSocketClient.js.md|WebSocketClient.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/app.js.md|app.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|gridstack-all.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/market-observer.js.md|market-observer.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/ta-indicators.js.md|ta-indicators.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/traded-volume.js.md|traded-volume.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/home.html.md|home.html]] (calls)
- [[web-interface/web-interface/web/pages/02-Ecosystem-Discovery/02-FleetLiveLogs.html.md|02-FleetLiveLogs.html]] (calls)
- [[web-interface/web-interface/web/static/js/brain_graph.js.md|brain_graph.js]] (calls)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|cose-base.js]] (calls)
- [[web-interface/web-interface/web/static/js/database-explorer.js.md|database-explorer.js]] (calls)
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|home-transport-mesh.js]] (calls)
- [[web-interface/web-interface/web/static/js/log-server-inspector.js.md|log-server-inspector.js]] (calls)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|mfe-loader.js]] (calls)
- [[web-interface/web-interface/web/static/js/nats-monitor.js.md|nats-monitor.js]] (calls)
- [[web-interface/web-interface/web/static/js/rag-mcp-inspector.js.md|rag-mcp-inspector.js]] (calls)
- [[web-interface/web-interface/web/static/js/tele-remote-inspector.js.md|tele-remote-inspector.js]] (calls)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|timescaledb-inspector.js]] (calls)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|bastien-ui.js]] (calls)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|bastien-ui.js]] (imports)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.js]] (calls)
- [[web-interface/web-interface/web/static/lib/components/organisms/DataGrid.js.md|DataGrid.js]] (calls)
- [[web-interface/web-interface/web/static/lib/layout/LayoutManager.js.md|LayoutManager.js]] (calls)
- [[web-interface/web-interface/web/static/lib/mfe/BastienMFEElement.js.md|BastienMFEElement.js]] (calls)
- [[web-interface/web-interface/web/static/lib/router/PageRouter.js.md|PageRouter.js]] (calls)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.js]] (calls)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.js]] (same_package)
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
