---
source: watchdog-agent/src/shipper/parser_test.go
workspace: watchdog-agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-08T15:50:25.313827
---

# Mirror: parser_test.go

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/shipper/parser_test.go`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[watchdog-agent/watchdog-agent/src/rest/rest_handler_test.go.md|mockWatchdogLogger.Error]] (method: calls)
- [[watchdog-agent/watchdog-agent/src/shipper/parser.go.md|ParseLogLine]] (function: calls) — *ParseLogLine attempts to parse a standardized log line. Returns (log, true) if level >= ERROR.*
- [[watchdog-agent/watchdog-agent/src/shipper/parser.go.md|parser.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/src/shipper/parser_test.go.md|TestParseLogLine_CriticalSeverity]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/parser_test.go.md|TestParseLogLine_FallbackRegex]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/parser_test.go.md|TestParseLogLine_FixedFormat]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/parser_test.go.md|TestParseLogLine_IgnoreInfoAndWarning]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/parser_test.go.md|TestParseLogLine_InvalidTimestampFallback]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/parser_test.go.md|TestParseLogLine_ShortLineWithKeyword]] (function: belongs_to)
- [[watchdog-agent/watchdog-agent/src/shipper/parser_test.go.md|TestParseLogLine_StackTraceMetadata]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
