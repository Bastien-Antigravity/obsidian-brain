---
microservice: web-interface
type: service-hub
status: active
tags:
- '#service/web-interface'
- '#type/service-hub'
- '#state/active'
- '#zone/3-fleet'
- '#ai/ignore'
---
# 🌐 Service Hub: Web-Interface

*Unified Fleet Dashboard: Go Templates / Vanilla ES6 / HSL CSS Frontend with custom Bastien UI Library.*

## 🔗 Knowledge Map
- **Code Repository**: [📂 web-interface](https://github.com/Bastien-Antigravity/web-interface)
- **Integration Protocol**: [[Web-Interface-Integration-Protocol|📜 Integration Rules]]
- **Page Rendering Standard**: [[Web-Interface-Page-Rendering|🎨 Bastien UI Design System & Tokens]]
- **OpenMFE Protocol**: [[OpenMFE-Integration-Protocol|🧩 Micro-Frontend Integration]]
- **Live State**: Connects to Log-Server, Tele-Remote, Config-Server, and TimescaleDB.

---

## 🏗️ Architecture & Subsystem Design

The `web-interface` follows the **Facade Pattern**, where HTTP handlers orchestrate calls to internal services, database backends, and external microservices.

### 📁 Project Structure
- `cmd/web-interface/main.go`: Application bootstrap and lifecycle wiring via `microservice-toolbox`.
- `src/server/facade.go`: Central facade orchestrating HTTP server startup, timeouts, and graceful shutdown.
- `src/core/controller.go`: System status info, uptime telemetry, and database connectivity health checks.
- `src/mfe/registry.go`: OpenMFE dynamic micro-frontend registration registry, 3-tier taxonomy normalization, and atomic persistence.
- `mfe_services.json`: Persistent disk cache (`dbFile` in `registry.go`) ensuring 0-second cold-start recovery for registered microfrontends upon restart.
- `src/renderer/renderer.go`: Go template rendering engine with session data and dynamic URL resolution.
- `src/router/`: Route registration (`autodiscovery.go`, `static.go`, `dynamic.go`, `router.go`).
  - `autodiscovery.go`: Scans `web/pages/` to automatically mount hierarchical static pages (`/page/<category-slug>/<page-slug>`) and build left `#Sidebar` accordion trees.
- `src/middleware/middleware.go`: Standardized middlewares (request logging, CORS, session auth, CSRF).
- `src/postgres_browser/postgres_browser.go`: Postgres metadata explorer and SQL query execution engine.
- `src/fundamental_analysis/fundamental_analysis.go`: Equities financial indicator and valuation metrics reader.
- `src/telegram/manager.go`: Dynamic interactive menu bridge connecting to `tele-remote`.
- `web/`: UI layer:
  - `web/pages/<XX-Category>/<YY-PageName>.html`: Autodiscovered static pages with `category.json` and frontmatter comments.
  - `web/templates/`: Core app shell templates (`base.html`, `login.html`).
  - `web/static/lib/`: Modern Bastien UI architecture (`tokens/`, `theme/`, `layout/`, `components/`).

### 🧭 Dual-Navigation Architecture
- **Left Sidebar (`#Sidebar`) — Static Knowledge & Content**:
  Displays auto-discovered documentation, research, and profile articles organized into collapsible category trees with guide lines and active state tracking.
- **Right Sidenav Drawer (`#Sidenav`) — Dynamic OpenMFE Micro-Frontends**:
  Displays pluggable microservices registered via OpenMFE, structured into 3 distinct tiers: `BASE FLEET (L1)`, `DOMAIN SERVICES (L2)`, and `SECURE CONTROLS (L3)`.

### 🔄 Data Flow
1. **HTTP Request**: Received by `server.ServerFacade`.
2. **Middleware**: Standardized logging (`universal-logger`), CORS headers, and CSRF token verification.
3. **Routing**: Mux dispatches to auto-discovered static page handlers or dynamic REST API / MFE endpoints.
4. **Data Aggregation**: Queries PostgreSQL or delegates to registered OpenMFE micro-frontends.
5. **Template Rendering**: Server-side template rendering with session state and host-resolved WebSocket URLs.

### 🕹️ Unified Control & Telemetry
The `web-interface` connects directly to `tele-remote` via `microservice-toolbox/go/pkg/teleremote`, dynamically registering interactive menus so fleet operators can check web dashboard health and database status directly via Telegram.

### 🛡️ Security & Secret Decryption
- **CSRF**: Enforced via `gorilla/csrf` with cookie security flags.
- **Sessions**: Managed via `alexedwards/scs/v2` with HTTP-only cookies.
- **Secret Decryption**: Sensitive credentials (such as PostgreSQL database passwords and admin login passwords) are stored as encrypted `ENC(...)` tokens in configurations and decrypted sovereignly in-memory at runtime via `appConfig.DecryptSecret()`. Plaintext passwords are never stored.

### 📊 Observability & Lifecycle
- **Logging**: Initialized via `toolbox_bootstrap.BootstrapService("web-interface")` wrapping `universal-logger`.
- **Graceful Shutdown**: Managed via `toolbox_lifecycle.Manager`, cleanly trapping `SIGINT`/`SIGTERM` to close HTTP listeners and background client connections without dropping in-flight requests.

---

## 🛠️ Squad Assignment
- **Lead Developer**: [[07-Core-KMS/Role-Prompts/03-Developer/Prompt-Lead-Developer|Lead-Dev]]
- **Primary Specialist**: [[07-Core-KMS/Role-Prompts/03-Developer/Squad/Web-UI-Specialist|Web-UI-Specialist]]

## 📊 Live Governance Dashboard
> [!info] Open Specifications
> ```dataview
> TABLE status, feature_id as "ID"
> FROM "02-Business-BDD/02-Behavior-Specs/web-interface"
> WHERE type = "behavior-spec"
> SORT feature_id ASC
> ```
