---
source: web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 19:46:58.267675
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: RtTaAnalyst.html

## 📝 Description
Automatically generated mirror for `web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/charts.js.md|volumeChart.volume]] (method: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|i.cloneNode]] (method: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/prism.js.md|prism.js]] (imports)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.get]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|#AnalystConfigForm (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|#AnalystConfigFormBody (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|#AnalystTickersList (button)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|#ConnnectionInfos (h4)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|#IndicatorsInfos (h3)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|#TableConnnectionInfos (table)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|#Tick_Datas (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|#broker_ticker (span)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|#collapsibleDiv (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|#connectionIcon (button)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|#connectionLogModal (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|#connectionStatus (p)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|#duplicateView (button)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|#modalContent (tbody)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|#patternChart (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|#searchBar (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|#volatilityChart (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|#volumeChart (div)]] (element: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|analyst_config]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|changeDatasource]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|formatDateUTC]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|indicators]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|infos_connection]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|onclose]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|onerror]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|onmessage]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|onopen]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|pattern]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|updateConnectionStatus]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|updateTitle]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
