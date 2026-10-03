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

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/docker_portability_and_slices_test.go.md|docker_portability_and_slices_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/docker_portability_and_slices_test.go.md|resolveDockerDeploymentDir]] (function: calls) — *resolveDockerDeploymentDir finds the docker-deployment directory relative to this test file.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Close]] (method: calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|secret_isolation_integration_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/nats_and_fleet_control_test.go.md|TestScenario_ConfigExplicitHierarchy]] (function: belongs_to) — *directory contains explicit, self-documenting subdirectories and backward-compatible symlinks.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/nats_and_fleet_control_test.go.md|TestScenario_FleetStopCommandPreserved]] (function: belongs_to) — *are fully preserved in scripts/fleet.py and delegated to by fleet.sh and fleet.cmd.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/nats_and_fleet_control_test.go.md|TestScenario_ObsoletePlatformScriptsRemoved]] (function: belongs_to) — *scripts (fleet-mac.sh, fleet-linux.sh, fleet-windows.cmd, deploy-*.sh) have been deleted.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/nats_and_fleet_control_test.go.md|TestScenario_PythonFleetOrchestratorIntegrity]] (function: belongs_to) — *and correctly delegated to by fleet.sh and fleet.cmd.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/nats_and_fleet_control_test.go.md|TestScenario_WatchdogNatsCrossPlatformResilience]] (function: belongs_to) — *safely handles NATS across different OS architectures without crashing or port fighting.*
<!-- SYNC:END -->
