---
source: web-interface/src/router/contracts_bridges_test.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-10 13:21:54.647120
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: contracts_bridges_test.go

## 📝 Description
Automatically generated mirror for `web-interface/src/router/contracts_bridges_test.go`.

> **Essential Process**:
> Unit tests verifying NATS and Tele-Remote exchange contract bridges operate on real runtime introspection payloads and registered microservice specs without hardcoding fake fallback schemas.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/src/mfe/registry.go.md|NewRegistry]] (function: calls) — *NewRegistry instantiates a new Registry, loading existing services from disk.*
- [[web-interface/src/mfe/registry.go.md|Registry.RegisterExtended]] (method: calls) — *RegisterExtended registers a microservice with full extended metadata fields.*
- [[web-interface/src/mfe/registry.go.md|registry.go]] (imports)
- [[web-interface/src/router/contracts_bridges.go.md|buildNatsContractsFromIntrospection]] (function: calls)
- [[web-interface/src/router/contracts_bridges.go.md|contracts_bridges.go]] (same_package)
- [[web-interface/src/router/contracts_bridges.go.md|handleGetNatsContracts]] (function: calls)
- [[web-interface/src/router/contracts_bridges.go.md|handleGetTeleRemoteContracts]] (function: calls)
- [[web-interface/src/router/dynamic.go.md|BuildServiceAIContext]] (function: calls) — *live runtime config, AI-Init.md, and AGENTS.md.*
- [[web-interface/src/router/dynamic.go.md|dynamic.go]] (same_package)
- [[web-interface/src/router/log_bridge.go.md|handleGetLogContracts]] (function: calls) — *falling back only to log-server's own published ServiceSpec in the MFE registry if gRPC is unavailable.*
- [[web-interface/src/router/log_bridge.go.md|log_bridge.go]] (same_package)
- [[web-interface/src/router/router.go.md|RegisterRoutes]] (function: calls) — *RegisterRoutes initializes the web interface endpoints on the provided ServeMux.*
- [[web-interface/src/router/router.go.md|router.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/src/router/contracts_bridges_test.go.md|TestBuildNatsContractsFromIntrospection]] (function: belongs_to)
- [[web-interface/src/router/contracts_bridges_test.go.md|TestBuildServiceAIContext]] (function: belongs_to)
- [[web-interface/src/router/contracts_bridges_test.go.md|TestLogContractsFailClosedWithoutConfig]] (function: belongs_to)
- [[web-interface/src/router/contracts_bridges_test.go.md|TestNatsContractsFailClosedWithoutConfig]] (function: belongs_to)
- [[web-interface/src/router/contracts_bridges_test.go.md|TestServiceAIContextEndpoint]] (function: belongs_to)
- [[web-interface/src/router/contracts_bridges_test.go.md|TestTeleRemoteContractsFromRegistry]] (function: belongs_to)
- [[web-interface/src/router/contracts_bridges_test.go.md|setupIsolatedLogServerDocs]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
