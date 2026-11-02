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
# 🌐 OpenMFE Microfrontend Integration Protocol

This protocol defines how to build, register, and test pluggable, decentralized user interfaces (Microfrontends) in the Bastien Ecosystem using the **OpenMFE standard** and HTML5 Web Components.

---

## 1. High-Level Architecture

The `web-interface` server includes an integrated **MFE Registry** and a client-side **MFE Loader** to mount sub-frontends dynamically into the right `#Sidenav` drawer without rebuilding the core server.

```mermaid
sequenceDiagram
    participant MS as Client Microservice (e.g. config-server)
    participant WI as Web Interface Core (Port 5000)
    participant Browser as Browser Client

    Note over MS, WI: Step 1: Registration
    MS->>WI: POST /api/v1/register {name, tag, url, navTitle, layer, category, priority, icon, requiresAuth}
    Note over WI: Persists to mfe_services.json cache
    
    Note over Browser, WI: Step 2: Discovery & Load
    Browser->>WI: Navigates to Dashboard
    WI-->>Browser: Serves base.html + mfe-loader.js
    Browser->>WI: GET /api/v1/services (Query active MFEs)
    WI-->>Browser: Returns registered services JSON (sorted by layer & priority)
    Browser->>Browser: Injects accordions & links into #Sidenav drawer

    Note over Browser, MS: Step 3: Mount & Interaction
    Browser->>Browser: User clicks Link -> Routes to /mfe/{name}
    Browser->>MS: Downloads MFE Script (from url)
    MS-->>Browser: Serves config-server-mfe.js
    Browser->>Browser: Instantiates <config-server-mfe>
    Browser->>MS: MFE Web Component calls backend REST API
```

---

## 2. Integration Specifications

### 2.1 The Registry Endpoints
The registry is built directly into the `web-interface` server on **Port 5000** (or dynamically resolved via `appConfig.GetListenAddr("web_interface")`).
- **POST `/api/v1/register`**: Used by microservices at boot time to publish their frontend configuration.
  ```json
  {
    "name": "config-server",
    "tag": "config-server-mfe",
    "url": "http://localhost:3308/static/js/mfe-loader.js",
    "navTitle": "⚙️ Config Server",
    "layer": "L1",
    "category": "Base Fleet",
    "priority": 20,
    "icon": "fa-cogs",
    "requiresAuth": true
  }
  ```
- **GET `/api/v1/services`**: Used by the web interface loader (`mfe-loader.js`) to fetch all active frontends organized by layer.

### 2.2 3-Tier Service Taxonomy
Micro-frontends are partitioned into 3 distinct operational layers:
1. **L1 - Base Fleet**:
   - Fundamental daemon services powering the node: `watchdog-agent`, `config-server`, `notif-server`, `obsidian-brain` (RAG Engine).
   - Displayed under the `BASE FLEET (L1)` accordion in `#Sidenav`.
2. **L2 - Domain Services**:
   - Business, pipeline, and market microservices: `market-observer`, `stock-analysis`, `realtime-analysis`.
   - Displayed under domain-specific accordions in `#Sidenav`.
3. **L3 - Secure Controls**:
   - Administrative dashboards, KMS key managers, security audits, and sensitive log monitors (`kms-manager`, `audit-vault`).
   - Displayed under `SECURE CONTROLS (L3)`.

### 2.3 Cold-Start Persistence (`mfe_services.json`)
The registry maintains an atomic disk-backed store (`mfe_services.json` via `dbFile` in `src/mfe/registry.go`). When `web-interface` restarts:
- It immediately loads the cached registration list into memory.
- All micro-frontend navigation links are visible with **0-second cold start**, even before microservice re-registration loops trigger.

### 2.4 Client-Side Requirements (The Microservice)
To expose a microfrontend, a sibling microservice must fulfill three strict technical conditions:

#### 1. Serve the Web Component Script (Embedded Standard)
To prevent runtime filesystem path lookup issues in containerized (Docker) or multi-environment setups, the Web Component bundle (`mfe.js`) should be embedded directly into the microservice binary.

