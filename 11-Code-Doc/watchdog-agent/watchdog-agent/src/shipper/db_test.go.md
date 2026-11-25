---
source: watchdog-agent/src/shipper/db_test.go
workspace: watchdog-agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-09 14:40:43.766918
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: db_test.go

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/shipper/db_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|DBConfig.DSN]] (method: calls) — *DSN returns the formatted PostgreSQL connection URI.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|ResolveBrainID]] (function: calls) — *documented in Multi-Brain Partitioning Standard: AppConfig -> env -> obsidian-brain.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|ResolveDBConfigWithAppConfig]] (function: calls) — *targeting Option B (base ecosystem 'obsidiandb') and fails fast on missing values.*
- [[watchdog-agent/watchdog-agent/src/shipper/db.go.md|db.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/src/shipper/db_test.go.md|TestDBConfig_DSN]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/db_test.go.md|TestResolveBrainID_Precedence]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/db_test.go.md|TestResolveDBConfigWithAppConfig_BooleanSSLCertTrue]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/db_test.go.md|TestResolveDBConfigWithAppConfig_FailFastValidation]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/db_test.go.md|TestResolveDBConfigWithAppConfig_FallbackToRagEngineDBName]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/db_test.go.md|TestResolveDBConfigWithAppConfig_SuccessAndPriority]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/db_test.go.md|makeTestAppConfig]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
