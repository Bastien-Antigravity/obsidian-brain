---
title: "Go Memory and Concurrency"
type: architecture
status: active
microservice: ecosystem-wide
---

# 📐 Go Memory and Concurrency

## Architectural Rule
- **Memory Efficiency**: Use fixed-length slices/ring-buffers (e.g., `200` length). NEVER expand arrays infinitely. Use `make` with capacity.
- **Concurrency**: Use `context.Context` for cancellation. Always deep-copy shared resources before crossing Goroutine boundaries.

## Motivation (Why?)
- Performance: Minimizes GC pressure and prevents OOM in high-throughput data processing.
- Safety: Eliminates data races in shared memory environments.

## Examples
```go
// Correct Slice Pre-allocation
data := make([]LogEntry, 0, 200)

// Safe concurrent map access
newMap := make(map[string]string)
for k, v := range sharedMap {
    newMap[k] = v
}
```