*   **Go (Native `//go:embed` - Recommended)**:
    Place the script in the handler's package directory (e.g. `src/rest/mfe.js`) and embed it inside the router handler:
    ```go
    import _ "embed"

    //go:embed mfe.js
    var mfeJS string

    func (h *RESTHandler) RegisterRoutes(mux *http.ServeMux) {
        // ...
        mfeHandler := func(w http.ResponseWriter, r *http.Request) {
            w.Header().Set("Content-Type", "application/javascript")
            w.Write([]byte(mfeJS))
        }
        mux.HandleFunc("/static/js/mfe-loader.js", mfeHandler)
        mux.HandleFunc("/static/mfe.js", mfeHandler) // Legacy path support
    }
    ```

*   **Go Legacy Path (Disk-based fallback)**:
    ```go
    fs := http.FileServer(http.Dir("web/static"))
    mux.Handle("/static/", http.StripPrefix("/static/", fs))
    ```

*   **Python (FastAPI)**:
    ```python
    from fastapi.staticfiles import StaticFiles
    app.mount("/static", StaticFiles(directory="web/static"), name="static")
    ```

#### 2. Support CORS (Cross-Origin Resource Sharing)
Because the Web Component executes in the client's browser (loaded under the `web-interface` domain, e.g., `localhost:5000`), browser security will block direct API queries to your microservice (running on a different port, e.g., `localhost:3308`) unless CORS headers are explicitly sent.
*   **Go (CORS Middleware)**:
    ```go
    func CorsMiddleware(next http.Handler) http.Handler {
        return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            w.Header().Set("Access-Control-Allow-Origin", "*") // Restrict to web-interface in production
            w.Header().Set("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE")
            w.Header().Set("Access-Control-Allow-Headers", "Content-Type, Authorization")
            
            if r.Method == "OPTIONS" {
                w.WriteHeader(http.StatusOK)
                return
            }
            next.ServeHTTP(w, r)
        })
    }
    ```
*   **Python (FastAPI CORS Middleware)**:
    ```python
    from fastapi.middleware.cors import CORSMiddleware
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    ```

#### 3. Automatic Non-Blocking Boot Registration (Ecosystem Standard: `microservice-toolbox/spec`)
During initial bootstrap, microservices register their declarative specification with `web-interface` using the standard `microservice-toolbox/spec` engine. 

> [!IMPORTANT]
> **Zero Manual Loops & Infinite Resilience Contract (`MaxRetries: -1`)**:
> Microservices MUST NOT write bespoke HTTP `urllib` or `http.Client` retry loops. All registration MUST leverage `spec.PublishWithLifecycle` (Go), `spec.publish_with_lifecycle` (Python), or `spec::publish_with_lifecycle` (Rust). The spec engine automatically handles:
> - Non-blocking execution (`ModeNonBlocking`) to prevent startup deadlocks.
> - Infinite retry with randomized exponential backoff until `web-interface` is reachable.
> - Docker Guard address resolution (`0.0.0.0` vs container/host IP).
> - Dynamic version resolution from `VERSION.txt`.
> - Strict fail-fast validation of required metadata.

*   **Go Auto-Registration Hook (`microservice-toolbox/go/pkg/spec`)**:
    ```go
    import (
        "fmt"
        "github.com/Bastien-Antigravity/microservice-toolbox/go/pkg/spec"
    )

    // Register OpenMFE & Service Specification during bootstrap
    spec.PublishWithLifecycle(appConfig, appLogger, spec.ServiceSpec{
        Name:        "config-server",
        Tag:         "config-server-mfe",
        URL:         fmt.Sprintf("http://127.0.0.1:%s/static/js/mfe-loader.js", restPort),
        NavTitle:    "⚙️ Config Server",
        Layer:       "L1",
        Category:    "Base Fleet",
        Priority:    20,
        Icon:        "fa-cogs",
        Description: "Central configuration repository and real-time distributor.",
        Protocol:    "TCP Sync / gRPC / REST",
        Framing:     fmt.Sprintf("Port %s TCP / Port %s REST / Port %s gRPC", tcpPort, restPort, grpcPort),
        DocLink:     "obsidian-brain/06-Microservices/config-server.md",
        RequiresAuth: true,
    })
    ```

