---
source: watchdog-agent/src/shipper/parser_test.go
workspace: watchdog-agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-08 15:50:25.313827
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: parser_test.go

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/shipper/parser_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/src/rest/rest_handler_test.go.md|mockWatchdogLogger.Error]] (method: calls)
- [[watchdog-agent/src/shipper/parser.go.md|ParseLogLine]] (function: calls) — *Returns (log, true) strictly for canonical ERROR (10) and CRITICAL (11) entries.*
- [[watchdog-agent/src/shipper/parser.go.md|parser.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/src/shipper/parser_test.go.md|TestParseLogLine_CloudJSONFormat]] (function: belongs_to)
- [[watchdog-agent/src/shipper/parser_test.go.md|TestParseLogLine_CriticalSeverity]] (function: belongs_to)
- [[watchdog-agent/src/shipper/parser_test.go.md|TestParseLogLine_FallbackRegex]] (function: belongs_to)
- [[watchdog-agent/src/shipper/parser_test.go.md|TestParseLogLine_FixedFormat]] (function: belongs_to)
- [[watchdog-agent/src/shipper/parser_test.go.md|TestParseLogLine_IgnoreInfoAndWarningAndMentionedError]] (function: belongs_to)
- [[watchdog-agent/src/shipper/parser_test.go.md|TestParseLogLine_RejectsInvalidTimestamp]] (function: belongs_to)
- [[watchdog-agent/src/shipper/parser_test.go.md|TestParseLogLine_SanitizesPoisonPillUTF8AndNUL]] (function: belongs_to)
- [[watchdog-agent/src/shipper/parser_test.go.md|TestParseLogLine_ShortLineWithKeyword]] (function: belongs_to)
- [[watchdog-agent/src/shipper/parser_test.go.md|TestParseLogLine_StackTraceMetadata]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
