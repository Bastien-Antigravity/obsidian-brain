# Knowledge Organization Strategy for Bastien-Antigravity

When dealing with a complex microservice ecosystem, a simple folder hierarchy is insufficient. We need a fluid architecture that supports multiple dimensions: strict categorization, dynamic states, contextual relationships, and algorithmic querying (both for you and me, the AI).

Here is the recommended paradigm for our Obsidian Brain:

## 1. The Core Layers of Organization

Depending on the task, we apply different conceptual layers.

### A. Folders: Structural Boundaries (The "Where")
**Use for:** Broad categorization and strict boundaries. 
**Our Paradigm:** Keep folders shallow. Folders represent the *physical department* of the file. If you have to wonder where a file goes, the folder system is too deep.
*Example:* `01-AI-Assistant/` vs `04-Deployment/`

### B. Tags: Dimensions & States (The "What" and "Status")
**Use for:** Cross-cutting concerns that apply regardless of the folder. Tags allow us to filter files globally.
**Our Paradigm:** Use nested tags.
* Examples of Type Tags: `#type/architecture`, `#type/test-scenario`, `#type/sprint-plan`
* Examples of State Tags: `#state/draft`, `#state/active`, `#state/deprecated`, `#ai/task` 
*(If you want me to look at something, tag it `#ai/task` and I'll know it's for me!)*

### C. YAML Frontmatter: Programmable Metadata (The "Database")
**Use for:** structured key-value pairs at the very top of your markdown files. Essential for using querying plugins like Dataview.
**Our Paradigm:** Every major system file gets frontmatter so we can track versions and targets.
```yaml
---
microservice: log-server
version: 1.2.0
author: Ruzava
---
```

### D. Bidirectional Links: Conceptual Fabric (The "Why")
**Use for:** connecting ideas contextually. 
**Our Paradigm:** If `log-server` relies on `microservice-toolbox`, the log-server architecture file should include the link `[[bastien_architecture]]` or `[[microservice-toolbox]]`. This naturally builds an interactive dependency graph we can visualize in Obsidian.

---

## 2. Multi-Dimensional Views & Paradigms

How do we view the data depending on the level of complexity we are trying to understand?

### Level 1: The Graph View (Macro / Organic Paradigm)
* **What it is:** Obsidian's native visualizer.
* **When to use:** When you want to see the "Big Picture" or detect forgotten orphans. E.g., visualizing which microservices are highly coupled to `safe-socket` by looking at the node density.

### Level 2: Dataview Matrix (Structured / Algorithmic Paradigm)
* **What it is:** A highly recommended Obsidian Community Plugin that turns Markdown metadata into SQL-like tables.
* **When to use:** Tracking QA or deployment. You can create a file that automatically queries: *"Show me all files tagged `#type/test-scenario` where `status: failed` grouped by `microservice`"*. 

### Level 3: Map of Content (MOC) (Curated / Human Paradigm)
* **What it is:** An index file (like a personalized Wikipedia landing page).
* **When to use:** For onboarding and general navigation. Instead of scrolling through an alphabetical folder list, an MOC is curated. 
*Example MOC format:*
```markdown
# 🗺 AI Microservice Ecosystem MOC
## Core Rules
- [[bastien_coding_style]]
- [[bastien_architecture]]

## Active Sprints
- [[Sprint-1-Refactoring-Log-Server]]
```

## 3. The 5-Dimensional Hybrid System
We employ a fusion of **PARA, Diátaxis, and Zettelkasten** to avoid chaos while maintaining creative flow.

* **WHERE (PARA Method):** Shallow folders (`04-Deployment`). No deep nesting!
* **WHAT & HOW (Diátaxis):** Tags classify the type of knowledge (`#type/tutorial`, `#type/how-to`, `#type/reference`, `#type/architecture`).
* **WHY (Zettelkasten):** Use `[[Bidirectional Links]]` to connect concepts to Architecture Decision Records (ADRs) or design philosophies.
* **HOW MANY (Metadata):** YAML frontmatter (`dependencies: 4`, `version: 1.2`) to empower Dataview queries.

## 4. AI Interaction & Session States
As your AI assistant, this system allows us to work together fluidly.

### A. How to initialize a coding session:
* Simply say: *"Read `00-Master-MOC.md` and `AI-Session-State.md` then let's begin."*
* Because I have filesystem access, I automatically load the rules, architecture, and current sprint goals directly from those documents.

### B. Session State Management
We don't need to lose our train of thought between days.
* **Save State:** At the end of a session, ask me to *"Save session state"*. I will summarize our progress, known bugs, and the next steps into `01-AI-Assistant/AI-Session-State.md`.
* **Restore State:** Next time you engage with me, just say *"Restore session state"* and I will pick up right where we left off based on that file!

---
> [!TIP] Split Information Aggressively!
> Do we need to split information? **YES!** Atomicity is powerful. If an architecture document gets too long, split it and use an MOC to group them. Many small, well-linked files always beat one massive file.
