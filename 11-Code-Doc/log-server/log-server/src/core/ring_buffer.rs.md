---
source: log-server/src/core/ring_buffer.rs
workspace: log-server
type: code-mirror
status: auto-generated
last_sync: 2026-11-07T22:45:07.606039
---

# Mirror: ring_buffer.rs

## 📝 Description
Automatically generated mirror for `log-server/src/core/ring_buffer.rs`.

> **Essential Process**:
> ! In-memory circular ring buffer for real-time log ingestion, querying, ! and zero-copy broadcast streaming via gRPC. ! ! DATA FLOW: ! 1. LogWriter -> push(entry) -> VecDeque (bounded FIFO memory) ! 2. Real-time broadcast -> broadcast_tx -> active gRPC StreamLogs subscribers ! 3. GetTailLogs -> thread-safe RwLock read -> filtered recent log snapshot ! ! KEY PARAMETERS: ! - capacity: Maximum entries retained in memory before FIFO rotation (default 5,000). ! - broadcast_tx: Tokio broadcast channel for real-time streaming subscribers (capacity 4,096). use std::collections::VecDeque; use std::sync::atomic::{AtomicU64, Ordering}; use std::sync::RwLock; use tokio::sync::broadcast; use crate::models::log_entry::LogEntry; / Thread-safe in-memory circular ring buffer with real-time broadcast pub struct LogRingBuffer { capacity: usize, buffer: RwLock<VecDeque<LogEntry>>, total_ingested: AtomicU64, broadcast_tx: broadcast::Sender<LogEntry>, }

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer.get_tail]] (method: defines_method) — *Retrieve the most recent entries up to `limit`, with optional filters*
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer.new]] (method: defines_method) — *Create new ring buffer with given capacity and internal broadcast channel*
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer.push]] (method: defines_method) — *Push a new log entry into the circular buffer and broadcast to live subscribers*
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer.subscribe]] (method: defines_method) — *Subscribe to real-time log stream*
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer.total_ingested]] (method: defines_method) — *Return total number of logs ingested since process start*
- [[log-server/log-server/src/facade/log_writer.rs.md|WriterConfig.default]] (method: calls)
- [[log-server/log-server/src/models/log_entry.rs.md|LogEntry]] (struct: calls) — *Internal log request wrapper for internal use*
- [[log-server/log-server/src/models/log_entry.rs.md|log_entry.rs]] (imports)
- [[log-server/log-server/src/models/mod.rs.md|mod.rs]] (imports)
- [[log-server/log-server/src/protocols/capnp/logger_msg.rs.md|Reader<'_,>.clone]] (method: calls)

### 🔌 Consumers (Inbound)
- [[log-server/log-server/src/core/contracts.rs.md|contracts.rs]] (calls)
- [[log-server/log-server/src/core/contracts.rs.md|contracts.rs]] (same_package)
- [[log-server/log-server/src/core/log_formatter.rs.md|log_formatter.rs]] (calls)
- [[log-server/log-server/src/core/log_formatter.rs.md|log_formatter.rs]] (same_package)
- [[log-server/log-server/src/core/protocol_handlers.rs.md|protocol_handlers.rs]] (calls)
- [[log-server/log-server/src/core/protocol_handlers.rs.md|protocol_handlers.rs]] (same_package)
- [[log-server/log-server/src/core/reorder_test.rs.md|reorder_test.rs]] (calls)
- [[log-server/log-server/src/core/reorder_test.rs.md|reorder_test.rs]] (same_package)
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer.get_tail]] (method: belongs_to) — *Retrieve the most recent entries up to `limit`, with optional filters*
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer.new]] (method: belongs_to) — *Create new ring buffer with given capacity and internal broadcast channel*
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer.push]] (method: belongs_to) — *Push a new log entry into the circular buffer and broadcast to live subscribers*
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer.subscribe]] (method: belongs_to) — *Subscribe to real-time log stream*
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer.total_ingested]] (method: belongs_to) — *Return total number of logs ingested since process start*
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer]] (struct: belongs_to) — *Thread-safe in-memory circular ring buffer with real-time broadcast*
- [[log-server/log-server/src/core/ring_buffer.rs.md|LogRingBuffer]] (struct: defines_method) — *Thread-safe in-memory circular ring buffer with real-time broadcast*
- [[log-server/log-server/src/core/ring_buffer.rs.md|test_ring_buffer_broadcast]] (function: belongs_to)
- [[log-server/log-server/src/core/ring_buffer.rs.md|test_ring_buffer_capacity_and_fifo]] (function: belongs_to)
- [[log-server/log-server/src/core/ring_buffer.rs.md|test_ring_buffer_filters]] (function: belongs_to)
- [[log-server/log-server/src/facade/log_server.rs.md|log_server.rs]] (imports)
- [[log-server/log-server/src/facade/log_writer.rs.md|log_writer.rs]] (calls)
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (calls)
- [[log-server/log-server/src/servers/grpc_server.rs.md|grpc_server.rs]] (imports)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
