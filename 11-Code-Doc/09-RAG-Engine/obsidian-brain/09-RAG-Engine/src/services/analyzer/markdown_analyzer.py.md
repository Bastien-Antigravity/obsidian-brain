---
source: obsidian-brain/09-RAG-Engine/src/services/analyzer/markdown_analyzer.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.449325
---

# Mirror: markdown_analyzer.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/analyzer/markdown_analyzer.py`.

> **Essential Process**:
> Markdown-specific analyzer for the RAG system. Splits markdown files into logical chunks based on hierarchical headers.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/analyzer.py.md|Analyzer]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/analyzer.py.md|analyzer.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|set]] (function: calls)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/facade/rag_facade.py.md|rag_facade.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/markdown_analyzer.py.md|MarkdownAnalyzer]] (class: belongs_to) — *Hierarchical header-based chunker for Markdown.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/markdown_analyzer.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/analyzer/markdown_analyzer.py.md|analyze]] (function: belongs_to) — *Analyzes markdown files and splits them into logical chunks by headers.*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
