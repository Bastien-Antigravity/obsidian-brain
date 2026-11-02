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
- [[web-interface/web-interface/web/static/lib/utils/Logger.js.md|BastienLogger.error]] (method: calls)
- [[web-interface/web-interface/web/templates/base.html.md|IS_LOGGED_IN]] (constant: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|DISCOVERY_SERVICE_URL]] (constant: belongs_to)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|fetchServices]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|init]] (function: belongs_to) — *Initialize*
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|injectNavigation]] (function: belongs_to)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|loadMFE]] (function: belongs_to)
<!-- SYNC:END -->
