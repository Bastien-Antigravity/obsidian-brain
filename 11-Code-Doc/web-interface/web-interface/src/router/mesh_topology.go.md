---
source: web-interface/src/router/mesh_topology.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-07T14:41:21.255918
---

# Mirror: mesh_topology.go

## 📝 Description
Automatically generated mirror for `web-interface/src/router/mesh_topology.go`.

> **Essential Process**:
> Builds the dynamic Interservice Transport Mesh Topology (/api/v1/system/mesh-topology) by cleanly separating and merging three distinct architectural tiers: 1. Standard Base Microservices (L1-L3 11 foundational services from base_ecosystem.go). 2. Other Ecosystem Components & Future Microservices (> L3 or OpenMFE spec-driven). 3. Real-Time WireTap Transport Telemetry (wiretap.Snapshot()) & External Gateways (EXT), which dynamically synthesizes nodes, links, particle streams, and segregated channels directly from live transport wrapper observations.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.List]] (method: calls) — *6. RegisteredAt timestamp*
- [[web-interface/web-interface/src/mfe/registry.go.md|registry.go]] (imports)
- [[web-interface/web-interface/src/router/base_ecosystem.go.md|baseProtocolCatalog]] (function: calls)
- [[web-interface/web-interface/src/router/base_ecosystem.go.md|base_ecosystem.go]] (same_package)
- [[web-interface/web-interface/src/router/base_ecosystem.go.md|defaultSegregatedChannelsForLink]] (function: calls)
- [[web-interface/web-interface/src/router/base_ecosystem.go.md|newBaseEcosystemNodes]] (function: calls) — *newBaseEcosystemNodes returns a fresh map of the 11 foundational L1-L3 nodes.*
- [[web-interface/web-interface/src/router/dynamic.go.md|GetMFERegistry]] (function: calls) — *GetMFERegistry returns the active MFE registry instance, if set.*
- [[web-interface/web-interface/src/router/dynamic.go.md|checkFleetServicesHealth]] (function: calls) — *Discovers targets dynamically from appConfig capabilities and OpenMFE registrations without hardcoded slices.*
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (same_package)
- [[web-interface/web-interface/src/router/dynamic.go.md|formatCapabilityTitle]] (function: calls) — *formatCapabilityTitle converts capability keys like "config_server" to "Config Server".*
- [[web-interface/web-interface/src/router/dynamic.go.md|resolveAuthoritativeEndpoint]] (function: calls) — *- Secondary Fallback: Alternate endpoint if distinct*
- [[web-interface/web-interface/web/static/js/home-transport-mesh.js.md|addLink]] (function: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (calls)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (same_package)
- [[web-interface/web-interface/src/router/mesh_topology.go.md|BuildMeshTopology]] (function: belongs_to) — *- Tier 3: Real-Time WireTap Telemetry (wiretap.Snapshot()) & External Clients (EXT)*
- [[web-interface/web-interface/src/router/mesh_topology.go.md|MeshTopologyLink]] (struct: belongs_to) — *MeshTopologyLink represents an authoritative interservice wire / connection in the mesh.*
- [[web-interface/web-interface/src/router/mesh_topology.go.md|MeshTopologyNode]] (struct: belongs_to) — *MeshTopologyNode represents an active ecosystem service or external node in the SVG mesh.*
- [[web-interface/web-interface/src/router/mesh_topology.go.md|MeshTopologyParticleStream]] (struct: belongs_to) — *MeshTopologyParticleStream represents an animated particle telemetry stream along a mesh link.*
- [[web-interface/web-interface/src/router/mesh_topology.go.md|MeshTopologyProtocol]] (struct: belongs_to) — *MeshTopologyProtocol describes a communication protocol filter and active wire count.*
- [[web-interface/web-interface/src/router/mesh_topology.go.md|MeshTopologyResponse]] (struct: belongs_to) — *MeshTopologyResponse holds the full serialized topology payload.*
- [[web-interface/web-interface/src/router/mesh_topology.go.md|calculateDynamicMeshNodePosition]] (function: belongs_to)
- [[web-interface/web-interface/src/router/mesh_topology.go.md|ensureWireTapNodeExists]] (function: belongs_to) — *that has not been registered yet.*
- [[web-interface/web-interface/src/router/mesh_topology.go.md|ingestBaseEcosystemTier]] (function: belongs_to) — *ingestBaseEcosystemTier resolves dynamic ports and live health for the 11 standard base services.*
- [[web-interface/web-interface/src/router/mesh_topology.go.md|ingestDynamicAndFutureMicroservicesTier]] (function: belongs_to) — *microservices (> L3, L2, L4+) from the OpenMFE specification registry.*
- [[web-interface/web-interface/src/router/mesh_topology.go.md|ingestWireTapRealTimeTelemetry]] (function: belongs_to) — *3. Enrich existing links with real-time frame/byte counters and segregated information channels.*
- [[web-interface/web-interface/src/router/mesh_topology.go.md|meshSlotCoord]] (struct: belongs_to)
- [[web-interface/web-interface/src/router/mesh_topology.go.md|normalizeTopologyNodeID]] (function: belongs_to)
- [[web-interface/web-interface/src/router/mesh_topology.go.md|resolveWireTapEdgeMetadata]] (function: belongs_to) — *badge label, inspector exchange ID, and particle color.*
- [[web-interface/web-interface/src/router/mesh_topology_test.go.md|mesh_topology_test.go]] (calls)
- [[web-interface/web-interface/src/router/mesh_topology_test.go.md|mesh_topology_test.go]] (same_package)
- [[web-interface/web-interface/src/router/spec_exchange_test.go.md|spec_exchange_test.go]] (calls)
- [[web-interface/web-interface/src/router/spec_exchange_test.go.md|spec_exchange_test.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
