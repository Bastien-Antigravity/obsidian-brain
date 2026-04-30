# Bastien-Antigravity: Obsidian Brain 🌌


# Too much work/time consuming to test, use, evaluate, re-organize, not used for the moment... (including tech-stack-brain, core-kms-brain) => stand by for the moment...


Welcome to the **Obsidian Brain**. This directory is the central Knowledge Management System (KMS) for the Bastien-Antigravity ecosystem. 

Unlike traditional flat documentation folders, this brain runs on a **5-Dimensional Hybrid System** combining PARA, Diátaxis, and Zettelkasten methods. It is designed to be the ultimate source of truth, equally readable by human engineers and AI Assistants.

---

## 🛠️ How it Works

The documentation here is not stored in deep, confusing folders. Instead, it relies on:
1. **Shallow Folders (PARA):** We strictly separate the generic `00-AI-Engine` from the `Project-` specific domains (e.g., `03-Project-Deployment`).
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
6. **Templates:** When creating a new AI task or architecture node, copy the relevant templates from `00-AI-Engine/State-and-Tasks/Inbox/Templates/`.

---

## 🤖 How to use it WITH AI (Assistant Mode)

This repository is powered by a completely generic, portable **AI Engine** (`00-AI-Engine`).

If you want to use the AI to generate code, write tests, or design architecture:
1. Please read **[[00-AI-Engine/User-Manual.md]]**.
2. Fill out an **Idea Pitch** in the `Inbox/`.
3. Run the automated Python `Agent-Dispatcher.py` to route your idea through the AI Roles (Orchestrator -> Architect -> QA -> Developer -> DevOps -> DocMaintainer).
