---
source: notif-server/src/sanitizer/sanitizer_test.go
workspace: notif-server
type: code-mirror
status: auto-generated
last_sync: 2026-11-18 03:39:57.321232
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: sanitizer_test.go

## 📝 Description
Automatically generated mirror for `notif-server/src/sanitizer/sanitizer_test.go`.

> **Essential Process**:
> Unit tests verifying the deny-by-default config exposure allowlist, header/filename sanitization, and exhaustive secret redaction across URLs, tokens, headers, and ENC(...) blobs.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[notif-server/src/sanitizer/sanitizer.go.md|IsPublicField]] (function: calls) — *Uses a deny-by-default allowlist: any unknown field, ENC(...) value, or embedded secret URL returns false.*
- [[notif-server/src/sanitizer/sanitizer.go.md|RedactSecrets]] (function: calls) — *from error strings and telemetry messages.*
- [[notif-server/src/sanitizer/sanitizer.go.md|SanitizeFilename]] (function: calls) — *quotes, backslashes, and MIME parameter delimiters.*
- [[notif-server/src/sanitizer/sanitizer.go.md|SanitizeHeader]] (function: calls) — *and Unicode line/paragraph separators to prevent MIME/HTTP header injection.*
- [[notif-server/src/sanitizer/sanitizer.go.md|sanitizer.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[notif-server/src/sanitizer/sanitizer_test.go.md|TestIsPublicFieldDenyByDefault]] (function: belongs_to)
- [[notif-server/src/sanitizer/sanitizer_test.go.md|TestRedactSecretsExhaustive]] (function: belongs_to)
- [[notif-server/src/sanitizer/sanitizer_test.go.md|TestSanitizeHeaderAndFilename]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
