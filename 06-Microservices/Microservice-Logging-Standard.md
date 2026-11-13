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

- **Unified Interface (`Logger`)**: Every microservice logs through the ecosystem `Logger` contract (`Debug`, `Info`, `Warning`, `Error`, `Critical`).
- **Standardized Identity**: Every service identifies itself using its canonical name initialized via `microservice-toolbox`.
- **Mission Traceability**: All logs propagate an `X-Bastien-Mission-ID` (Trace ID) across service boundaries (HTTP headers, gRPC metadata, NATS message headers).
- **Zero Secrets in Logs**: NEVER log PII, tokens, or raw credentials. All sensitive configuration parameters must use the `ENC(...)` pattern.
- **Graceful Failure**: Logging failures must fail gracefully to `os.Stderr` and never crash the host service. Never call `os.Exit()` inside log sinks.
- **Non-Blocking Network Sink**: Log streaming to `log-server` (Port 9020 via `safe-socket`) uses dedicated write goroutines/buffers to prevent blocking business logic.

---

## 2. Standard Log Levels & Domain Guidelines

> [!IMPORTANT] Canonical Source of Truth (`flexible-logger/src/models/level.go`)
> Only the 12 enum values in `flexible-logger/src/models/level.go` (`LevelNotSet = 0` plus active levels `1..11`) exist in the ecosystem (`universal-logger`, `log-server`, `microservice-toolbox`, and `watchdog-agent`). Aliases like `WARN`, `CRIT`, `TRACE`, `NOTICE`, `ALERT`, `EMERG`, `FATAL`, or `PANIC` do NOT exist.

| Level | Severity (`uint8`) | Usage Scope & Guidelines | Example |
| :--- | :---: | :--- | :--- |
| **DEBUG** | `1` | Detailed diagnostic data, raw payloads (sanitized), loop iterations. | `Evaluating ticker BTCUSDT depth ladder` |
| **STREAM** | `2` | High-frequency market data / continuous frame ingestion telemetry. | `Subscribed NATS tick stream BTCUSDT` |
| **INFO** | `3` | Milestones, successful operations, worker lifecycle events. | `Starting web-interface under profile: native` |
| **LOGON** | `4` | Session authentication / exchange or client handshake establishment. | `Authenticated WebSocket session user=admin` |
| **LOGOUT** | `5` | Clean session termination / teardown milestones. | `Closed FIX session on operator request` |
| **TRADE** | `6` | Order lifecycle, execution fills, strategy signal transitions. | `Filled limit order BUY 1.5 BTC @ 64500` |
| **SCHEDULE** | `7` | Scheduled task triggers, periodic batch jobs, cron ticks. | `Triggered daily TimescaleDB retention sweep` |
| **REPORT** | `8` | Analytical summaries, compliance reports, telemetry digests. | `Published end-of-day PnL ledger digest` |
| **WARNING** | `9` | Retries, transient reconnects, CSRF token rejections, non-fatal auth failures. | `Retrying upstream MFE registration (attempt 2/5)` |
| **ERROR** | `10` | Recoverable faults, DB connection drops, query failures, external API timeouts (`shipper` persisted). | `Database query execution failed: %v` |
| **CRITICAL** | `11` | Fatal failures, inability to bind configured network port, unrecoverable state corruption (`shipper` persisted). | `Failed to bind TCP listener on configured address %s: %v` |

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
				time.Now().UTC().Format("02/Jan/2006:15:04:05 -0700"),
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