*   **Python Auto-Registration Hook (`microservice_toolbox.spec`)**:
    ```python
    from microservice_toolbox.spec import publish_with_lifecycle, ServiceSpec

    # Register OpenMFE & Service Specification during bootstrap
    publish_with_lifecycle(
        app_config,
        logger,
        ServiceSpec(
            name="market-observer",
            tag="market-observer-mfe",
            url=f"http://127.0.0.1:{rest_port}/static/mfe.js",
            nav_title="📈 Market Observer",
            layer="L2",
            category="Trading & Execution",
            priority=10,
            icon="fa-line-chart",
            description="Real-time market data observer and signal ingestion.",
            protocol="HTTP/1.1 REST",
            framing=f"Port {rest_port} REST",
            doc_link="obsidian-brain/06-Microservices/market-observer.md",
            requires_auth=True,
        )
    )
    ```

*   **Rust Auto-Registration Hook (`microservice-toolbox/rust/src/spec.rs`)**:
    ```rust
    use microservice_toolbox::spec::{publish_with_lifecycle, ServiceSpec};

    publish_with_lifecycle(
        &app_config,
        app_logger.clone(),
        ServiceSpec {
            name: "log-server".to_string(),
            tag: "log-server-mfe".to_string(),
            url: format!("http://127.0.0.1:{}/static/mfe.js", rest_port),
            nav_title: "📋 Log Server".to_string(),
            layer: "L1".to_string(),
            category: "Base Fleet".to_string(),
            priority: 30,
            icon: "fa-terminal".to_string(),
            description: "High-performance Rust logging daemon.".to_string(),
            protocol: "SafeSocket TCP / REST".to_string(),
            framing: format!("Port {} SafeSocket TCP", tcp_port),
            doc_link: "obsidian-brain/06-Microservices/log-server.md".to_string(),
            requires_auth: false,
        },
    );
    ```


### 2.3 The Web Component Standard
The microfrontend bundle must register a standard custom HTML5 element. It receives context variables dynamically from the parent loader via attributes (e.g. `base-url`):

```javascript
class ConfigServerMFE extends HTMLElement {
    async connectedCallback() {
        // Inherits parent window location unless explicitly passed
        const baseUrl = this.getAttribute('base-url') || window.location.origin;
        this.innerHTML = `
            <div class="w3-container w3-padding-16">
                <h2 class="w3-border-bottom w3-border-light-grey w3-padding-16">⚙️ Configuration Server</h2>
                <div id="config-list" class="w3-card-4 w3-white w3-padding">
                    <p><i class="fa fa-spinner fa-spin"></i> Fetching active parameters...</p>
                </div>
            </div>
        `;
        this.loadParameters();
    }

    async loadParameters() {
        try {
            // Direct REST communication with microservice (on Port 3308, bypassing facade if needed)
            const res = await fetch('http://localhost:3308/api/v1/config/list');
            const data = await res.json();
            this.renderConfig(data.json_config);
        } catch (err) {
            this.querySelector('#config-list').innerHTML = `<p class="w3-text-red">Error: ${err.message}</p>`;
        }
    }

    renderConfig(jsonConfig) {
        // Render editable fields, update forms, and bind submit to config-server POST API
    }
}
customElements.define('config-server-mfe', ConfigServerMFE);
```

### 2.4 Thematic UI Alignment (Theme Inheritance)
To ensure that pluggable Web Components blend seamlessly into the `web-interface` dashboard shell, they **must not** use hardcoded HEX or RGB colors for themeable elements.

Instead, they must inherit the parent container's styles using **Bastien UI Design Tokens** (CSS variables). These variables are globally defined on the `<html>` or `<body>` tag and change automatically based on active theme settings (e.g., Dark, Light, High Contrast).

