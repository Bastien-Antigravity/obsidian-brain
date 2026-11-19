---
source: notif-server/src/sanitizer/sanitizer.go
workspace: notif-server
type: code-mirror
status: auto-generated
last_sync: 2026-11-18T03:39:57.316134
---

# Mirror: sanitizer.go

## 📝 Description
Automatically generated mirror for `notif-server/src/sanitizer/sanitizer.go`.

> **Essential Process**:
> Provides the standard, exhaustive security sanitization and secret-redaction library for notif-server. Enforces deny-by-default config exposure for web-interface, strips injection characters from headers and filenames, and scrubs credentials from logs and error telemetry.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[notif-server/notif-server/src/grpc_control/service.go.md|service.go]] (calls)
- [[notif-server/notif-server/src/grpc_control/service.go.md|service.go]] (imports)
- [[notif-server/notif-server/src/notifiers/discord.go.md|discord.go]] (calls)
- [[notif-server/notif-server/src/notifiers/discord.go.md|discord.go]] (imports)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|gmail.go]] (calls)
- [[notif-server/notif-server/src/notifiers/gmail.go.md|gmail.go]] (imports)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|matrix.go]] (calls)
- [[notif-server/notif-server/src/notifiers/matrix.go.md|matrix.go]] (imports)
- [[notif-server/notif-server/src/notifiers/telegram.go.md|telegram.go]] (calls)
- [[notif-server/notif-server/src/notifiers/telegram.go.md|telegram.go]] (imports)
- [[notif-server/notif-server/src/sanitizer/sanitizer.go.md|IsPublicField]] (function: belongs_to) — *Uses a deny-by-default allowlist: any unknown field, ENC(...) value, or embedded secret URL returns false.*
- [[notif-server/notif-server/src/sanitizer/sanitizer.go.md|MaskedPlaceholder]] (constant: belongs_to) — *MaskedPlaceholder is the canonical placeholder returned to UIs for sensitive fields.*
- [[notif-server/notif-server/src/sanitizer/sanitizer.go.md|RedactSecrets]] (function: belongs_to) — *from error strings and telemetry messages.*
- [[notif-server/notif-server/src/sanitizer/sanitizer.go.md|SanitizeFilename]] (function: belongs_to) — *quotes, backslashes, and MIME parameter delimiters.*
- [[notif-server/notif-server/src/sanitizer/sanitizer.go.md|SanitizeHeader]] (function: belongs_to) — *and Unicode line/paragraph separators to prevent MIME/HTTP header injection.*
- [[notif-server/notif-server/src/sanitizer/sanitizer_test.go.md|sanitizer_test.go]] (calls)
- [[notif-server/notif-server/src/sanitizer/sanitizer_test.go.md|sanitizer_test.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
