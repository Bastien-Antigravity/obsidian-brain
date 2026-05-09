#!/usr/bin/env python
# coding:utf-8
"""
🚀 CLOSE MISSION (Governance Gate)
Finalizes the AI session by verifying state updates and documentation health.
Run this before concluding any major task.
"""

import sys
from pathlib import Path
from datetime import datetime, timedelta

# Add lib directory to sys.path
script_dir = Path(__file__).resolve().parent
sys.path.append(str(script_dir / "lib"))

try:
    from sovereignty import Sovereignty
except ImportError:
    print("❌ Error: Could not find sovereignty.py in lib/")
    sys.exit(1)

def main():
    print("\n🏁 Closing Mission: Sovereignty Audit...")
    
    workspace_root = script_dir.parents[1]
    vault_root = workspace_root / "obsidian-brain"
    
    engine = Sovereignty()
    valid_stems = set()
    valid_paths = set()
    
    # 1. Quick Scan for valid links
    for path in vault_root.rglob("*.md"):
        if ".git" in path.parts or ".obsidian" in path.parts:
            continue
        valid_stems.add(path.stem)
        valid_paths.add(path.relative_to(vault_root).as_posix())
    
    # 2. Identify "Hot" files (modified in the last 2 hours)
    # This represents the current session's work
    hot_threshold = datetime.now() - timedelta(hours=2)
    hot_files = []
    
    for path in vault_root.rglob("*.md"):
        if ".git" in path.parts or ".obsidian" in path.parts:
            continue
        mtime = datetime.fromtimestamp(path.stat().st_mtime)
        if mtime > hot_threshold:
            hot_files.append(path)
            
    if not hot_files:
        print("⚠️ No files modified in the last 2 hours. Is this an empty session?")
        return

    print(f"🔍 Auditing {len(hot_files)} session-modified files...")
    
    # 3. Audit Hot Files
    state_updated = False
    for path in hot_files:
        engine.audit_file(path, valid_stems, valid_paths)
        if "AI-Session-State" in path.name:
            state_updated = True
            
    report = engine.get_report()
    
    # 4. Final Verdict
    print("\n" + "="*60)
    print("📜 MISSION CLOSURE REPORT")
    print("="*60)
    
    if state_updated:
        print("✅ AI-Session-State.md: UPDATED")
    else:
        print("❌ AI-Session-State.md: NOT FOUND IN SESSION WORK")
        engine.log_error("Mandatory update of AI-Session-State.md is missing.")
        
    if report["success"] and state_updated:
        print("\n✨ VERDICT: MISSION ACCOMPLISHED")
        print("   All documentation is compliant and state is logged.")
    else:
        print("\n⚠️ VERDICT: MISSION BLOCKED")
        print("   Please resolve the following sovereignty violations:")
        for err in engine.errors:
            print(f"   [!] {err}")
            
    if report["warnings"]:
        print("\n💡 HYGIENE SUGGESTIONS:")
        for warn in report["warnings"]:
            print(f"   [~] {warn}")
            
    print("="*60 + "\n")
    
    if not (report["success"] and state_updated):
        sys.exit(1)

if __name__ == "__main__":
    main()
