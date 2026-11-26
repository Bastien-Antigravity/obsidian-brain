---
source: tele-remote/src/telegram/core/rate_limiter.go
workspace: tele-remote
type: code-mirror
status: auto-generated
last_sync: 2026-11-23 01:29:29.496165
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: rate_limiter.go

## 📝 Description
Automatically generated mirror for `tele-remote/src/telegram/core/rate_limiter.go`.

> **Essential Process**:
> Enforces sliding-window rate limiting and anti-flooding controls per Telegram ConversationKey to protect microservices and prevent Telegram API 429 Too Many Requests penalties.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|GetConvKey]] (function: calls) — *falling back to UserID: 0 when c.Sender() is nil.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|MaskChatID]] (function: calls) — *(e.g. "...3982") to prevent plaintext credential leakage in logs and telemetry.*
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|bot.go]] (same_package)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|MockLogger.Warning]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (same_package)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext.Callback]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|fakeContext.Send]] (method: calls)
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|Bot.RateLimitMiddleware]] (method: defines_method) — *RateLimitMiddleware drops rapid updates per ConversationKey before executing handlers.*
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|RateLimiter.Allow]] (method: defines_method) — *and (allowed=false, sendWarning=false) for subsequent floods within cooldown.*

### 🔌 Consumers (Inbound)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|bot.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/core/bot.go.md|bot.go]] (same_package)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/core/bot_test.go.md|bot_test.go]] (same_package)
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|Bot.RateLimitMiddleware]] (method: belongs_to) — *RateLimitMiddleware drops rapid updates per ConversationKey before executing handlers.*
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|Bot]] (struct: defines_method) — *RateLimitMiddleware drops rapid updates per ConversationKey before executing handlers.*
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|DefaultBurstLimit]] (constant: belongs_to) — *DefaultBurstLimit allows up to 60 requests per window for high-speed UI interaction.*
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|DefaultRateCooldown]] (constant: belongs_to) — *DefaultRateCooldown is the minimum interval between throttle warnings sent to the user.*
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|DefaultRateWindow]] (constant: belongs_to) — *DefaultRateWindow is the sliding window duration.*
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|MaxTrackedClients]] (constant: belongs_to) — *MaxTrackedClients caps the in-memory rate limiter client map to prevent unbounded growth.*
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|NewRateLimiter]] (function: belongs_to) — *NewRateLimiter instantiates a sliding-window rate limiter with sensible defaults.*
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|RateLimiter.Allow]] (method: belongs_to) — *and (allowed=false, sendWarning=false) for subsequent floods within cooldown.*
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|RateLimiter]] (struct: belongs_to) — *RateLimiter tracks recent activity per ConversationKey and enforces flood protection.*
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|RateLimiter]] (struct: defines_method) — *RateLimiter tracks recent activity per ConversationKey and enforces flood protection.*
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter.go.md|clientBucket]] (struct: belongs_to)
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter_test.go.md|rate_limiter_test.go]] (calls)
- [[tele-remote/tele-remote/src/telegram/core/rate_limiter_test.go.md|rate_limiter_test.go]] (same_package)
- [[tele-remote/tele-remote/src/telegram/routes/routes.go.md|routes.go]] (calls)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
