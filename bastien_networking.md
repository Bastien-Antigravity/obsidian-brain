# Networking & Communications: gRPC, NATS, WebSockets

## Networking Stack
Our microservices communicate through three primary channels: gRPC for control, NATS for async messaging, and WebSockets for metrics.

### 1. gRPC Control Service
- **Role**: Every microservice exposes a native `ProcessController` proto service for management.
- **Methods**: Must support `Start()`, `Stop()`, and `Restart()`.
- **Location**: `src/grpc_control/` with proto definitions and service implementation.
- **Separation**: Decouple the gRPC socket server scaffolding (`grpc_service.go`) from the underlying execution definitions (`grpc_control.go`).

### 2. NATS Asynchronous Bus
- **Role**: Use NATS as the primary asynchronous ingestion bus for high-throughput data streams.
- **Pattern**: Pub/Sub for market data and events.
- **Handling**: Use asynchronous subscribers to avoid blocking the network thread.

### 3. Metric WebSockets (WSPublisher)
- **Role**: Outbound metrics (performance, health status, real-time data) are streamed via non-blocking concurrent Websocket publishers.
- **Implementation**: `WSPublisher` is a standard component found in most microservices.
- **Performance**: Metrics must be buffered and sent asynchronously to avoid performance hits on the main processing engine.

### 4. Health & Status
- **Standard**: Always implement `grpc_health_v1` for service health checks.
- **Status Reporting**: Report serving status as `SERVING` only when all internal sub-processes (ingestor, analysis engine) are successfully initialized.
