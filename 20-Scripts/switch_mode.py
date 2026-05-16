#!/usr/bin/env python
# coding:utf-8
"""
ESSENTIAL PROCESS:
Switches the operational protocol of the AI Squad by atomically updating
BOTH the MODE-MANUAL.md and AI-Session-State.md files.

DATA FLOW:
1. Inputs a mode selection from the user.
2. Resolves paths to MODE-MANUAL.md and AI-Session-State.md.
3. Updates 'active_mode' in MODE-MANUAL.md.
4. Updates 'active-protocol' in AI-Session-State.md to match.

KEY PARAMETERS:
- modes: Dict mapping numeric choices to protocol names.
"""

from os.path import abspath as osPathAbspath, join as osPathJoin, dirname as osPathDirname, exists as osPathExists
from re import sub as reSub

# -----------------------------------------------------------------------------------------------

def _update_file_field(file_path: str, field_pattern: str, replacement: str) -> bool:
    """
    Updates a specific YAML field in a markdown file.
    Returns True if the field was found and updated.
    """
    if not osPathExists(file_path):
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = reSub(field_pattern, replacement, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# -----------------------------------------------------------------------------------------------

def main() -> None:
    modes = {
        "1": "🛡️ Spec-First",
        "2": "🧪 Free-Labs",
        "3": "🛰️ Fleet-Commander"
    }
    
    print("\n--- 🕹️ Bastien-Antigravity: Mode Switcher ---")
    for key, name in modes.items():
        print("[{0}] {1}".format(key, name))
    
    choice = input("\nSelect new active mode [1-3]: ").strip()
    
    if choice in modes:
        # Resolve paths relative to this script
        script_dir = osPathDirname(osPathAbspath(__file__))
        orchestration_dir = osPathAbspath(osPathJoin(script_dir, "../00-AI-Orchestration"))
        
        mode_file = osPathJoin(orchestration_dir, "MODE-MANUAL.md")
        session_orch = osPathJoin(orchestration_dir, "AI-Session-State.md")
        session_root = osPathJoin(script_dir, "../AI-Session-State.md")
        
        # 1. Update MODE-MANUAL.md
        mode_updated = _update_file_field(
            mode_file,
            r"active_mode:\s*\d+",
            "active_mode: {0}".format(choice)
        )
        
        if not mode_updated:
            print("❌ Error: Could not find or update MODE-MANUAL.md at {0}".format(mode_file))
            return
        
        # 2. Atomically update BOTH AI-Session-State.md to match
        field_pattern = r'active-protocol:\s*".*?"'
        replacement = 'active-protocol: "[[MODE-MANUAL#Mode-{0}]]"'.format(choice)
        
        orch_synced = _update_file_field(session_orch, field_pattern, replacement)
        root_synced = _update_file_field(session_root, field_pattern, replacement)
        
        print("\n✅ SUCCESS: Protocol updated to {0}".format(modes[choice]))
        print("   MODE-MANUAL.md: {0}".format("Updated" if mode_updated else "No change"))
        print("   AI-Session-State (Orch): {0}".format("Synced" if orch_synced else "Not found"))
        print("   AI-Session-State (Root): {0}".format("Synced" if root_synced else "Not found"))
        print("📢 Next time you launch the Squad, they will follow the rules of Mode {0}.".format(choice))
    else:
        print("❌ Invalid selection. No changes made.")

# -----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
