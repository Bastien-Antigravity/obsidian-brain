# 🎨 Coding Style Rules Extracted from Source Code

## 1. Comment Separators
Every Go file uses **horizontal rule comments** to separate logical sections:
```go
// -----------------------------------------------------------------------------
```
This is applied:
- Between every exported function
- Between interface method groups
- Between struct definitions and their methods
- In section headers like `// SCAN`, `// TOOLS`, `// CSS GENERATION`

**Consistency**: This is the MOST consistent pattern across the entire codebase. Every single `.go` file follows it.

---

## 2. Comment Style (Go)
- **Function docs**: Single-line `//` comments directly above the function
- **Multi-line docs**: Start with `//` on each line (never `/* */`)
- **Parameter docs**: Inline in the function signature comment using `//   - paramName:` format
- **No inline comments**: Comments are always on their own line, never at end of code

Example pattern:
```go
// ProcessRequest handles the business logic for incoming configuration requests.
// It returns a response message to be sent back to the client.
// It may also trigger a broadcast via the provided callback.
// -----------------------------------------------------------------------------
func ProcessRequest(data []byte, ...) (*config.ConfigMsg, error) {
```

---

## 3. Error Handling Patterns

### Go — `if err != nil` Chain
```go
if err := proto.Unmarshal(data, req); err != nil {
    return nil, fmt.Errorf("protobuf unmarshal error: %w", err)
}
```
- Always wraps errors with `fmt.Errorf("context: %w", err)`
- Fatal errors use `os.Exit(1)` (never `panic`)
- Non-fatal errors log and `continue`

### Rust — `Result<T, Box<dyn Error>>`
```rust
fn run_server(...) -> Result<(), Box<dyn std::error::Error>> {
```
- Uses `?` operator for propagation
- Entry points use `match` with `eprintln!` + `std::process::exit(1)`
- Never uses `unwrap()` in production paths (only in parsing after validation)

### Python — Exceptions with Descriptive Messages
```python
raise FileNotFoundError(f"Toolbox (Python): Config file '{filename}' not found for profile '{profile}'")
raise ValueError(f"capability {capability} not found")
```
- Uses built-in exception types
- Error messages include the component name as prefix: `"Toolbox (Python): ..."`

---

## 4. Concurrency Patterns (Go)

### Goroutine Conventions
- **Fire-and-forget broadcasts**: `go s.broadcastRegistry()`
- **Per-connection handlers**: `go s.handleConnection(conn)`
- **Async sends**: `go func(n string, sk ...) { sk.Write(bytes) }(name, sock)`

### Lock Patterns
- **RWMutex for client maps**: `listenersLock sync.RWMutex`
- **Lock/Unlock in same function**: Never deferred if followed by mutations
- **Deferred RUnlock for reads**: `s.listenersLock.RLock(); defer s.listenersLock.RUnlock()`

### Channel Patterns
- **Buffered notification queues**: `make(chan *utils.NotifMessage, 1024)`
- **Graceful shutdown**: `shutdown chan struct{}` with `select` multiplexing

---

## 5. Type Alias Pattern
Both `safe-socket` and `universal-logger` re-export internal types via aliases at the facade level:
```go
type Socket = interfaces.Socket
type SocketConfig = models.SocketConfig
type Level = logger_models.Level
type NotifMessage = logger_models.NotifMessage
```
**Rule**: The facade file provides ALL necessary types so consumers never need to import internal packages.

---

## 6. Printf-Style Logging
The entire ecosystem uses **printf-style** log methods:
```go
logger.Info("Config Server listening on " + addr)
logger.Error("Accept error: " + err.Error())
```
Also supports format strings:
```go
Debug(format string, args ...any)
Info(format string, args ...any)
```
**Hidden Rule**: String concatenation (`+`) is used for simple messages. Format strings (`%s`, `%v`) are used when variables need interpolation.

---

## 7. Python-Specific Patterns

### Type Hints
- Uses `Optional[Type]` from `typing` module
- Function signatures always include type annotations for parameters
- `@staticmethod` decorator for utility methods like `deep_merge()`

### Private Methods
- Prefixed with `_underscore`: `_load_from_file()`, `_apply_cli_overrides()`
- Matches the Go `unexported` convention semantically

### Import Aliasing
```python
from .args import parse_cli_args
from ..utils.logger import ILogger, ensure_safe_logger
```
Uses relative imports within the package hierarchy.
