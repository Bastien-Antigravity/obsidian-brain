---
microservice: microservice-toolbox
type: note
status: active
tags:
- '#service/microservice-toolbox'
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
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.GetCapability]] (method: calls) — *Get a capability configuration as JSON*
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/args_test.go.md|args_test.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/config/loader.go.md|AppConfig.GetLocalTLSConfig]] (method: calls) — *Precedence: local.<serviceKey>.tls (exact, then '-'/'_' normalized) -> local.tls.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|EnsureSafeLogger]] (function: calls) — *production microservices from silently running dark without operational logs.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|logger.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Error]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Info]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/logger/logger.go.md|noOpLogger.Warning]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/grpc_server.go.md|grpc_server.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/tls.go.md|DialTransportCredentials]] (function: calls) — *DialTransportCredentials builds gRPC client TransportCredentials according to target locality and policy.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/network/tls.go.md|NormalizeTLSMode]] (function: calls) — *NormalizeTLSMode canonicalizes a TLS policy mode string, defaulting empty values to "auto".*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.AddAction]] (method: defines_method) — *AddAction registers a new action or sub-menu tree*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.Close]] (method: defines_method) — *Close gracefully stops the client*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.ConfigureFromAppConfig]] (method: defines_method) — *and registers a live-configuration callback to refresh them dynamically at runtime.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.GenerateMenuJSON]] (method: defines_method) — *GenerateMenuJSON returns the structured JSON representation of the action tree*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.PushMenuUpdate]] (method: defines_method) — *This is typically called by microservices after updating their Actions or internal state.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SendTelemetry]] (method: defines_method) — *SendTelemetry streams an arbitrary text message to the Telegram admin chat*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SetAuthToken]] (method: defines_method) — *SetAuthToken configures the shared secret sent in outgoing x-tele-auth gRPC metadata*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SetLocalTLS]] (method: defines_method) — *SetLocalTLS configures service-private X.509 TLS/mTLS file paths from the local: section*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SetPriority]] (method: defines_method) — *SetPriority configures the OpenMFE menu priority for this component*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SetTLSConfig]] (method: defines_method) — *SetTLSConfig configures an explicit TLS configuration for the gRPC connection*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SetTLSPolicy]] (method: defines_method) — *SetTLSPolicy configures local/remote-aware TLS enforcement*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.Start]] (method: defines_method) — *Start initiates the connection and registration process*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.UpdateActions]] (method: defines_method) — *UpdateActions replaces all current actions and handlers*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.applyAppConfigPolicy]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.commandDispatcher]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.connectionManager]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.convertActionToBtn]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.disconnect]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.registerHandlersRecursive]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.sendRegistration]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/grpc_client/teleremote.pb.go.md|teleremote.pb.go]] (imports)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/grpc_client/teleremote_grpc.pb.go.md|NewTeleRemoteServiceClient]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/wiretap/grpc_wrapper.go.md|ClientDialOptions]] (function: calls) — *WireTap Unary and Stream client interceptors pre-configured.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/wiretap/wiretap_test.go.md|wiretap_test.go]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|Action]] (struct: belongs_to) — *Action defines a single interactive element in the Telegram UI*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|NewTeleClient]] (function: belongs_to) — *NewTeleClient initializes a new Tele-Remote client*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.AddAction]] (method: belongs_to) — *AddAction registers a new action or sub-menu tree*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.Close]] (method: belongs_to) — *Close gracefully stops the client*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.ConfigureFromAppConfig]] (method: belongs_to) — *and registers a live-configuration callback to refresh them dynamically at runtime.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.GenerateMenuJSON]] (method: belongs_to) — *GenerateMenuJSON returns the structured JSON representation of the action tree*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.PushMenuUpdate]] (method: belongs_to) — *This is typically called by microservices after updating their Actions or internal state.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SendTelemetry]] (method: belongs_to) — *SendTelemetry streams an arbitrary text message to the Telegram admin chat*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SetAuthToken]] (method: belongs_to) — *SetAuthToken configures the shared secret sent in outgoing x-tele-auth gRPC metadata*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SetLocalTLS]] (method: belongs_to) — *SetLocalTLS configures service-private X.509 TLS/mTLS file paths from the local: section*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SetPriority]] (method: belongs_to) — *SetPriority configures the OpenMFE menu priority for this component*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SetTLSConfig]] (method: belongs_to) — *SetTLSConfig configures an explicit TLS configuration for the gRPC connection*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.SetTLSPolicy]] (method: belongs_to) — *SetTLSPolicy configures local/remote-aware TLS enforcement*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.Start]] (method: belongs_to) — *Start initiates the connection and registration process*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.UpdateActions]] (method: belongs_to) — *UpdateActions replaces all current actions and handlers*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.applyAppConfigPolicy]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.commandDispatcher]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.connectionManager]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.convertActionToBtn]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.disconnect]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.registerHandlersRecursive]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient.sendRegistration]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient]] (struct: belongs_to) — *TeleClient maintains a resilient gRPC connection to tele-remote*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|TeleClient]] (struct: defines_method) — *TeleClient maintains a resilient gRPC connection to tele-remote*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|btnDef]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|menuEnvelope]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|parseCapabilityBool]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|rowDef]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client.go.md|teleRemoteCapability]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client_test.go.md|client_test.go]] (calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/client_test.go.md|client_test.go]] (same_package)
<!-- SYNC:END -->
