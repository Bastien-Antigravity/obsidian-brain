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
- None detected

### 🔌 Consumers (Inbound)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/docker_portability_and_slices_test.go.md|TestScenario_DockerComposeStandardCompliance]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/docker_portability_and_slices_test.go.md|TestScenario_DockerCrossPlatformKeyFallback]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/docker_portability_and_slices_test.go.md|TestScenario_DockerServiceSlicesIntegrity]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/docker_portability_and_slices_test.go.md|resolveDockerDeploymentDir]] (function: belongs_to)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/nats_and_fleet_control_test.go.md|nats_and_fleet_control_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/nats_and_fleet_control_test.go.md|nats_and_fleet_control_test.go]] (same_package)
<!-- SYNC:END -->
