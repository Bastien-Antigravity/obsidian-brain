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
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.List]] (method: defines_method) — *6. RegisteredAt timestamp*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.RegisterExtended]] (method: defines_method) — *RegisterExtended registers a microservice with full extended metadata fields.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.RegisterHandlers]] (method: defines_method) — *RegisterHandlers binds the MFE endpoints to the HTTP ServeMux.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.Register]] (method: defines_method) — *Register adds or updates a microfrontend service in the registry with automatic deduplication.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.Unregister]] (method: defines_method) — *Unregister removes a service from the registry by name or tag, persisting changes immediately.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.enrichServiceDefaults]] (method: defines_method)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.handleList]] (method: defines_method)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.handleRegister]] (method: defines_method)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.load]] (method: defines_method)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.saveLocked]] (method: defines_method)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.save]] (method: defines_method)
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
- [[web-interface/web-interface/src/mfe/registry.go.md|NewRegistry]] (function: belongs_to) — *NewRegistry instantiates a new Registry, loading existing services from disk.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.List]] (method: belongs_to) — *6. RegisteredAt timestamp*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.RegisterExtended]] (method: belongs_to) — *RegisterExtended registers a microservice with full extended metadata fields.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.RegisterHandlers]] (method: belongs_to) — *RegisterHandlers binds the MFE endpoints to the HTTP ServeMux.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.Register]] (method: belongs_to) — *Register adds or updates a microfrontend service in the registry with automatic deduplication.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.Unregister]] (method: belongs_to) — *Unregister removes a service from the registry by name or tag, persisting changes immediately.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.enrichServiceDefaults]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.handleList]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.handleRegister]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.load]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.saveLocked]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.save]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry]] (struct: belongs_to) — *Registry manages the registration and listing of microfrontend services.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry]] (struct: defines_method) — *Registry manages the registration and listing of microfrontend services.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Service]] (struct: belongs_to) — *Service represents a registered Micro-Frontend service with layer taxonomy.*
- [[web-interface/web-interface/src/mfe/registry.go.md|parsePriority]] (function: belongs_to) — *Supports integer, float64, numeric string, or order alias; defaults to 100 if missing or invalid.*
- [[web-interface/web-interface/src/mfe/registry.go.md|registerReq]] (struct: belongs_to)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|registry_test.go]] (calls)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|registry_test.go]] (same_package)
- [[web-interface/web-interface/src/router/dynamic.go.md|dynamic.go]] (imports)
<!-- SYNC:END -->
