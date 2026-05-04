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
    # Automatically resolves the path to the current directory where this script lives
    obsidian_path = os.path.abspath(os.path.dirname(__file__))
    
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

def main():
    print("\n🧠 Initializing Bastien-Antigravity AI Squad...")
    setup_mcp()
    
    print("\n🚀 Firing up the Gemini CLI...")
    print("   (To test delegation, try: 'Ask QA to review the sandbox standards')\n")
    try:
        # Hand over control to the gemini CLI
        subprocess.run(["gemini"])
    except FileNotFoundError:
        print("\n❌ Error: The 'gemini' CLI command was not found.")
        print("Please make sure it's installed and available in your PATH.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nSession terminated. Squad resting.")

if __name__ == "__main__":
    main()
