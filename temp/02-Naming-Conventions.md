# 📐 Naming Conventions Extracted from Source Code

## 1. Interface Naming (Go)
All Go interfaces follow a **domain-specific naming** convention (NOT `I`-prefix in practice):

| Interface | Package | File |
|-----------|---------|------|
| `Logger` | `interfaces` | `universal-logger/src/interfaces/logger.go` |
| `Socket` | `interfaces` | `safe-socket/src/interfaces/socket.go` |
| `SocketProfile` | `interfaces` | `safe-socket/src/interfaces/profile.go` |
| `TransportConnection` | `interfaces` | `safe-socket/src/interfaces/transport.go` |
| `ConfigStrategy` | `interfaces` | `distributed-config/src/interfaces/config_strategy.go` |
| `Notificator` | `interfaces` | `notif-server/src/interfaces/notifie.go` |

> **Hidden Pattern**: Despite the Obsidian rule saying "Interfaces MUST start with `I`", the actual Go code does NOT use `I`-prefix. It follows idiomatic Go naming (`Logger`, not `ILogger`).

> **Exception**: Python DOES use `I`-prefix: `ILogger` in `microservice_toolbox/utils/logger.py`.

---

## 2. Package Organization (Go)
Every Go repository follows a consistent directory layout:
```
{repo}/
├── cmd/           # Entry points (main.go files)
│   ├── {service}/   # Production binary
│   └── test/        # Test binary
├── src/           # Core business logic
│   ├── core/        # Business rules
│   ├── interfaces/  # Public contracts
│   ├── models/      # Data structures
│   ├── factory/     # Creational logic
│   ├── facade/      # Simplified API layer
│   ├── profiles/    # Named configurations
│   ├── schemas/     # Protobuf/serialization schemas
│   └── utils/       # Helpers
└── {facade}.go    # Root-level facade re-export
```

---

## 3. File Naming
| Language | Convention | Example |
|----------|-----------|---------|
| Go | `snake_case.go` | `request_handler.go`, `socket_factory.go` |
| Rust | `snake_case.rs` | `loader.rs`, `args.rs`, `mod.rs` |
| Python | `snake_case.py` | `loader.py`, `args.py`, `test_logger.py` |
| Scripts | `PascalCase-Hyphenated.py` | `Build-Wrapper.py`, `Hide-Empty-Folders.py` |

---

## 4. Function/Method Naming

### Go
- **Exported**: `PascalCase` — `ProcessRequest()`, `NewStore()`, `LoadConfig()`
- **Unexported**: `camelCase` — `handleConnection()`, `broadcastRegistry()`, `ensurePath()`
- **Constructor**: `New{Type}()` — `NewServer()`, `NewStore()`, `NewUniLog()`

### Rust
- **Functions**: `snake_case` — `load_config()`, `run_server()`, `deep_merge()`
- **Structs**: `PascalCase` — `AppConfig`, `LogServer`, `ToolboxArgs`
- **Methods**: `snake_case` — `get_listen_addr()`, `apply_cli_overrides()`

### Python
- **Functions**: `snake_case` — `load_config()`, `parse_cli_args()`, `deep_merge()`
- **Classes**: `PascalCase` — `AppConfig`
- **Private**: `_underscore_prefix` — `_load_from_file()`, `_apply_cli_overrides()`

---

## 5. Variable Naming
| Pattern | Convention | Example |
|---------|-----------|---------|
| Configuration objects | `ac` or `dConf` | `ac := &AppConfig{}` |
| Loggers | `logger`, `flexLogger`, `unilog` | `flexLogger = profiles.NewStandardLogger()` |
| Sockets | `sock`, `serverSock`, `conn` | `serverSock, err := factory.Create(...)` |
| Error handling | Always `err` | `if err != nil { return nil, err }` |

---

## 6. Import Aliasing (Go)
Go imports use **descriptive aliases** to disambiguate packages:
```go
factory "github.com/Bastien-Antigravity/safe-socket"
socket_interfaces "github.com/Bastien-Antigravity/safe-socket/src/interfaces"
schemas "github.com/Bastien-Antigravity/distributed-config/src/schemas"
utilconf "github.com/Bastien-Antigravity/microservice-toolbox/go/pkg/config"
flex_interfaces "github.com/Bastien-Antigravity/flexible-logger/src/interfaces"
logger_models "github.com/Bastien-Antigravity/flexible-logger/src/models"
```
**Rule**: Aliases use `snake_case` and follow the pattern `{domain}_{type}`.
