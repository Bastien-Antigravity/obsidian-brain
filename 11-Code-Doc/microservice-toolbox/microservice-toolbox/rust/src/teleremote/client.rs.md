---
source: microservice-toolbox/rust/src/teleremote/client.rs
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-09-18 19:06:08.572273
microservice: 08-Base-Scripts
tags:
- '#service/08-Base-Scripts'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: client.rs

## 📝 Description
Automatically generated mirror for `microservice-toolbox/rust/src/teleremote/client.rs`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/DistConf.hpp.md|DistConfig.Sync]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/conn_manager/ManagedConnection.hpp.md|ManagedConnection.Send]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/grpc_client/teleremote.pb.go.md|ComponentMessage]] (struct: calls)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/grpc_client/teleremote.pb.go.md|Registration]] (struct: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action.new]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action.with_callback]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action.with_input_prompt]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action.with_sub_menu]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.actions]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.add_action]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.close]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.convert_action_to_btn]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.generate_menu_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.handlers]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.new]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.push_menu_update]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.register_handlers_recursive]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.send_telemetry]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.start]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.update_actions]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.error]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.info]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.warning]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|Logger]] (trait: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|ensure_safe_logger]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|logger.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/mod.rs.md|mod.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action.new]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action.with_callback]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action.with_input_prompt]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action.with_sub_menu]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|BtnDef]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|RowDef]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.actions]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.add_action]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.close]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.convert_action_to_btn]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.generate_menu_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.handlers]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.new]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.push_menu_update]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.register_handlers_recursive]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.send_telemetry]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.start]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.update_actions]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/mod.rs.md|mod.rs]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
