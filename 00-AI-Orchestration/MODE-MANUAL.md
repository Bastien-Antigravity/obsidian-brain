---
title: "AI Operating Manual: Multi-Mode Protocols"
version: 2.0
type: architecture
status: active
active_mode: 2
---

# 🕹️ AI Operating Manual: Multi-Mode Protocols

This document defines the "Rules of Engagement" for the Antigravity AI assistant. By switching
between these modes, the USER can balance between **Safety (Specs)**, **Speed (Labs)**, and
**Scale (Orchestrator)**.

> [!IMPORTANT]
> Changing the mode changes the **Workflow**, not the **Brain**. All knowledge remains shared
> across all modes. The `active_mode` field in the header governs which protocol is active.

---

## 🛡️ Mode 1: Spec-First (The Governance Gate)

**Objective**: Maximum stability and zero-drift.
- **Rule 1**: No code changes without an approved BDD Spec in `02-Business-BDD/02-Behavior-Specs/`.
- **Rule 2**: Every fix must be audited against the spec before merging.
- **Rule 3**: Code cannot be merged until it strictly passes all Spec tests.
- **Primary Brains**: `02-Business-BDD`, `03-Tech-Stack`
- **AI Persona**: Unified **Systems Engineer** (applying QA, Architecture, and Development rules natively without roleplaying).
- **Best For**: Core libraries, financial logic, and stable infrastructure.

---

## 🚀 Mode 2: Free-Labs (The Fast Path)

**Objective**: Rapid prototyping and experimental flow.
- **Rule 1**: BDD Specs are optional. Focus on speed and "MVP" (Minimum Viable Product).
- **Rule 2**: Work is isolated in `04-Rapid-Prototyping/`. Experiments are logged in
  `01-Experiment-Index/` using the experiment template.
- **Rule 3**: After a "Labs" feature is validated, perform a "Graduation Ceremony" — creating the BDD spec in `02-Business-BDD` and transitioning the code to Mode 1 standards.
- **Primary Brain**: `04-Rapid-Prototyping`
- **AI Persona**: Unified **Systems Engineer** (focused on fast-track development and rapid iteration).
- **Best For**: UI/UX design, new trading strategies, and one-off 20-Scripts.

---

## 🛰️ Mode 3: Agent Orchestrator (The Fleet Commander)

**Objective**: Scale and mass-execution.
- **Rule 1**: AI operates across multiple repositories simultaneously.
- **Rule 2**: Focus on "Fleet-Wide Action Plans" in
  `05-Fleet-Operation/01-Fleet-Action-Plans/` rather than individual lines of code.
- **Rule 3**: Automated testing is mandatory for every repo in the action plan.
- **Primary Brain**: `05-Fleet-Operation`
- **AI Persona**: Unified **Systems Engineer** (focused on global architecture, synchronization, and ecosystem integrity).
- **Best For**: Global refactors, dependency updates, and release cycles.

---

## 🚦 The Switching Protocol

To switch modes, the USER must:
1. Say: `"Switch to Mode X"` (where X is 1, 2, or 3).
2. The AI will update `active_mode` in the YAML header of this file.
3. The AI will update `AI-Session-State.md` with: `Active Protocol: [[MODE-MANUAL#Mode-X]]`.
4. The AI will announce:
   - Which **rules are activated** for this mode (e.g., Unified Systems Engineer).
   - Which **brains are primary** for this mode.
   - Which **constraints are relaxed or enforced** (e.g., "BDD Specs optional" in Mode 2).

To deactivate all modes: `"Switch to Mode: none"`.

---

## 🔄 Mode Interaction Matrix

| Action | Mode 1 (Spec-First) | Mode 2 (Free-Labs) | Mode 3 (Fleet) |
|--------|---------------------|---------------------|-----------------|
| BDD Spec required? | ✅ Mandatory | ❌ Optional | ✅ Per action plan |
| Sandbox tests? | ✅ Mandatory | ❌ Optional | ✅ Mandatory |
| Multi-repo ops? | ❌ Single repo | ❌ Single repo | ✅ Fleet-wide |
| Graduation needed? | N/A | ✅ To Mode 1 | N/A |
| AI Persona Focus | Strict Compliance | Rapid Iteration | Ecosystem Sync |
