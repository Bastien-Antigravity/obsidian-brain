---
title: "Rust Safety and Async"
type: architecture
status: active
microservice: ecosystem-wide
---

# 📐 Rust Safety and Async

## Architectural Rule
- **Async Runtime**: Use `tokio` with full features.
- **Error Handling**: Use `Result<T, Box<dyn std::error::Error>>` and propagate with `?`.
- **Ownership**: Prefer borrowing over cloning.

## Motivation (Why?)
- Performance: Leverages Rust's zero-cost abstractions for high-performance servers.
- Reliability: Enforces compiled-time safety and prevents runtime panics.

## Examples
```rust
// Preferred borrowing
fn process(data: &str) { ... }

// Error propagation
fn run() -> Result<(), Box<dyn Error>> {
    let config = load_config()?;
    Ok(())
}
```
