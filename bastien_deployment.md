# Deployment Standards: Docker & Infrastructure

## Deployment Architecture
The platform runs as a set of Docker containers orchestrated by `docker-compose`. Each service has its own `Dockerfile` and `docker-compose.yml` for local development, while `docker-deployment/docker-compose.yaml` defines the production stack.

### 1. Infrastructure Services
| Service | Image | Default Port | Purpose |
|---|---|---|---|
| `timescale-db` | `timescale/timescaledb-ha:pg18` | 5432 | TimescaleDB (PostgreSQL) for time-series storage |
| `nats-server` | `nats:2.12.6-alpine3.22` | 4222 (client), 8222 (monitoring) | NATS messaging bus |
| `watchtower` | `containrrr/watchtower` | — | Auto-update containers from GitHub Container Registry |

### 2. Application Services
| Service | Image | Default Port | gRPC Port |
|---|---|---|---|
| `tele-remote` | `ghcr.io/bastien-antigravity/tele-remote` | 1863 | 1864 |
| `log-server` | `ghcr.io/bastien-antigravity/log-server` | 9020 | 9021 |
| `config-server` | `ghcr.io/bastien-antigravity/config-server` | 1862 | — |
| `notif-server` | `ghcr.io/bastien-antigravity/notif-server` | — | — |
| `web-interface` | `ghcr.io/bastien-antigravity/web-interface` | 8080 | — |

### 3. Container Networking
- Services communicate through **Docker's internal DNS resolver** (e.g., `postgresql://timescale-db:5432`).
- The `Docker Guard` in `microservice-toolbox` ensures CLI network overrides are ignored inside containers, preserving container-to-container DNS resolution.
- External access is mapped via `${SERVICE_IP}:${HOST_PORT}:${CONTAINER_PORT}`.

### 4. Environment Variables
Production secrets and configuration are injected via environment variables:
- `DB_NAME`, `DB_PORT`, `DB_USER`, `DB_PASSWORD` — Database credentials.
- `NATS_IP`, `NATS_PORT` — NATS connectivity.
- `TB_IP`, `TB_PORT` — Tele-remote binding.
- `ENV_PROD` — Production environment flag.
- `TAG` — Docker image tag (default: `latest`).

### 5. Health Checks
- **TimescaleDB**: Uses `pg_isready` to verify database readiness.
- **NATS**: Monitors the HTTP monitoring endpoint on port 8222.
- **Application Services**: Implement `grpc_health_v1` for gRPC health checks with `SERVING` status.

### 6. Build Requirements
- **Go**: Binary at `/usr/local/bin/go`. Run `go mod tidy` before building.
- **Rust**: Requires `protoc` at `/usr/local/bin/protoc`. Set `PROTOC=/usr/local/bin/protoc` for builds.
- **Python**: Use `pip install -r requirements.txt`.

### 7. CI/CD
- Container images are published to **GitHub Container Registry** (`ghcr.io/bastien-antigravity/`).
- Watchtower polls for new images every 300 seconds and auto-updates labeled containers.
- Database containers (`timescale-db`) are excluded from auto-update via label opt-out.

### 8. Testing
- **testing-sandbox**: Contains integration test scenarios and a resilience test harness (`run_resilience_test.sh`).
- **Orchestrator**: The `testing-sandbox/orchestrator/` directory contains Go-based test orchestration tooling.
