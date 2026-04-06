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
- `cmd/<service-name>/main.go`: The entry point. It should ONLY handle bootstrap (config, logging, signal handling, and Facade instantiation).
- `src/`: The heart of the application logic.
    - `src/interfaces/`: Interface definitions (`IBroker`, `IDataSource`).
    - `src/models/`: Shared data structures (`MMarketData`).
    - `src/config/`: Configuration mapping (`config.go`).
    - `src/grpc_control/`: Service lifecycle and gRPC management.
    - `src/factories/`: Strategy pattern implementations for creating concrete types.
- `config/`: Root folder containing `default.yaml` and other environment-specific configurations.
- `doc/`: Architectural documentation and ASCII diagrams.

### 4. Process Lifecycle
- Services are managed via a gRPC `ProcessController`.
- **Standard Methods**: `Start()`, `Stop()`, `Restart()`.
- Graceful shutdown is mandatory. Use `context.WithTimeout` and listen for `SIGTERM`/`SIGINT` in `main.go`.
