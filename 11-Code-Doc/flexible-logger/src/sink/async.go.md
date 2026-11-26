---
microservice: flexible-logger
type: note
status: active
tags:
- '#service/flexible-logger'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `flexible-logger/src/sink/async.go`.

> **Essential Process**:
> Asynchronous channel-buffered sink decoupling caller execution from underlying I/O latency.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/flexible-logger/src/error_handler/fallback_logger.go.md|ReportInternalError]] (function: calls) — *It formats the error as a LogEntry to maintain consistency.*
- [[flexible-logger/flexible-logger/src/error_handler/fallback_logger.go.md|fallback_logger.go]] (imports)
- [[flexible-logger/flexible-logger/src/interfaces/sink.go.md|sink.go]] (imports)
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Release]] (method: calls) — *Release decrements the reference count and returns the entry to the pool if 0.*
- [[flexible-logger/flexible-logger/src/models/entry.go.md|LogEntry.Retain]] (method: calls) — *Must be called when passing the entry to an additional async consumer.*
- [[flexible-logger/flexible-logger/src/models/level.go.md|Level.String]] (method: calls)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.Close]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.DroppedCount]] (method: defines_method) — *DroppedCount returns the total number of log entries dropped due to buffer saturation.*
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.SetDrainTimeout]] (method: defines_method) — *SetDrainTimeout overrides the maximum duration Close() will wait for the buffer to drain.*
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.SetDropAlertInterval]] (method: defines_method) — *SetDropAlertInterval overrides the minimum duration between throttled buffer-drop alerts (default 60s).*
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.SetDropNotifier]] (method: defines_method) — *SetDropNotifier attaches a Notifier (e.g., RemoteNotifier / Telegram) to receive throttled buffer saturation alerts.*
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.SetOnDropAlert]] (method: defines_method) — *SetOnDropAlert registers an optional callback invoked at most once per dropAlertInterval when logs are dropped.*
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.SetOnError]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.Write]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.maybeTriggerDropAlert]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.worker]] (method: defines_method)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|mockDropNotifier.Notify]] (method: calls)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|sink_test.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/src/profiles/cloud_native.go.md|cloud_native.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/high_perf.go.md|high_perf.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/minimal.go.md|minimal.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|no_lock.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/notif_logger.go.md|notif_logger.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/standard.go.md|standard.go]] (calls)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.Close]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.DroppedCount]] (method: belongs_to) — *DroppedCount returns the total number of log entries dropped due to buffer saturation.*
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.SetDrainTimeout]] (method: belongs_to) — *SetDrainTimeout overrides the maximum duration Close() will wait for the buffer to drain.*
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.SetDropAlertInterval]] (method: belongs_to) — *SetDropAlertInterval overrides the minimum duration between throttled buffer-drop alerts (default 60s).*
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.SetDropNotifier]] (method: belongs_to) — *SetDropNotifier attaches a Notifier (e.g., RemoteNotifier / Telegram) to receive throttled buffer saturation alerts.*
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.SetOnDropAlert]] (method: belongs_to) — *SetOnDropAlert registers an optional callback invoked at most once per dropAlertInterval when logs are dropped.*
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.SetOnError]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.Write]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.maybeTriggerDropAlert]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink.worker]] (method: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink]] (struct: belongs_to) — *AsyncSink wraps another sink and writes asynchronously using a buffered channel.*
- [[flexible-logger/flexible-logger/src/sink/async.go.md|AsyncSink]] (struct: defines_method) — *AsyncSink wraps another sink and writes asynchronously using a buffered channel.*
- [[flexible-logger/flexible-logger/src/sink/async.go.md|NewAsyncSink]] (function: belongs_to)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|sink_test.go]] (calls)
- [[flexible-logger/flexible-logger/src/sink/sink_test.go.md|sink_test.go]] (same_package)
<!-- SYNC:END -->
