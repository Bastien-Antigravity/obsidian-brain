# Documentation Standards: Diagrams & Schemas

## Architectural Documentation
We maintain high-level topological records inside the `/doc` directory of every microservice.

### 1. ASCII Diagrams
- **Role**: Every repository must contain an architectural overview in ASCII format within the `/doc` directory (e.g., `doc/architecture.txt` or `ARCHITECTURE.md`).
- **Explanation**: This diagram must detail the Data Flow schemas and OHLCV Data Models whenever the architecture evolves.
- **Tools**: Use `monodraw` or standard text-based diagram tools for consistent layout.

### 2. Protocol Schemas
- **Cap'n Proto**: Fast serialization schemas are stored in the `/capnp` directory at the root.
- **Protobuf**: gRPC protocol definitions are stored in `src/grpc_control/` or `proto/`.
- **JSON**: Data models must always provide clear `json` tags for consistent REST/WebSocket serialization.

### 3. Change Logs & TODOs
- **File**: `todo` or `README.md` must be maintained at the root of the project to track in-progress features or issues.
- **Status Reporting**: All major architectural changes MUST be documented in the repository's `ARCHITECTURE.md` file.

### 4. Technical Walkthroughs
- Use **Walkthrough** documents for any major features or integrations that require manual verification.
- **Recordings**: Screenshots or recordings of the UI/Terminal behavior are encouraged for documentation.
