#!/usr/bin/env python3
import os

def main():
    modes = {
        "1": "🛡️ Spec-First",
        "2": "🧪 Free-Labs",
        "3": "🛰️ Fleet-Commander"
    }
    
    print("\n--- 🕹️ Bastien-Antigravity: Mode Switcher ---")
    for key, name in modes.items():
        print(f"[{key}] {name}")
    
    choice = input("\nSelect new active mode [1-3]: ").strip()
    
    if choice in modes:
        # Resolve path relative to this script
        mode_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../00-AI-Orchestration/MODE-MANUAL.md"))
        
        if not os.path.exists(mode_file):
            print(f"❌ Error: Could not find MODE-MANUAL.md at {mode_file}")
            return

        with open(mode_file, 'r') as f:
            lines = f.readlines()
        
        with open(mode_file, 'w') as f:
            for line in lines:
                if line.startswith("active_mode:"):
                    f.write(f"active_mode: {choice}\n")
                else:
                    f.write(line)
        
        print(f"\n✅ SUCCESS: Protocol updated to {modes[choice]}")
        print(f"📢 Next time you launch the Squad, they will follow the rules of Mode {choice}.")
    else:
        print("❌ Invalid selection. No changes made.")

if __name__ == "__main__":
    main()
