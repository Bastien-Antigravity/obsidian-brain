---
source: distributed-config/cmd/config-tool/tlsgen.go
workspace: distributed-config
type: code-mirror
status: auto-generated
last_sync: 2026-11-23 20:26:00.772653
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: tlsgen.go

## 📝 Description
Automatically generated mirror for `distributed-config/cmd/config-tool/tlsgen.go`.

> **Essential Process**:
> Pure-Go RSA-2048 X.509 Fleet Root CA and per-service leaf TLS certificate generator with zero external OpenSSL dependency.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[distributed-config/cmd/config-tool/main.go.md|main.go]] (calls)
- [[distributed-config/cmd/config-tool/main.go.md|main.go]] (same_package)
- [[distributed-config/cmd/config-tool/tlsgen.go.md|buildSANs]] (function: belongs_to)
- [[distributed-config/cmd/config-tool/tlsgen.go.md|defaultCADays]] (constant: belongs_to)
- [[distributed-config/cmd/config-tool/tlsgen.go.md|defaultLeafDays]] (constant: belongs_to)
- [[distributed-config/cmd/config-tool/tlsgen.go.md|expandHomePrefix]] (function: belongs_to)
- [[distributed-config/cmd/config-tool/tlsgen.go.md|fileExists]] (function: belongs_to)
- [[distributed-config/cmd/config-tool/tlsgen.go.md|generateFleetCA]] (function: belongs_to)
- [[distributed-config/cmd/config-tool/tlsgen.go.md|generateServiceCert]] (function: belongs_to)
- [[distributed-config/cmd/config-tool/tlsgen.go.md|handleTLSGen]] (function: belongs_to)
- [[distributed-config/cmd/config-tool/tlsgen.go.md|loadFleetCA]] (function: belongs_to)
- [[distributed-config/cmd/config-tool/tlsgen.go.md|printCertResult]] (function: belongs_to)
- [[distributed-config/cmd/config-tool/tlsgen.go.md|randomSerialNumber]] (function: belongs_to)
- [[distributed-config/cmd/config-tool/tlsgen.go.md|rsaKeyBits]] (constant: belongs_to)
- [[distributed-config/cmd/config-tool/tlsgen.go.md|splitHosts]] (function: belongs_to)
- [[distributed-config/cmd/config-tool/tlsgen.go.md|subjectKeyID]] (function: belongs_to)
- [[distributed-config/cmd/config-tool/tlsgen.go.md|validateServiceName]] (function: belongs_to)
- [[distributed-config/cmd/config-tool/tlsgen.go.md|writePEMFile]] (function: belongs_to)
- [[distributed-config/cmd/config-tool/tlsgen_test.go.md|tlsgen_test.go]] (calls)
- [[distributed-config/cmd/config-tool/tlsgen_test.go.md|tlsgen_test.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
