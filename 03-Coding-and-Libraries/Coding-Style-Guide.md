# Coding Style: Multi-Language Idioms & Performance

## General Standards
Our microservices are designed for high-performance and clear readability across Go, Rust, and Python.

### 1. Naming Conventions (All Languages)
- **Interfaces**: MUST start with `I` (e.g., `IBroker`, `IDataSource`). In Python, use abstract base classes with the same prefix.
- **Models**: The target standard is to prefix with `M` (e.g., `MMarketData`, `MOrderBook`).
  - *Note*: You may encounter legacy models without this prefix. When creating NEW models, ALWAYS apply the `M` prefix.
- **Functions/Methods**: Use descriptive naming. Go: `CamelCase`. Rust: `snake_case`. Python: `snake_case`.
- **Variables**: Short and descriptive (e.g., `app_logger`, `svc`, `config`).

---

## Go-Specific Standards

### 2. Memory Efficiency
- **Fixed-Length Slices**: Use ring-buffers or sliding slices with fixed-size bounds (e.g., `200` length). NEVER expand arrays infinitely.
- **Pre-allocation**: Use `make([]Type, 0, capacity)` for slices whenever the expected size is known.
- **Data Copies**: ALWAYS deep-copy or snapshot maps/dictionaries before sharing them across Goroutines or JSON serializers to avoid race conditions.

### 3. Error Handling
- **Main Level**: `log.Fatal` or `os.Exit(1)` is only permissible in `main.go`.
- **Logic Level**: Functions must return an `error` if they encounter a failure.
- **Logging**: Use `universal-logger` with levels (`Info`, `Warning`, `Error`, `Critical`).
- **Sentinel Errors**: Avoid comparing error strings. Use `errors.Is()` or typed errors.

### 4. Concurrency Guardrails
- **Goroutine Management**: Use `context.Context` to propagate cancellation signals.
- **Safe Mutexes**: Use `sync.RWMutex` for shared resources. Prefer `RUnlock()` for readers.
- **Background Workers**: Offload database I/O or external API calls into background Goroutines or worker pools.

### 5. Dependency Management
- **Go Mod**: `go.mod` is mandatory.
- **Minimal Dependencies**: Only include external libraries that are absolutely necessary.
- **Tidy**: ALWAYS run `go mod tidy` before committing changes.

---

## Rust-Specific Standards

### 6. Async Runtime
- **Tokio**: All async code uses the `tokio` runtime with `features = ["full"]`.
- **Error Handling**: Use `Result<T, Box<dyn std::error::Error>>` for functions that can fail. Propagate errors with `?`.
- **Ownership**: Prefer borrowing (`&str`, `&[u8]`) over cloning. Clone only when ownership transfer is required.

### 7. Dependencies
- **Cargo.toml**: Always specify exact or compatible versions for critical dependencies.
- **Local Path Dependencies**: Use `path = "../microservice-toolbox/rust"` for shared ecosystem crates during development.
- **Build**: If the project uses `protoc`, set `PROTOC=/usr/local/bin/protoc` when building.

---

## Python-Specific Standards

### 8. Structure
- **Abstract Base Classes**: Use `abc.ABC` and `@abstractmethod` for interface definitions in `src/interfaces/`.
- **Type Hints**: Always use type hints for function signatures.
- **Dependencies**: Use `requirements.txt` for dependency management. Pin versions.
- **Config Loading**: Use `microservice_toolbox.config.load_config(profile)` for configuration.
