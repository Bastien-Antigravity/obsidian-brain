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

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[flexible-logger/flexible-logger/src/engine/log_engine_test.go.md|log_engine_test.go]] (imports)
- [[flexible-logger/flexible-logger/src/error_handler/fallback_logger.go.md|ReportInternalError]] (function: calls) — *It formats the error as a LogEntry to maintain consistency.*
- [[flexible-logger/flexible-logger/src/error_handler/fallback_logger.go.md|fallback_logger.go]] (imports)
- [[flexible-logger/flexible-logger/src/factory/logger_factory.go.md|CreateLogEngine]] (function: calls) — *CreateLogEngine creates a new fully configured LogEngine instance.*
- [[flexible-logger/flexible-logger/src/factory/logger_factory.go.md|logger_factory.go]] (imports)
- [[flexible-logger/flexible-logger/src/helpers/paths.go.md|GetLogPath]] (function: calls) — *If name is empty, it falls back to the executable name.*
- [[flexible-logger/flexible-logger/src/helpers/paths.go.md|paths.go]] (imports)
- [[flexible-logger/flexible-logger/src/interfaces/sink.go.md|sink.go]] (imports)
- [[flexible-logger/flexible-logger/src/models/notif_message.go.md|notif_message.go]] (imports)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|NewLocalNotifier]] (function: calls)
- [[flexible-logger/flexible-logger/src/notifier/local_notifier.go.md|local_notifier.go]] (imports)
- [[flexible-logger/flexible-logger/src/notifier/remote_notifier.go.md|NewRemoteNotifier]] (function: calls)
- [[flexible-logger/flexible-logger/src/serializers/capn_serializer.go.md|NewCapnpSerializer]] (function: calls)
- [[flexible-logger/flexible-logger/src/serializers/text_serializer.go.md|NewTextSerializer]] (function: calls)
- [[flexible-logger/flexible-logger/src/serializers/text_serializer.go.md|text_serializer.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/async.go.md|NewAsyncSink]] (function: calls)
- [[flexible-logger/flexible-logger/src/sink/console.go.md|NewConsoleSink]] (function: calls)
- [[flexible-logger/flexible-logger/src/sink/console.go.md|console.go]] (imports)
- [[flexible-logger/flexible-logger/src/sink/multi.go.md|NewMultiSink]] (function: calls)
- [[flexible-logger/flexible-logger/src/sink/writer.go.md|NewWriterSink]] (function: calls)

### 🔌 Consumers (Inbound)
- [[flexible-logger/flexible-logger/cmd/test-log-server/connection_test.go.md|connection_test.go]] (calls)
- [[flexible-logger/flexible-logger/cmd/test-log-server/main.go.md|main.go]] (calls)
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|NewNoLockLogger]] (function: belongs_to) — *- Notif (Async)*
- [[flexible-logger/flexible-logger/src/profiles/no_lock.go.md|ServerCap]] (struct: belongs_to)
<!-- SYNC:END -->
