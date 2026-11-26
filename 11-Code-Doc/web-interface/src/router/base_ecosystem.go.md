---
source: web-interface/src/router/base_ecosystem.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-07 14:41:21.244114
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: base_ecosystem.go

## 📝 Description
Automatically generated mirror for `web-interface/src/router/base_ecosystem.go`.

> **Essential Process**:
> Defines the baseline structural topology and default segregated channel descriptors strictly for the 11 Standard Base Microservices (L1-L3 foundational ecosystem). All non-base ecosystem components, external clients/gateways (EXT), and future domain microservices (> L3) are discovered dynamically via WireTap and OpenMFE in mesh_topology.go.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[web-interface/cmd/web-interface/fleet_health_scenario_test.go.md|fleet_health_scenario_test.go]] (imports)
- [[web-interface/cmd/web-interface/home_dynamic_test.go.md|home_dynamic_test.go]] (imports)
- [[web-interface/cmd/web-interface/main.go.md|main.go]] (imports)
- [[web-interface/cmd/web-interface/main_test.go.md|main_test.go]] (imports)
- [[web-interface/src/router/base_ecosystem.go.md|baseProtocolCatalog]] (function: belongs_to)
- [[web-interface/src/router/base_ecosystem.go.md|defaultSegregatedChannelsForLink]] (function: belongs_to)
- [[web-interface/src/router/base_ecosystem.go.md|newBaseEcosystemNodes]] (function: belongs_to) — *newBaseEcosystemNodes returns a fresh map of the 11 foundational L1-L3 nodes.*
- [[web-interface/src/router/mesh_topology.go.md|mesh_topology.go]] (calls)
- [[web-interface/src/router/mesh_topology.go.md|mesh_topology.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
