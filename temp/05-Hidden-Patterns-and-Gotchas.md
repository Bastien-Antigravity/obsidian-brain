# ⚠️ Hidden Patterns & Gotchas Extracted from Source Code

## 1. The "Safe Logger" Guard
Every entry point in the toolbox uses a **nil-safe logger wrapper**:
```go
safeLogger := utils.EnsureSafeLogger(logger)  // Go
let final_logger = ensure_safe_logger(logger)  // Rust
self.logger = ensure_safe_logger(logger)        // Python
```
**Why**: Prevents nil-pointer panics when a logger isn't provided. This is a MANDATORY first step in all `LoadConfig` functions across all three languages.

---

## 2. gRPC Port Convention: `base_port + 1`
When no explicit gRPC configuration exists, ALL three toolbox implementations fall back to `port + 1`:
```go
// Go: ac.Config.GetGRPCAddress(capability) — internally does port+1
// Rust: Ok(format!("{}:{}", host, port + 1))
// Python: return f"{ip}:{port + 1}"
```
**Gotcha**: If you set port `9020`, gRPC will automatically bind to `9021`. This is never documented in READMEs.

---

## 3. Duplicate GoDoc Comments in Factory
`safe-socket/src/factory/socket_factory.go` has the **Create function documented TWICE** (lines 14-43). This appears to be a copy-paste artifact from refactoring. The function body is correct but the documentation is duplicated.

---

## 4. Broadcast via Goroutine-per-Client
In `config-server/src/server/server.go`, broadcasts iterate a map and spawn a goroutine per client:
```go
for name, sock := range s.listeners {
    go func(n string, sk TransportConnection) {
        sk.Write(bytes)
    }(name, sock)
}
```
**Gotcha**: The closure captures loop variables correctly (via function params), but there's NO error handling on `Write()`. Failed sends are silently dropped.

---

## 5. Store Immutability Contract
`config-server/src/store/store.go` Get() returns a pointer to shared data:
```go
func (s *Store) Get() ConfigMap {
    val := s.config.Load()
    return *val // SHARED reference
}
```
The comment says "SHOULD NOT be modified", but there's no enforcement. `GetSection()` returns a proper copy, but `Get()` does not.

---

## 6. Python `ILogger` vs Go `Logger`
The Go ecosystem uses idiomatic naming (`Logger`), but the Python toolbox uses `ILogger`:
```python
from ..utils.logger import ILogger, ensure_safe_logger
```
This is the ONLY place where the `I`-prefix convention from the Obsidian brain rules is actually followed.

---

## 7. Config Profile Detection
The "dev mode" check is hardcoded identically in all three languages:
```go
isDev := (profile == "standalone" || profile == "test")   // Go
let is_dev = profile == "standalone" || profile == "test"  // Rust
is_dev = profile in ["standalone", "test"]                 // Python
```
**Gotcha**: The profiles `"production"` and `"preprod"` are NOT dev mode but are never explicitly checked — they fall through to the `else` branch.

---

## 8. CGO Bridge Isolation
`universal-logger` exposes a CGO shared library (`libunilog.dll`) but the language wrappers (C++, Python, Rust, VBA) do NOT call the Go functions directly. They go through:
```
Language Wrapper → libunilog.dll (CGO) → Go Core
```
**Hidden Rule**: The Go function signature can change without breaking wrappers, as long as the CGO bridge (`src/cgo_bridge/initialize.go`) remains stable.

---

## 9. Domain-Specific Log Levels
The flexible-logger defines **custom domain log levels** beyond the standard set:
```
LevelNotSet → LevelDebug → LevelStream → LevelInfo →
LevelLogon → LevelLogout → LevelTrade → LevelSchedule →
LevelReport → LevelWarning → LevelError → LevelCritical
```
**Hidden Pattern**: `Stream`, `Logon`, `Logout`, `Trade`, `Schedule`, `Report` are trading/finance domain levels. This reveals the ecosystem's target domain: **financial services / market data**.

---

## 10. Protobuf Command Enum Pattern
`distributed-config/src/schemas/` defines commands via Protobuf enums:
```
ConfigMsg_GET_SYNC
ConfigMsg_PUT_SYNC
ConfigMsg_ACK
ConfigMsg_ERROR
ConfigMsg_BROADCAST_SYNC
ConfigMsg_BROADCAST_REGISTRY
```
**Pattern**: All commands follow `{Message}_{VERB}_{NOUN}` naming.

---

## 11. File Config Naming Convention
Config files always follow `{profile}.yaml`:
- `standalone.yaml` (local dev)
- `config_preprod.yaml` (pre-production)
- `config_test.yaml` (testing)

**Gotcha**: The naming is NOT fully consistent — some use `config_` prefix (`config_preprod.yaml`) and others don't (`standalone.yaml`).
