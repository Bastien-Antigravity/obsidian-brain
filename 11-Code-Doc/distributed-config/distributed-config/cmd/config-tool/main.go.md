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

## 📝 Description
Automatically generated mirror for `distributed-config/cmd/config-tool/main.go`.

> **Essential Process**:
> Fleet administrative utility for RSA-2048 keypair generation and plaintext token encryption into canonical ENC(...) format for configuration files.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/src/secret/crypto.go.md|Encrypt]] (function: calls)
- [[distributed-config/distributed-config/src/secret/crypto.go.md|crypto.go]] (imports)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/cmd/config-tool/main.go.md|handleEncrypt]] (function: belongs_to)
- [[distributed-config/distributed-config/cmd/config-tool/main.go.md|handleKeygen]] (function: belongs_to)
- [[distributed-config/distributed-config/cmd/config-tool/main.go.md|main]] (function: belongs_to)
- [[distributed-config/distributed-config/cmd/config-tool/main.go.md|printUsage]] (function: belongs_to)
<!-- SYNC:END -->
