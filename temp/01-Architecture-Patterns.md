# 🏗️ Architecture Patterns Extracted from Source Code

## 1. Facade Pattern (Universal Entry Point)
Every library exposes a **root-level facade file** that re-exports its internals:

| Repo | Facade File | Purpose |
|------|-------------|---------|
| `safe-socket` | `safe_socket.go` | Re-exports `factory.Create()` as `safesocket.Create()` |
| `distributed-config` | `distributed_config.go` | Re-exports `facade.NewConfig()` as `distributed_config.New()` |
| `universal-logger` | `src/bootstrap/unilog.go` | `Init()` bootstraps config + logger in one call |
| `microservice-toolbox` | `go/pkg/config/loader.go` | `LoadConfig()` wraps distributed-config + CLI + env layering |

**Rule**: Consumers never import internal packages directly. They use the facade.

---

## 2. Factory Pattern (Profile-Based Construction)
Both `safe-socket` and `flexible-logger` use a **factory + profile registry**:

- `safe-socket/src/factory/socket_factory.go` → `Create(profileName, ...)` dispatches to `profiles.NewTcpHelloClientProfile()`, `profiles.NewUdpProfile()`, etc.
- `flexible-logger/src/profiles/` → `NewStandardLogger()`, `NewDevelLogger()`, `NewAuditLogger()`, etc.

**Hidden Rule**: Profile names are **lowercase string constants** (`"tcp-hello"`, `"standard"`, `"devel"`, `"cloud_native"`). They are matched via `switch` statements, never enums.

---

## 3. Strategy Pattern (Config Loading)
`distributed-config/src/interfaces/config_strategy.go` defines:
```go
type ConfigStrategy interface {
    Name() string
    Load(cfg *core.Config) error
    Sync(cfg *core.Config) error
    GetHandler() *network.ConfigProtoHandler
}
```
Profiles (`production`, `preprod`, `test`, `standalone`) are implemented as strategy structs in `src/strategies/`.

---

## 4. Layered Configuration (4-Phase Priority)
The `microservice-toolbox` config loader follows **identical 4-phase layering** across Go, Rust, and Python:

1. **Base File** (`{profile}.yaml`) — loaded via `load_from_file()`
2. **Dev Override** — If `standalone` or `test`, re-applies file as hard override
3. **CLI Flags** — Applied via `apply_cli_overrides()` (highest priority)
4. **gRPC Overrides** — Separate gRPC host/port flags

**Hidden Rule**: gRPC fallback is always `port + 1` if no explicit gRPC config exists.

---

## 5. Atomic State Management (Lock-Free Reads)
`config-server/src/store/store.go` uses Go's `atomic.Pointer` for a CAS (Compare-And-Swap) loop:
- **Reads**: Lock-free via `atomic.Load()`
- **Writes**: Retry loop using `CompareAndSwap()`
- **Immutability**: Returned maps must be treated as immutable; modifications require `DeepCopy()`

---

## 6. Bootstrap Composition (Dependency Injection)
`universal-logger/src/bootstrap/unilog.go` demonstrates the **composition root** pattern:
- `Init()` is the simple entry point (string params)
- `InitWithOptions(BootstrapOptions{})` is the advanced entry point (struct with optional injection)
- `ExistingConfig` field allows injecting a pre-existing `DistConfig` (dependency injection)

---

## 7. Go Workspace Monorepo
The root `go.work` file binds 7 Go modules into a single workspace:
```
./config-server, ./distributed-config, ./flexible-logger,
./microservice-toolbox/go, ./notif-server, ./safe-socket, ./universal-logger
```
**Rule**: All inter-module references use `github.com/Bastien-Antigravity/{repo}` imports, but local development resolves them via `go.work`.
