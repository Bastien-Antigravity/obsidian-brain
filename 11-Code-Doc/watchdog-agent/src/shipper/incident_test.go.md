---
source: watchdog-agent/src/shipper/incident_test.go
workspace: watchdog-agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-09 16:48:55.455732
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: incident_test.go

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/shipper/incident_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/src/rest/rest_handler_test.go.md|mockWatchdogLogger.Error]] (method: calls)
- [[watchdog-agent/src/shipper/incident.go.md|BuildIncidentEvent]] (function: calls) — *BuildIncidentEvent creates a structured IncidentEvent from a ParsedErrorLog.*
- [[watchdog-agent/src/shipper/incident.go.md|IncidentThrottler.ShouldDispatch]] (method: calls) — *Returns (shouldDispatch, accumulatedCount).*
- [[watchdog-agent/src/shipper/incident.go.md|LocalIncidentNotifier.GetIncidents]] (method: calls) — *GetIncidents returns a copy of captured incidents.*
- [[watchdog-agent/src/shipper/incident.go.md|LocalIncidentNotifier.PublishIncident]] (method: calls) — *PublishIncident records the incident locally.*
- [[watchdog-agent/src/shipper/incident.go.md|NewIncidentThrottler]] (function: calls) — *NewIncidentThrottler creates a throttler with a specified suppression window.*
- [[watchdog-agent/src/shipper/incident.go.md|NewLocalIncidentNotifier]] (function: calls) — *NewLocalIncidentNotifier creates a testable local incident recorder.*
- [[watchdog-agent/src/shipper/incident.go.md|NewNatsIncidentPublisher]] (function: calls) — *NewNatsIncidentPublisher constructs a brain-aware NATS-backed incident publisher.*
- [[watchdog-agent/src/shipper/incident.go.md|ResolveIncidentSubject]] (function: calls) — *ResolveIncidentSubject builds the canonical NATS topic partitioned per brain_id.*
- [[watchdog-agent/src/shipper/incident.go.md|incident.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/src/shipper/incident_test.go.md|TestBuildIncidentEvent]] (function: belongs_to)
- [[watchdog-agent/src/shipper/incident_test.go.md|TestIncidentThrottler_Debounce]] (function: belongs_to)
- [[watchdog-agent/src/shipper/incident_test.go.md|TestLocalIncidentNotifier]] (function: belongs_to)
- [[watchdog-agent/src/shipper/incident_test.go.md|TestNatsIncidentPublisher_PublishesPartitionedPayload]] (function: belongs_to)
- [[watchdog-agent/src/shipper/incident_test.go.md|TestResolveIncidentSubject_MultiBrain]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
