---
source: web-interface/backup_cleaned_assets/web/static/js/base.js
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 19:46:58.515772
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: base.js

## 📝 Description
Automatically generated mirror for `web-interface/backup_cleaned_assets/web/static/js/base.js`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/html/CV.html.md|#sidebar (div)]] (element: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.closeSidebar]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.closeSidenav]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.getSidebarWidth]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.init]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.loadSavedTheme]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.openSidebar]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.openSidenav]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.setupClock]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.setupResponsiveTriggers]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.showLoginModal]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.toggleDropdown]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.toggleSidebar]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.toggleSidenav]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.toggleTheme]] (method: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/base.html.md|#avatarSidebar (img)]] (element: calls)
- [[web-interface/web-interface/backup_cleaned_assets/web/templates/base.html.md|#avatarTop (img)]] (element: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.closeSidebar]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.closeSidenav]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.getSidebarWidth]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.init]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.loadSavedTheme]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.openSidebar]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.openSidenav]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.setupClock]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.setupResponsiveTriggers]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.showLoginModal]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.toggleDropdown]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.toggleSidebar]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.toggleSidenav]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController.toggleTheme]] (method: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController]] (class: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|BaseUIController]] (class: defines_method)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|CloseNav]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|OpenCloseNav]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|OpenNav]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|drop_down_func_id]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|toggleTheme]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|update]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|w3_OpenClose]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|w3_close]] (function: belongs_to)
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/base.js.md|w3_open]] (function: belongs_to) — *Global aliases for HTML event handlers*
- [[web-interface/web-interface/web/static/js/database-explorer.js.md|database-explorer.js]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
