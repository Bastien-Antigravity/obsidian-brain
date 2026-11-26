---
source: tele-remote/cmd/tele-remote/contracts.go
workspace: tele-remote
type: code-mirror
status: auto-generated
last_sync: 2026-11-10 13:21:53.401126
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: contracts.go

## 📝 Description
Automatically generated mirror for `tele-remote/cmd/tele-remote/contracts.go`.

> **Essential Process**:
> Builds the service's ExchangeContract metadata for publication to web-interface via microservice-toolbox/go/pkg/spec, reflecting both the gRPC bidirectional control stream and the Telegram Bot API gateway.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[tele-remote/src/grpc_control/teleremote.pb.go.md|teleremote.pb.go]] (imports)

### 🔌 Consumers (Inbound)
- [[tele-remote/cmd/tele-remote/contracts.go.md|buildTeleRemoteContracts]] (function: belongs_to)
- [[tele-remote/cmd/tele-remote/contracts_test.go.md|contracts_test.go]] (calls)
- [[tele-remote/cmd/tele-remote/contracts_test.go.md|contracts_test.go]] (same_package)
- [[tele-remote/cmd/tele-remote/main.go.md|main.go]] (calls)
- [[tele-remote/cmd/tele-remote/main.go.md|main.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
