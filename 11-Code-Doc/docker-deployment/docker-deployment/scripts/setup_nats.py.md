---
source: docker-deployment/scripts/setup_nats.py
workspace: docker-deployment
type: code-mirror
status: auto-generated
last_sync: 2026-09-14 00:32:39.750684
microservice: 08-Base-Scripts
tags:
- '#service/08-Base-Scripts'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: setup_nats.py

## 📝 Description
Automatically generated mirror for `docker-deployment/scripts/setup_nats.py`.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[docker-deployment/docker-deployment/modes/local/infra.py.md|infra.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|operations.py]] (calls)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|operations.py]] (imports)
- [[docker-deployment/docker-deployment/scripts/operations.py.md|operations.py]] (same_package)
- [[docker-deployment/docker-deployment/scripts/setup_nats.py.md|NATS_VERSION]] (constant: belongs_to)
- [[docker-deployment/docker-deployment/scripts/setup_nats.py.md|detect_platform_target]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/setup_nats.py.md|download_and_install_nats]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/setup_nats.py.md|ensure_nats_available]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/setup_nats.py.md|find_existing_nats]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/setup_nats.py.md|get_nats_target_dir]] (function: belongs_to)
- [[docker-deployment/docker-deployment/scripts/setup_nats.py.md|print_fallback_instructions]] (function: belongs_to)
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
