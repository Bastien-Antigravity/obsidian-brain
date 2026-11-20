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
Automatically generated mirror for `web-interface/src/router/router_test.go`.

> **Essential Process**:
> Unit tests for the web interface router, security endpoints, and API status. Verifies route registration, decryption endpoint suppression, and toolbox status.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/mfe/registry.go.md|NewRegistry]] (function: calls) — *NewRegistry instantiates a new Registry, loading existing services from disk.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.RegisterExtended]] (method: calls) — *RegisterExtended registers a microservice with full extended metadata fields.*
- [[web-interface/web-interface/src/mfe/registry.go.md|registry.go]] (imports)
- [[web-interface/web-interface/src/router/dynamic.go.md|BuildServiceRegistry]] (function: calls) — *Adheres strictly to the principle that microservices own and return their own information.*
- [[web-interface/web-interface/src/router/dynamic.go.md|GetMFERegistry]] (function: calls) — *GetMFERegistry returns the active MFE registry instance, if set.*
- [[web-interface/web-interface/src/router/dynamic.go.md|RegisterDynamicRoutes]] (function: calls) — *RegisterDynamicRoutes binds all API, Stock query, and OpenMFE dynamic routes.*
- [[web-interface/web-interface/src/router/dynamic.go.md|SetMFERegistry]] (function: calls) — *SetMFERegistry associates the active MFE registry instance with the router.*
- [[web-interface/web-interface/src/router/dynamic.go.md|dockerProbeCandidates]] (function: calls) — *it prefers the sibling container DNS name and host.docker.internal so container loopback is avoided.*
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (same_package)
- [[web-interface/web-interface/src/router/dynamic.go.md|findRepoPath]] (function: calls) — *workspace and any mounted multi-brain extra workspace directories.*
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Close]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Critical]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Debug]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Error]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Info]] (method: defines_method)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Warning]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/router/autodiscovery.go.md|autodiscovery.go]] (calls)
- [[web-interface/web-interface/src/router/autodiscovery.go.md|autodiscovery.go]] (same_package)
- [[web-interface/web-interface/src/router/contracts_bridges.go.md|contracts_bridges.go]] (calls)
- [[web-interface/web-interface/src/router/contracts_bridges.go.md|contracts_bridges.go]] (same_package)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (same_package)
- [[web-interface/web-interface/src/router/log_bridge.go.md|log_bridge.go]] (calls)
- [[web-interface/web-interface/src/router/log_bridge.go.md|log_bridge.go]] (same_package)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (calls)
- [[web-interface/web-interface/src/router/router.go.md|router.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|TestDecryptionEndpointRemoved]] (function: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|TestDockerProbeCandidatesAndRegistryPreservesBrowserURL]] (function: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|TestExtraWorkspacesDelimitersAndWorkspacesYAMLEndpoints]] (function: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|TestFleetStatusEndpoint]] (function: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|TestMultiBrainAPIEndpointsAndRepoDiscovery]] (function: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|TestSystemLogsEndpoints]] (function: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|TestTelemetryLogEndpoint]] (function: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|TestToolboxStatusEndpoint]] (function: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|init]] (function: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|logRecord]] (struct: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Close]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Critical]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Debug]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Error]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Info]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Warning]] (method: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger]] (struct: belongs_to)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger]] (struct: defines_method)
<!-- SYNC:END -->
