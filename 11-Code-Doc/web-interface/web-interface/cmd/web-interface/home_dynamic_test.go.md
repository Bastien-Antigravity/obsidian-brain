---
source: web-interface/cmd/web-interface/home_dynamic_test.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-10-31 21:42:35.175172
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: home_dynamic_test.go

## 📝 Description
Automatically generated mirror for `web-interface/cmd/web-interface/home_dynamic_test.go`.

> **Essential Process**:
> Unit and integration verification for the Home Page dynamic information, dynamic port shifting in fleet health checks, and data accuracy of the service inspector DOM elements (//*[@id="service-inspector"]/div[3]).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/mfe/registry.go.md|NewRegistry]] (function: calls) — *NewRegistry instantiates a new Registry, loading existing services from disk.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.RegisterExtended]] (method: calls) — *RegisterExtended registers a microservice with full extended metadata fields.*
- [[web-interface/web-interface/src/mfe/registry.go.md|registry.go]] (imports)
- [[web-interface/web-interface/src/router/dynamic.go.md|SetMFERegistry]] (function: calls) — *SetMFERegistry associates the active MFE registry instance with the router.*
- [[web-interface/web-interface/src/router/router.go.md|RegisterRoutes]] (function: calls) — *RegisterRoutes initializes the web interface endpoints on the provided ServeMux.*
- [[web-interface/web-interface/src/router/router_test.go.md|router_test.go]] (imports)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/home_dynamic_test.go.md|TestHomeDynamicFleetStatusPortShifting]] (function: belongs_to) — *dynamically returns shifted capability ports from configuration rather than hardcoded fallbacks.*
- [[web-interface/web-interface/cmd/web-interface/home_dynamic_test.go.md|TestKnowledgeGraphPageAndRAGMCPAirGapped]] (function: belongs_to) — *200 OK and that RAG MCP is actively included in the fleet health checks.*
- [[web-interface/web-interface/cmd/web-interface/home_dynamic_test.go.md|TestServiceInspectorDOMAccuracy]] (function: belongs_to) — *and all 10 data-binding elements.*
- [[web-interface/web-interface/cmd/web-interface/home_dynamic_test.go.md|stServiceRegistryEndpointAndDynamicShifting(t]] (function: belongs_to) — *and correctly merges extended OpenMFE microservices.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
