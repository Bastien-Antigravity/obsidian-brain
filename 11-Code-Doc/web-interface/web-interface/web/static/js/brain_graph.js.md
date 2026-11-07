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
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/gridstack-all.js.md|i.sort]] (method: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.addClass]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.hasClass]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/DomUtils.js.md|DomUtils.removeClass]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/brain_graph.js.md|COLORS]] (constant: belongs_to)
- [[web-interface/web-interface/web/static/js/brain_graph.js.md|applyFilters]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/brain_graph.js.md|doFit]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/brain_graph.js.md|hideNodeInfo]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/brain_graph.js.md|highlightNeighborhood]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/brain_graph.js.md|initGraph]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/brain_graph.js.md|loadAndInitGraph]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/brain_graph.js.md|nodeColor]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/brain_graph.js.md|populateFilters]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/brain_graph.js.md|resetHighlights]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/brain_graph.js.md|setupEvents]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/brain_graph.js.md|showNodeInfo]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/brain_graph.js.md|updateStats]] (function: belongs_to)
<!-- SYNC:END -->
