---
microservice: web-interface
type: protocol
status: active
tags:
- '#service/web-interface'
- '#type/protocol'
- '#state/active'
- '#zone/3-fleet'
- '#ai/ignore'
---
# 🌐 Web Interface Integration Protocol

This protocol defines how to centralize microservice management, monitoring, and real-time data visualization within the primary `web-interface` dashboard.

## 1. The Gateway Plugin Pattern

To keep the `web-interface` maintainable, every microservice integration MUST follow the **Plugin Pattern**. Instead of adding logic directly to `main.go`, create a dedicated integration package.

### File Structure
```text
web-interface/
  src/
    integrations/
      {service_name}/
        controller.go   # REST/WebSocket handlers
        grpc_client.go  # Communication with the microservice
        router.go       # Route registration
```

## 2. Integration Workflow

### Step 1: gRPC Client Initialization
Use the `microservice-toolbox` to resolve the service address and initialize a gRPC client. Do NOT hardcode IPs.

```go
// Resolved via toolbox
addr, _ := toolbox.GetGRPCListenAddr("data-ingestor")
conn, _ := grpc.Dial(addr, grpc.WithInsecure())
client := pb.NewControlServiceClient(conn)
```

### Step 2: Route Registration
Implement a `RegisterRoutes` function that takes the main `http.ServeMux`.

```go
func RegisterRoutes(mux *http.ServeMux, client pb.ControlServiceClient) {
    mux.HandleFunc("/api/v1/ingestor/start", handleStart(client))
    mux.HandleFunc("/ws/ingestor/logs", handleLogStream(client))
}
```

### Step 3: WebSocket Multiplexing (Live Streams)
For real-time data (prices, logs), the backend should:
1.  Open a gRPC stream to the microservice.
2.  Upgrade the browser request to a WebSocket.
3.  Forward gRPC messages to the WebSocket in a non-blocking loop.

## 3. Frontend Standards

The UI design is optimized for a premium, low-fatigue developer experience. Full visual guidelines, styling tokens, and layout schemas are formalized in [[Web-Interface-Page-Rendering|📜 Page Rendering & UI Styling Specification]].

### Visual Identity & Theme Architecture
*   **Theme Tokens**: Style rules and colors reference CSS variables defined in `/web/static/lib/tokens/design-tokens.css`. Light/dark variations are defined as overrides in `/web/static/lib/theme/themes.css`. Hardcoded colors are strictly prohibited.
*   **Default Theme**: Dark theme uses soft, non-fatiguing deep blue-gray backgrounds (`hsl(222, 25%, 10%)`).
*   **Light Theme**: Light theme overrides backgrounds with clean, non-glaring warm gray-whites (`hsl(210, 15%, 93%)`).
*   **Typography**: Adheres to the strict three-family font system defined in [[Web-Interface-Page-Rendering|Page Rendering Specification]]:
    *   `var(--font-display)` (`Outfit`): Used for headings, main titles, and KPI stats metrics.
    *   `var(--font-sans)` (`Inter`): Used for paragraphs, forms, UI menus, and buttons.
    *   `var(--font-mono)` (`JetBrains Mono` / `Fira Code`): Used for numbers, code blocks, raw data tables (depth/prices), and inputs to prevent layout shifting. AI agents must utilize token variables instead of raw family names.

### Component System
*   **Layout Wrapper**: Child dashboard pages must omit `<html>`, `<head>`, `<body>`, and layout headers. They are encapsulated inside the `{{define "content"}}` block, wrapped in `.bastien-container`, and structured using Bootstrap grids (`.row`, `.col-lg-*`).
*   **Panels & Cards**: Dashboards utilize the glassmorphic `.bastien-card--glass` layout with internal padding segments (`.bastien-card__header`, `.bastien-card__body`).
*   **Forms & Fields**: Input controls and dropdown select fields must use `.bastien-input` and `.bastien-form-group` classes.
*   **Buttons**: Trigger controls use `.bastien-btn` with state modifiers: `--primary` (blue), `--secondary` (glass), and `--danger` (red).
*   **Icons**: Consistent Font Awesome v4.7 (`fa fa-*`) icon utilization is required:
    *   `fa-terminal` / `fa-code`: Code consoles, shell tools.
    *   `fa-cogs` / `fa-sliders`: Configuration panels.
    *   `fa-bar-chart` / `fa-line-chart`: Metrics and statistics.
    *   `fa-moon-o` / `fa-sun-o`: Theme toggling.
*   **Dynamic Component Registration**: UI widgets bind interaction dynamically through `data-component="..."` declarations processed by `web/static/lib/bastien-ui.js`. Inline scripting and inline styling are not allowed.

