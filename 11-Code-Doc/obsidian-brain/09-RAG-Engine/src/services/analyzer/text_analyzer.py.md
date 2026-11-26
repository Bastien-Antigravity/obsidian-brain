

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/analyzer/text_analyzer.py`.

> **Essential Process**:
> Generic analyzer for plain text and configuration files (JSON, YAML, TOML). Provides sensible default chunking for files that do not have dedicated AST parsers.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/analyzer.py.md|Analyzer]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/analyzer.py.md|analyzer.py]] (imports)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/text_analyzer.py.md|TextAnalyzer]] (class: belongs_to) — *Handles chunking for generic text and configuration files.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/text_analyzer.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/text_analyzer.py.md|analyze]] (function: belongs_to) — *Analyzes text/config files and splits them into logical chunks.*
<!-- SYNC:END -->
