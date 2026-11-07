---
source: web-interface/cmd/web-interface/fleet_health_scenario_test.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-02 15:37:18.722257
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: fleet_health_scenario_test.go

## 📝 Description
Automatically generated mirror for `web-interface/cmd/web-interface/fleet_health_scenario_test.go`.

> **Essential Process**:
> End-to-end scenario tests for ecosystem fleet health monitoring. Verifies live status probing, multi-candidate fallback for RAG Dashboard and MCP Server, and isolated fault tolerance when watchdog-agent is down.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|main_test.go]] (same_package)
- [[web-interface/web-interface/cmd/web-interface/main_test.go.md|mockLogger.Close]] (method: calls)
- [[web-interface/web-interface/src/mfe/registry.go.md|NewRegistry]] (function: calls) — *NewRegistry instantiates a new Registry, loading existing services from disk.*
- [[web-interface/web-interface/src/mfe/registry.go.md|registry.go]] (imports)
- [[web-interface/web-interface/src/router/dynamic.go.md|SetMFERegistry]] (function: calls) — *SetMFERegistry associates the active MFE registry instance with the router.*
- [[web-interface/web-interface/src/router/spec_exchange_test.go.md|spec_exchange_test.go]] (imports)

### 🔌 Consumers (Inbound)
- [[web-interface/web-interface/cmd/web-interface/fleet_health_scenario_test.go.md|FleetHealthRAGMultiCandidateFallback(t *testing.]] (function: belongs_to) — *3. When both are closed: reports primary address as offline (never 'unresolved').*
- [[web-interface/web-interface/cmd/web-interface/fleet_health_scenario_test.go.md|TestScenarioFleetHealthAllServicesOnline]] (function: belongs_to) — *detects all services and reports all_online: true.*
- [[web-interface/web-interface/cmd/web-interface/fleet_health_scenario_test.go.md|enarioFleetHealthWatchdogAgentDown(t *te]] (function: belongs_to) — *4. All other 10 base services (including RAG MCP Server and RAG Dashboard) remain ONLINE.*
- [[web-interface/web-interface/cmd/web-interface/fleet_health_scenario_test.go.md|spawnMockListener]] (function: belongs_to) — *helper to spawn a local TCP listener on an ephemeral port.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
