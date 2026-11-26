---
microservice: distributed-config
type: note
status: active
tags:
- '#service/distributed-config'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `distributed-config/src/network/client.go`.

> **Essential Process**:
> safe-socket network client managing TCP connection lifecycle, exponential backoff reconnection, and real-time bidirectional synchronization with config-server.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/src/core/config.go.md|ParseSharePayload]] (function: calls) — *Supports map[string]map[string]string, map[string]string, and map[string]interface{}.*
- [[distributed-config/src/core/config.go.md|config.go]] (imports)
- [[distributed-config/src/network/backoff.go.md|Backoff.GetDelay]] (method: calls) — *GetDelay calculates the delay for the current attempt.*
- [[distributed-config/src/network/backoff.go.md|NewBackoff]] (function: calls) — *NewBackoff creates a new backoff strategy using parameters from the config*
- [[distributed-config/src/network/backoff.go.md|backoff.go]] (same_package)
- [[distributed-config/src/network/client.go.md|Client.Close]] (method: defines_method) — *Close closes the connection and stops the background listener.*
- [[distributed-config/src/network/client.go.md|Client.DeleteKeysWithOCC]] (method: defines_method) — *Returns ErrVersionConflict if the server version does not match expectedVersion.*
- [[distributed-config/src/network/client.go.md|Client.DeleteKeys]] (method: defines_method) — *DeleteKeys sends a deletion request for specific section keys to the server and waits for ACK.*
- [[distributed-config/src/network/client.go.md|Client.FullRefresh]] (method: defines_method) — *FullRefresh explicitly requests the full configuration from the server.*
- [[distributed-config/src/network/client.go.md|Client.GetConfig]] (method: defines_method) — *GetConfig fetches configuration from the server.*
- [[distributed-config/src/network/client.go.md|Client.GetVersion]] (method: defines_method) — *GetVersion returns the last seen server configuration version.*
- [[distributed-config/src/network/client.go.md|Client.IsConnected]] (method: defines_method) — *IsConnected returns true if the client is currently connected.*
- [[distributed-config/src/network/client.go.md|Client.UpdateConfigMapWithOCC]] (method: defines_method) — *Returns ErrVersionConflict if the server version does not match expectedVersion.*
- [[distributed-config/src/network/client.go.md|Client.UpdateConfigMap]] (method: defines_method) — *UpdateConfigMap sends a specific configuration map to the server and waits for ACK.*
- [[distributed-config/src/network/client.go.md|Client.UpdateConfig]] (method: defines_method) — *UpdateConfig sends the entire current live configuration to the server.*
- [[distributed-config/src/network/client.go.md|Client.Watch]] (method: defines_method) — *Watch starts a background goroutine to handle asynchronous updates (BROADCASTs).*
- [[distributed-config/src/network/client.go.md|Client.connect]] (method: defines_method) — *connect establishes the connection and acts the handshake.*
- [[distributed-config/src/network/client.go.md|Client.requestSync]] (method: defines_method)
- [[distributed-config/src/network/client.go.md|Client.sendWithUpdateAck]] (method: defines_method) — *sendWithUpdateAck transmits a payload and waits for the server ACK or ERROR response.*
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.GetLastSeenVersion]] (method: calls)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.HandleIncoming]] (method: calls)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.HandleOutgoingWithVersion]] (method: calls)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.HandleOutgoing]] (method: calls)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnGapDetected]] (method: calls)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnSyncReceived]] (method: calls)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnUpdateResult]] (method: calls)
- [[distributed-config/src/network/proto_handler.go.md|NewConfigHandler]] (function: calls)
- [[distributed-config/src/network/proto_handler.go.md|proto_handler.go]] (same_package)
- [[distributed-config/src/schemas/config.pb.go.md|config.pb.go]] (imports)

### 🔌 Consumers (Inbound)
- [[distributed-config/src/network/client.go.md|Client.Close]] (method: belongs_to) — *Close closes the connection and stops the background listener.*
- [[distributed-config/src/network/client.go.md|Client.DeleteKeysWithOCC]] (method: belongs_to) — *Returns ErrVersionConflict if the server version does not match expectedVersion.*
- [[distributed-config/src/network/client.go.md|Client.DeleteKeys]] (method: belongs_to) — *DeleteKeys sends a deletion request for specific section keys to the server and waits for ACK.*
- [[distributed-config/src/network/client.go.md|Client.FullRefresh]] (method: belongs_to) — *FullRefresh explicitly requests the full configuration from the server.*
- [[distributed-config/src/network/client.go.md|Client.GetConfig]] (method: belongs_to) — *GetConfig fetches configuration from the server.*
- [[distributed-config/src/network/client.go.md|Client.GetVersion]] (method: belongs_to) — *GetVersion returns the last seen server configuration version.*
- [[distributed-config/src/network/client.go.md|Client.IsConnected]] (method: belongs_to) — *IsConnected returns true if the client is currently connected.*
- [[distributed-config/src/network/client.go.md|Client.UpdateConfigMapWithOCC]] (method: belongs_to) — *Returns ErrVersionConflict if the server version does not match expectedVersion.*
- [[distributed-config/src/network/client.go.md|Client.UpdateConfigMap]] (method: belongs_to) — *UpdateConfigMap sends a specific configuration map to the server and waits for ACK.*
- [[distributed-config/src/network/client.go.md|Client.UpdateConfig]] (method: belongs_to) — *UpdateConfig sends the entire current live configuration to the server.*
- [[distributed-config/src/network/client.go.md|Client.Watch]] (method: belongs_to) — *Watch starts a background goroutine to handle asynchronous updates (BROADCASTs).*
- [[distributed-config/src/network/client.go.md|Client.connect]] (method: belongs_to) — *connect establishes the connection and acts the handshake.*
- [[distributed-config/src/network/client.go.md|Client.requestSync]] (method: belongs_to)
- [[distributed-config/src/network/client.go.md|Client.sendWithUpdateAck]] (method: belongs_to) — *sendWithUpdateAck transmits a payload and waits for the server ACK or ERROR response.*
- [[distributed-config/src/network/client.go.md|Client]] (struct: belongs_to) — *Client provides an interface to interact with the Config Server.*
- [[distributed-config/src/network/client.go.md|Client]] (struct: defines_method) — *Client provides an interface to interact with the Config Server.*
- [[distributed-config/src/network/client.go.md|NewClient]] (function: belongs_to) — *NewClient creates a new Config Client and connects to the server.*
- [[distributed-config/src/network/network_resilience_test.go.md|network_resilience_test.go]] (calls)
- [[distributed-config/src/network/network_resilience_test.go.md|network_resilience_test.go]] (same_package)
- [[distributed-config/src/network/network_test.go.md|network_test.go]] (calls)
- [[distributed-config/src/network/network_test.go.md|network_test.go]] (same_package)
- [[distributed-config/src/strategies/cloud.go.md|cloud.go]] (calls)
- [[distributed-config/src/strategies/strategies_test.go.md|strategies_test.go]] (calls)
- [[distributed-config/src/strategies/test.go.md|test.go]] (calls)
<!-- SYNC:END -->
