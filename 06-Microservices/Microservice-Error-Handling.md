

---
type: protocol
status: active
microservice: ecosystem-wide
tags:
- '#type/protocol'
- '#state/active'
---

# ⚠️ Microservice Error Handling Protocol

This protocol ensures that failures are handled and propagated consistently across Go, Rust, Python, and C++ microservices.

## 1. Unified Error Codes
We align all ecosystem errors with standard **gRPC Status Codes**. Even when using REST or internal logic, use these semantic mappings:

| Code | Meaning | Usage |
| :--- | :--- | :--- |
| `OK` (0) | Success | Operation completed. |
| `INVALID_ARGUMENT` (3) | Client Error | Bad input, missing fields. |
| `NOT_FOUND` (5) | Missing Resource | Entity does not exist. |
| `ALREADY_EXISTS` (6) | Conflict | Duplicate entry. |
| `INTERNAL` (13) | System Failure | Database down, panic, bug. |
| `UNAVAILABLE` (14) | Overloaded | Service temporary down (retryable). |

## 2. Language-Specific Implementation

### 🐹 Go
Always wrap errors with context to provide a stack-trace-like path:
```go
if err != nil {
    return fmt.Errorf("failed to fetch user: %w", err)
}
```

### 🦀 Rust
Use the `anyhow` or `thiserror` crate for structured errors. Never `panic!` in production unless the error is truly unrecoverable.

### 🐍 Python
Use custom exception classes that include an `error_code` attribute matching the gRPC standard.

## 3. The "Silent Failure" Prohibition
Every error MUST be logged via the `universal-logger` at the appropriate level:
*   **WARNING**: Recoverable issues (e.g., retrying a connection).
*   **ERROR**: Failed operations that don't crash the service.
*   **CRITICAL**: Service-wide failures (e.g., failed to load config).

## 4. Propagation Rule
When a microservice (A) calls microservice (B), any error from (B) must be caught by (A) and translated into a local error context before being returned to the user or upper layer.

---
*Last Updated: 2026-05-09*
*See also: [[Microservice-Startup-Protocol]]*
