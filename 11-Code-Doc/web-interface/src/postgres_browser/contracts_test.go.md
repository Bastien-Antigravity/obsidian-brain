---
source: web-interface/src/postgres_browser/contracts_test.go
workspace: web-interface
type: code-mirror
status: auto-generated
last_sync: 2026-11-10 13:21:54.579702
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: contracts_test.go

## 📝 Description
Automatically generated mirror for `web-interface/src/postgres_browser/contracts_test.go`.

> **Essential Process**:
> Unit tests verifying synthesizeTimescaleEnvelope constructs accurate SQL DDL, hypertable metadata, wire v3 info, and REST API specs from introspected catalogs.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[web-interface/src/postgres_browser/connection_test.go.md|connection_test.go]] (same_package)
- [[web-interface/src/postgres_browser/connection_test.go.md|loadIsolatedPostgresBrowserConfig]] (function: calls)
- [[web-interface/src/postgres_browser/contracts.go.md|BrowserHandler.GetTimescaleContracts]] (method: calls) — *GetTimescaleContracts queries live PostgreSQL/TimescaleDB catalogs and returns exhaustive exchange contracts.*
- [[web-interface/src/postgres_browser/contracts.go.md|contracts.go]] (same_package)
- [[web-interface/src/postgres_browser/contracts.go.md|synthesizeTimescaleEnvelope]] (function: calls)

### 🔌 Consumers (Inbound)
- [[web-interface/src/postgres_browser/contracts_test.go.md|TestGetTimescaleContractsFailClosedWhenUnconfigured]] (function: belongs_to)
- [[web-interface/src/postgres_browser/contracts_test.go.md|TestSynthesizeTimescaleEnvelope]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
