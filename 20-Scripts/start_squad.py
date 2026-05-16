#!/usr/bin/env python
# coding:utf-8
"""
ESSENTIAL PROCESS:
Initializes the Bastien-Antigravity AI Squad Command Center. Handles MCP binding,
pre-session audits, role synchronization, and launches the Gemini CLI.

DATA FLOW:
1. Performs Preflight and Sovereignty audits to detect architecture drift.
2. Synchronizes Role-Prompts to agent definitions (convert_agents.py).
3. Invokes the Mode Selector and applies the protocol (switch_mode.py).
4. Configures the MCP server-filesystem based on mode isolation rules.
5. Launches the Gemini CLI in a re-launchable lifecycle loop.

KEY PARAMETERS:
- vault_root: Resolved path to the Obsidian Brain vault.
- mcp_args: Dynamic arguments for the filesystem MCP server.
"""

import sys
import os
import json
from subprocess import run as subprocessRun
from os.path import abspath as osPathAbspath, join as osPathJoin, dirname as osPathDirname, exists as osPathExists, expanduser as osPathExpanduser, isdir as osPathIsdir

# Add current directory to sys.path to enable library imports
script_dir = osPathDirname(osPathAbspath(__file__))
if script_dir not in sys.path:
    sys.path.append(script_dir)

try:
    from switch_mode import get_mode_choice_interactive, apply_mode_protocol, MODES
except ImportError:
    print("❌ Error: Could not find switch_mode.py in 20-Scripts/")
    sys.exit(1)

# Standardize terminal output encoding for Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except (AttributeError, Exception):
        pass

# -----------------------------------------------------------------------------------------------

def setup_mcp(mode_choice: str) -> None:
    """
    DATA FLOW:
    Resolves vault root and configures the MCP filesystem server.
    Implements the Isolation Protocol by excluding forbidden zones.
    """
    settings_dir = osPathExpanduser("~/.gemini")
    settings_file = osPathJoin(settings_dir, "settings.json")
    
    if not osPathExists(settings_dir):
        os.makedirs(settings_dir, exist_ok=True)
    
    settings = {}
    if osPathExists(settings_file):
        try:
            with open(settings_file, 'r', encoding='utf-8') as f:
                settings = json.load(f)
        except Exception:
            print("⚠️ Warning: Corruption detected in settings.json. Starting fresh.")
    
    if "mcpServers" not in settings:
        settings["mcpServers"] = {}
        
    vault_root = osPathAbspath(osPathJoin(script_dir, ".."))
    
    # --- Dynamic Context Exclusion Logic (The Firewall) ---
    global_excludes = {".obsidian", ".git", ".gemini", "node_modules", "99-Humans", "quick-overview"}
    mode_excludes_map = {
        "1": {"01-Strategic-Nexus", "04-Rapid-Prototyping", "05-Fleet-Operation"},
        "2": {"01-Strategic-Nexus", "02-Business-BDD", "05-Fleet-Operation", "06-Microservices"},
        "3": {"01-Strategic-Nexus", "02-Business-BDD", "04-Rapid-Prototyping"},
        "4": set()
    }
    
    current_excludes = mode_excludes_map.get(mode_choice, set())
    allowed_dirs = []
    
    for item in os.listdir(vault_root):
        if item in global_excludes or item in current_excludes:
            continue
        item_path = osPathJoin(vault_root, item)
        if osPathIsdir(item_path):
            allowed_dirs.append(item_path)
        
    mcp_args = ["-y", "@modelcontextprotocol/server-filesystem"] + allowed_dirs
    
    settings["mcpServers"]["obsidian_vault"] = {
        "command": "npx",
        "args": mcp_args
    }
    
    with open(settings_file, 'w', encoding='utf-8') as f:
        json.dump(settings, f, indent=2)
        
    print(f"✅ MCP Context Boundary defined. Vault bound: {vault_root}")

# -----------------------------------------------------------------------------------------------

def run_preflight() -> None:
    """
    ESSENTIAL PROCESS:
    Runs the full audit chain to ensure the brain is healthy before session start.
    """
    workspace_root = osPathAbspath(osPathJoin(script_dir, "..", ".."))
    
    # Candidates for Preflight and Audit scripts
    scripts = [
        osPathJoin(workspace_root, "core-kms-brain", "Scripts", "Preflight-Check.py"),
        osPathJoin(script_dir, "../07-Core-KMS/Scripts/Preflight-Check.py"),
        osPathJoin(workspace_root, "core-kms-brain", "Scripts", "Brain-Health-Audit.py"),
        osPathJoin(script_dir, "../07-Core-KMS/Scripts/Brain-Health-Audit.py")
    ]
    
    for script in scripts:
        if osPathExists(script):
            print(f"📡 Executing Governance Audit: {os.path.basename(script)}...")
            subprocessRun([sys.executable, script])

def regenerate_agents() -> None:
    """
    DATA FLOW:
    Triggers the multi-AI agent converter to ensure prompts are synchronized.
    """
    convert_script = osPathJoin(script_dir, "convert_agents.py")
    if osPathExists(convert_script):
        print("🔄 Synchronizing AI Squad Roles across adapters...")
        subprocessRun([sys.executable, convert_script])

# -----------------------------------------------------------------------------------------------

def start_engine() -> None:
    """
    FUNCTIONAL ANALYSE:
    Implements the Master Lifecycle Loop. This allows the user to re-launch
    the engine or switch modes without manually restarting the script.
    """
    while True:
        print("\n" + "="*60)
        print("🧠 BASTIEN-ANTIGRAVITY: AI SQUAD COMMAND")
        print("="*60)

        # 1. Verification & Sync
        run_preflight()
        regenerate_agents()

        # 2. Mode Management
        choice = get_mode_choice_interactive()
        if choice:
            apply_mode_protocol(choice)
        else:
            # Re-read current mode if skip
            choice = "4"
            mode_file = osPathJoin(script_dir, "../00-AI-Orchestration/MODE-MANUAL.md")
            if osPathExists(mode_file):
                with open(mode_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.startswith("active_mode:"):
                            choice = line.split(":")[1].strip()
                            break
        
        # 3. Protocol Enforcement
        setup_mcp(choice)
        
        # 4. CLI Execution
        print(f"\n🚀 Firing up the Gemini CLI [Protocol: {choice}]...")
        try:
            if os.name == 'nt':
                subprocessRun(["gemini"], shell=True)
            else:
                subprocessRun(["gemini"])
        except Exception as e:
            print(f"❌ CLI Execution Error: {e}")
            break
            
        # 5. Lifecycle Decision
        print("\n--- 🏁 Session Paused ---")
        decision = input("Re-launch Squad? [y: Yes / n: Exit / s: Switch Mode]: ").lower().strip()
        
        if decision == 's' or decision == 'y':
            continue
        else:
            print("👋 Squad resting. Mission concluded.")
            break

# -----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        start_engine()
    except KeyboardInterrupt:
        print("\n\n👋 Forced exit. Session terminated.")
        sys.exit(0)
