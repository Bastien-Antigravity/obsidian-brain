

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/analyzer/markdown_analyzer.py`.

> **Essential Process**:
> Markdown-specific analyzer for the RAG system. Splits markdown files into logical chunks based on hierarchical headers.

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/analyzer.py.md|Analyzer]] (class: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/interfaces/analyzer.py.md|analyzer.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)

### 🔌 Consumers (Inbound)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/markdown_analyzer.py.md|MarkdownAnalyzer]] (class: belongs_to) — *Hierarchical header-based chunker for Markdown.*
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/markdown_analyzer.py.md|__init__]] (function: belongs_to)
- [[obsidian-brain/obsidian-brain/09-RAG-Engine/src/services/analyzer/markdown_analyzer.py.md|analyze]] (function: belongs_to) — *Analyzes markdown files and splits them into logical chunks by headers.*
<!-- SYNC:END -->
