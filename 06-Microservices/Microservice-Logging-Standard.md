---
title: Microservice Logging Standard
type: protocol
status: active
microservice: ecosystem-wide
tags:
- '#service/ecosystem-wide'
- '#type/protocol'
- '#domain/observability'
- '#state/active'
- '#zone/3-fleet'
- '#ai/ignore'
---

# 📜 Microservice Logging Standard

This protocol defines the standardized logging behavior, interface contracts, initialization rituals, and log-level guidelines for all microservices across the Bastien-Antigravity ecosystem.

---

## 1. Core Principles

- **Unified Interface (`ILogger`)**: Every microservice logs through the ecosystem `ILogger` contract (`Debug`, `Info`, `Warning`, `Error`, `Critical`).
- **Standardized Identity**: Every service identifies itself using its canonical name initialized via `microservice-toolbox`.
- **Mission Traceability**: All logs propagate an `X-Bastien-Mission-ID` (Trace ID) across service boundaries (HTTP headers, gRPC metadata, NATS message headers).
- **Zero Secrets in Logs**: NEVER log PII, tokens, or raw credentials. All sensitive configuration parameters must use the `ENC(...)` pattern.
- **Graceful Failure**: Logging failures must fail gracefully to `os.Stderr` and never crash the host service. Never call `os.Exit()` inside log sinks.
- **Non-Blocking Network Sink**: Log streaming to `log-server` (Port 9020 via `safe-socket`) uses dedicated write goroutines/buffers to prevent blocking business logic.

---

## 2. Standard Log Levels & Domain Guidelines

| Level | Severity | Usage Scope & Guidelines | Example |
| :--- | :---: | :--- | :--- |
| **DEBUG** | 1 | Detailed diagnostic data, raw payloads (sanitized), loop iterations. | `Evaluating ticker BTCUSDT depth ladder` |
| **INFO** | 2 | Milestones, successful operations, worker lifecycle events. | `Starting web-interface under profile: native` |
| **WARNING** | 3 | Retries, fallback address resolutions, CSRF token rejections, auth failures. | `Falling back to default listen address 127.0.0.1:5000` |
| **ERROR** | 4 | Recoverable faults, DB connection drops, query failures, external API timeouts. | `Database query execution failed: %v` |
| **CRITICAL**| 5 | Fatal failures, inability to bind network port, unrecoverable state corruption. | `Failed to bind TCP listener on port 5000: %v` |

---

## 3. Polyglot Service Bootstrap Ritual

All microservices MUST initialize logging through the unified `microservice-toolbox` facade:

### 🐹 Go
```go
package main

import (
	toolbox_bootstrap "github.com/Bastien-Antigravity/microservice-toolbox/go/pkg/bootstrap"
)

func main() {
	// Single-call bootstrapper: loads layered configuration & configures universal-logger sinks
	appConfig, appLogger := toolbox_bootstrap.BootstrapService("my-service")
	defer appLogger.Close()

	appLogger.Info("Service initialized under profile: %s", appConfig.Profile)
}
```

### 🐍 Python
```python
from microservice_toolbox.config.loader import load_config
from microservice_toolbox.logger import UniLog

config = load_config("standalone")
logger = UniLog(app_name="my-service", config_profile="standalone")

logger.info("Service initialized successfully.")
```

### 🦀 Rust
```rust
use microservice_toolbox::config::load_config;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let app_config = load_config("standalone")?;
    // logger initialized via universal-logger Rust crate
    Ok(())
}
```

---

## 4. HTTP Request Logging Middleware (Standard Format)

Every HTTP-based microservice (e.g. `web-interface`, `notif-server`, REST gateways) MUST implement a request logging middleware outputting requests in the standardized Nginx/Gunicorn format:

```text
{remote_addr} - - [{timestamp}] "{method} {path} {proto}" {user_agent} {duration}
```

### Go Implementation Example (`src/middleware/middleware.go`):
```go
func LoggerMiddleware(logger unilog_interfaces.Logger) func(http.Handler) http.Handler {
	return func(next http.Handler) http.Handler {
		return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			start := time.Now()
			sw := &statusWriter{ResponseWriter: w, statusCode: http.StatusOK}

			next.ServeHTTP(sw, r)

			duration := time.Since(start)
			logger.Info("%s - - [%s] \"%s %s %s\" \"%s\" %v (status: %d)",
				r.RemoteAddr,
				time.Now().Format("02/Jan/2006:15:04:05 -0700"),
				r.Method,
				r.URL.Path,
				r.Proto,
				r.UserAgent(),
				duration,
				sw.statusCode,
			)
		})
	}
}
```

---

## 5. Security & Sensitive Data Guardrails

1. **No PII**: User identities, cookies, auth headers, and IP addresses (beyond network logs) must be stripped.
2. **CSRF & Security Violations**: Logged at `WARNING` level with remote IP to detect brute-force or malicious probes.
3. **Database Errors**: Connection failures and query execution errors MUST be logged at `ERROR` level without leaking plaintext passwords in connection strings.
4. **Fatal Shutdown**: If port resolution or server binding fails during startup, emit a `CRITICAL` log before invoking lifecycle termination.

---
*Back-links: [[Web-Interface-Hub]], [[Universal-Logger-Hub]], [[Log-Server-Hub]], [[03-Repository-Structure]]*
