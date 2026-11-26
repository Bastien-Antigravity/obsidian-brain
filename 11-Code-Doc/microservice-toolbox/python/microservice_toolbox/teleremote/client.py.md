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
Automatically generated mirror for `microservice-toolbox/python/microservice_toolbox/teleremote/client.py`.

> **Essential Process**:
> Provides a resilient, bi-directional gRPC Tele-Remote client matching the Go package design. Maintains a resilient stream connection to the tele-remote service, manages action registration, serializes menu configuration (including OpenMFE priority & ordering) to JSON, enforces TLS/mTLS and x-tele-auth policies, and dispatches callbacks.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/grpc_client/teleremote.pb.go.md|ComponentMessage]] (struct: calls) — *A message sent from the external component/service to the Bot*
- [[microservice-toolbox/microservice-toolbox/go/pkg/teleremote/grpc_client/teleremote.pb.go.md|Registration]] (struct: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/local_tls.py.md|LocalTLSConfig]] (class: calls) — *Service-private X.509 TLS/mTLS file paths from the local: configuration section.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/config/local_tls.py.md|local_tls.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/logger/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/network/tls.py.md|create_aio_channel]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/network/tls.py.md|normalize_tls_mode]] (function: calls) — *Canonicalizes a TLS policy mode string, defaulting empty values to 'auto'.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/network/tls.py.md|tls.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/grpc_client/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/grpc_client/teleremote_pb2_grpc.py.md|TeleRemoteServiceStub]] (class: calls) — *Missing associated documentation comment in .proto file.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|is_enabled]] (function: calls) — *Returns whether real-time connection tracking is active.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|record_event]] (function: calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/wiretap.py.md|wiretap.py]] (imports)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|Action]] (class: belongs_to) — *Action defines a single interactive element in the Telegram UI.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|TeleClient]] (class: belongs_to) — *TeleClient maintains a resilient gRPC connection to tele-remote.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|__init__]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|_apply_app_config_policy]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|_command_dispatcher]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|_connection_manager]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|_convert_action_to_btn]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|_disconnect]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|_on_live_update]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|_parse_capability_bool]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|_register_handlers_recursive]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|_run_handler]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|_send_registration]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|add_action]] (function: belongs_to) — *Registers a new action or sub-menu tree.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|close]] (function: belongs_to) — *Gracefully stops the client.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|configure_from_app_config]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|generate_menu_json]] (function: belongs_to) — *Returns the structured JSON representation of the action tree.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|send_log]] (function: belongs_to) — *Pushes a raw string update to the channel.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|send_log_tree]] (function: belongs_to) — *Pushes a menu tree update to the channel.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|send_telemetry]] (function: belongs_to) — *Streams an arbitrary text message to the Telegram admin chat.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|set_auth_token]] (function: belongs_to) — *Configures the shared secret sent in outgoing x-tele-auth gRPC metadata.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|set_local_tls]] (function: belongs_to) — *Configures service-private X.509 TLS/mTLS file paths from the local: section.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|set_priority]] (function: belongs_to) — *Configures the OpenMFE menu priority for this component.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|set_ssl_credentials]] (function: belongs_to) — *Configures explicit gRPC ChannelCredentials for the connection.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|set_tls_policy]] (function: belongs_to) — *Configures local/remote-aware TLS enforcement.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|start]] (function: belongs_to) — *Initiates the connection and registration process.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/teleremote/client.py.md|update_actions]] (function: belongs_to) — *Replaces all current actions and handlers.*
<!-- SYNC:END -->
