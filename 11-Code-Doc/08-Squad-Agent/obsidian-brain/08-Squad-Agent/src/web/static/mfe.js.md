---
source: obsidian-brain/08-Squad-Agent/src/web/static/mfe.js
workspace: 08-Squad-Agent
type: code-mirror
status: auto-generated
last_sync: 2026-10-22 16:53:55.509215
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: mfe.js

## 📝 Description
Automatically generated mirror for `obsidian-brain/08-Squad-Agent/src/web/static/mfe.js`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/telegram/manager.py.md|push]] (function: calls) — *Trigger background transmission of the updated UI menu state*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.appendChatMessage]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.bindSquadTabs]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.connectedCallback]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.disconnectedCallback]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.handleUserSend]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.loadActiveMode]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.loadAll]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.loadChatHistory]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.loadCommands]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.loadContracts]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.loadStatus]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.printTerminalLine]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.removeThinkingIndicator]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.renderSessionList]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.renderSkeleton]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.runCommand]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.setProcessingState]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.setupEventListeners]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.showThinkingIndicator]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.startChatStream]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.switchMode]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.switchSession]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.updateLastUserBadge]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.updateUI]] (method: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.updateUserBadge]] (method: defines_method)
- [[09-RAG-Engine/obsidian-brain/09-RAG-Engine/src/services/config/db_config.py.md|get]] (function: calls)
- [[10-Agent-Factory/obsidian-brain/10-Agent-Factory/src/interfaces/identity.py.md|name]] (function: calls)

### 🔌 Consumers (Inbound)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.appendChatMessage]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.bindSquadTabs]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.connectedCallback]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.disconnectedCallback]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.handleUserSend]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.loadActiveMode]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.loadAll]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.loadChatHistory]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.loadCommands]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.loadContracts]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.loadStatus]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.printTerminalLine]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.removeThinkingIndicator]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.renderSessionList]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.renderSkeleton]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.runCommand]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.setProcessingState]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.setupEventListeners]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.showThinkingIndicator]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.startChatStream]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.switchMode]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.switchSession]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.updateLastUserBadge]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.updateUI]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE.updateUserBadge]] (method: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE]] (class: belongs_to)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|SquadAgentMFE]] (class: defines_method)
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|getSquadLogger]] (function: belongs_to) — *use strict';*
- [[08-Squad-Agent/obsidian-brain/08-Squad-Agent/src/web/static/mfe.js.md|sendMsg]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
