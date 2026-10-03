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
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/docker_portability_and_slices_test.go.md|TestScenario_DockerComposeStandardCompliance]] (function: belongs_to) — *read-only key mounts for consumers, zero key mounts for web-interface/config-server).*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/docker_portability_and_slices_test.go.md|TestScenario_DockerCrossPlatformKeyFallback]] (function: belongs_to) — *(outside Git repositories, e.g. in /etc/bastien or ~/.bastien/keys) are used for encryption.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/docker_portability_and_slices_test.go.md|TestScenario_DockerServiceSlicesIntegrity]] (function: belongs_to) — *YAML slices follow the ecosystem standard: minimal, isolated, valid YAML, and loadable.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/docker_portability_and_slices_test.go.md|resolveDockerDeploymentDir]] (function: belongs_to) — *resolveDockerDeploymentDir finds the docker-deployment directory relative to this test file.*
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/nats_and_fleet_control_test.go.md|nats_and_fleet_control_test.go]] (calls)
- [[sandbox-testing/sandbox-testing/02-Scenarios/go/nats_and_fleet_control_test.go.md|nats_and_fleet_control_test.go]] (same_package)
<!-- SYNC:END -->
