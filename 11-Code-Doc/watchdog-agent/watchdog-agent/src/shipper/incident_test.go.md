---
source: watchdog-agent/src/shipper/incident_test.go
workspace: watchdog-agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-09T16:48:55.455732
---

# Mirror: incident_test.go

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/shipper/incident_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler_test.go.md|mockWatchdogLogger.Error]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|BuildIncidentEvent]] (function: calls) — *BuildIncidentEvent creates a structured IncidentEvent from a ParsedErrorLog.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|IncidentThrottler.ShouldDispatch]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|LocalIncidentNotifier.GetIncidents]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|LocalIncidentNotifier.PublishIncident]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|NewIncidentThrottler]] (function: calls) — *NewIncidentThrottler creates a throttler with a specified suppression window.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|NewLocalIncidentNotifier]] (function: calls) — *NewLocalIncidentNotifier creates a testable local incident recorder.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|incident.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/src/shipper/incident_test.go.md|TestBuildIncidentEvent]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/incident_test.go.md|TestIncidentThrottler_Debounce]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/incident_test.go.md|TestLocalIncidentNotifier]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
