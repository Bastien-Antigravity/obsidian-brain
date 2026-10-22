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
- [[web-interface/web-interface/web/static/js/ChartManager.js.md|ChartManager.clear]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.error]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.get]] (method: calls)
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|Logger.js]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/lib/bastien-ui.js.md|bastien-ui.js]] (imports)
<!-- SYNC:END -->
