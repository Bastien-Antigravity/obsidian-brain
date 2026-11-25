---
source: watchdog-agent/src/rest/contracts.go
workspace: watchdog-agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-10 13:21:53.843290
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: contracts.go

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/rest/contracts.go`.

> **Essential Process**:
> Constructs exhaustive, microservice-authored Exchange Contracts for watchdog-agent covering its REST supervision API, NATS heartbeat & incident bus, TimescaleDB error log shipper SQL DDL, and ecosystem client/probe integrations.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/rest/contracts.go.md|RESTHandler.handleContracts]] (method: defines_method)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|RESTHandler.sendJSON]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler.go.md|rest_handler.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler_test.go.md|mockWatchdogControl.GetStatus]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler_test.go.md|mockWatchdogLogger.Error]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler_test.go.md|rest_handler_test.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/server/controller.go.md|controller.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/shipper/checkpoint.go.md|checkpoint.go]] (imports)
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|ResolveBrainID]] (function: calls) — *documented in Multi-Brain Partitioning Standard: AppConfig -> env -> obsidian-brain.*
- [[watchdog-agent/watchdog-agent/src/shipper/incident.go.md|ResolveIncidentSubject]] (function: calls) — *ResolveIncidentSubject builds the canonical NATS topic partitioned per brain_id.*

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/main.go.md|main.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/rest/contracts.go.md|BuildExchangeContracts]] (function: belongs_to) — *BuildExchangeContracts constructs the exhaustive contract catalog from watchdog-agent sources.*
- [[watchdog-agent/watchdog-agent/src/rest/contracts.go.md|RESTHandler.handleContracts]] (method: belongs_to)
- [[watchdog-agent/watchdog-agent/src/rest/contracts.go.md|RESTHandler]] (struct: defines_method)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
