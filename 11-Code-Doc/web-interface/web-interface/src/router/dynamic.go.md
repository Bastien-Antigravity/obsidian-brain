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
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|logBridgeClient.GetTailLogs]] (method: calls)
- [[web-interface/web-interface/src/logclient/log_service_grpc.pb.go.md|log_service_grpc.pb.go]] (imports)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.Get]] (method: calls) — *Get looks up a registered service by name or tag (case-insensitive, flexible with hyphens/underscores/spaces).*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.List]] (method: calls) — *6. RegisteredAt timestamp*
- [[web-interface/web-interface/src/mfe/registry.go.md|registry.go]] (imports)
- [[web-interface/web-interface/src/renderer/renderer.go.md|RenderPage]] (function: calls) — *RenderPage parses templates and executes them using context-resolved configuration parameters.*
- [[web-interface/web-interface/src/renderer/renderer.go.md|renderer.go]] (imports)
- [[web-interface/web-interface/src/router/autodiscovery.go.md|autodiscovery.go]] (same_package)
- [[web-interface/web-interface/src/router/autodiscovery.go.md|slugify]] (function: calls)
- [[web-interface/web-interface/src/router/log_bridge.go.md|getLogBridgeClient]] (function: calls) — *getLogBridgeClient resolves or reuses the singleton gRPC connection to log-server.*
- [[web-interface/web-interface/src/router/log_bridge.go.md|handleGetTailLogs]] (function: calls) — *handleGetTailLogs queries recent buffered logs from log-server ring buffer via gRPC*
- [[web-interface/web-interface/src/router/log_bridge.go.md|handleStreamLogsSSE]] (function: calls) — *handleStreamLogsSSE streams incoming fleet logs in real-time over HTTP Server-Sent Events (SSE).*
- [[web-interface/web-interface/src/router/log_bridge.go.md|log_bridge.go]] (same_package)
- [[web-interface/web-interface/src/router/mesh_topology.go.md|BuildMeshTopology]] (function: calls) — *- Tier 3: Real-Time WireTap Telemetry (wiretap.Snapshot()) & External Clients (EXT)*
- [[web-interface/web-interface/src/router/mesh_topology.go.md|mesh_topology.go]] (same_package)
- [[web-interface/web-interface/src/router/mesh_topology.go.md|normalizeTopologyNodeID]] (function: calls)
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
- [[web-interface/web-interface/cmd/web-interface/fleet_health_scenario_test.go.md|fleet_health_scenario_test.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/home_dynamic_test.go.md|home_dynamic_test.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|BuildServiceRegistry]] (function: belongs_to) — *Adheres strictly to the principle that microservices own and return their own information.*
- [[web-interface/web-interface/src/router/dynamic.go.md|FleetHealthResponse]] (struct: belongs_to) — *FleetHealthResponse summarizes overall fleet health for UI alerting.*
- [[web-interface/web-interface/src/router/dynamic.go.md|GetMFERegistry]] (function: belongs_to) — *GetMFERegistry returns the active MFE registry instance, if set.*
- [[web-interface/web-interface/src/router/dynamic.go.md|MCPCallRecord]] (struct: belongs_to) — *MCPCallRecord captures request and response metadata for the live FastMCP inspector.*
- [[web-interface/web-interface/src/router/dynamic.go.md|RegisterDynamicRoutes]] (function: belongs_to) — *RegisterDynamicRoutes binds all API, Stock query, and OpenMFE dynamic routes.*
- [[web-interface/web-interface/src/router/dynamic.go.md|ServiceHealthStatus]] (struct: belongs_to) — *ServiceHealthStatus holds individual service reachability state.*
- [[web-interface/web-interface/src/router/dynamic.go.md|ServiceProtocolSpec]] (struct: belongs_to) — *ServiceProtocolSpec describes an individual network port/protocol of a service.*
- [[web-interface/web-interface/src/router/dynamic.go.md|ServiceRegistryEntry]] (struct: belongs_to) — *ServiceRegistryEntry represents the complete dynamic and mechanical metadata for a microservice.*
- [[web-interface/web-interface/src/router/dynamic.go.md|ServiceRegistryResponse]] (struct: belongs_to) — *ServiceRegistryResponse holds the fleet map and metadata summary.*
- [[web-interface/web-interface/src/router/dynamic.go.md|SetMFERegistry]] (function: belongs_to) — *SetMFERegistry associates the active MFE registry instance with the router.*
- [[web-interface/web-interface/src/router/dynamic.go.md|checkFleetServicesHealth]] (function: belongs_to) — *Discovers targets dynamically from appConfig capabilities and OpenMFE registrations without hardcoded slices.*
- [[web-interface/web-interface/src/router/dynamic.go.md|clientInfo]] (struct: belongs_to)
- [[web-interface/web-interface/src/router/dynamic.go.md|formatCapabilityTitle]] (function: belongs_to) — *formatCapabilityTitle converts capability keys like "config_server" to "Config Server".*
- [[web-interface/web-interface/src/router/dynamic.go.md|getSubCapabilityAddr]] (function: belongs_to) — *getSubCapabilityAddr extracts host:port for a nested capability block (e.g. capabilities.rag_engine.mcp).*
- [[web-interface/web-interface/src/router/dynamic.go.md|menuItem]] (struct: belongs_to)
- [[web-interface/web-interface/src/router/dynamic.go.md|normalizeCapKey]] (function: belongs_to) — *normalizeCapKey normalizes capability identifiers to canonical snake_case capability keys.*
- [[web-interface/web-interface/src/router/dynamic.go.md|recordMCPCall]] (function: belongs_to)
- [[web-interface/web-interface/src/router/dynamic.go.md|resolveAuthoritativeEndpoint]] (function: belongs_to) — *- Secondary Fallback: Alternate endpoint if distinct*
- [[web-interface/web-interface/src/router/dynamic.go.md|resolveFastMCPBaseURL]] (function: belongs_to) — *resolveFastMCPBaseURL resolves the root HTTP base URL of the FastMCP daemon directly from config.*
- [[web-interface/web-interface/src/router/dynamic.go.md|resolveMCPURL]] (function: belongs_to) — *resolveMCPURL resolves the authoritative FastMCP HTTP/SSE endpoint for RAG Engine directly from config.*
- [[web-interface/web-interface/src/router/dynamic.go.md|targetSvc]] (struct: belongs_to)
- [[web-interface/web-interface/src/router/mesh_topology.go.md|mesh_topology.go]] (calls)
- [[web-interface/web-interface/src/router/mesh_topology.go.md|mesh_topology.go]] (same_package)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (calls)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|router_test.go]] (calls)
- [[web-interface/web-interface/src/router/router_test.go.md|router_test.go]] (same_package)
- [[web-interface/web-interface/src/router/spec_exchange_test.go.md|spec_exchange_test.go]] (calls)
- [[web-interface/web-interface/src/router/spec_exchange_test.go.md|spec_exchange_test.go]] (same_package)
<!-- SYNC:END -->
