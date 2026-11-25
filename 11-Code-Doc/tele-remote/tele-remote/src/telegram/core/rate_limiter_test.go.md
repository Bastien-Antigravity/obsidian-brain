---
source: tele-remote/src/telegram/core/rate_limiter_test.go
workspace: tele-remote
type: code-mirror
status: auto-generated
last_sync: 2026-11-23 01:29:29.521744
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: rate_limiter_test.go

## 📝 Description
Automatically generated mirror for `tele-remote/src/telegram/core/rate_limiter_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|NewRateLimiter]] (function: calls) — *NewRateLimiter instantiates a sliding-window rate limiter with sensible defaults.*
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|RateLimiter.Allow]] (method: calls) — *and (allowed=false, sendWarning=false) for subsequent floods within cooldown.*
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|rate_limiter.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter_test.go.md|TestRateLimiter_BurstAllowedThenThrottled]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter_test.go.md|TestRateLimiter_IndependentConversations]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter_test.go.md|TestRateLimiter_MaxTrackedClientsEviction]] (function: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter_test.go.md|TestRateLimiter_NilSafe]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
