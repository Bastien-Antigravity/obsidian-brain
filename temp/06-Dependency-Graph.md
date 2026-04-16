# 🔗 Dependency Graph Extracted from Source Code

## Go Module Dependencies (from go.mod + imports)

```
                    ┌──────────────────┐
                    │  config-server   │
                    │     (Go)         │
                    └───────┬──────────┘
                            │ depends on
            ┌───────────────┼───────────────────┐
            │               │                   │
            ▼               ▼                   ▼
   ┌────────────────┐  ┌──────────────┐  ┌──────────────────┐
   │  safe-socket   │  │ distributed- │  │ microservice-    │
   │     (Go)       │  │   config     │  │   toolbox (Go)   │
   └────────────────┘  │   (Go)       │  └────────┬─────────┘
            │          └──────┬───────┘           │
            │                 │                   │
            │                 └─────────┬─────────┘
            │                           │
            ▼                           ▼
   ┌────────────────┐          ┌────────────────┐
   │ universal-     │◄─────────│ flexible-      │
   │   logger       │          │   logger       │
   │     (Go)       │          │     (Go)       │
   └───────┬────────┘          └────────────────┘
           │
           ▼
   ┌────────────────┐
   │ notif-server   │
   │     (Go)       │
   └────────────────┘
```

## Rust Dependencies

```
   ┌────────────────┐
   │  log-server    │──────► microservice-toolbox (Rust crate)
   │   (Rust)       │
   └────────────────┘
```
- `log-server` uses `microservice_toolbox::config::load_config()`
- `microservice-toolbox (Rust)` has optional `unilog` feature flag for UniLogger integration

## Python Dependencies

```
   microservice-toolbox (Python package)
       └── PyYAML (yaml)
       └── argparse
```
- Self-contained, no cross-repo Python dependencies

## Polyglot Parity Map

| Component | Go | Rust | Python |
|-----------|-----|------|--------|
| Config Loader | `microservice-toolbox/go` | `microservice-toolbox/rust` | `microservice-toolbox/python` |
| Log Engine | `flexible-logger` | N/A (uses Go CGO) | N/A (uses Go CGO) |
| Log Facade | `universal-logger` | `unilog-rs` (binding) | `unilog-py` (binding) |
| Socket | `safe-socket` | N/A (planned) | `safe-socket/python` |
| Config Service | `distributed-config` | N/A | N/A |
| Serialization | Protobuf + JSON | Cap'n Proto + Protobuf | MessagePack |

## Go Workspace Binding (`go.work`)

```
go 1.25.4

use (
    ./config-server
    ./distributed-config
    ./flexible-logger
    ./microservice-toolbox/go
    ./notif-server
    ./safe-socket
    ./universal-logger
)
```

**Rule**: All 7 Go modules are bound into a single workspace. Local changes propagate instantly without git push/pull.
