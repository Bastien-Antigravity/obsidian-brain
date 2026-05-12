---
microservice: obsidian-brain
type: governance
status: active
tags: ['#type/governance', '#state/active']
---

# 🧬 Project DNA: obsidian-brain

## 🎯 High-Level Intent (BDD)
- **Goal**: Knowledge management system using Obsidian as the source of truth for project logic and agent choreography.
- **Key Pattern**: **Graph-based Knowledge Base**.

## 🛠 Technical Constraints
- **Architecture Standard**: Adheres to the ecosystem-wide standards in [[03-Tech-Stack/02-Project-Architecture/Global-Architecture-Rules|Global-Architecture-Rules]].

## 👥 Roles & Responsibilities
- **Architect**: 
    - Ensure the graph structure remains consistent and traversable by AI agents.
    - **Frontend Standard**: The Brain Graph visualization must follow [[03-Tech-Stack/02-Project-Architecture/Global-Architecture-Rules|Global-Architecture-Rules]] (D3.js or similar within Bootstrap).
- **Developer**:
    - Use relative paths or environment variables for vault imports.
    - Reference [[03-Tech-Stack/02-Project-Architecture/Global-Architecture-Rules|Global-Architecture-Rules]] for UI and graph interaction standards.
