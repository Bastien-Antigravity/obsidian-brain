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
Automatically generated mirror for `microservice-toolbox/go/pkg/teleremote/client.go`.

> **Essential Process**:
> Client facade connecting Go services to the central tele-remote Telegram bot via gRPC.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.Send]] (method: calls) — *Send data, reconnecting if necessary*
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|EnsureSafeLogger]] (function: calls) — *production microservices from silently running dark without operational logs.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|logger.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Error]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Info]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Warning]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.AddAction]] (method: defines_method) — *AddAction registers a new action or sub-menu tree*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.Close]] (method: defines_method) — *Close gracefully stops the client*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.GenerateMenuJSON]] (method: defines_method) — *GenerateMenuJSON returns the structured JSON representation of the action tree*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.PushMenuUpdate]] (method: defines_method) — *This is typically called by microservices after updating their Actions or internal state.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SendTelemetry]] (method: defines_method) — *SendTelemetry streams an arbitrary text message to the Telegram admin chat*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.Start]] (method: defines_method) — *Start initiates the connection and registration process*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.UpdateActions]] (method: defines_method) — *UpdateActions replaces all current actions and handlers*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.commandDispatcher]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.connectionManager]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.convertActionToBtn]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.disconnect]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.registerHandlersRecursive]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.sendRegistration]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/grpc_client/teleremote.pb.go.md|teleremote.pb.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/grpc_client/teleremote_grpc.pb.go.md|NewTeleRemoteServiceClient]] (function: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|Action]] (struct: belongs_to) — *Action defines a single interactive element in the Telegram UI*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|NewTeleClient]] (function: belongs_to) — *NewTeleClient initializes a new Tele-Remote client*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.AddAction]] (method: belongs_to) — *AddAction registers a new action or sub-menu tree*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.Close]] (method: belongs_to) — *Close gracefully stops the client*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.GenerateMenuJSON]] (method: belongs_to) — *GenerateMenuJSON returns the structured JSON representation of the action tree*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.PushMenuUpdate]] (method: belongs_to) — *This is typically called by microservices after updating their Actions or internal state.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SendTelemetry]] (method: belongs_to) — *SendTelemetry streams an arbitrary text message to the Telegram admin chat*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.Start]] (method: belongs_to) — *Start initiates the connection and registration process*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.UpdateActions]] (method: belongs_to) — *UpdateActions replaces all current actions and handlers*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.commandDispatcher]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.connectionManager]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.convertActionToBtn]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.disconnect]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.registerHandlersRecursive]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.sendRegistration]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient]] (struct: belongs_to) — *Close gracefully stops the client*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient]] (struct: defines_method) — *Close gracefully stops the client*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|btnDef]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|rowDef]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client_test.go.md|client_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client_test.go.md|client_test.go]] (same_package)
<!-- SYNC:END -->
