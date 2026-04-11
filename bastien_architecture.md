# Architecture Standards: Facade & Decoupling

## Architectural Philosophy
Our microservices are designed for high throughput and long-term maintainability using **Clean Architecture** principles and the **Facade Pattern**.

### 1. The Facade Pattern (SystemFacade)
- Every microservice must have a central orchestrator, usually named `SystemFacade` or a domain-specific equivalent (e.g., `Ingestor`, `Manager`).
- **Location**: `src/facade/` or `src/<domain>/`.
- **Responsibility**: It is the ONLY component that coordinates between different sub-packages. Lower-level packages (storage, network, serializers) must NEVER talk to each other directly; they must communicate via the Facade or through interfaces.

### 2. Component Decoupling via Interfaces
- **Strict Interface Usage**: Business logic must NEVER depend on concrete implementations (drivers).
- **Location**: All core interfaces must reside in `src/interfaces/`.
- **Naming Convention**: All interfaces MUST be prefixed with a capital `I` (e.g., `IBroker`, `IStorage`, `IPublisher`).
- **Dependency Injection**: Concrete types must be injected into the Facade/Engine using Factory patterns (`src/factories/`).

### 3. Repository Structure

#### Go Services (Primary Language)
- `cmd/<service-name>/main.go`: The entry point. It should ONLY handle bootstrap (config, logging, signal handling, and Facade instantiation).
- `src/`: The heart of the application logic.
    - `src/interfaces/`: Interface definitions (`IBroker`, `IDataSource`).
    - `src/models/`: Shared data structures (`MMarketData`).
    - `src/config/`: Configuration mapping (`config.go`).
    - `src/grpc_control/`: Service lifecycle and gRPC management.
    - `src/factories/`: Strategy pattern implementations for creating concrete types.
- `config/`: Root folder containing `standalone.yaml` and other environment-specific configurations.
- `doc/`: Architectural documentation and ASCII diagrams.

#### Rust Services (e.g., log-server)
- `src/main.rs`: The entry point. Uses `microservice-toolbox` for config loading.
- `src/core/`: Central server/engine logic.
- `src/servers/`: Network server implementations (TCP, gRPC).
- `src/models/`: Shared data structures.
- `src/protocols/`: Serialization schemas (Cap'n Proto).
- `Cargo.toml`: Dependency manifest. Use local `path` dependencies for `microservice-toolbox`.

#### Python Services (e.g., enhanced-backtesting, fundamental-analysis)
- `main.py`: The entry point.
- `src/`: Business logic modules.
    - `src/interfaces/`: Abstract base classes for decoupling.
    - `src/factories/`: Strategy pattern.
    - `src/calculators/`, `src/data_loaders/`, `src/strategies/`: Domain logic.
- `config/`: YAML configuration files.
- `requirements.txt`: Python dependency manifest.

### 4. Process Lifecycle
- Services are managed via a gRPC `ProcessController`.
- **Standard Methods**: `Start()`, `Stop()`, `Restart()`.
- Graceful shutdown is mandatory. Use `context.WithTimeout` (Go) or `tokio::signal` (Rust) and listen for `SIGTERM`/`SIGINT` in the entry point.

### 5. Ecosystem Service Map
The platform consists of the following services and libraries:

| Repository | Language | Role |
|---|---|---|
| `config-server` | Go | Centralized config distribution via gRPC |
| `data-ingestor` | Go | Market data ingestion from exchanges |
| `market-observer` | Go | Real-time market analysis and monitoring |
| `orderbook-aggregator` | Go | Order book aggregation and scalping signals |
| `technical-analysis` | Go | Technical indicator computation engine |
| `tele-remote` | Go | Telegram bot interface for remote control |
| `notif-server` | Go | Notification routing (Telegram, email) |
| `web-interface` | Go | Web dashboard and PostgreSQL browser |
| `log-server` | Rust | Centralized logging server (TCP + gRPC) |
| `enhanced-backtesting` | Python | Strategy backtesting engine |
| `fundamental-analysis` | Python | Stock fundamental analysis & scoring |
| `microservice-toolbox` | Go/Rust/Python | Shared config, CLI, networking primitives |
| `universal-logger` | Go/C++ | Standardized logging facade and bootstrap |
| `distributed-config` | Go | Configuration loading, env expansion, sync |
| `safe-socket` | Go/Python | Cap'n Proto transport for log messages |
| `flexible-logger` | Go | **DEPRECATED** — replaced by `universal-logger` |
| `docker-deployment` | Docker | Production docker-compose orchestration |
| `testing-sandbox` | Shell | Integration and resilience testing harness |
