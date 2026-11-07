---
source: web-interface/src/router/mesh_topology_test.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-07T11:06:52.531145
---

# Mirror: mesh_topology_test.go

## 📝 Description
Automatically generated mirror for `web-interface/src/router/mesh_topology_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/mfe/registry.go.md|NewRegistry]] (function: calls) — *NewRegistry instantiates a new Registry, loading existing services from disk.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.Get]] (method: calls) — *Get looks up a registered service by name or tag (case-insensitive, flexible with hyphens/underscores/spaces).*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.RegisterExtended]] (method: calls) — *RegisterExtended registers a microservice with full extended metadata fields.*
- [[web-interface/web-interface/src/mfe/registry.go.md|registry.go]] (imports)
- [[web-interface/web-interface/src/router/mesh_topology.go.md|BuildMeshTopology]] (function: calls) — *- Tier 3: Real-Time WireTap Telemetry (wiretap.Snapshot()) & External Clients (EXT)*
- [[web-interface/web-interface/src/router/mesh_topology.go.md|mesh_topology.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/router/mesh_topology_test.go.md|TestBuildMeshTopology_BaseFleet]] (function: belongs_to)
- [[web-interface/web-interface/src/router/mesh_topology_test.go.md|TestBuildMeshTopology_DynamicRegistrationAndDependencies]] (function: belongs_to)
- [[web-interface/web-interface/src/router/mesh_topology_test.go.md|TestBuildMeshTopology_WireTapTeleRemoteExternalAndSegregation]] (function: belongs_to)
- [[web-interface/web-interface/src/router/mesh_topology_test.go.md|TestMeshTopologyEndpoint_HTTPHandler]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
