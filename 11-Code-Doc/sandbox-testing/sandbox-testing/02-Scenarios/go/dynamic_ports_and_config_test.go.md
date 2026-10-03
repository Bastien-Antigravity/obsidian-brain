---
source: sandbox-testing/02-Scenarios/go/dynamic_ports_and_config_test.go
workspace: sandbox-testing
type: code-mirror
status: auto-generated
last_sync: 2026-10-01T01:10:03.391922
---

# Mirror: dynamic_ports_and_config_test.go

## 📝 Description
Automatically generated mirror for `sandbox-testing/02-Scenarios/go/dynamic_ports_and_config_test.go`.

> **Essential Process**:
> Dynamic Port Resolution and 4-Layer Drift Prevention Scenario Suite. Verifies that: 1. All microservices resolve network listen addresses dynamically from configuration without hardcoded port fallbacks. 2. Port shifting (e.g. +10000) works end-to-end across distributed-config and microservice-toolbox. 3. Network sockets can dynamically bind to shifted ports. 4. Ports across the 4 architectural layers (native.yaml SSoT, docker-compose.yaml manifests, service-registry.json, and documentation tables) remain in 100% strict alignment without drift.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Close]] (method: calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Error]] (method: calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|secret_isolation_integration_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/dynamic_ports_and_config_test.go.md|TestScenario_CrossLayerPortDriftAudit]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/dynamic_ports_and_config_test.go.md|TestScenario_DynamicPortShiftingAndZeroHardcodedFallbacks]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/dynamic_ports_and_config_test.go.md|resolveWorkspaceRoot]] (function: belongs_to) — *resolveWorkspaceRoot locates the root Bastien-Antigravity directory.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
