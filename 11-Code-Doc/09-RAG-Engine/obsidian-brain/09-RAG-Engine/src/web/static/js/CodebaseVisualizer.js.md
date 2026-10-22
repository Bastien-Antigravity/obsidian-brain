---
source: obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js
workspace: 09-RAG-Engine
type: code-mirror
status: auto-generated
last_sync: 2026-10-22T16:53:56.095434
---

# Mirror: CodebaseVisualizer.js

## 📝 Description
Automatically generated mirror for `obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/code_engine/models.py.md|Node]] (class: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/indexing_pipeline/standard.py.md|worker]] (function: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.(nodeId, p]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.Code(fileNode,]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.barActiveStates(nodeId) {]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.buildContextualTreeAndList]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.checkWebGLSupport]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.dSymbols(data) {
 ]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.detachPanel]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.filterContextualData]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.getNodeById]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.iggerCodebaseScan()]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.iggerSearchFilter()]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.ilsView(node) {
 ]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.initWorker]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.init]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.leTree(treeRoo]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.loadDatabase]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.mbolsList(symbols]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.ne(lineNum) ]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.ntent(noteNode)]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.onDatabaseLoadError]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.onDatabaseLoaded]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.reSymbols() {
   ]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.safeCreateIcons]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.setupEventListeners]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.updateRightPanelTabs]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.xp(string) {]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/GraphManager.js.md|GraphManager.   ]] (method: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/GraphManager.js.md|GraphManager.js]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/GraphManager.js.md|GraphManager.js]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/GraphManager.js.md|GraphManager.render]] (method: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/GraphManager.js.md|GraphManager.resetForces]] (method: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/GraphManager.js.md|GraphManager.updateForces]] (method: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/HistoryManager.js.md|HistoryManager.js]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/HtmlObjectVisualizer.js.md|HtmlObjectVisualizer.js]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/SessionManager.js.md|SessionManager.createSession]] (method: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/SessionManager.js.md|SessionManager.js]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/SessionManager.js.md|SessionManager.js]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/graph/NodeRenderer.js.md|NodeRenderer.isWebGLAvailable]] (method: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|CodebaseNode.isFile]] (method: calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|models.js]] (imports)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/models.js.md|models.js]] (same_package)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/identity.py.md|name]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|mfe.js]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.(nodeId, p]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.Code(fileNode,]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.barActiveStates(nodeId) {]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.buildContextualTreeAndList]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.checkWebGLSupport]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.dSymbols(data) {
 ]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.detachPanel]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.filterContextualData]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.getNodeById]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.iggerCodebaseScan()]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.iggerSearchFilter()]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.ilsView(node) {
 ]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.initWorker]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.init]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.leTree(treeRoo]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.loadDatabase]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.mbolsList(symbols]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.ne(lineNum) ]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.ntent(noteNode)]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.onDatabaseLoadError]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.onDatabaseLoaded]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.reSymbols() {
   ]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.safeCreateIcons]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.setupEventListeners]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.updateRightPanelTabs]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer.xp(string) {]] (method: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer]] (class: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|CodebaseVisualizer]] (class: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|bolNode = (name) ]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|copyAndFilter]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|eeNodes = (cont]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|tTransitionDuration =]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/CodebaseVisualizer.js.md|updateForceSimulation]] (function: belongs_to)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/HistoryManager.js.md|HistoryManager.js]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/HistoryManager.js.md|HistoryManager.js]] (same_package)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/SessionManager.js.md|SessionManager.js]] (calls)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/web/static/js/SessionManager.js.md|SessionManager.js]] (same_package)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
