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

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/html/CommonToolbox.html.md|#resolver-result (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/CommonToolbox.html.md|#service-input (input)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/CommonToolbox.html.md|#status-baseurl (strong)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/CommonToolbox.html.md|#status-name (strong)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/CommonToolbox.html.md|#status-profile (strong)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/CommonToolbox.html.md|#status-wssurl (strong)]] (element: belongs_to)
- [[web-interface/web-interface/web/html/CommonToolbox.html.md|resolveCapability]] (function: belongs_to)
<!-- SYNC:END -->
