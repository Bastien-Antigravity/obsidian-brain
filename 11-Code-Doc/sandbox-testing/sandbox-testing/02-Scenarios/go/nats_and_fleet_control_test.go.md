

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/docker_portability_and_slices_test.go.md|docker_portability_and_slices_test.go]] (same_package)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/docker_portability_and_slices_test.go.md|resolveDockerDeploymentDir]] (function: calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|scenarioMockLogger.Close]] (method: calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/secret_isolation_integration_test.go.md|secret_isolation_integration_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/nats_and_fleet_control_test.go.md|TestScenario_ConfigExplicitHierarchy]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/nats_and_fleet_control_test.go.md|TestScenario_FleetStopCommandPreserved]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/nats_and_fleet_control_test.go.md|TestScenario_ObsoletePlatformScriptsRemoved]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/nats_and_fleet_control_test.go.md|TestScenario_PythonFleetOrchestratorIntegrity]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/nats_and_fleet_control_test.go.md|TestScenario_WatchdogNatsCrossPlatformResilience]] (function: belongs_to)
<!-- SYNC:END -->
