---
source: distributed-config/cmd/config-tool/tlsgen_test.go
workspace: distributed-config
type: code-mirror
status: auto-generated
last_sync: 2026-11-23 20:26:00.776578
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: tlsgen_test.go

## 📝 Description
Automatically generated mirror for `distributed-config/cmd/config-tool/tlsgen_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/cmd/config-tool/tlsgen.go.md|generateFleetCA]] (function: calls)
- [[distributed-config/distributed-config/cmd/config-tool/tlsgen.go.md|generateServiceCert]] (function: calls)
- [[distributed-config/distributed-config/cmd/config-tool/tlsgen.go.md|tlsgen.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/cmd/config-tool/tlsgen_test.go.md|TestTLSGen_CAAndServiceLeafChain]] (function: belongs_to)
- [[distributed-config/distributed-config/cmd/config-tool/tlsgen_test.go.md|TestTLSGen_ValidateServiceName]] (function: belongs_to)
- [[distributed-config/distributed-config/cmd/config-tool/tlsgen_test.go.md|mustReadCert]] (function: belongs_to)
- [[distributed-config/distributed-config/cmd/config-tool/tlsgen_test.go.md|mustReadRSAPrivateKey]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
