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
- **Atomic State**: Use `atomic.Pointer` with CAS loops for lock-free reads (see `config-server/src/store/store.go`).

## Concurrency Patterns (from source code)

### Goroutine Conventions
- **Fire-and-forget broadcasts**: `go s.broadcastRegistry()`
- **Per-connection handlers**: `go s.handleConnection(conn)`
- **Async sends with captured variables**: `go func(n string, sk ...) { sk.Write(bytes) }(name, sock)`

### Lock Patterns
- **RWMutex for client maps**: `listenersLock sync.RWMutex`
- **Lock/Unlock in same function**: Never deferred if followed by mutations
- **Deferred RUnlock for reads**: `s.listenersLock.RLock(); defer s.listenersLock.RUnlock()`

### Channel Patterns
- **Buffered notification queues**: `make(chan *utils.NotifMessage, 1024)`
- **Graceful shutdown**: `shutdown chan struct{}` with `select` multiplexing

## Error Handling Pattern
```go
// Always wrap errors with context
if err := proto.Unmarshal(data, req); err != nil {
    return nil, fmt.Errorf("protobuf unmarshal error: %w", err)
}

// Fatal errors use os.Exit(1), never panic()
// Non-fatal errors log and continue
```

## Comment Style
Every Go file uses **horizontal rule comments** to separate logical sections:
```go
// -----------------------------------------------------------------------------
// Section Name
// -----------------------------------------------------------------------------
```
Applied between every exported function, interface method groups, and struct definitions.

## Motivation (Why?)
- Performance: Minimizes GC pressure and prevents OOM in high-throughput data processing.
- Safety: Eliminates data races in shared memory environments.

## Examples
```go
// Correct Slice Pre-allocation
data := make([]LogEntry, 0, 200)

// Atomic Store with CAS loop (from config-server)
func (s *Store) UpdateAtomic(modFn func(current ConfigMap) (ConfigMap, error)) error {
    for {
        currentPtr := s.config.Load()
        newConfig, err := modFn(*currentPtr)
        if err != nil { return err }
        if s.config.CompareAndSwap(currentPtr, &newConfig) { return nil }
    }
}
```
