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
Automatically generated mirror for `microservice-toolbox/rust/src/config/loader.rs`.

> **Essential Process**:
> Loads layered configuration from local YAML, environment variables, and distributed config server.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/models.py.md|from_str]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/serializers/serializer.py.md|T]] (constant: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/args.rs.md|ToolboxArgs.parse_cli_args]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/args.rs.md|ToolboxArgs]] (struct: calls) — *internal network-aware resolution in dynamic container environments.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/args.rs.md|args.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/args.rs.md|args.rs]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/ffi.rs.md|DistConfLib]] (struct: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/ffi.rs.md|ffi.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/ffi.rs.md|ffi.rs]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/ffi.rs.md|get_lib]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/ffi.rs.md|to_rust_string]] (function: calls) — ** After calling this function, `c_ptr` must not be used again.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.apply_cli_overrides]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.apply_file_override]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.bridge_handle]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.common]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.decrypt_secret]] (method: defines_method) — *Uses the hardened distributed-config engine for cross-language consistency.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.decrypt_secret_by_handle]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.deep_merge]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.default]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.drop]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.extract_local_tls_config]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.from_value]] (method: defines_method) — *Creates an AppConfig wrapping explicit yaml value data.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_addr]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_bridge_error]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_capability]] (method: defines_method) — *Resolves a capability block as JSON via CGO bridge or local YAML tree.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_capability_by_handle]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_config]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_grpc_listen_addr]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_listen_addr]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_local]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_local_tls_config]] (method: defines_method) — *Precedence: `local.<service_key>.tls` (exact, then '-'/'_' normalized) -> `local.tls`.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_public_ip]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_rest_addr]] (method: defines_method) — *Resolves the REST Management address for a capability.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_service_name]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_value]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_version]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.internal_cb]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.internal_reg_cb]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.load_config]] (method: defines_method) — *Loads and merges configuration data based on the provided profile.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.load_from_file]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.load_public_key]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.on_live_conf_update]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.on_registry_update]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.read_and_expand_yaml]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.set_logger]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.set_value]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.share_config]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.sync]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.sync_from_bridge]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.unmarshal_local]] (method: defines_method) — *Parity with Go's UnmarshalLocal.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.validate_unique_ports]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|LocalTLSConfig.is_empty]] (method: defines_method) — *Returns true when all fields are unset/empty.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|LocalTLSConfig.should_verify_client]] (method: defines_method) — *Defaults to true whenever `ca_file` is configured and `verify_client` is not explicitly `false`.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/merger.rs.md|merger.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.info]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|DefaultLogger.warning]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|Logger]] (trait: calls) — *Logger trait defines the standard interface for structured logging across the toolbox.*
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|UniLogger.new]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|ensure_safe_logger]] (function: calls) — *In strict mode (STRICT_LOGGER=true), panics to prevent microservices from running dark.*
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/logger.rs.md|logger.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/utils/mod.rs.md|mod.rs]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/integration/expansion_check.rs.md|expansion_check.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/integration/expansion_check.rs.md|expansion_check.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/examples/test_logger.rs.md|test_logger.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/examples/test_logger.rs.md|test_logger.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/args.rs.md|args.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/args.rs.md|args.rs]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/ffi.rs.md|ffi.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/ffi.rs.md|ffi.rs]] (same_package)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.apply_cli_overrides]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.apply_file_override]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.bridge_handle]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.common]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.decrypt_secret]] (method: belongs_to) — *Uses the hardened distributed-config engine for cross-language consistency.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.decrypt_secret_by_handle]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.deep_merge]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.default]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.drop]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.extract_local_tls_config]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.from_value]] (method: belongs_to) — *Creates an AppConfig wrapping explicit yaml value data.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_addr]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_bridge_error]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_capability]] (method: belongs_to) — *Resolves a capability block as JSON via CGO bridge or local YAML tree.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_capability_by_handle]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_config]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_grpc_listen_addr]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_listen_addr]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_local]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_local_tls_config]] (method: belongs_to) — *Precedence: `local.<service_key>.tls` (exact, then '-'/'_' normalized) -> `local.tls`.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_public_ip]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_rest_addr]] (method: belongs_to) — *Resolves the REST Management address for a capability.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_service_name]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_value]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.get_version]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.internal_cb]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.internal_reg_cb]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.load_config]] (method: belongs_to) — *Loads and merges configuration data based on the provided profile.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.load_from_file]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.load_public_key]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.on_live_conf_update]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.on_registry_update]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.read_and_expand_yaml]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.set_logger]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.set_value]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.share_config]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.sync]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.sync_from_bridge]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.unmarshal_local]] (method: belongs_to) — *Parity with Go's UnmarshalLocal.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig.validate_unique_ports]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|AppConfig]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|LocalTLSConfig.is_empty]] (method: belongs_to) — *Returns true when all fields are unset/empty.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|LocalTLSConfig.should_verify_client]] (method: belongs_to) — *Defaults to true whenever `ca_file` is configured and `verify_client` is not explicitly `false`.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|LocalTLSConfig]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|LocalTLSConfig]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|MyConfig]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|get_live_cb]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|get_reg_cb]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|load_config]] (function: belongs_to) — *Initializes a configuration loader following the Microservice Toolbox 'Hierarchy of Truth'.*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|load_config_with_logger]] (function: belongs_to) — *Semantic helper to match Go LoadConfigWithLogger().*
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|test_address_resolution]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|test_cli_override_targets_single_capability]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|test_config_deep_merge]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|test_decrypt_enc_block_errors_without_bridge]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|test_decrypt_plaintext_passthrough]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|test_env_expansion]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|test_get_local]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|test_get_local_empty]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|test_get_local_tls_config_precedence_and_normalization]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|test_grpc_missing_returns_error]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|test_load_config_from_file]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|test_missing_file_returns_error]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|test_set_logger]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/loader.rs.md|test_unmarshal_local]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/rust/src/config/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/conn_manager/manager.rs.md|manager.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|client.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/notification/client.rs.md|client.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/spec.rs.md|spec.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/spec.rs.md|spec.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|client.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/teleremote/client.rs.md|client.rs]] (imports)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|mod.rs]] (calls)
- [[microservice-toolbox/microservice-toolbox/rust/src/wiretap/mod.rs.md|mod.rs]] (imports)
<!-- SYNC:END -->
