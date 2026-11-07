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
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.clock]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.compact]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.currency]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.date]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.duration]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.number]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.percent]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.signColor]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.timeAgo]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.time]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.titleCase]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.truncate]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/MarketObserver.html.md|MarketObserver.html]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/RtTaAnalyst.html.md|RtTaAnalyst.html]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/TAIndicatorsAll.html.md|TAIndicatorsAll.html]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/charts.js.md|charts.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|realtime-common.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/ta-indicators.js.md|ta-indicators.js]] (calls)
- [[web-interface/web-interface/web/static/js/timescaledb-inspector.js.md|timescaledb-inspector.js]] (calls)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.clock]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.compact]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.currency]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.date]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.duration]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.number]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.percent]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.signColor]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.timeAgo]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.time]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.titleCase]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter.truncate]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter]] (class: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/Formatter.js.md|Formatter]] (class: defines_method)
<!-- SYNC:END -->
