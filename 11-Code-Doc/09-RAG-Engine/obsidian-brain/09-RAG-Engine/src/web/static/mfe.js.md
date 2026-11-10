---
source: obsidian-brain/09-RAG-Engine/src/web/static/mfe.js
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.031362
---

# Mirror: mfe.js

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/web/static/mfe.js`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/GraphManager.js.md|GraphManager.fit]] (method: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.appendTerminalLine]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.bindEvents]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.closeSSE]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.connectedCallback]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.destroyResizeObserver]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.destroyThemeSync]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.disconnectedCallback]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.escapeHtml]] (method: defines_method) — *Helper functions*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.initThemeSync]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.loadContracts]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.renderConfigView]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.renderContractTab]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.renderLayout]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.renderReloadView]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.renderSearchView]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.renderStatsView]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.renderVisualizerView]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.switchTab]] (method: defines_method)

### 🔌 Consumers (Inbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.appendTerminalLine]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.bindEvents]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.closeSSE]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.connectedCallback]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.destroyResizeObserver]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.destroyThemeSync]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.disconnectedCallback]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.escapeHtml]] (method: belongs_to) — *Helper functions*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.initThemeSync]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.loadContracts]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.renderConfigView]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.renderContractTab]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.renderLayout]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.renderReloadView]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.renderSearchView]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.renderStatsView]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.renderVisualizerView]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE.switchTab]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE]] (class: belongs_to) — *use strict';*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|ObsidianBrainMFE]] (class: defines_method) — *use strict';*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|executeSearch]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|loadScript]] (function: belongs_to) — *Helper functions*
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|loadStylesheet]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|setupImportmap]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/mfe.js.md|syncTheme]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
