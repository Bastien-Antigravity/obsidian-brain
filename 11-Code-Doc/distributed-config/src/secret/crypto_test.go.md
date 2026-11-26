---
microservice: distributed-config
type: note
status: active
tags:
- '#service/distributed-config'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `distributed-config/src/secret/crypto_test.go`.

> **Essential Process**:
> Unit test suite verifying RSA keypair generation, token encryption, and round-trip ciphertext decryption using temporary test keys and env overrides.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[distributed-config/distributed-config/src/secret/crypto.go.md|Decrypt]] (function: calls)
- [[distributed-config/distributed-config/src/secret/crypto.go.md|Encrypt]] (function: calls)
- [[distributed-config/distributed-config/src/secret/crypto.go.md|ProcessConfigSecrets]] (function: calls)
- [[distributed-config/distributed-config/src/secret/crypto.go.md|ResetKeyCache]] (function: calls) — *ResetKeyCache clears the in-memory memoized RSA private key.*
- [[distributed-config/distributed-config/src/secret/crypto.go.md|crypto.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/secret/crypto_test.go.md|TestEncryptionRoundTrip]] (function: belongs_to)
- [[distributed-config/distributed-config/src/secret/crypto_test.go.md|TestPrivateKeyLookupPrecedence]] (function: belongs_to)
- [[distributed-config/distributed-config/src/secret/crypto_test.go.md|TestProcessConfigSecrets]] (function: belongs_to)
- [[distributed-config/distributed-config/src/secret/crypto_test.go.md|TestProcessConfigSecrets_FailFastAndCaching]] (function: belongs_to)
- [[distributed-config/distributed-config/src/secret/crypto_test.go.md|isolateSystemPrivateKey]] (function: belongs_to)
<!-- SYNC:END -->
