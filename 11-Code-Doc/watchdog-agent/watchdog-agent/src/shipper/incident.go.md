---
source: watchdog-agent/src/shipper/incident.go
workspace: watchdog-agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-09T16:48:55.308665
---

# Mirror: incident.go

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/shipper/incident.go`.

> **Essential Process**:
> Real-time incident event dispatcher and alert rate-limiter for watchdog-agent. Emits structured incident notifications to the Squad Agent over the ecosystem event bus (NATS / webhook) to trigger real-time AI triage and auto-repair.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|IncidentThrottler.ShouldDispatch]] (method: defines_method) — *Returns (shouldDispatch, suppressedCount).*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|LocalIncidentNotifier.GetIncidents]] (method: defines_method) — *GetIncidents returns a copy of captured incidents.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|LocalIncidentNotifier.PublishIncident]] (method: defines_method) — *PublishIncident records the incident locally.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|NatsIncidentPublisher.PublishIncident]] (method: defines_method) — *PublishIncident serializes and publishes the incident to NATS.*

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|BuildIncidentEvent]] (function: belongs_to) — *BuildIncidentEvent creates a structured IncidentEvent from a ParsedErrorLog.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|IncidentEvent]] (struct: belongs_to) — *IncidentEvent represents a real-time actionable error payload sent to the Squad Agent.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|IncidentPublisher]] (interface: belongs_to) — *IncidentPublisher interface defines the contract for dispatching incidents.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|IncidentThrottler.ShouldDispatch]] (method: belongs_to) — *Returns (shouldDispatch, suppressedCount).*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|IncidentThrottler]] (struct: belongs_to) — *IncidentThrottler debounces high-frequency log lines to prevent AI prompt flooding.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|IncidentThrottler]] (struct: defines_method) — *IncidentThrottler debounces high-frequency log lines to prevent AI prompt flooding.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|LocalIncidentNotifier.GetIncidents]] (method: belongs_to) — *GetIncidents returns a copy of captured incidents.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|LocalIncidentNotifier.PublishIncident]] (method: belongs_to) — *PublishIncident records the incident locally.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|LocalIncidentNotifier]] (struct: belongs_to) — *LocalIncidentNotifier is an in-memory/callback notifier for unit testing or direct routing.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|LocalIncidentNotifier]] (struct: defines_method) — *LocalIncidentNotifier is an in-memory/callback notifier for unit testing or direct routing.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|NatsIncidentPublisher.PublishIncident]] (method: belongs_to) — *PublishIncident serializes and publishes the incident to NATS.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|NatsIncidentPublisher]] (struct: belongs_to) — *NatsIncidentPublisher publishes events to NATS subject 'bastien-antigravity.fleet.incident'.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|NatsIncidentPublisher]] (struct: defines_method) — *NatsIncidentPublisher publishes events to NATS subject 'bastien-antigravity.fleet.incident'.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|NewIncidentThrottler]] (function: belongs_to) — *NewIncidentThrottler creates a throttler with a specified suppression window.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|NewLocalIncidentNotifier]] (function: belongs_to) — *NewLocalIncidentNotifier creates a testable local incident recorder.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|NewNatsIncidentPublisher]] (function: belongs_to) — *NewNatsIncidentPublisher constructs a NATS-backed incident publisher.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|throttleRecord]] (struct: belongs_to) — *throttleRecord tracks recurrence state for a single error signature.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident_test.go.md|incident_test.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/incident_test.go.md|incident_test.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|shipper.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|shipper.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
