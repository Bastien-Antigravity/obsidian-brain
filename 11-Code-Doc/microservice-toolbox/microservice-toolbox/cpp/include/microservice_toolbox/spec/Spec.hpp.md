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
> Standardizes self-describing microservice specifications and dynamic registration with web-interface across the Bastien-Antigravity fleet for C++. Auto-resolves runtime listen/REST addresses, dynamic semver, host node, canvas/health metadata, and documentation links from AppConfig. FAIL-FAST PRINCIPLE: Zero silent fallbacks, zero default values, and zero dummy placeholders. Microservices must explicitly declare their own specification metadata (name, tag, layer, category, description, docLink, protocol, framing). Configuration addresses (including web_interface) must resolve strictly; missing capabilities, missing ports, or missing metadata FAIL FAST immediately.

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
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/contracts.hpp.md|contracts.hpp]] (imports)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|CanvasSpec.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|CanvasSpec.IsEmpty]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|CanvasSpec.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|CanvasSpec.fromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|CanvasSpec.from_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|CanvasSpec.toJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|CanvasSpec.to_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|DependencySpec.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|DependencySpec.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|DependencySpec.fromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|DependencySpec.from_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|DependencySpec.toJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|DependencySpec.to_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|HealthSpec.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|HealthSpec.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|HealthSpec.fromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|HealthSpec.from_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|HealthSpec.toJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|HealthSpec.to_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec.fromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec.from_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec.toJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec.to_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec.FromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec.ToJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec.fromJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec.from_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec.toJson]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec.to_json]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.BuildSpecFromConfig]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.PublishSync]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.PublishWithLifecycle]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.Publish]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.buildSpecFromConfig]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.contracts_detail_trim]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.publishSync]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.publishWithLifecycle]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.publish]] (method: defines_method)
- [[microservice-toolbox/microservice-toolbox/go/pkg/spec/spec.go.md|extractPort]] (function: calls)

### 🔌 Consumers (Inbound)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|CanvasSpec.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|CanvasSpec.IsEmpty]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|CanvasSpec.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|CanvasSpec.fromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|CanvasSpec.from_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|CanvasSpec.toJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|CanvasSpec.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|CanvasSpec]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|CanvasSpec]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|CurrentHostname]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|DependencySpec.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|DependencySpec.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|DependencySpec.fromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|DependencySpec.from_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|DependencySpec.toJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|DependencySpec.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|DependencySpec]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|DependencySpec]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|HealthSpec.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|HealthSpec.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|HealthSpec.fromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|HealthSpec.from_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|HealthSpec.toJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|HealthSpec.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|HealthSpec]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|HealthSpec]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|JitteredBackoffMs]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|MICROSERVICE_TOOLBOX_SPEC_HPP]] (macro: belongs_to) — *ifndef MICROSERVICE_TOOLBOX_SPEC_HPP*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec.fromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec.from_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec.toJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ProtocolSpec]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SendHttpRequest]] (function: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec.FromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec.ToJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec.fromJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec.from_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec.toJson]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec.to_json]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec]] (struct: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|ServiceSpec]] (struct: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.BuildSpecFromConfig]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.PublishSync]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.PublishWithLifecycle]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.Publish]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.buildSpecFromConfig]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.contracts_detail_trim]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.publishSync]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.publishWithLifecycle]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher.publish]] (method: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher]] (class: belongs_to)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|SpecPublisher]] (class: defines_method)
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|addrinfo]] (struct: belongs_to) — *endif*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|envHost]] (constant: belongs_to) — *if defined(_WIN32)*
- [[microservice-toolbox/microservice-toolbox/cpp/include/microservice_toolbox/spec/spec.hpp.md|timeval]] (struct: belongs_to) — *else*
<!-- SYNC:END -->

## 🔍 Implementation Details
(Add manual notes here)
