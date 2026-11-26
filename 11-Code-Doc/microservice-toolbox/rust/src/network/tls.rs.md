---
source: microservice-toolbox/rust/src/network/tls.rs
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-11-23 20:26:01.904041
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: tls.rs

## 📝 Description
Automatically generated mirror for `microservice-toolbox/rust/src/network/tls.rs`.

> **Essential Process**:
> Provides reusable X.509 TLS/mTLS client configuration builders and local/remote policy helpers for tonic gRPC endpoints.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/rust/src/config/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/rust/src/network/tls.rs.md|TempTlsDir.drop]] (method: defines_method)
- [[microservice-toolbox/rust/src/network/tls.rs.md|TempTlsDir.new]] (method: defines_method)
- [[microservice-toolbox/rust/src/network/tls.rs.md|TempTlsDir.path]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/rust/src/network/mod.rs.md|mod.rs]] (imports)
- [[microservice-toolbox/rust/src/network/tls.rs.md|TempTlsDir.drop]] (method: belongs_to)
- [[microservice-toolbox/rust/src/network/tls.rs.md|TempTlsDir.new]] (method: belongs_to)
- [[microservice-toolbox/rust/src/network/tls.rs.md|TempTlsDir.path]] (method: belongs_to)
- [[microservice-toolbox/rust/src/network/tls.rs.md|TempTlsDir]] (struct: belongs_to)
- [[microservice-toolbox/rust/src/network/tls.rs.md|TempTlsDir]] (struct: defines_method)
- [[microservice-toolbox/rust/src/network/tls.rs.md|build_client_endpoint]] (function: belongs_to) — *Builds a tonic transport Endpoint with TLS/mTLS or plaintext according to target locality and policy.*
- [[microservice-toolbox/rust/src/network/tls.rs.md|build_client_tls_config]] (function: belongs_to) — *Loads and validates X.509 client TLS/mTLS credentials on the cold path.*
- [[microservice-toolbox/rust/src/network/tls.rs.md|extract_host]] (function: belongs_to) — *Extracts the bare host portion from an optional host:port or [ipv6]:port target string.*
- [[microservice-toolbox/rust/src/network/tls.rs.md|generate_test_certs]] (function: belongs_to)
- [[microservice-toolbox/rust/src/network/tls.rs.md|is_local_address]] (function: belongs_to) — *Reports whether host represents a loopback or localhost address.*
- [[microservice-toolbox/rust/src/network/tls.rs.md|normalize_tls_mode]] (function: belongs_to) — *Canonicalizes a TLS policy mode string, defaulting empty values to "auto".*
- [[microservice-toolbox/rust/src/network/tls.rs.md|should_use_client_tls]] (function: belongs_to) — *Determines whether a client connection to target_ip should use TLS under the active policy.*
- [[microservice-toolbox/rust/src/network/tls.rs.md|test_build_client_endpoint_schemes]] (function: belongs_to)
- [[microservice-toolbox/rust/src/network/tls.rs.md|test_build_client_tls_config_validation_and_certs]] (function: belongs_to)
- [[microservice-toolbox/rust/src/network/tls.rs.md|test_is_local_address]] (function: belongs_to)
- [[microservice-toolbox/rust/src/network/tls.rs.md|test_normalize_tls_mode]] (function: belongs_to)
- [[microservice-toolbox/rust/src/network/tls.rs.md|test_should_use_client_tls]] (function: belongs_to)
- [[microservice-toolbox/rust/src/teleremote/client.rs.md|client.rs]] (calls)
- [[microservice-toolbox/rust/src/teleremote/client.rs.md|client.rs]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
