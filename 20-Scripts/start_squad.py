#!/usr/bin/env python
# coding:utf-8
"""
ESSENTIAL PROCESS:
Initializes the Bastien-Antigravity AI Squad by configuring MCP servers,
selecting the operational mode, and launching the Gemini CLI.

DATA FLOW:
1. Reads/Writes ~/.gemini/settings.json to bind the obsidian_vault.
2. Updates 00-AI-Orchestration/MODE-MANUAL.md based on user selection.
3. Spawns the 'gemini' CLI subprocess.

KEY PARAMETERS:
- modes: Dict of available operational protocols.
- obsidian_path: Resolved path to the vault root.
"""

from os import name as osName, makedirs as osMakedirs
from os.path import expanduser as osPathExpanduser, exists as osPathExists, abspath as osPathAbspath, join as osPathJoin, dirname as osPathDirname
from json import load as jsonLoad, dump as jsonDump, JSONDecodeError as jsonJSONDecodeError
from sys import exit as sysExit, executable as sysExecutable
from subprocess import run as subprocessRun

# -----------------------------------------------------------------------------------------------

def setup_mcp() -> None:
    settings_dir = osPathExpanduser("~/.gemini")
    settings_file = osPathJoin(settings_dir, "settings.json")
    
    osMakedirs(settings_dir, exist_ok=True)
    
    # Load existing config or create new
    if osPathExists(settings_file):
        with open(settings_file, 'r', encoding='utf-8') as f:
            try:
                settings = jsonLoad(f)
            except jsonJSONDecodeError:
                print("⚠️ Warning: Existing settings.json is corrupted. Starting fresh.")
                settings = {}
    else:
        settings = {}
        
    # Ensure mcpServers block exists
    if "mcpServers" not in settings:
        settings["mcpServers"] = {}
        
    # Add obsidian_vault configuration
    # Automatically resolves the path to the vault root (one level up from this script)
    obsidian_path = osPathAbspath(osPathJoin(osPathDirname(__file__), ".."))
    
    settings["mcpServers"]["obsidian_vault"] = {
        "command": "npx",
        "args": [
            "-y",
            "@modelcontextprotocol/server-filesystem",
            obsidian_path
        ]
    }
    
    # Save back
    with open(settings_file, 'w', encoding='utf-8') as f:
        jsonDump(settings, f, indent=2)
        
    print(f"✅ Successfully configured 'obsidian_vault' MCP server in {settings_file}")
    print(f"📁 Target vault bound to: {obsidian_path}")

# -----------------------------------------------------------------------------------------------

def select_mode() -> None:
    modes = {
        "1": ("🛡️ Spec-First", "High safety, BDD mandatory."),
        "2": ("🧪 Free-Labs", "High speed, experimentions."),
        "3": ("🛰️ Fleet-Commander", "Global sync, multi-repo."),
        "4": ("🥷 Direct-Action", "Bypass mode logic, sporadically used.")
    }
    
    print("\n--- 🕹️ Select Operational Mode ---")
    for key, (name, desc) in modes.items():
        print(f"[{key}] {name.ljust(18)} : {desc}")
    
    choice = input("\nSelect mode [1-4] (default: keep current): ").strip()
    
    if choice == "4":
        print("✅ Mode: Direct-Action (No changes to MODE-MANUAL.md)")
        return

    if choice in modes:
        mode_file = osPathJoin(osPathDirname(__file__), "../00-AI-Orchestration/MODE-MANUAL.md")
        with open(mode_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        with open(mode_file, 'w', encoding='utf-8') as f:
            for line in lines:
                if line.startswith("active_mode:"):
                    f.write(f"active_mode: {choice}\n")
                else:
                    f.write(line)
        
        print(f"✅ Mode switched to: {modes[choice][0]}")
    else:
        print("➡️ Keeping current mode as defined in MODE-MANUAL.md")

# -----------------------------------------------------------------------------------------------

def print_mission_examples() -> None:
    print("\n--- 💡 Mission Cheat Sheet (Copy-Paste Ready) ---")
    print("\n🛡️ Mode 1: Spec-First")
    print("   > Ask QA to audit @06-Microservices against specs in @02-Business-BDD.")
    
    print("\n🧪 Mode 2: Free-Labs")
    print("   > Ask Developer to build a rapid prototype in @04-Rapid-Prototyping.")
    
    print("\n🛰️ Mode 3: Fleet-Commander")
    print("   > Ask Fleet Commander to sync the ecosystem to the develop branch.")
    
    print("\n🔄 Changing Protocols")
    print("   > Ask Sentinel to switch to Mode 2 and update the manual.")
    
    print("\n🧹 Maintenance")
    print("   > Ask DocMaintainer to repair links in the vault and update the MOC.")
    print(f"   > !{sysExecutable} 20-Scripts/convert_agents.py (Regenerate Squad)")
    
    print("\n💬 Direct Interaction (Tier 1)")
    print("   > [SCAN] Analyze @Ecosystem-Map-MOC.md and suggest next steps.")
    
    print("\n🔑 Keywords & Personas")
    print("   - [SCAN]   : Mandatory header for every AI response.")
    print("   - @<file> : Mention a file for context.")
    print("   - !<cmd>  : Execute a shell command.")
    print("   - Squad   : Orchestrator, Architect, Developer, QA, Sentinel, Oracle,")
    print("               FleetArchitect, FleetCommander, DocMaintainer, Purger.")
    print("\n-------------------------------------------------\n")

# -----------------------------------------------------------------------------------------------

def run_preflight() -> None:
    """
    Runs the Preflight-Check.py from core-kms-brain to detect and auto-fix drift.
    """
    script_dir = osPathDirname(osPathAbspath(__file__))
    workspace_root = osPathAbspath(osPathJoin(script_dir, "..", ".."))
    preflight_script = osPathJoin(workspace_root, "core-kms-brain", "Scripts", "Preflight-Check.py")
    
    if osPathExists(preflight_script):
        print("\n🛫 Running Preflight Check...")
        subprocessRun([sysExecutable, preflight_script])
    else:
        print("\n⚠️ Preflight-Check.py not found at {0} — skipping.".format(preflight_script))

# -----------------------------------------------------------------------------------------------

def main() -> None:
    print("\n🧠 Initializing Bastien-Antigravity AI Squad...")
    run_preflight()
    select_mode()
    setup_mcp()
    print_mission_examples()
    
    print("\n🚀 Firing up the Gemini CLI...")
    print("   (To test delegation, try: 'Ask QA to review the sandbox standards')\n")
    try:
        # Hand over control to the gemini CLI
        if osName == 'nt':
            subprocessRun(["gemini"], shell=True)
        else:
            subprocessRun(["gemini"])
    except FileNotFoundError as e:
        print(f"\n❌ Error: The 'gemini' CLI command was not found. -> {e}")
        print("Please make sure it's installed and available in your PATH.")
        sysExit(1)
    except KeyboardInterrupt:
        print("\n\nSession terminated. Squad resting.")

# -----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
