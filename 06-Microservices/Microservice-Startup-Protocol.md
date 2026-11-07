---
microservice: ecosystem-wide
type: protocol
status: active
tags:
- '#service/ecosystem-wide'
- '#type/protocol'
- '#state/active'
- '#zone/3-fleet'
- '#ai/ignore'
---
# 📜 Microservice Startup Protocol

This protocol defines the standardized initialization sequence for all microservices in the Bastien Ecosystem. It ensures parity in configuration loading, argument handling, and logging across **Go, Rust, Python, and C++**.

## 1. The Startup Sequence (The 5-Phase Truth)

Every microservice MUST follow this sequence during the `main()` initialization phase, managed by the `microservice-toolbox`:

1.  **Phase 1: Base Configuration**: Load `{profile}.yaml` as the foundation.
2.  **Phase 2: Local Overrides**: If in `standalone` or `test` profile, re-apply the local YAML file as a hard override to ensure developer-intent parity.
3.  **Phase 3: CLI Arguments**: Apply command-line flags. **CLI always wins.**
4.  **Phase 4: Remote Sync**: If the bridge is active, synchronize with the global configuration state (Service Discovery).
5.  **Phase 5: OpenMFE Auto-Registration & Real-Time WireTap Telemetry**:
    - All microservices register their declarative `ServiceSpec` via `spec.PublishWithLifecycle` (Go), `spec.publish_with_lifecycle` (Python), or `spec::publish_with_lifecycle` (Rust) in a non-blocking background loop (`MaxRetries: -1`) to `web-interface` (see [[OpenMFE-Integration-Protocol]]).
    - `BootstrapService` (Go) and `init_microservice` / `configure_from_config` (Python) automatically initialize the lock-free **WireTap** transport telemetry engine (`microservice-toolbox/go/pkg/wiretap`, `microservice_toolbox/wiretap.py`), binding `safe-socket`, gRPC (`teleremote`, `notification`, `network`), and NATS (`messaging`) to stream live `EdgeReport`s and segregated logical channels to `web-interface`.

### 1.1 Level 3 Hybrid Logic (Standalone vs. Connected)
For Level 3 services (Analysis/Observation), an additional logic gate is required during Phase 2:
- **If `profile == standalone`**:
    - Initialize local SQLite3 engine.
    - Mount file-system data providers.
    - Disable NATS/Bus initializers.
- **If `profile == production/develop`**:
    - Connect to NATS endpoint.
    - Initialize gRPC remote consumers.
    - Disable local file-based overrides.

## 2. Standard CLI Interface

The following flags are mandatory and handled automatically by the toolbox:

| Flag | Shorthand | Description | Priority |
| :--- | :--- | :--- | :--- |
| `--profile` | `-p` | Selects the config profile (standalone, production, etc.) | Critical |
| `--name` | | Overrides the service identity | High |
| `--host` | | Overrides the listening IP (ignored in Docker) | High |
| `--port` | | Overrides the listening port (ignored in Docker) | High |
| `--conf` | | Path to an explicit configuration file | Medium |
| `--log_level`| | Sets the initial logging threshold (DEBUG, INFO, etc.) | Medium |
| `--key` | | Path to RSA private key for secret decryption | Security |

## 3. Polyglot Implementation Examples

### 🐹 Go
```go
func main() {
    // Toolbox handles --profile and standard flags automatically
    appConfig, err := config.LoadConfig("standalone", nil) 
    // Access custom flags via appConfig.Args.Extra["my-flag"]
}
```

### 🦀 Rust
```rust
fn main() {
    let ac = AppConfig::load_config("standalone", None)?;
    // Access custom flags via ac.cli_args.extras
}
```

### 🐍 Python
```python
def main():
    ac = load_config("standalone")
    # Access custom flags via ac.args.extras
```

### 🧊 C++
```cpp
int main(int argc, char** argv) {
    auto ac = LoadConfig("standalone", argc, argv);
    // Access custom flags via ac->GetArgs().extras
}
```

## 4. The Docker Guard
All toolbox implementations MUST implement the **Docker Guard**. If `DOCKER_ENV=true` or `.dockerenv` is detected, CLI overrides for `--host` and `--port` are ignored to prevent breaking internal network-aware resolution.

## 5. L1 Resilience, Connectivity & Reconnection Standard

All microservices communicating with sibling daemons or central ecosystem infrastructure MUST implement the **Ecosystem L1 Retry and Resilience Contract** provided by `microservice-toolbox`:

### 5.1 Connection Manager (`conn_manager`)
- **Critical Strategy (`NewCriticalStrategy(logger)`)**:
  - `MaxRetries: -1` (Infinite Retries): Reconnection loops run indefinitely until the downstream dependency recovers. **This is a design requirement, not a bug.**
  - `BaseDelay: 200ms`, `MaxDelay: 10000ms`, `ConnectTimeout: 5000ms`, `Backoff: 2.0`, `Jitter: 0.2`.
  - **Asynchronous Mode (`ModeNonBlocking`)**: Startup sequences MUST NEVER block indefinitely on downstream dependencies. Establish connections asynchronously so the daemon remains healthy and responsive.
- **Target Transports**:
  - `conn_manager.EstablishConnection`: Wraps `safe-socket` framed TCP (`safesocket.Create`).
  - gRPC Streams: Integrated into `microservice-toolbox/go/pkg/teleremote` (`TeleClient.connectionManager`) with automatic infinite reconnect loop.
  - NATS / JetStream: Managed via `microservice-toolbox/go/pkg/messaging` (`Connect`) with automated reconnect handlers.

### 5.2 Dynamic Capability Resolution & Docker Guard (`connectivity.Resolver`)
- **No Hardcoded Addresses**: Always resolve sibling endpoints dynamically using toolbox capability accessors (e.g. `appConfig.GetListenAddr("web_interface")`, `appConfig.GetGRPCListenAddr("tele_remote")`).
- **Docker Guard Suppression**: `connectivity.Resolver` automatically translates bind addresses to `0.0.0.0` in container environments (`DOCKER_ENV=true`) while preserving native loopback/host bindings in local environments.

### 5.3 Lifecycle Supervision (`lifecycle.Manager`)
- **LIFO Graceful Shutdown**: Traps OS signals (`SIGINT`, `SIGTERM`) and context cancellations via `lm.Wait(ctx)`.
- **Registered Cleanup Hooks**: Sockets, gRPC streams, background workers, and persistence stores must be cleanly flushed in reverse order of initialization.

---
*Last Updated: 2026-10-11*
*See also: [[03-Tech-Stack/02-Project-Architecture/Global-Architecture-Rules|Architecture-Patterns]], [[Web-Interface-Integration-Protocol]], [[OpenMFE-Integration-Protocol]]*
