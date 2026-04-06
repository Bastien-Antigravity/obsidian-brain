# Configuration Standards: YAML & Profiles

## Configuration Philosophy
Our microservices avoid hardcoded parameters in the source code. All flexible settings are sourced from nested YAML structs.

### 1. Nested YAML Structure
- **Location**: Store all core configuration fields in `src/config/config.go`.
- **Naming**: Map YAML fields (e.g., `grpc_host`) to Go struct tags (e.g., `` `yaml:"grpc_host"` ``).
- **Default Profile**: `config/default.yaml` must always exist and be loaded at startup.

### 2. Environment Variables & Overrides
- **Distributed Config**: For dynamic updates, use `distributed-config` library.
- **Prefixes**: Use environment variable prefixes (e.g., `TR_`, `TS_`, `LS_`, `NT_`, `WB_`) to provide overrides for keys as required.
- **Precedence**: Config file -> Environment variables -> Defaults.

### 3. Service Metadata
- **Name**: Always include a `name` field in the configuration for service identification.
- **Version**: Versioning is handled via the gRPC control protocol and the config struct.

### 4. Shared Libraries
- Use `github.com/Bastien-Antigravity/distributed-config` for unified configuration management across all Go projects.
- The `New(profile string)` function is the primary entry point for distributed configuration.
