---
source: web-interface/src/router/contracts_bridges.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-10T13:21:54.639538
---

# Mirror: contracts_bridges.go

## 📝 Description
Automatically generated mirror for `web-interface/src/router/contracts_bridges.go`.

> **Essential Process**:
> Provides live contract introspection bridges for infrastructure and stream-only base microservices (NATS HTTP Monitoring & JetStream, Tele-Remote registry specs). Ensures OpenMFE contract tabs render reliable, exhaustive specifications sourced directly from active runtime endpoints and microservice-published ServiceSpecs.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.Get]] (method: calls) — *Get looks up a registered service by name or tag (case-insensitive, flexible with hyphens/underscores/spaces).*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.List]] (method: calls) — *6. RegisteredAt timestamp*
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (same_package)
- [[web-interface/web-interface/src/router/dynamic.go.md|resolveAuthoritativeEndpoint]] (function: calls) — *- Secondary Fallback: Alternate endpoint if distinct*
- [[web-interface/web-interface/src/router/router_test.go.md|router_test.go]] (same_package)
- [[web-interface/web-interface/src/router/router_test.go.md|testLogger.Close]] (method: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/router/contracts_bridges.go.md|buildNatsContractsFromIntrospection]] (function: belongs_to)
- [[web-interface/web-interface/src/router/contracts_bridges.go.md|handleGetNatsContracts]] (function: belongs_to)
- [[web-interface/web-interface/src/router/contracts_bridges.go.md|handleGetTeleRemoteContracts]] (function: belongs_to)
- [[web-interface/web-interface/src/router/contracts_bridges.go.md|natsMonitorFetcher]] (struct: belongs_to)
- [[web-interface/web-interface/src/router/contracts_bridges_test.go.md|contracts_bridges_test.go]] (calls)
- [[web-interface/web-interface/src/router/contracts_bridges_test.go.md|contracts_bridges_test.go]] (same_package)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
