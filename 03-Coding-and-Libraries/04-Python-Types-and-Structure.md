---
title: "Python Types and Structure"
type: architecture
status: active
microservice: ecosystem-wide
---

# 📐 Python Types and Structure

## Architectural Rule
- **Structure**: Use `abc.ABC` for interfaces.
- **Interface Naming**: Python interfaces use `I`-prefix: `ILogger`, `IDataProcessor`.
- **Type Hints**: Always use type hints for all function signatures. Use `Optional[Type]` from `typing`.
- **Private Methods**: Prefix with `_underscore`: `_load_from_file()`, `_apply_cli_overrides()`.
- **Static Methods**: Use `@staticmethod` for utility functions like `deep_merge()`.
- **Dependency Management**: Pinned `requirements.txt`.
- **Imports**: Use relative imports within the package hierarchy.

## Error Handling
```python
# Descriptive exception messages with component prefix
raise FileNotFoundError(f"Toolbox (Python): Config file '{filename}' not found for profile '{profile}'")
raise ValueError(f"capability {capability} not found")
```
> ⚠️ **Note**: Python raises hard exceptions for missing config files, while Go/Rust silently skip them.

## Naming Conventions (Python-specific)
- **Functions**: `snake_case` — `load_config()`, `parse_cli_args()`, `deep_merge()`
- **Classes**: `PascalCase` — `AppConfig`
- **Private**: `_underscore_prefix` — `_load_from_file()`, `_apply_cli_overrides()`

## Motivation (Why?)
- Maintainability: Makes Python services easier to audit and refactor in a polyglot environment.
- Alignment: Matches the structural rigor of Go and Rust.

## Examples
```python
from abc import ABC, abstractmethod
from typing import Optional

class IDataProcessor(ABC):
    @abstractmethod
    def process_data(self, payload: dict) -> bool:
        pass

# Semantic helper to match Go LoadConfig()
def load_config(profile, specific_flags=None):
    return AppConfig(profile, specific_flags)

# Private method convention
class AppConfig:
    def _load_from_file(self, filename):
        ...
    def _apply_cli_overrides(self):
        ...
    @staticmethod
    def deep_merge(dst, src):
        ...
```
