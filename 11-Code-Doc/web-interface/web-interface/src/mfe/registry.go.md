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
Automatically generated mirror for `web-interface/src/mfe/registry.go`.

> **Essential Process**:
> Manages dynamic Micro-Frontend (OpenMFE) service registration and cataloging. Enforces ecosystem layer taxonomy (L1 Core, L2 Domain, L3 Secure), priority ordering, URL/tag deduplication, and atomic disk persistence.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/mfe/registry.go.md|CanvasSpec.UnmarshalJSON]] (method: defines_method) — *UnmarshalJSON supports both camelCase (preferredX) and snake_case (preferred_x).*
- [[web-interface/web-interface/src/mfe/registry.go.md|HealthSpec.UnmarshalJSON]] (method: defines_method) — *UnmarshalJSON supports both camelCase (timeoutMs) and snake_case (timeout_ms).*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.EnsureFoundationalServices]] (method: defines_method) — *have complete self-describing manifests loaded into the registry using dynamic parameters from appConfig.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.ensureFoundationalServicesLocked]] (method: defines_method) — *ensureFoundationalServicesLocked guarantees baseline infrastructure daemons exist using appConfig.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.load]] (method: defines_method)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|mockLogger.Error]] (method: calls)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|mockLogger.Info]] (method: calls)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|mockLogger.Warning]] (method: calls)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|registry_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/fleet_health_scenario_test.go.md|fleet_health_scenario_test.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/fleet_health_scenario_test.go.md|fleet_health_scenario_test.go]] (imports)
- [[web-interface/web-interface/cmd/web-interface/home_dynamic_test.go.md|home_dynamic_test.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/home_dynamic_test.go.md|home_dynamic_test.go]] (imports)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main.go.md|main.go]] (imports)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|main_test.go]] (calls)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|main_test.go]] (imports)
- [[web-interface/web-interface/src/mfe/registry.go.md|Alias]] (struct: belongs_to)
- [[web-interface/web-interface/src/mfe/registry.go.md|CanvasSpec.UnmarshalJSON]] (method: belongs_to) — *UnmarshalJSON supports both camelCase (preferredX) and snake_case (preferred_x).*
- [[web-interface/web-interface/src/mfe/registry.go.md|CanvasSpec]] (struct: belongs_to) — *CanvasSpec declares presentation attributes for the transport SVG mesh canvas and UI tiers.*
- [[web-interface/web-interface/src/mfe/registry.go.md|CanvasSpec]] (struct: defines_method) — *CanvasSpec declares presentation attributes for the transport SVG mesh canvas and UI tiers.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Dependency]] (struct: belongs_to) — *Dependency represents a declared downstream dependency of a microservice.*
- [[web-interface/web-interface/src/mfe/registry.go.md|HealthSpec.UnmarshalJSON]] (method: belongs_to) — *UnmarshalJSON supports both camelCase (timeoutMs) and snake_case (timeout_ms).*
- [[web-interface/web-interface/src/mfe/registry.go.md|HealthSpec]] (struct: belongs_to) — *HealthSpec standardizes declarative health check and reachability probes.*
- [[web-interface/web-interface/src/mfe/registry.go.md|HealthSpec]] (struct: defines_method) — *HealthSpec standardizes declarative health check and reachability probes.*
- [[web-interface/web-interface/src/mfe/registry.go.md|NewRegistry]] (function: belongs_to) — *NewRegistry instantiates a new Registry, loading existing services from disk.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.EnsureFoundationalServices]] (method: belongs_to) — *have complete self-describing manifests loaded into the registry using dynamic parameters from appConfig.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.ensureFoundationalServicesLocked]] (method: belongs_to) — *ensureFoundationalServicesLocked guarantees baseline infrastructure daemons exist using appConfig.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.load]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry]] (struct: belongs_to) — *Registry manages the registration and listing of microfrontend services.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry]] (struct: defines_method) — *Registry manages the registration and listing of microfrontend services.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Service]] (struct: belongs_to) — *Service represents a registered Micro-Frontend service with layer taxonomy.*
- [[web-interface/web-interface/src/mfe/registry.go.md|erReq struc]] (struct: belongs_to)
- [[web-interface/web-interface/src/mfe/registry.go.md|riority(prior]] (function: belongs_to) — *Supports integer, float64, numeric string, or order alias; defaults to 100 if missing or invalid.*
- [[web-interface/web-interface/src/mfe/registry_test.go.md|registry_test.go]] (calls)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|registry_test.go]] (same_package)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (imports)
- [[web-interface/web-interface/src/router/mesh_topology_test.go.md|mesh_topology_test.go]] (calls)
- [[web-interface/web-interface/src/router/mesh_topology_test.go.md|mesh_topology_test.go]] (imports)
- [[web-interface/web-interface/src/router/spec_exchange_test.go.md|spec_exchange_test.go]] (calls)
- [[web-interface/web-interface/src/router/spec_exchange_test.go.md|spec_exchange_test.go]] (imports)
<!-- SYNC:END -->
