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
- None detected

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/web/static/js/mfe-loader.js.md|mfe-loader.js]] (calls)
- [[web-interface/web-interface/web/templates/base.html.md|#MicroServices (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#OverlayNav (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#OverlaySide (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#Sidebar (nav)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#Sidenav (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#avatarSidebar (img)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#avatarTop (img)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#cat_{{.ID}} (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#date_time (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#fleet-status-banner (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#fleet-status-details (span)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#fleet-status-dismiss (button)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#fleet-status-refresh (button)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#main (main)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#mfe-l1-accordion (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#mfe-l1-items (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#mfe-l2-accordion (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#mfe-l2-items (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#mfe-l3-accordion (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#mfe-l3-items (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#mfe-nav-accordion (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#partOfProject (div)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#sidebar-close-mobile (button)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#sidebar-toggle (button)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#sidenav-close (button)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|#theme-toggle (button)]] (element: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|IS_LOGGED_IN]] (constant: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|SITE_BASE_URL]] (constant: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|SITE_WSS_URL]] (constant: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|pollFleetStatus]] (function: belongs_to)
- [[web-interface/web-interface/web/templates/base.html.md|updateClock]] (function: belongs_to)
<!-- SYNC:END -->
