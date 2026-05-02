---
title: "AI Operating Manual: Multi-Mode Protocols"
version: 1.0
active_mode: Agent Orchestrator
---

# 🕹️ AI Operating Manual: Multi-Mode Protocols

This document defines the "Rules of Engagement" for the Antigravity AI assistant. By switching between these modes, the USER can balance between **Safety (Specs)**, **Speed (Labs)**, and **Scale (Orchestrator)**.

---

## 🛡️ Mode 1: Spec-First (The Governance Gate)

**Objective**: Maximum stability and zero-drift.
- **Rule 1**: No code changes without an approved BDD Spec in `02-Governance-Brain`.
- **Rule 2**: Every fix must be audited against the spec.
- **Rule 3**: "Mister Straight-to-Goal" acts as a Purger Gate for every implementation plan.
- **Best For**: Core libraries, financial logic, and stable infrastructure.

---

## 🚀 Mode 2: Free-Labs (The Fast Path)
**Objective**: Rapid prototyping and experimental flow.
- **Rule 1**: BDD Specs are optional. Focus on speed and "MVP" (Minimum Viable Product).
- **Rule 2**: Work is isolated in `03-Labs-Brain`.
- **Rule 3**: After a "Labs" feature is validated, it must be "Hardened" by moving it to Mode 1.
- **Best For**: UI/UX design, new trading strategies, and one-off scripts.

---

## 🛰️ Mode 3: Agent Orchestrator (The Fleet Commander)
*Current Active Mode*

**Objective**: Scale and mass-execution.
- **Rule 1**: AI operates across multiple repositories simultaneously.
- **Rule 2**: Focus on "Fleet-Wide Action Plans" rather than individual lines of code.
- **Rule 3**: Automated testing is mandatory for every repo in the action plan.
- **Best For**: Global refactors, dependency updates, and release cycles.

---

## 🚦 The Switching Protocol
To switch modes, the USER must:
1.  Update the `active_mode` in the header of this file.
2.  Update the `AI-Session-State.md` with: `Active Protocol: [[MODE-MANUAL#Mode-X]]`.
3.  The AI must confirm the switch by announcing its new "Inhibited" and "Activated" roles.

---

> [!IMPORTANT]
> Changing the mode changes the **Workflow**, not the **Brain**. All knowledge remains shared across all modes.
