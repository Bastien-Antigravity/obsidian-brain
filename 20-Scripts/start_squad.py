#!/usr/bin/env python3
import json
import os
import sys
import subprocess

def setup_mcp():
    settings_dir = os.path.expanduser("~/.gemini")
    settings_file = os.path.join(settings_dir, "settings.json")
    
    os.makedirs(settings_dir, exist_ok=True)
    
    # Load existing config or create new
    if os.path.exists(settings_file):
        with open(settings_file, 'r') as f:
            try:
                settings = json.load(f)
            except json.JSONDecodeError:
                print("⚠️ Warning: Existing settings.json is corrupted. Starting fresh.")
                settings = {}
    else:
        settings = {}
        
    # Ensure mcpServers block exists
    if "mcpServers" not in settings:
        settings["mcpServers"] = {}
        
    # Add obsidian_vault configuration
    # Automatically resolves the path to the vault root (one level up from this script)
    obsidian_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    settings["mcpServers"]["obsidian_vault"] = {
        "command": "npx",
        "args": [
            "-y",
            "@modelcontextprotocol/server-filesystem",
            obsidian_path
        ]
    }
    
    # Save back
    with open(settings_file, 'w') as f:
        json.dump(settings, f, indent=2)
        
    print(f"✅ Successfully configured 'obsidian_vault' MCP server in {settings_file}")
    print(f"📁 Target vault bound to: {obsidian_path}")

def select_mode():
    modes = {
        "1": ("🛡️ Spec-First", "High safety, BDD mandatory."),
        "2": ("🧪 Free-Labs", "High speed, experimental."),
        "3": ("🛰️ Fleet-Commander", "Global sync, multi-repo.")
    }
    
    print("\n--- 🕹️ Select Operational Mode ---")
    for key, (name, desc) in modes.items():
        print(f"[{key}] {name.ljust(18)} : {desc}")
    
    choice = input("\nSelect mode [1-3] (default: keep current): ").strip()
    
    if choice in modes:
        mode_file = os.path.join(os.path.dirname(__file__), "../00-AI-Orchestration/MODE-MANUAL.md")
        with open(mode_file, 'r') as f:
            lines = f.readlines()
        
        with open(mode_file, 'w') as f:
            for line in lines:
                if line.startswith("active_mode:"):
                    f.write(f"active_mode: {choice}\n")
                else:
                    f.write(line)
        
        print(f"✅ Mode switched to: {modes[choice][0]}")
    else:
        print("➡️ Keeping current mode as defined in MODE-MANUAL.md")

def print_mission_examples():
    print("\n--- 💡 Mission Cheat Sheet (Copy-Paste Ready) ---")
    print("\n🛡️ Mode 1: Spec-First")
    print("   > Ask QA to use the obsidian_vault tool to compare microservices in @06-Microservices ")
    print("     against specs in @02-Business-BDD. [SCAN] Audit for missing specs.")
    
    print("\n🧪 Mode 2: Free-Labs")
    print("   > Ask Developer to build a rapid prototype for a new UI dashboard in @04-Rapid-Prototyping. ")
    print("     [SCAN] Priority: Speed over Docs.")
    
    print("\n🛰️ Mode 3: Fleet-Commander")
    print("   > Ask Fleet Commander to add all changes, commit with 'chore: sync', ")
    print("     and push to the develop branch. [SCAN] Goal: Global Sync.")
    print("\n-------------------------------------------------\n")

def main():
    print("\n🧠 Initializing Bastien-Antigravity AI Squad...")
    select_mode()
    setup_mcp()
    print_mission_examples()
    
    print("\n🚀 Firing up the Gemini CLI...")
    print("   (To test delegation, try: 'Ask QA to review the sandbox standards')\n")
    try:
        # Hand over control to the gemini CLI
        subprocess.run(["gemini"])
    except FileNotFoundError as e:
        print(f"\n❌ Error: The 'gemini' CLI command was not found. -> {e}")
        print("Please make sure it's installed and available in your PATH.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nSession terminated. Squad resting.")

if __name__ == "__main__":
    main()
