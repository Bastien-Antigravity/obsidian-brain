---
title: "Python Types and Structure"
type: architecture
status: active
microservice: ecosystem-wide
---

# 📐 Python Types and Structure

## Architectural Rule
- **Structure**: Use `abc.ABC` for interfaces.
- **Type Hints**: Always use type hints for all function signatures.
- **Dependency Management**: Pinned `requirements.txt`.

## Motivation (Why?)
- Maintainability: Makes Python services easier to audit and refactor in a polyglot environment.
- Alignment: Matches the structural rigor of Go and Rust.

## Examples
```python
from abc import ABC, abstractmethod

class IDataProcessor(ABC):
    @abstractmethod
    def process_data(self, payload: dict) -> bool:
        pass
```
