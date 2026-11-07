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
- [[web-interface/web-interface/backup_cleaned_assets/web/static/js/realtime-common.js.md|ConnectionManager.log]] (method: calls)
- [[web-interface/web-interface/src/graph/vault_parser_test.go.md|vault_parser_test.go]] (imports)
- [[web-interface/web-interface/src/mfe/registry.go.md|registry.go]] (imports)
- [[web-interface/web-interface/src/renderer/renderer.go.md|RenderPage]] (function: calls) — *RenderPage parses templates and executes them using context-resolved configuration parameters.*
- [[web-interface/web-interface/src/renderer/renderer.go.md|renderer.go]] (imports)
- [[web-interface/web-interface/src/router/router.go.md|requireAuth]] (function: calls) — *If the user_id session property is missing (0), the request is redirected to the /login endpoint.*
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|router_test.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Close]] (method: calls)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/fleet_health_scenario_test.go.md|fleet_health_scenario_test.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/home_dynamic_test.go.md|home_dynamic_test.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|	raw = strings.]] (function: belongs_to) — *normalizeCapKey normalizes capability identifiers to canonical snake_case capability keys.*
- [[web-interface/web-interface/src/router/dynamic.go.md|                      `]] (struct: belongs_to) — *ServiceRegistryResponse holds the fleet map and metadata summary.*
- [[web-interface/web-interface/src/router/dynamic.go.md|                    ]] (struct: belongs_to) — *ServiceRegistryEntry represents the complete dynamic and mechanical metadata for a microservice.*
- [[web-interface/web-interface/src/router/dynamic.go.md| string `json:"name]] (struct: belongs_to) — *ServiceHealthStatus holds individual service reachability state.*
- [[web-interface/web-interface/src/router/dynamic.go.md| string {
	words := s]] (function: belongs_to) — *formatCapabilityTitle converts capability keys like "config_server" to "Config Server".*
- [[web-interface/web-interface/src/router/dynamic.go.md| strings.ToLower(string]] (function: belongs_to)
- [[web-interface/web-interface/src/router/dynamic.go.md|"id"`
	Name     ]] (struct: belongs_to) — *MeshTopologyNode represents an active ecosystem service node in the transport SVG mesh.*
- [[web-interface/web-interface/src/router/dynamic.go.md|) MeshTopologyRes]] (function: belongs_to) — *invariant transport links, and declared interservice dependencies.*
- [[web-interface/web-interface/src/router/dynamic.go.md|GetMFERegistry]] (function: belongs_to) — *GetMFERegistry returns the active MFE registry instance, if set.*
- [[web-interface/web-interface/src/router/dynamic.go.md|MCPCallRecord]] (struct: belongs_to) — *MCPCallRecord captures request and response metadata for the live FastMCP inspector.*
- [[web-interface/web-interface/src/router/dynamic.go.md|RegisterDynamicRoutes]] (function: belongs_to) — *RegisterDynamicRoutes binds all API, Stock query, and OpenMFE dynamic routes.*
- [[web-interface/web-interface/src/router/dynamic.go.md|SetMFERegistry]] (function: belongs_to) — *SetMFERegistry associates the active MFE registry instance with the router.*
- [[web-interface/web-interface/src/router/dynamic.go.md|box_config.AppConfig)]] (function: belongs_to) — *resolveFastMCPBaseURL resolves the root HTTP base URL of the FastMCP daemon directly from config.*
- [[web-interface/web-interface/src/router/dynamic.go.md|fig) ServiceRegistry]] (function: belongs_to) — *Adheres strictly to the principle that microservices own and return their own information.*
- [[web-interface/web-interface/src/router/dynamic.go.md|g
		capab]] (struct: belongs_to)
- [[web-interface/web-interface/src/router/dynamic.go.md|g *toolbox_config.AppConfig,]] (function: belongs_to) — *- Secondary Fallback: Alternate endpoint if distinct*
- [[web-interface/web-interface/src/router/dynamic.go.md|id"`
	From      ]] (struct: belongs_to) — *MeshTopologyLink represents an authoritative interservice wire / connection in the mesh.*
- [[web-interface/web-interface/src/router/dynamic.go.md|ientInfo s]] (struct: belongs_to)
- [[web-interface/web-interface/src/router/dynamic.go.md|ig.AppConfig)]] (function: belongs_to) — *resolveMCPURL resolves the authoritative FastMCP HTTP/SSE endpoint for RAG Engine directly from config.*
- [[web-interface/web-interface/src/router/dynamic.go.md|n:"type"` // "TCP",]] (struct: belongs_to) — *ServiceProtocolSpec describes an individual network port/protocol of a service.*
- [[web-interface/web-interface/src/router/dynamic.go.md|ne       bool      ]] (struct: belongs_to) — *FleetHealthResponse summarizes overall fleet health for UI alerting.*
- [[web-interface/web-interface/src/router/dynamic.go.md|nuItem s]] (struct: belongs_to)
- [[web-interface/web-interface/src/router/dynamic.go.md|on:"id"`
	Name      ]] (struct: belongs_to) — *MeshTopologyProtocol describes a communication protocol filter and active wire count.*
- [[web-interface/web-interface/src/router/dynamic.go.md|oolbox_config.AppConfig)]] (function: belongs_to) — *Discovers targets dynamically from appConfig capabilities and OpenMFE registrations without hardcoded slices.*
- [[web-interface/web-interface/src/router/dynamic.go.md|ox_config.AppConfig,]] (function: belongs_to) — *getSubCapabilityAddr extracts host:port for a nested capability block (e.g. capabilities.rag_engine.mcp).*
- [[web-interface/web-interface/src/router/dynamic.go.md|recordMCPCall]] (function: belongs_to)
- [[web-interface/web-interface/src/router/dynamic.go.md|ring]MeshTopologyNod]] (struct: belongs_to)
- [[web-interface/web-interface/src/router/dynamic.go.md|shTopologyNode, nodeID string) (]] (function: belongs_to)
- [[web-interface/web-interface/src/router/dynamic.go.md|son:"linkId"`
	Color  stri]] (struct: belongs_to) — *MeshTopologyParticleStream represents an animated particle telemetry stream along a mesh link.*
- [[web-interface/web-interface/src/router/dynamic.go.md|ynamicMeshSlo]] (struct: belongs_to)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (calls)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|router_test.go]] (calls)
- [[web-interface/web-interface/src/router/router_test.go.md|router_test.go]] (same_package)
<!-- SYNC:END -->
