---
source: microservice-toolbox/rust/src/teleremote/client.rs
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-09-18 19:06:08.572273
microservice: microservice-toolbox
tags:
- '#service/microservice-toolbox'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: client.rs

## 📝 Description
Automatically generated mirror for `microservice-toolbox/rust/src/teleremote/client.rs`.

> **Essential Process**:
> Client facade connecting Rust services to the central tele-remote Telegram bot via gRPC.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/grpc_client/teleremote.pb.go.md|ComponentMessage]] (struct: calls) — *A message sent from the external component/service to the Bot*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/grpc_client/teleremote.pb.go.md|Registration]] (struct: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.bridge_handle]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.decrypt_secret]] (method: calls) — *Uses the hardened distributed-config engine for cross-language consistency.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.decrypt_secret_by_handle]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_capability]] (method: calls) — *Resolves a capability block as JSON via CGO bridge or local YAML tree.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_capability_by_handle]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_local_tls_config]] (method: calls) — *Precedence: `local.<service_key>.tls` (exact, then '-'/'_' normalized) -> `local.tls`.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.on_live_conf_update]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig]] (struct: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|LocalTLSConfig.is_empty]] (method: calls) — *Returns true when all fields are unset/empty.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|LocalTLSConfig]] (struct: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|loader.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/network/tls.rs.md|build_client_endpoint]] (function: calls) — *Builds a tonic transport Endpoint with TLS/mTLS or plaintext according to target locality and policy.*
- [[microservice-toolbox/microservice-toolbox/rust/src/network/tls.rs.md|normalize_tls_mode]] (function: calls) — *Canonicalizes a TLS policy mode string, defaulting empty values to "auto".*
- [[microservice-toolbox/microservice-toolbox/rust/src/network/tls.rs.md|tls.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action.new]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action.with_callback]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action.with_input_prompt]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action.with_order]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action.with_sub_menu]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.actions]] (method: defines_method) — *Returns a reference to the actions collection.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.add_action]] (method: defines_method) — *Registers a new action or submenu tree.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.build_menu_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.close]] (method: defines_method) — *Gracefully closes the tele-remote client connection.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.configure_from_app_config]] (method: defines_method) — *a live-configuration callback to refresh policy dynamically at runtime.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.convert_action_to_btn]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.generate_menu_json]] (method: defines_method) — *Returns the structured JSON representation of the action tree.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.handlers]] (method: defines_method) — *Returns a reference to the registered command handlers map.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.new]] (method: defines_method) — *Creates a new TeleClient instance.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.parse_capability_bool]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.parse_tele_remote_capability]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.push_menu_update]] (method: defines_method) — *Manually triggers transmission of updated menu schema to tele-remote.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.register_handlers_recursive]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.send_telemetry]] (method: defines_method) — *Streams an arbitrary text telemetry message to the Telegram bot admin chat.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.set_auth_token]] (method: defines_method) — *Configures the shared secret sent in outgoing `x-tele-auth` gRPC metadata.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.set_local_tls]] (method: defines_method) — *Configures service-private X.509 TLS/mTLS file paths from the `local:` section.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.set_priority]] (method: defines_method) — *Configures the OpenMFE menu priority for this component.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.set_tls_policy]] (method: defines_method) — *Configures local/remote-aware TLS enforcement.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.start]] (method: defines_method) — *Spawns the background connection manager and command dispatcher.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.update_actions]] (method: defines_method) — *Replaces all current actions and handlers.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClientPolicy.default]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.error]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.info]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.warning]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|Logger]] (trait: calls) — *Logger trait defines the standard interface for structured logging across the toolbox.*
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|ensure_safe_logger]] (function: calls) — *In strict mode (STRICT_LOGGER=true), panics to prevent microservices from running dark.*
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|logger.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/mod.rs.md|mod.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action.new]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action.with_callback]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action.with_input_prompt]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action.with_order]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action.with_sub_menu]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action]] (struct: belongs_to) — *Action defines a single interactive element in the Telegram UI.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|Action]] (struct: defines_method) — *Action defines a single interactive element in the Telegram UI.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|BtnDef]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|MenuEnvelope]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|RowDef]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.actions]] (method: belongs_to) — *Returns a reference to the actions collection.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.add_action]] (method: belongs_to) — *Registers a new action or submenu tree.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.build_menu_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.close]] (method: belongs_to) — *Gracefully closes the tele-remote client connection.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.configure_from_app_config]] (method: belongs_to) — *a live-configuration callback to refresh policy dynamically at runtime.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.convert_action_to_btn]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.generate_menu_json]] (method: belongs_to) — *Returns the structured JSON representation of the action tree.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.handlers]] (method: belongs_to) — *Returns a reference to the registered command handlers map.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.new]] (method: belongs_to) — *Creates a new TeleClient instance.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.parse_capability_bool]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.parse_tele_remote_capability]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.push_menu_update]] (method: belongs_to) — *Manually triggers transmission of updated menu schema to tele-remote.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.register_handlers_recursive]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.send_telemetry]] (method: belongs_to) — *Streams an arbitrary text telemetry message to the Telegram bot admin chat.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.set_auth_token]] (method: belongs_to) — *Configures the shared secret sent in outgoing `x-tele-auth` gRPC metadata.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.set_local_tls]] (method: belongs_to) — *Configures service-private X.509 TLS/mTLS file paths from the `local:` section.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.set_priority]] (method: belongs_to) — *Configures the OpenMFE menu priority for this component.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.set_tls_policy]] (method: belongs_to) — *Configures local/remote-aware TLS enforcement.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.start]] (method: belongs_to) — *Spawns the background connection manager and command dispatcher.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient.update_actions]] (method: belongs_to) — *Replaces all current actions and handlers.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClientPolicy.default]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClientPolicy]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClientPolicy]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient]] (struct: belongs_to) — *TeleClient maintains a resilient gRPC connection to tele-remote.*
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|TeleClient]] (struct: defines_method) — *TeleClient maintains a resilient gRPC connection to tele-remote.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
