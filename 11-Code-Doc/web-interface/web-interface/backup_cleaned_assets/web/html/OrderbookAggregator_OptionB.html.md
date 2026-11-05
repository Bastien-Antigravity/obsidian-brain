---
source: web-interface/backup_cleaned_assets/web/html/OrderbookAggregator_OptionB.html
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 19:46:58.200487
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: OrderbookAggregator_OptionB.html

## 📝 Description
Automatically generated mirror for `web-interface/backup_cleaned_assets/web/html/OrderbookAggregator_OptionB.html`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/TradedVolume.html.md|TradedVolume.html]] (same_package)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/TradedVolume.html.md|onclose]] (function: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/TradedVolume.html.md|onerror]] (function: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/TradedVolume.html.md|onmessage]] (function: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/TradedVolume.html.md|onopen]] (function: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.error]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.get]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/OrderbookAggregator_OptionB.html.md|ROW_COUNT_HALF]] (constant: belongs_to) — *Render +/- 20 ticks from the center to fully saturate the layout*
- [[web-interface/web-interface/backup_cleaned_assets/web/html/OrderbookAggregator_OptionB.html.md|checkArr]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/OrderbookAggregator_OptionB.html.md|connectVolumeMechanic]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/OrderbookAggregator_OptionB.html.md|connect]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/OrderbookAggregator_OptionB.html.md|initMockVolumeProfile]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/OrderbookAggregator_OptionB.html.md|logEvent]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/OrderbookAggregator_OptionB.html.md|processStats]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/OrderbookAggregator_OptionB.html.md|renderDOM]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/OrderbookAggregator_OptionB.html.md|renderVolumeProfileOverlay]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/OrderbookAggregator_OptionB.html.md|setStatus]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/DOMRenderer.js.md|DOMRenderer.js]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
