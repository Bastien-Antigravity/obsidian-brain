---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
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
- [[distributed-config/distributed-config/src/secret/crypto.go.md|crypto.go]] (same_package)
- [[distributed-config/distributed-config/src/utils/logger.go.md|noOpLogger.Error]] (method: calls)

### 🔌 Consumers (Inbound)
- [[distributed-config/distributed-config/src/secret/crypto_test.go.md|TestEncryptionRoundTrip]] (function: belongs_to)
- [[distributed-config/distributed-config/src/secret/crypto_test.go.md|TestProcessConfigSecrets]] (function: belongs_to)
<!-- SYNC:END -->
