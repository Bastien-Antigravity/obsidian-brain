---
microservice: 08-Base-Scripts
type: note
status: active
tags:
- '#service/08-Base-Scripts'
- '#type/note'
- '#state/active'
- '#zone/3-fleet'
---

## 📝 Description
Automatically generated mirror for `microservice-toolbox/go/pkg/messaging/config.go`.

> **Essential Process**:
> Configuration parameters for message broker connectors (NATS, JetStream).

## 🏗️ Architectural Context

<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- None detected

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/go/pkg/messaging/config.go.md|JetStreamConfig]] (struct: belongs_to) — *JetStreamConfig holds specific settings for stream creation and publishing.*
- [[microservice-toolbox/microservice-toolbox/go/pkg/messaging/config.go.md|NatsConfig]] (struct: belongs_to) — *NatsConfig holds configuration for the NATS client connection.*
<!-- SYNC:END -->
