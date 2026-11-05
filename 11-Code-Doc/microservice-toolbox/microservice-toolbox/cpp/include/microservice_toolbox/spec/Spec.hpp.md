---
source: microservice-toolbox/cpp/include/microservice_toolbox/spec/Spec.hpp
workspace: microservice-toolbox
type: code-mirror
status: auto-generated
last_sync: 2026-11-01 20:18:27.520375
microservice: 08-Squad-Agent
tags:
- '#service/08-Squad-Agent'
- '#type/code-mirror'
- '#state/auto-generated'
- '#zone/3-fleet'
---

# Mirror: Spec.hpp

## 📝 Description
Automatically generated mirror for `microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp`.

> **Essential Process**:
> Standardizes self-describing microservice specifications and dynamic registration with web-interface across the Bastien-Antigravity fleet for C++. Auto-resolves runtime listen/REST addresses, dynamic semver, active profile, and documentation links from AppConfig. FAIL-FAST PRINCIPLE: Zero silent fallbacks, zero default values, and zero dummy placeholders. Microservices must explicitly declare their own specification metadata (name, tag, layer, category, description, docLink, protocol, framing). Configuration addresses (including web_interface) must resolve strictly; missing capabilities, missing ports, or missing metadata FAIL FAST immediately.

## 🏗️ Architectural Context
<!-- SYNC:START -->
### 📦 Dependencies (Outbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.GetGRPCListenAddr]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.GetListenAddr]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.GetLogger]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.GetRESTAddr]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.GetVersion]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/config/AppConfig.hpp.md|AppConfig.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.Register]] (method: calls)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/lifecycle/LifecycleManager.hpp.md|LifecycleManager.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/logger/Logger.hpp.md|Logger.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec.toJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec.toJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.BuildSpecFromConfig]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.PublishSync]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.PublishWithLifecycle]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.Publish]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.buildSpecFromConfig]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.publishSync]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.publishWithLifecycle]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.publish]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/spec/spec.go.md|extractPort]] (function: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|MICROSERVICE_TOOLBOX_SPEC_HPP]] (macro: belongs_to) — *ifndef MICROSERVICE_TOOLBOX_SPEC_HPP*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec.toJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SendHttpRequest]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec.toJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.BuildSpecFromConfig]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.PublishSync]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.PublishWithLifecycle]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.Publish]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.buildSpecFromConfig]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.publishSync]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.publishWithLifecycle]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.publish]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher]] (class: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|addrinfo]] (struct: belongs_to) — *endif*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|timeval]] (struct: belongs_to) — *else*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
