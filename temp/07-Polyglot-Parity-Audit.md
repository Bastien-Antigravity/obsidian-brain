# 🌍 Polyglot Parity Audit (Go vs Rust vs Python)

## microservice-toolbox Config Loader — Line-by-Line Comparison

### Constructor Signature

| Language | Signature |
|----------|-----------|
| Go | `LoadConfig(profile string, specificFlags []string) (*AppConfig, error)` |
| Rust | `load_config(profile: &str) -> Result<AppConfig, Box<dyn Error>>` |
| Python | `load_config(profile, specific_flags=None) -> AppConfig` |

> ⚠️ **Parity Gap**: Go and Python accept `specificFlags`/`specific_flags`, but Rust does NOT accept specific flags in the public API.

### Phase Ordering ✅ IDENTICAL

| Phase | Go | Rust | Python |
|-------|-----|------|--------|
| 1. Load base file | `dConf := distconf.New(profile)` | `ac.load_from_file(...)` | `self._load_from_file(filename)` |
| 2. Dev override | `ac.applyFileOverride(...)` | `ac.apply_file_override(...)` | `self._apply_file_override(filename)` |
| 3. CLI overrides | `ac.applyCLIOverrides(...)` | `ac.apply_cli_overrides()` | `self._apply_cli_overrides()` |
| 4. gRPC overrides | `ac.applyCLIGRPCOverrides(...)` | (merged into step 3) | (merged into step 3) |

> ⚠️ **Parity Gap**: Go separates gRPC overrides into a dedicated function. Rust and Python merge it into the main CLI override function.

### DeepMerge ✅ IDENTICAL LOGIC

All three implement recursive map merging:
- If both `dst[key]` and `src[key]` are maps → recurse
- Otherwise → `dst[key] = src[key]` (overwrite)

### GetListenAddr ✅ IDENTICAL

All three construct `"{host}:{port}"` from `capabilities.{name}.ip` + `capabilities.{name}.port`.

### GetGRPCListenAddr ✅ IDENTICAL

All three:
1. Try explicit `grpc_ip` + `grpc_port`
2. Fallback to `ip` + `port + 1`

### Error Handling

| Scenario | Go | Rust | Python |
|----------|-----|------|--------|
| Missing config file | Returns nil, not fatal | `fs::read_to_string` silently skips | `FileNotFoundError` raised |
| Missing capability | Returns error string | Returns `Err(String)` | Raises `ValueError` |

> ⚠️ **Parity Gap**: Go and Rust silently skip missing files. Python raises a hard exception. This means Python is stricter and may break in scenarios where Go/Rust would degrade gracefully.

### Logger Integration

| Language | Logger Source |
|----------|-------------|
| Go | Injected via `LoadConfigWithLogger()` or uses `EnsureSafeLogger()` |
| Rust | Injected via `load_config_with_logger()`, auto-bootstraps UniLogger if `unilog` feature enabled |
| Python | Injected via constructor or uses `ensure_safe_logger()` |

> ⚠️ **Parity Gap**: Rust has a unique `#[cfg(feature = "unilog")]` that auto-bootstraps the logger. Go and Python never auto-bootstrap.
