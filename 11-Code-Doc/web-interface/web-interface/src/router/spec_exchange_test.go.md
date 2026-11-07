---
source: web-interface/src/router/spec_exchange_test.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-07T12:21:44.820555
---

# Mirror: spec_exchange_test.go

## 📝 Description
Automatically generated mirror for `web-interface/src/router/spec_exchange_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/mfe/registry.go.md|NewRegistry]] (function: calls) — *NewRegistry instantiates a new Registry, loading existing services from disk.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.EnsureFoundationalServices]] (method: calls) — *have complete self-describing manifests loaded into the registry using dynamic parameters from appConfig.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.Get]] (method: calls) — *Get looks up a registered service by name or tag (case-insensitive, flexible with hyphens/underscores/spaces).*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.RegisterHandlers]] (method: calls) — *RegisterHandlers binds the MFE endpoints to the HTTP ServeMux.*
- [[web-interface/web-interface/src/mfe/registry.go.md|registry.go]] (imports)
- [[web-interface/web-interface/src/router/dynamic.go.md|BuildServiceRegistry]] (function: calls) — *Adheres strictly to the principle that microservices own and return their own information.*
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (same_package)
- [[web-interface/web-interface/src/router/mesh_topology.go.md|BuildMeshTopology]] (function: calls) — *- Tier 3: Real-Time WireTap Telemetry (wiretap.Snapshot()) & External Clients (EXT)*
- [[web-interface/web-interface/src/router/mesh_topology.go.md|mesh_topology.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/router/spec_exchange_test.go.md|TestSpecExchangeDynamicConfigOverride_BaseEcosystemServices]] (function: belongs_to) — *with ZERO hardcoded static literals.*
- [[web-interface/web-interface/src/router/spec_exchange_test.go.md|TestSpecExchangeEndToEnd_RegistrationAvailabilityAndUsage]] (function: belongs_to) — *and authoritative exchange links) with ZERO hardcoded fallbacks or overrides.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
