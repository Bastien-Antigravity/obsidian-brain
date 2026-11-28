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
Automatically generated mirror for `distributed-config/src/network/proto_handler.go`.

> **Essential Process**:
> Protobuf protocol handler deserializing incoming wire messages from config-server, updating local atomic configuration snapshots, and triggering client callbacks.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/src/core/config.go.md|Config.ReplaceLive]] (method: calls)
- [[distributed-config/src/core/config.go.md|Config.SetVersion]] (method: calls)
- [[distributed-config/src/core/config.go.md|Config.Set]] (method: calls)
- [[distributed-config/src/core/config.go.md|config.go]] (imports)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.GetLastSeenVersion]] (method: defines_method)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.HandleIncoming]] (method: defines_method)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.HandleOutgoingWithVersion]] (method: defines_method)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.HandleOutgoing]] (method: defines_method) — *restarted config-server with a lower store revision can be resynchronized via GET_SYNC.*
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnGapDetected]] (method: defines_method)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnLiveConfUpdate]] (method: defines_method)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnRegistryUpdate]] (method: defines_method)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnSyncReceived]] (method: defines_method)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnUpdateResult]] (method: defines_method)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.updateLiveConfig]] (method: defines_method)
- [[distributed-config/src/schemas/config.pb.go.md|config.pb.go]] (imports)

### 🔌 Consumers (Inbound)
- [[distributed-config/src/facade/config_facade.go.md|config_facade.go]] (calls)
- [[distributed-config/src/network/client.go.md|client.go]] (calls)
- [[distributed-config/src/network/client.go.md|client.go]] (same_package)
- [[distributed-config/src/network/network_test.go.md|network_test.go]] (calls)
- [[distributed-config/src/network/network_test.go.md|network_test.go]] (same_package)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.GetLastSeenVersion]] (method: belongs_to)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.HandleIncoming]] (method: belongs_to)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.HandleOutgoingWithVersion]] (method: belongs_to)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.HandleOutgoing]] (method: belongs_to) — *restarted config-server with a lower store revision can be resynchronized via GET_SYNC.*
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnGapDetected]] (method: belongs_to)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnLiveConfUpdate]] (method: belongs_to)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnRegistryUpdate]] (method: belongs_to)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnSyncReceived]] (method: belongs_to)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.SetOnUpdateResult]] (method: belongs_to)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler.updateLiveConfig]] (method: belongs_to)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler]] (struct: belongs_to)
- [[distributed-config/src/network/proto_handler.go.md|ConfigProtoHandler]] (struct: defines_method)
- [[distributed-config/src/network/proto_handler.go.md|NewConfigHandler]] (function: belongs_to)
- [[distributed-config/src/network/sync_logic_test.go.md|sync_logic_test.go]] (calls)
- [[distributed-config/src/network/sync_logic_test.go.md|sync_logic_test.go]] (same_package)
<!-- SYNC:END -->