### Dual-Navigation Architecture
The web interface segregates user navigation into two dedicated surfaces:
1. **Left Sidebar (`#Sidebar`) — Static Knowledge & Content**:
   - Houses documentation articles, guides, and static views auto-discovered from `web/pages/`.
   - Driven by `src/router/autodiscovery.go`.
2. **Right Sidenav Drawer (`#Sidenav`) — Dynamic OpenMFE Microservices**:
   - Houses pluggable microservice interfaces registered at runtime via OpenMFE.
   - Organized into 3 tiers (`L1 - Base Fleet`, `L2 - Domain Services`, `L3 - Secure Controls`).
   - Driven by `web/static/js/mfe-loader.js`.

### UI Template Integration & Static Page Autodiscovery
Static pages and documentation are fully autodiscovered by `src/router/autodiscovery.go` without requiring any manual route registration or Go code changes:
1. **File Hierarchy**: Place the page template in `web/pages/<XX-Category>/<YY-PageName>.html` (e.g. `web/pages/01-Overview/01-WhoAmI.html`).
2. **Category Configuration**: Optionally create `category.json` in the category directory:
   ```json
   {
     "title": "01. Overview",
     "icon": "fa-compass",
     "order": 10
   }
   ```
3. **In-File Metadata**: Include an HTML frontmatter comment at the top of the file:
   ```html
   <!-- title: Who Am I | subtitle: Overview of Bastien's background | icon: fa-user-circle -->
   {{define "content"}}
   <div class="bastien-container">
       <!-- Scoped Page Content -->
   </div>
   {{end}}
   ```
4. **Automatic Routing**: At boot, `autodiscovery.go` mounts `/page/<category-slug>/<page-slug>` and creates the corresponding collapsible accordion menu items in `#Sidebar`. Legacy aliases (e.g. `/WhoAmI`, `/CV`) are preserved automatically.
5. **Zero Hardcoded Routes**: Developers and AI agents MUST NOT add hardcoded page routes to `static.go` or static icon/subtitle dictionaries in Go code.

## 4. Service Discovery Truth
The `web-interface` MUST be the only service that has an "Overview" of the entire fleet. It uses the `distributed-config` bridge to discover the `capabilities` of every running node and dynamically renders its UI based on what is currently active in the ecosystem.

## 5. Config Server Management Integration (OpenMFE `<config-server-mfe>`)
The `web-interface` manages `config-server` through the OpenMFE component `<config-server-mfe>` dynamically registered at boot time (`POST /api/v1/register`).

### Architecture
- **Shadow gRPC Sync Port**: Dynamically resolved via `appConfig.GetGRPCListenAddr("config_server")` or `capabilities.config_server.grpc_port` (default `127.0.0.1:3307`).
- **OpenMFE View**: Served at `/mfe/config-server` inside the universal shell (`web/templates/mfe.html`), allowing fleet operators to inspect active nodes, apply live runtime overrides, and trigger schema reloads without modifying template files.
- **Zero `web/html/` Files**: In accordance with Ecosystem Invariants, all legacy `web/html/` directories are deleted and strictly prohibited.

## 6. Two-Tier OpenMFE Shell & Strict Invariants
1. **Tier 1 (Universal Shell)**:
   - Hosted at `web/templates/mfe.html` and decomposed into modular sub-template partials under `web/templates/mfe/*.html` (`_spec_modal.html`, `_panel_ai.html`).
   - Standard tabs are immutable: Live Inspector (`#panel-live`), WireTap Message Flow (`#panel-flow`), SDK & Polyglot Code Snippets (`#panel-sdk`), AI & Runbook Context (`#panel-ai`).
   - `#mfe-meta-popover` provides a single-column diagnostic modal displaying live IP & port, transport framing, profile, and runtime mode (`native`, `docker`, or `production`).
2. **Tier 2 (Dynamic Custom Tab Ingress)**:
   - Microservices register custom domain tabs via `customTabs: [{ id, title, icon, tag, content }]` (or `dataStructure.custom_tabs`).
   - `mfe-loader.js` mounts `.mfe-tab-btn--custom` into `#mfe-tab-list` and `.mfe-tab-panel--custom` into `#mfe-shell-root` on-demand, purging them cleanly on service navigation.
3. **Strict Prohibition of "localhost"**:
   - `POST /api/v1/register` rejects URLs containing `"localhost"` with HTTP 400.
   - All client connections, network definitions, and test fixtures must use explicit loopback (`127.0.0.1`), container DNS, or relative routes (`/static/...`).
4. **Zero Silent Fallback**:
   - Never default missing network attributes to `"127.0.0.1"`, `"0.0.0.0"`, or `"0.0.1"`. Missing values must render `—` or `Unspecified`.

---
*Last Updated: 2026-11-16*
*See also: [[Microservice-Startup-Protocol]], [[OpenMFE-Integration-Protocol]], [[Web-Interface-Page-Rendering]], [[Web-Interface-Hub]]*
