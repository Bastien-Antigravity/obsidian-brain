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
5.  **Phase 5: OpenMFE Auto-Registration, Exchange Contracts & Real-Time WireTap Telemetry**:
    - All microservices resolve version via `appConfig.GetVersion()` / `app_config.get_version()` and register their declarative `ServiceSpec` + `Contracts` (`ExchangeContract[]`) via `spec.PublishWithLifecycle` (Go), `spec.publish_with_lifecycle` (Python), `spec::publish_with_lifecycle` (Rust), or `SpecPublisher::PublishWithLifecycle` (C++, with `contracts.h` for C ABI) in a non-blocking background loop (`MaxRetries: -1`) to `web-interface` (see [[OpenMFE-Integration-Protocol]]). `BuildSpecFromConfig` automatically enriches `URL`, `%s` ports in `Framing`, `DataStructure` (`version` from `appConfig.GetVersion()`, `capability`, `ports`, `node`), `NavRoute`, `Canvas`, and `Health`; HTTP-capable services also expose `GET /api/v1/contracts`.
    - `BootstrapService` (Go) and `init_microservice` / `configure_from_config` (Python) automatically initialize the lock-free **WireTap** transport telemetry engine (mirrored across Go, Python, Rust `src/wiretap/mod.rs`, and C++17 `wiretap/WireTap.hpp`), binding `safe-socket`, gRPC (`teleremote`, `notification`, `network`), and NATS (`messaging`) to stream live `EdgeReport`s and segregated logical channels to `web-interface`.

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
    appConfig, log := bootstrap.BootstrapService("my-service")
    defer log.Close()
    ver := appConfig.GetVersion() // Dedicated AppConfig method (VERSION.txt only)
}
```

### 🦀 Rust
```rust
fn main() -> Result<(), Box<dyn std::error::Error>> {
    let ac = AppConfig::load_config("standalone", None)?;
    let ver = ac.get_version(); // Dedicated AppConfig method (VERSION.txt only)
    Ok(())
}
```

### 🐍 Python
```python
def main():
    ac, log, lm = init_microservice(__file__, app_name="my_service")
    ver = ac.get_version()  # Dedicated AppConfig method (VERSION.txt only)
```

### 🧊 C++17
```cpp
int main(int argc, char** argv) {
    auto ac = LoadConfig("standalone", argc, argv);
    std::string ver = ac->GetVersion(); // Dedicated AppConfig method (VERSION.txt only)
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

### 5.2 Config-Verbatim Capability Resolution (`connectivity.Resolver` & CLI Docker Guard)
- **No Hardcoded Addresses & Trust `AppConfig`**: Always resolve sibling endpoints directly from pre-validated `AppConfig` string getters (`appConfig.GetListenAddr("web_interface")`, `appConfig.GetGRPCListenAddr("tele_remote")`), failing fast if empty or unconfigured (zero silent fallback).
- **Verbatim Binding (`connectivity.Resolver`)**: `connectivity.Resolver` preserves configured `AppConfig` IP, hostname, and port values **verbatim** in both Native and Docker environments (never rewriting them to `0.0.0.0`), while CLI Docker Guard (`config`) suppresses CLI `--host`/`--port`/`--grpc_host`/`--grpc_port` overrides inside containers.

### 5.3 Lifecycle Supervision (`lifecycle.Manager`)
- **LIFO Graceful Shutdown**: Traps OS signals (`SIGINT`, `SIGTERM`) and context cancellations via `lm.Wait(ctx)`.
- **Registered Cleanup Hooks**: Sockets, gRPC streams, background workers, and persistence stores must be cleanly flushed in reverse order of initialization.

---
*Last Updated: 2026-10-11*
*See also: [[03-Tech-Stack/02-Project-Architecture/Global-Architecture-Rules|Architecture-Patterns]], [[Web-Interface-Integration-Protocol]], [[OpenMFE-Integration-Protocol]]*
