---
source: obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22 16:53:55.925490
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: persona_extractor.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py`.

> **Essential Process**:
> Scans the fleet repositories for Go, Rust, and Python code, extracting structural patterns (AST, Regex matching of structs, traits, interfaces) to build persona context for the AI RAG engine.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/bootstrap.py.md|bootstrap.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|get_logger]] (function: calls)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|orchestration_lib.py]] (imports)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/lib/orchestration_lib.py.md|resolve_vault_and_workspace]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/main.py.md|parse_args]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/pkg/mod/github.com/!bastien-!antigravity/microservice-toolbox@v0.0.1/python/microservice_toolbox/utils/bootstrap.py.md|ensure_import_paths]] (function: calls) — *Ensure the script directory and vault root are available on sys.path.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/pkg/mod/github.com/!bastien-!antigravity/microservice-toolbox@v0.0.1/python/microservice_toolbox/utils/bootstrap.py.md|ensure_virtualenv]] (function: calls) — *Re-launch the current script using the nearest virtualenv Python if available.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/pkg/mod/github.com/!bastien-!antigravity/microservice-toolbox@v0.0.1/python/microservice_toolbox/utils/bootstrap.py.md|prepend_venv_bin]] (function: calls) — *Ensure the vault virtualenv bin/Scripts directory is on PATH.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/pkg/mod/github.com/!bastien-!antigravity/microservice-toolbox@v0.0.1/python/microservice_toolbox/utils/process_lock.py.md|prevent_double_start]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|walk]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py.md|GoExtractor]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py.md|PythonExtractor]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py.md|RustExtractor]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py.md|__init__]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py.md|_get_exception_names]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py.md|extract_personas]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py.md|main]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py.md|parse]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py.md|visit_AsyncFunctionDef]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py.md|visit_Call]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py.md|visit_ClassDef]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py.md|visit_ExceptHandler]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py.md|visit_FunctionDef]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py.md|visit_ImportFrom]] (function: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/extraction/persona_extractor.py.md|visit_Import]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
