---
source: microservice-toolbox/go/pkg/teleremote/client_test.go
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-09-18 14:33:31.301813
microservice: microservice-toolbox
tags:
- '#service/microservice-toolbox'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: client_test.go

## 📝 Description
Automatically generated mirror for `microservice-toolbox/go/pkg/teleremote/client_test.go`.

> **Essential Process**:
> Unit tests for TeleClient action tree generation, menu JSON serialization, and handler dispatching.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/NetworkManager.hpp.md|NetworkManager.New]] (method: calls) — *Unified Factory Method combining AppConfig and Logger in one function with pointers*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args_test.go.md|args_test.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|NewTeleClient]] (function: calls) — *NewTeleClient initializes a new Tele-Remote client*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.AddAction]] (method: calls) — *AddAction registers a new action or sub-menu tree*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.ConfigureFromAppConfig]] (method: calls) — *and registers a live-configuration callback to refresh them dynamically at runtime.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.GenerateMenuJSON]] (method: calls) — *GenerateMenuJSON returns the structured JSON representation of the action tree*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SendTelemetry]] (method: calls) — *SendTelemetry streams an arbitrary text message to the Telegram admin chat*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SetAuthToken]] (method: calls) — *SetAuthToken configures the shared secret sent in outgoing x-tele-auth gRPC metadata*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SetLocalTLS]] (method: calls) — *SetLocalTLS configures service-private X.509 TLS/mTLS file paths from the local: section*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SetPriority]] (method: calls) — *SetPriority configures the OpenMFE menu priority for this component*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SetTLSConfig]] (method: calls) — *SetTLSConfig configures an explicit TLS configuration for the gRPC connection*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SetTLSPolicy]] (method: calls) — *SetTLSPolicy configures local/remote-aware TLS enforcement*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.UpdateActions]] (method: calls) — *UpdateActions replaces all current actions and handlers*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|client.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client_test.go.md|TestGenerateMenuJSON_WithPriorityAndOrder]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client_test.go.md|TestTeleClient_ActionAndMenuGeneration]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client_test.go.md|TestTeleClient_ConfigureFromAppConfig_LocalTLSAndPolicy]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client_test.go.md|TestTeleClient_SendTelemetryDisconnected]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client_test.go.md|TestTeleClient_SettersAndTLSPolicy]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client_test.go.md|TestTeleClient_UpdateActions]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
