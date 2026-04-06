# Coding Style: Go Idioms & Performance

## Go Coding Standards
Our Go microservices are designed for high-performance and clear readability.

### 1. Naming Conventions
- **Interfaces**: MUST start with `I` (e.g., `IBroker`, `IDataSource`). This is the absolute standard for all decoupling layers.
- **Models**: The target standard is to prefix with `M` (e.g., `MMarketData`, `MOrderBook`). 
  - *Note*: You may encounter legacy models (like `LogEntry` or `OrderBookSnapshot`) without this prefix. When creating NEW models or refactoring existing ones, ALWAYS apply the `M` prefix for consistency.
- **Functions**: Use descriptive CamelCase. Public functions (e.g., `GetSymbols`) must be capitalized.
- **Variables**: Short and descriptive (e.g., `appLogger`, `svc`, `config`).

### 2. Memory Efficiency
- **Fixed-Length Slices**: Use ring-buffers or sliding slices with fixed-size bounds (e.g., `200` length). NEVER expand arrays infinitely.
- **Pre-allocation**: Use `make([]Type, 0, capacity)` for slices whenever the expected size is known.
- **Data Copies**: ALWAYS deep-copy or snapshot maps/dictionaries before sharing them across Goroutines or JSON serializers to avoid race conditions.

### 3. Error Handling
- **Main Level**: `log.Fatal` or `os.Exit(1)` is only permissible in `main.go`.
- **Logic Level**: Functions must return an `error` if they encounter a failure.
- **Logging**: Use the custom `logger` with levels (`Info`, `Warning`, `Error`, `Critical`).
- **Sentinel Errors**: Avoid comparing error strings. Use `errors.Is()` or typed errors defined in `src/models/errors.go` if necessary.

### 4. Concurrency Guardrails
- **Goroutine Management**: Use `context.Context` to propagate cancellation signals.
- **Safe Mutexes**: Use `sync.RWMutex` for shared resources. Prefer `RUnlock()` for readers to maximize performance.
- **Background Workers**: Offload database I/O or external API calls into fire-and-forget background Goroutines or worker pools.

### 5. Dependency Management
- **Go Mod**: `go.mod` is mandatory.
- **Minimal Dependencies**: Only include external libraries that are absolutely necessary (e.g., `grpc`, `nats`, `yaml`).
- **Tidy**: ALWAYS run `go mod tidy` before committing changes.
