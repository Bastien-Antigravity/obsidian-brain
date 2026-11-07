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
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.addClass]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.afterTransition]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.buildDomMap]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.byId]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.clearStyles]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.create]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.delegate]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.empty]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.getCssVar]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.getData]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.hasClass]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.qs]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.qsa]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.removeClass]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.setCssVar]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.setData]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.setStyles]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.toggleClass]] (method: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.warn]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|Logger.js]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/OrderbookAggregator_OptionB.html.md|OrderbookAggregator_OptionB.html]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/analyst/charts.js.md|charts.js]] (calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/ChartManager.js.md|ChartManager.js]] (calls)
- [[web-interface/web-interface/web/static/js/brain_graph.js.md|brain_graph.js]] (calls)
- [[web-interface/web-interface/web/static/js/cose-base.js.md|cose-base.js]] (calls)
- [[web-interface/web-interface/web/static/lib/components/ComponentRegistry.js.md|ComponentRegistry.js]] (calls)
- [[web-interface/web-interface/web/static/lib/components/atoms/MetricBadge.js.md|MetricBadge.js]] (calls)
- [[web-interface/web-interface/web/static/lib/components/atoms/StatusIndicator.js.md|StatusIndicator.js]] (calls)
- [[web-interface/web-interface/web/static/lib/components/molecules/Card.js.md|Card.js]] (calls)
- [[web-interface/web-interface/web/static/lib/components/molecules/MetricCard.js.md|MetricCard.js]] (calls)
- [[web-interface/web-interface/web/static/lib/components/organisms/DataGrid.js.md|DataGrid.js]] (calls)
- [[web-interface/web-interface/web/static/lib/layout/LayoutManager.js.md|LayoutManager.js]] (calls)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.addClass]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.afterTransition]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.buildDomMap]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.byId]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.clearStyles]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.create]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.delegate]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.empty]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.getCssVar]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.getData]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.hasClass]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.qs]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.qsa]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.removeClass]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.setCssVar]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.setData]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.setStyles]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.toggleClass]] (method: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils]] (class: belongs_to)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils]] (class: defines_method)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|done]] (function: belongs_to)
<!-- SYNC:END -->
