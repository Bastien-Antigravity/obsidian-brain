# Bastien-Antigravity: Obsidian Brain 🌌

Welcome to the **Obsidian Brain**. This directory is the central Knowledge Management System (KMS) for the Bastien-Antigravity ecosystem. 

Unlike traditional flat documentation folders, this brain runs on a **5-Dimensional Hybrid System** combining PARA, Diátaxis, and Zettelkasten methods. It is designed to be the ultimate source of truth, equally readable by human engineers and AI Assistants.

---

## 🛠️ How it Works

The documentation here is not stored in deep, confusing folders. Instead, it relies on:
1. **Shallow Folders (PARA):** Only used for strict physical boundaries (e.g., `04-Deployment`).
2. **Metadata & Tags (Dataview):** Every major file should have a YAML frontmatter block at the top and specific tags (e.g., `#type/architecture`).
3. **Live Dashboards:** Because we use Dataview, we write algorithms inside `.md` files that dynamically track active Tasks and Bugs (e.g., `Sprint-Dashboard.md`).
4. **Visual Topologies:** We utilize `.canvas` Obsidian files (e.g., `Ecosystem-Topology.canvas`) to physically map and wire up infrastructure dependencies on an infinite 2D board.
5. **Bidirectional Links (Zettelkasten):** Files use `[[Links]]` to connect concepts, creating an organic graph of architectural decisions.

---

## 🧑‍💻 How to use it WITHOUT AI (Human Mode)

If you are a developer looking at this repository on your own:
1. **Install Obsidian:** Download Obsidian (it's free).
2. **Configure the App:** Follow the steps in **[[00-Obsidian-App-Config.md]]** (at the root) to set up Dataview and Sidebar Automation.
3. **Start at the MOC:** Open `00-Master-MOC.md`. This is the Map of Content, functioning as the table of contents for the entire ecosystem.
4. **Navigate via Graph/Links:** Click on `[[links]]` inside the documents to jump between rules, tutorials, and architecture decisions.
5. **Authoring:** Keep files atomic. If an architecture document gets too large, split it into smaller documents!
6. **Templates:** When creating a new AI task or architecture node, make sure your core Templates plugin is pointed to `obsidian-brain/05-Scripts/.obsidian-templates/`. You can inject the required Dataview frontmatter automatically.

---

## 🤖 How to use it WITH AI (Assistant Mode)

If you are pair-programming with the Antigravity AI Assistant, this brain becomes dynamic.

**1. Loading Context (Initialization)**
Before beginning a coding session, direct your AI to load the architectural rules by prompting:
> *"Read `00-Master-MOC.md`, load the rules and current sprint, then we can begin."*

**2. Session State Management**
You never have to lose context between days.
* **Saving:** At the end of your sprint, tell the AI: *"Save session state."* The AI will document your progress, bugs, and next steps in `01-AI-Assistant/AI-Session-State.md`.
* **Restoring:** The next morning, simply prompt: *"Restore session state"* and the AI will pick up right where you left off.

---

## 🤖 For AI Assistants (Initialization)

If you are an AI assistant tasked with working in this ecosystem, you MUST initialize your context using the following prompt:

> *"Read the ecosystem map in **[[00-Master-MOC]]** and restore session state from **[[01-AI-Assistant/AI-Session-State]]**. Follow the standardized loop in **[[00-Daily-AI-Playbook]]**."*

