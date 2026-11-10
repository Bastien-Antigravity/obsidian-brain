---
source: watchdog-agent/src/shipper/parser.go
workspace: watchdog-agent
type: code-mirror
status: auto-generated
last_sync: 2026-11-08T15:50:14.847705
---

# Mirror: parser.go

## 📝 Description
Automatically generated mirror for `watchdog-agent/src/shipper/parser.go`.

> **Essential Process**:
> High-performance parser for fleet standardized 8-column log text lines. Identifies and extracts operational failures (level >= ERROR) into structured telemetry models for TimescaleDB ingestion.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[watchdog-agent/watchdog-agent/src/shipper/parser.go.md|ParseLogLine]] (function: belongs_to) — *ParseLogLine attempts to parse a standardized log line. Returns (log, true) if level >= ERROR.*
- [[watchdog-agent/watchdog-agent/src/shipper/parser.go.md|ParsedErrorLog]] (struct: belongs_to) — *ParsedErrorLog represents a structured error event ready for TimescaleDB storage.*
- [[watchdog-agent/watchdog-agent/src/shipper/parser_test.go.md|parser_test.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/parser_test.go.md|parser_test.go]] (same_package)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|shipper.go]] (calls)
- [[watchdog-agent/watchdog-agent/src/shipper/shipper.go.md|shipper.go]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
