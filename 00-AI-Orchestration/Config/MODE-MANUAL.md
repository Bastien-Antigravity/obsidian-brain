---
microservice: ecosystem-core
type: configuration
status: active
active_mode: 4
active_client: antigravity
tags:
- '#zone/0-orchestration'
- '#service/ecosystem-core'
- '#type/configuration'
- '#state/active'
---
# 🕹️ AI Operating Manual: Multi-Mode Governance Protocols

This document defines the canonical operating modes for AI agents across `obsidian-brain` and external Zero-Mixing Domain Workspaces. Across all modes, `07-Core-KMS` remains write-protected from unapproved automated mutation (`access_matrix.yaml`).

## 🛡️ Mode 1: Spec-First (Default Production Engineering)
- **Purpose**: High-reliability microservice and SDK development driven by approved behavioral contracts.
- **Gatekeeping Rule**: Author or verify the Gherkin behavior specification (`02-Business-BDD/02-Behavior-Specs/<service>/FEAT-*.md`) and `ExchangeContract` definitions before modifying production source code.
- **Verification**: Requires passing Zone-1 standalone unit + adversarial tests and `validate-compliance --strict-imports --strict-lean`.

## 🧪 Mode 2: Free-Labs (Rapid Prototyping & Spikes)
- **Purpose**: Exploratory benchmarking, external reference comparison, and isolated proof-of-concept spikes inside `04-Rapid-Prototyping/EXP-XXX-*`.
- **Gatekeeping Rule**: Laboratory experiments never mutate base L1/L2 production repositories directly; validated designs graduate to Mode 1 via an `EXP-XXX` merge proposal.

## 🛰️ Mode 3: Fleet-Commander (Multi-Repository Sync & Release Ops)
- **Purpose**: Cross-repository version alignment (`VERSION.txt`), CI/CD workflow synchronization (`master-ci.yml` / `master-docker-publish.yml`), inventory updates, and coordinated branch checkpoints.
- **Gatekeeping Rule**: Atomic fleet operations halt immediately on the first repository build, test, or compliance failure.

## 🥷 Mode 4: Direct-Action (Targeted Hotfix & Auto-Repair)
- **Purpose**: Surgical bugfixes, incident remediation (`AutoRepairCoordinator`), and vault/compliance maintenance with full cross-zone visibility (`00`–`09`), still enforcing `07-Core-KMS` write protection and full post-edit test/compliance verification.
