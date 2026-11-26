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

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/src/engine/log_engine.go.md|LogEngine.Error]] (method: calls)
- [[flexible-logger/src/models/entry.go.md|LogEntry.Release]] (method: calls) — *Release decrements the reference count and returns the entry to the pool if 0.*
- [[flexible-logger/src/models/entry.go.md|LogEntry.Reset]] (method: calls) — *Reset clears the LogEntry for reuse.*
- [[flexible-logger/src/models/level.go.md|Level.String]] (method: calls)
- [[flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/src/sink/async.go.md|AsyncSink.DroppedCount]] (method: calls) — *DroppedCount returns the total number of log entries dropped due to buffer saturation.*
- [[flexible-logger/src/sink/async.go.md|AsyncSink.SetDrainTimeout]] (method: calls) — *SetDrainTimeout overrides the maximum duration Close() will wait for the buffer to drain.*
- [[flexible-logger/src/sink/async.go.md|AsyncSink.SetDropAlertInterval]] (method: calls) — *SetDropAlertInterval overrides the minimum duration between throttled buffer-drop alerts (default 60s).*
- [[flexible-logger/src/sink/async.go.md|AsyncSink.SetDropNotifier]] (method: calls) — *SetDropNotifier attaches a Notifier (e.g., RemoteNotifier / Telegram) to receive throttled buffer saturation alerts.*
- [[flexible-logger/src/sink/async.go.md|AsyncSink.SetOnDropAlert]] (method: calls) — *SetOnDropAlert registers an optional callback invoked at most once per dropAlertInterval when logs are dropped.*
- [[flexible-logger/src/sink/async.go.md|NewAsyncSink]] (function: calls)
- [[flexible-logger/src/sink/async.go.md|async.go]] (same_package)
- [[flexible-logger/src/sink/multi.go.md|NewMultiSink]] (function: calls)
- [[flexible-logger/src/sink/multi.go.md|multi.go]] (same_package)
- [[flexible-logger/src/sink/sink_test.go.md|MockSerializer.Serialize]] (method: defines_method)
- [[flexible-logger/src/sink/sink_test.go.md|MockSink.Close]] (method: defines_method)
- [[flexible-logger/src/sink/sink_test.go.md|MockSink.GetLastEntry]] (method: defines_method)
- [[flexible-logger/src/sink/sink_test.go.md|MockSink.GetWriteCount]] (method: defines_method)
- [[flexible-logger/src/sink/sink_test.go.md|MockSink.IsClosed]] (method: defines_method)
- [[flexible-logger/src/sink/sink_test.go.md|MockSink.Write]] (method: defines_method)
- [[flexible-logger/src/sink/sink_test.go.md|blockingMockSink.Close]] (method: defines_method)
- [[flexible-logger/src/sink/sink_test.go.md|blockingMockSink.Write]] (method: defines_method)
- [[flexible-logger/src/sink/sink_test.go.md|errorFailingSink.Close]] (method: defines_method)
- [[flexible-logger/src/sink/sink_test.go.md|errorFailingSink.Write]] (method: defines_method)
- [[flexible-logger/src/sink/sink_test.go.md|mockDropNotifier.Close]] (method: defines_method)
- [[flexible-logger/src/sink/sink_test.go.md|mockDropNotifier.Count]] (method: defines_method)
- [[flexible-logger/src/sink/sink_test.go.md|mockDropNotifier.Last]] (method: defines_method)
- [[flexible-logger/src/sink/sink_test.go.md|mockDropNotifier.Notify]] (method: defines_method)
- [[flexible-logger/src/sink/writer.go.md|NewWriterSink]] (function: calls)
- [[flexible-logger/src/sink/writer.go.md|writer.go]] (same_package)

### 🔌 Consumers (Inbound)
- [[flexible-logger/src/sink/async.go.md|async.go]] (calls)
- [[flexible-logger/src/sink/async.go.md|async.go]] (same_package)
- [[flexible-logger/src/sink/sink_test.go.md|MockSerializer.Serialize]] (method: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|MockSerializer]] (struct: belongs_to) — *MockSerializer for testing*
- [[flexible-logger/src/sink/sink_test.go.md|MockSerializer]] (struct: defines_method) — *MockSerializer for testing*
- [[flexible-logger/src/sink/sink_test.go.md|MockSink.Close]] (method: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|MockSink.GetLastEntry]] (method: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|MockSink.GetWriteCount]] (method: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|MockSink.IsClosed]] (method: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|MockSink.Write]] (method: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|MockSink]] (struct: belongs_to) — *MockSink for testing*
- [[flexible-logger/src/sink/sink_test.go.md|MockSink]] (struct: defines_method) — *MockSink for testing*
- [[flexible-logger/src/sink/sink_test.go.md|TestAsyncSink_BufferFull_DropsLog]] (function: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|TestAsyncSink_Close_DrainTimeout]] (function: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|TestAsyncSink_Close_DrainsAllEnqueuedEntries]] (function: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|TestAsyncSink_ThrottledDropAlert_PreventsTelegramStorm]] (function: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|TestAsyncSink_Write]] (function: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|TestMultiSink_ChildError_ContinuesAndReleases]] (function: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|TestMultiSink_Close_AllSinksClosed]] (function: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|TestMultiSink_MixedSyncAndAsync]] (function: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|TestMultiSink_OneSink]] (function: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|TestMultiSink_Write]] (function: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|TestMultiSink_ZeroSinks]] (function: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|TestWriterSink_Write]] (function: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|blockingMockSink.Close]] (method: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|blockingMockSink.Write]] (method: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|blockingMockSink]] (struct: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|blockingMockSink]] (struct: defines_method)
- [[flexible-logger/src/sink/sink_test.go.md|errorFailingSink.Close]] (method: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|errorFailingSink.Write]] (method: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|errorFailingSink]] (struct: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|errorFailingSink]] (struct: defines_method)
- [[flexible-logger/src/sink/sink_test.go.md|mockDropNotifier.Close]] (method: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|mockDropNotifier.Count]] (method: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|mockDropNotifier.Last]] (method: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|mockDropNotifier.Notify]] (method: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|mockDropNotifier]] (struct: belongs_to)
- [[flexible-logger/src/sink/sink_test.go.md|mockDropNotifier]] (struct: defines_method)
- [[flexible-logger/src/sink/writer.go.md|writer.go]] (calls)
- [[flexible-logger/src/sink/writer.go.md|writer.go]] (same_package)
<!-- SYNC:END -->