#### Required Design Token Variables:
- **Backdrops**: `var(--color-bg-primary)`, `var(--color-bg-secondary)`, `var(--color-bg-surface)`
- **Text**: `var(--color-text-primary)`, `var(--color-text-secondary)`, `var(--color-text-muted)`
- **Accents**: `var(--color-accent-primary)`, `var(--color-accent-success)`, `var(--color-accent-warning)`, `var(--color-accent-danger)`
- **Fonts**: `var(--font-sans)`, `var(--font-display)`, `var(--font-mono)`
- **Sizing**: `var(--font-size-xs)`, `var(--font-size-sm)`, `var(--font-size-base)`, `var(--font-size-lg)`, `var(--font-size-xl)`, `var(--font-size-2xl)`

#### Outer Container & Dynamic Responsive Header Spacing Contract:
To prevent topbar header overlap and ensure fluid, responsive centering across all viewports (Mobile, Tablet, Desktop, Ultra-Wide) for microservices (`config-server`, `notif-server`, `watchdog-agent`, `obsidian-brain` RAG Engine, `squad-control`), every Web Component root container enforces fluid `clamp()` layout math:

```css
.mfe-container, .squad-container, .rag-mfe {
    font-family: var(--font-sans, system-ui, sans-serif);
    color: var(--color-text-primary, #e2e8f0);
    width: 100%;
    max-width: var(--content-max-width, 1400px);
    margin: 0 auto;
    padding: clamp(1.25rem, 2.5vh, 2.25rem) clamp(1.25rem, 3vw, 2.5rem) 3.5rem;
    box-sizing: border-box;
}
```
* **Dynamic Fluid Header Clearance**: `<main id="main" class="bastien-main">` provides `--header-spacing-fluid: calc(var(--topbar-height) + clamp(2.5rem, 5vh, 4.5rem))` (~88px to 120px depending on viewport height).
* **Component Display**: Custom element tags (`<config-server-mfe>`, `<watchdog-agent-mfe>`, etc.) are assigned `display: block; width: 100%; box-sizing: border-box;`.

#### Styling Example (Embedded CSS inside component template):
Define the component's styles utilizing the variables, and provide safe fallback values for standalone rendering:
```css
.mfe-container {
    font-family: var(--font-sans, system-ui, sans-serif);
    color: var(--color-text-primary, #333);
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 16px 24px 40px;
    box-sizing: border-box;
}
.mfe-card {
    background: var(--color-bg-surface, #ffffff);
    border: 1px solid var(--color-bg-secondary, #edf2f7);
}
.mfe-card-title {
    color: var(--color-text-muted, #718096);
    font-size: var(--font-size-xs, 0.75rem);
}
.mfe-mono-data {
    font-family: var(--font-mono, monospace);
}
```

### 2.5 Standardized Client-Side Logging & Telemetry (`BastienLogger`)
To align frontend UI components with the fleet observability standard, all OpenMFE Web Components MUST use the standardized `BastienLogger` utility provided by `web-interface` (`web/static/lib/utils/Logger.js`), accessible globally as `window.BastienLogger`.

#### 1. Ecosystem Log Level Parity
JavaScript `LogLevel` constants strictly mirror the 12-severity-level enumeration defined in `flexible-logger` and `log-server`:
- `NOTSET` = 0
- `DEBUG` = 1
- `STREAM` = 2
- `INFO` = 3
- `LOGON` = 4
- `LOGOUT` = 5
- `TRADE` = 6
- `SCHEDULE` = 7
- `REPORT` = 8
- `WARNING` = 9
- `ERROR` = 10
- `CRITICAL` = 11

> [!NOTE]
> **Warning vs. Warn**: The ecosystem canonical level name is **`WARNING`** (Level 9). Browser DevTools naturally use `console.warn()`. `BastienLogger` provides `logger.warn()` solely as a convenience alias pointing to `logger.warning()`, guaranteeing 1:1 parity with the backend Cap'n Proto and wire schemas.

#### 2. OpenMFE Component Usage Example
Inside any custom element or MFE loader:
```javascript
class MyServiceMFE extends HTMLElement {
    connectedCallback() {
        // Scoped logger instantiation (falls back gracefully to console if run standalone)
        this.logger = window.BastienLogger 
            ? window.BastienLogger.get('my-service-mfe') 
            : console;

        this.logger.info('MyServiceMFE mounted into DOM');
    }

    async fetchData() {
        try {
            const resp = await fetch('http://localhost:3308/api/v1/data');
            // ...
        } catch (err) {
            this.logger.error('Failed to fetch data from backend', { error: err.message });
        }
    }
}
```

