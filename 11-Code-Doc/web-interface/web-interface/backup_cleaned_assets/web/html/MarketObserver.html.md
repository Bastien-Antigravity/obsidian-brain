---
source: web-interface/backup_cleaned_assets/web/html/MarketObserver.html
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 19:46:58.334771
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: MarketObserver.html

## 📝 Description
Automatically generated mirror for `web-interface/backup_cleaned_assets/web/html/MarketObserver.html`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.fetchConfig]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.getDisplayData]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.initializeApp]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.mergeData]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.openConnectionLog]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.openSymbolWindow]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.renderList]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.scheduleUpdate]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.sendSubscription]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.setupTimeframeEventListener]] (method: defines_method) — *Ensure default is valid if possible*
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.setupTimeframeSelector]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.startWebSocket]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.updateAnalysisBlocks]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.updateConnectionStatus]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.updateMetrics]] (method: defines_method) — *We re-subscribe, which triggers a fresh INITIAL payload from server*
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.updateSymbolsList]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.updateUI]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/TradedVolume.html.md|TradedVolume.html]] (same_package)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/TradedVolume.html.md|onclose]] (function: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/TradedVolume.html.md|onerror]] (function: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/TradedVolume.html.md|onmessage]] (function: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/TradedVolume.html.md|onopen]] (function: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/charts.js.md|volumeChart.volume]] (method: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|i.sort]] (method: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.time]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.error]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.warn]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|#abnormalVolList (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|#activeSymbols (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|#aggLatency (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|#blockAbnormalVol (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|#blockHighActivity (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|#blockLowActivity (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|#blockTopGainers (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|#blockTopLosers (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|#connectionIcon (button)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|#highActivityList (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|#lastUpdate (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|#lowActivityList (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|#metricsGrid (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|#processedItems (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|#symbolsGrid (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|#timeframeSelector (select)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|#topGainersList (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|#topLosersList (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|APP_CONFIG]] (constant: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.fetchConfig]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.getDisplayData]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.initializeApp]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.mergeData]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.openConnectionLog]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.openSymbolWindow]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.renderList]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.scheduleUpdate]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.sendSubscription]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.setupTimeframeEventListener]] (method: belongs_to) — *Ensure default is valid if possible*
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.setupTimeframeSelector]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.startWebSocket]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.updateAnalysisBlocks]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.updateConnectionStatus]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.updateMetrics]] (method: belongs_to) — *We re-subscribe, which triggers a fresh INITIAL payload from server*
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.updateSymbolsList]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard.updateUI]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard]] (class: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserverDashboard]] (class: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|activityRenderer]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|formatPct]] (function: belongs_to) — *Helper for formatting*
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|gainerLoserRenderer]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
