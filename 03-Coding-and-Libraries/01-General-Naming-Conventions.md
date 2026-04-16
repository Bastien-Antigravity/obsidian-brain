---
title: "General Naming Conventions"
type: architecture
status: active
microservice: ecosystem-wide
---

# 📐 General Naming Conventions

## Architectural Rule
- **Interfaces**: MUST start with `I` (e.g., `IBroker`, `IDataSource`).
- **Models**: prefix with `M` (e.g., `MMarketData`, `MOrderBook`).
- **Functions/Methods**: Use descriptive naming. Go: `CamelCase`. Rust: `snake_case`. Python: `snake_case`.

## Motivation (Why?)
- Unified readability across polyglot microservices.
- Instant recognition of types and abstractions when switching between Go, Rust, and Python.

## Examples
- `IBroker` (Interface)
- `MMarketData` (Model)
- `app_logger` (Variable)
