# 📜 Interface Contracts Extracted from Source Code

## Master Interface Map

### Logger Ecosystem (3 layers)

```
flexible-logger/interfaces.Logger (Engine)
    ├── Debug/Info/Warning/Error/Critical
    ├── Stream/Logon/Logout/Trade/Schedule/Report  (Domain-specific)
    ├── Log(level, format, args)
    ├── SetLevel(level)
    ├── SetCallerSkip(skip int)
    └── Close()
        │
        ▼
universal-logger/interfaces.Logger (Facade — SUPERSET)
    ├── [All of flexible-logger.Logger]
    ├── GetNotifQueue() <-chan *NotifMessage
    ├── SetLocalNotifQueue(chan *NotifMessage)
    ├── SetMetadata(map[string]string)
    └── AddMetadata(key, value string)
        │
        ▼
safe-socket/interfaces.Logger (Consumer — minimal)
    └── (used by socket for debug logging)
```

**Hidden Rule**: `universal-logger.Logger` is a **strict superset** of `flexible-logger.Logger`. It wraps it and adds metadata + notification capabilities.

---

### Socket Ecosystem

```
safe-socket/interfaces.Socket
    ├── Common:  Close(), SetLogger()
    ├── Client:  Open(), Send(), Write(), Read(), Receive()
    ├── Server:  Listen(), Accept() -> TransportConnection
    └── Deadlines: SetDeadline(), SetReadDeadline(), SetWriteDeadline()

safe-socket/interfaces.SocketProfile
    ├── GetName() string
    ├── GetAddress() string
    ├── GetTransport() TransportType   // FramedTCP | UDP | SharedMemory
    ├── GetProtocol() ProtocolType     // none | hello
    └── GetConnectTimeout() int

safe-socket/interfaces.TransportConnection
    └── (per-connection handle returned by Accept())
```

---

### Config Ecosystem

```
distributed-config/interfaces.ConfigStrategy
    ├── Name() string
    ├── Load(cfg *core.Config) error
    ├── Sync(cfg *core.Config) error
    └── GetHandler() *network.ConfigProtoHandler

microservice-toolbox.AppConfig (WRAPPER)
    ├── *distconf.Config  (embedded)
    ├── Resolver
    ├── Profile string
    ├── Logger
    ├── LoadConfig() / LoadConfigWithLogger()
    ├── GetListenAddr(capability) (string, error)
    └── GetGRPCListenAddr(capability) (string, error)
```

---

### Notification Ecosystem

```
notif-server/interfaces.Notificator
    ├── Send(msg *utils.NotifMessage)
    ├── SendRaw(data []byte)
    └── LoadNotifSender(notifiersConf) map[string][]string
```

---

## Cross-Language Interface Parity

| Method | Go | Rust | Python |
|--------|-----|------|--------|
| `load_config(profile)` | `LoadConfig(profile, flags)` | `load_config(profile)` | `load_config(profile, flags)` |
| `get_listen_addr(cap)` | `GetListenAddr(cap)` | `get_listen_addr(cap)` | `get_listen_addr(cap)` |
| `get_grpc_addr(cap)` | `GetGRPCListenAddr(cap)` | `get_grpc_listen_addr(cap)` | `get_grpc_listen_addr(cap)` |
| `deep_merge(dst, src)` | `DeepMerge(dst, src)` | `deep_merge(dst, src)` | `deep_merge(dst, src)` |
| `ensure_safe_logger(l)` | `EnsureSafeLogger(l)` | `ensure_safe_logger(l)` | `ensure_safe_logger(l)` |

**Hidden Rule**: All three languages implement the SAME semantic API with identical phase ordering. The Rust and Python implementations are explicitly annotated as "matching Go implementation".
