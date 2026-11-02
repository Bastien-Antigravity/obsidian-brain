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

## 📝 Description
Automatically generated mirror for `web-interface/src/router/dynamic.go`.

> **Essential Process**:
> Handles all dynamic API endpoints, stock analysis dashboards, OpenMFE mounting hooks, and system status listings.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/graph/vault_parser.go.md|GetVaultGraph]] (function: calls) — *GetVaultGraph returns the parsed knowledge graph, serving from cache if valid.*
- [[web-interface/web-interface/src/graph/vault_parser.go.md|ResolveVaultPath]] (function: calls) — *ResolveVaultPath discovers the active obsidian-brain vault directory on the host filesystem.*
- [[web-interface/web-interface/src/graph/vault_parser_test.go.md|vault_parser_test.go]] (imports)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.List]] (method: calls) — *6. RegisteredAt timestamp*
- [[web-interface/web-interface/src/mfe/registry.go.md|registry.go]] (imports)
- [[web-interface/web-interface/src/renderer/renderer.go.md|RenderPage]] (function: calls) — *RenderPage parses templates and executes them using context-resolved configuration parameters.*
- [[web-interface/web-interface/src/renderer/renderer.go.md|renderer.go]] (imports)
- [[web-interface/web-interface/src/router/autodiscovery.go.md|autodiscovery.go]] (same_package)
- [[web-interface/web-interface/src/router/autodiscovery.go.md|slugify]] (function: calls)
- [[web-interface/web-interface/src/router/router.go.md|requireAuth]] (function: calls) — *If the user_id session property is missing (0), the request is redirected to the /login endpoint.*
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|router_test.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Close]] (method: calls)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Critical]] (method: calls)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Debug]] (method: calls)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Error]] (method: calls)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Info]] (method: calls)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Warning]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|BuildServiceRegistry]] (function: belongs_to) — *Adheres strictly to the principle that microservices own and return their own information.*
- [[web-interface/web-interface/src/router/dynamic.go.md|FleetHealthResponse]] (struct: belongs_to) — *FleetHealthResponse summarizes overall fleet health for UI alerting.*
- [[web-interface/web-interface/src/router/dynamic.go.md|GetMFERegistry]] (function: belongs_to) — *GetMFERegistry returns the active MFE registry instance, if set.*
- [[web-interface/web-interface/src/router/dynamic.go.md|RegisterDynamicRoutes]] (function: belongs_to) — *RegisterDynamicRoutes binds all API, Stock query, and OpenMFE dynamic routes.*
- [[web-interface/web-interface/src/router/dynamic.go.md|ServiceHealthStatus]] (struct: belongs_to) — *ServiceHealthStatus holds individual service reachability state.*
- [[web-interface/web-interface/src/router/dynamic.go.md|ServiceProtocolSpec]] (struct: belongs_to) — *ServiceProtocolSpec describes an individual network port/protocol of a service.*
- [[web-interface/web-interface/src/router/dynamic.go.md|ServiceRegistryEntry]] (struct: belongs_to) — *ServiceRegistryEntry represents the complete dynamic and mechanical metadata for a microservice.*
- [[web-interface/web-interface/src/router/dynamic.go.md|ServiceRegistryResponse]] (struct: belongs_to) — *ServiceRegistryResponse holds the fleet map and metadata summary.*
- [[web-interface/web-interface/src/router/dynamic.go.md|SetMFERegistry]] (function: belongs_to) — *SetMFERegistry associates the active MFE registry instance with the router.*
- [[web-interface/web-interface/src/router/dynamic.go.md|checkFleetServicesHealth]] (function: belongs_to) — *Discovers targets dynamically from appConfig capabilities and OpenMFE registrations without hardcoded slices.*
- [[web-interface/web-interface/src/router/dynamic.go.md|formatCapabilityTitle]] (function: belongs_to) — *formatCapabilityTitle converts capability keys like "config_server" to "Config Server".*
- [[web-interface/web-interface/src/router/dynamic.go.md|normalizeCapKey]] (function: belongs_to) — *normalizeCapKey normalizes capability identifiers to canonical snake_case capability keys.*
- [[web-interface/web-interface/src/router/dynamic.go.md|parseMCPPort]] (function: belongs_to) — *parseMCPPort extracts the MCP SSE port from rag_engine capability.*
- [[web-interface/web-interface/src/router/dynamic.go.md|targetSvc]] (struct: belongs_to)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (calls)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|router_test.go]] (calls)
- [[web-interface/web-interface/src/router/router_test.go.md|router_test.go]] (same_package)
<!-- SYNC:END -->
