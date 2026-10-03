---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `web-interface/src/mfe/registry_test.go`.

> **Essential Process**:
> Unit tests for the OpenMFE dynamic service registry and HTTP handlers. Verifies registration, JSON persistence, CORS compliance, and listing.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/src/mfe/registry.go.md|NewRegistry]] (function: calls) — *NewRegistry instantiates a new Registry, loading existing services from disk.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.List]] (method: calls) — *List returns a slice of all currently registered microfrontends.*
- [[web-interface/web-interface/src/mfe/registry.go.md|Registry.RegisterHandlers]] (method: calls) — *RegisterHandlers binds the MFE endpoints to the HTTP ServeMux.*
- [[web-interface/web-interface/src/mfe/registry.go.md|registry.go]] (same_package)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|mockLogger.Close]] (method: defines_method)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|mockLogger.Critical]] (method: defines_method)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|mockLogger.Debug]] (method: defines_method)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|mockLogger.Error]] (method: defines_method)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|mockLogger.Info]] (method: defines_method)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|mockLogger.Warning]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/src/mfe/registry.go.md|registry.go]] (calls)
- [[web-interface/web-interface/src/mfe/registry.go.md|registry.go]] (same_package)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|TestRegistryRegisterAndListHandlers]] (function: belongs_to)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|TestRegistryRejectsInvalidRegistration]] (function: belongs_to)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|mockLogger.Close]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|mockLogger.Critical]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|mockLogger.Debug]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|mockLogger.Error]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|mockLogger.Info]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|mockLogger.Warning]] (method: belongs_to)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|mockLogger]] (struct: belongs_to)
- [[web-interface/web-interface/src/mfe/registry_test.go.md|mockLogger]] (struct: defines_method)
<!-- SYNC:END -->