#### 3. Dual-Sink Routing & Telemetry Architecture
Client logs are routed through a dual-sink architecture:
1. **Local Sink (Console)**: Immediate, rich CSS color-coded badges in browser DevTools.
2. **Remote Telemetry Sink**: Events at or above `ERROR` severity (or configurable `remoteMinLevel`) are asynchronously dispatched to `POST /api/v1/telemetry/log` using `navigator.sendBeacon` (or non-blocking `fetch({ keepalive: true })`).

```mermaid
sequenceDiagram
    participant Browser as Browser (OpenMFE Component)
    participant WI as web-interface (Port 5000)
    participant UL as universal-logger
    participant LS as log-server (Port 9020 SafeSocket TCP)

    Browser->>Browser: logger.error("Component failed", { code: 500 })
    Browser->>Browser: Print styled badge to DevTools
    Browser->>WI: POST /api/v1/telemetry/log (sendBeacon / fetch)
    Note over WI: Dynamic router unpacks payload
    WI->>UL: universal-logger.Error("[my-service-mfe] Component failed")
    UL->>LS: SafeSocket TCP 4-byte BE framed payload
    Note over LS: Sequenced & written to logs/_main.log
```

#### 4. Network Isolation: Why Browsers Cannot Reach `log-server` Directly
1. **Transport Sandbox**: `log-server` operates on high-speed raw TCP with length-prefixed binary framing (`safe-socket`). Web browsers operate in a sandbox where raw TCP sockets cannot be opened (only HTTP/WebSockets are permitted).
2. **Docker Guard & Security Segmentation**: Internal microservice daemon ports (such as `9020`) are bound to internal container bridges or localhost loops. Directly exposing backend TCP logging ports to external browsers is a critical security vulnerability. `web-interface` acts as the authorized telemetry gateway.

#### 5. Offline Fallback & Self-Healing Queue
When a client cannot reach `web-interface` (e.g. offline client, network partition, or `web-interface` restarting):
- **Zero UI Disruption**: The logger never throws exceptions and never blocks the UI thread.
- **Bounded Offline Ring Buffer**: Unsent telemetry payloads are saved in memory (`_offlineQueue`, max 50 entries) using FIFO eviction to prevent memory bloat.
- **Reconnection Drain**: When network connectivity is restored (`window.addEventListener('online')`), the buffered queue is automatically flushed to `web-interface`.

---

## 3. How to Test & Verify

Follow these steps to run a local sandbox validation:

### 1. Boot up the Web Interface
Navigate to the web interface directory and start the server:
```bash
cd web-interface
go run ./cmd/web-interface
```

### 2. Register a Mockup Service
Simulate a microservice startup by registering a mockup metadata node:
```bash
curl -X POST http://localhost:5000/api/v1/register \
  -H "Content-Type: application/json" \
  -d '{
    "name": "mock-service",
    "tag": "mock-mfe",
    "url": "/static/js/ta-indicators.js",
    "navTitle": "🧪 Mockup Service",
    "layer": "L2",
    "category": "Trading & Execution",
    "priority": 50,
    "icon": "fa-flask",
    "requiresAuth": false
  }'
```

### 3. Open the Dashboard
Open the main `web-interface` (`http://localhost:5000`):
1. **Dynamic Navigation:** Open the right `#Sidenav` drawer (gear / services toggle). The accordion under `TRADING & EXECUTION (L2)` automatically renders the link **🧪 Mockup Service** with its `fa-flask` icon.
2. **Mounting:** Clicking the link loads `/mfe/mock-service`. The loader downloads `ta-indicators.js` and mounts `<mock-mfe>` dynamically inside the page frame.
3. **Cold-Start Verification:** Stop and restart `web-interface`. The mockup service remains immediately available in the menu via `mfe_services.json` cache without re-registering.
