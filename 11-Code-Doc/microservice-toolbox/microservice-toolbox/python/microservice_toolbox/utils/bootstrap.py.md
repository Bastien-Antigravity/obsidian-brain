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

## 📝 Description
Automatically generated mirror for `microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py`.

> **Essential Process**:
> Bootstrapping utilities for running Python processes in the Bastien-Antigravity ecosystem. Manages automatic virtualenv re-execution, library path injections, and directory redirection.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/lib_loader.py.md|lib_loader.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/lib_loader.py.md|lib_loader.py]] (same_package)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/lib_loader.py.md|resolve_library_path]] (function: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/__init__.py.md|__init__.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|_find_nearest_venv]] (function: belongs_to) — *Walk up from the start directory until a directory containing .venv is found.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|bootstrap_microservice]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|ensure_import_paths]] (function: belongs_to) — *Ensure the script directory and vault root are available on sys.path.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|ensure_virtualenv]] (function: belongs_to) — *Re-launch the current script using the nearest virtualenv Python if available.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|find_vault_root]] (function: belongs_to) — *Walk up from the start directory until the vault root (obsidian-brain) is found.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|get_venv_python]] (function: belongs_to) — *Return the expected virtualenv python executable path for the current OS.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|prepend_venv_bin]] (function: belongs_to) — *Ensure the vault virtualenv bin/Scripts directory is on PATH.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/bootstrap.py.md|redirect_working_directory]] (function: belongs_to) — *Redirects the current working directory to the target directory reliably.*
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/init.py.md|init.py]] (calls)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/init.py.md|init.py]] (imports)
- [[microservice-toolbox/microservice-toolbox/python/microservice_toolbox/utils/init.py.md|init.py]] (same_package)
<!-- SYNC:END -->
