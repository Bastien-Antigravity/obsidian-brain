---
title: "General Naming Conventions"
type: architecture
status: active
microservice: ecosystem-wide
---

# 📐 General Naming Conventions

## Architectural Rule
- **Interfaces (Python)**: MUST start with `I` (e.g., `ILogger`, `IDataProcessor`).
- **Interfaces (Go)**: Follow idiomatic Go — NO `I`-prefix. Use descriptive nouns (e.g., `Logger`, `Socket`, `ConfigStrategy`).
- **Interfaces (Rust)**: Use traits with descriptive names (e.g., `Logger`).
- **Models**: prefix with `M` (e.g., `MMarketData`, `MOrderBook`).
- **Functions/Methods**: Go: `PascalCase` (exported) / `camelCase` (unexported). Rust: `snake_case`. Python: `snake_case` with `_underscore_prefix` for private.
- **Constructors (Go)**: Always `New{Type}()` — e.g., `NewServer()`, `NewStore()`, `NewUniLog()`.

## File Naming

| Language | Convention | Example |
|----------|-----------|---------|
| Go | `snake_case.go` | `request_handler.go`, `socket_factory.go` |
| Rust | `snake_case.rs` | `loader.rs`, `args.rs`, `mod.rs` |
| Python | `snake_case.py` | `loader.py`, `args.py`, `test_logger.py` |
| Scripts | `PascalCase-Hyphenated.py` | `Build-Wrapper.py`, `Hide-Empty-Folders.py` |

## Go Import Aliasing
Use `snake_case` descriptive aliases to disambiguate packages:
```go
factory "github.com/Bastien-Antigravity/safe-socket"
socket_interfaces "github.com/Bastien-Antigravity/safe-socket/src/interfaces"
schemas "github.com/Bastien-Antigravity/distributed-config/src/schemas"
utilconf "github.com/Bastien-Antigravity/microservice-toolbox/go/pkg/config"
flex_interfaces "github.com/Bastien-Antigravity/flexible-logger/src/interfaces"
logger_models "github.com/Bastien-Antigravity/flexible-logger/src/models"
```

## Variable Naming Conventions

| Pattern | Convention | Example |
|---------|-----------|---------|
| Configuration objects | `ac` or `dConf` | `ac := &AppConfig{}` |
| Loggers | `logger`, `flexLogger`, `unilog` | `flexLogger = profiles.NewStandardLogger()` |
| Sockets | `sock`, `serverSock`, `conn` | `serverSock, err := factory.Create(...)` |
| Error handling | Always `err` | `if err != nil { return nil, err }` |

## Motivation (Why?)
- Unified readability across polyglot microservices.
- Instant recognition of types and abstractions when switching between Go, Rust, and Python.

## Examples
- `Logger` (Go Interface)
- `ILogger` (Python Interface)
- `MMarketData` (Model)
- `app_logger` (Variable)
- `NewServer()` (Go Constructor)
