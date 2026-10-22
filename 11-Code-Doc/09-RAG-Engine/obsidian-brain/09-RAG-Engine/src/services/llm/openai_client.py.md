---
source: obsidian-brain/09-RAG-Engine/src/services/llm/openai_client.py
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.243163
---

# Mirror: openai_client.py

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/services/llm/openai_client.py`.

> **Essential Process**:
> OpenAI-compatible client implementation of the LLMClient interface. Supports local engines (Ollama, LM Studio) and public cloud engines (DeepSeek, Qwen, OpenAI).

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|config.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/core/config.py.md|get_enrichment_settings]] (function: calls) — *Resolves LLM enrichment configuration with automatic secret decryption.*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/llm_client.py.md|LLMClient]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/interfaces/llm_client.py.md|llm_client.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/llm/__init__.py.md|__init__.py]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/llm/__init__.py.md|__init__.py]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/llm/__init__.py.md|__init__.py]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/llm/openai_client.py.md|OpenAILLMClient]] (class: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/llm/openai_client.py.md|__init__]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/llm/openai_client.py.md|generate_response]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
