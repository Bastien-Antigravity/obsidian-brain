#!/usr/bin/env python
# coding:utf-8
"""
ESSENTIAL PROCESS: Mission Help - Displays a cheat sheet of missions, personas, and keywords.
DATA FLOW: Prints static help content to the terminal to assist the user in AI squad delegation.
KEY PARAMETERS: None
"""

import sys
from typing import Optional

# Standardize terminal output encoding for Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except (AttributeError, Exception):
        pass

# ### COMPONENT CLASS ###

class MissionHelper:
    Name: str = "MissionHelper"

    def __init__(self, config: Optional[object] = None, logger: Optional[object] = None) -> None:
        self.config = config
        self.logger = logger

    # -----------------------------------------------------------------------------------------------

    def print_cheat_sheet(self) -> None:
        """Prints the formatted help content to stdout."""
        print("\n--- 💡 Bastien-Antigravity Squad Cheat Sheet ---")
        
        print("\n👥 The Squad (Available for Delegation)")
        print("   - Orchestrator, Architect, Developer, QA, Sentinel, Oracle,")
        print("     FleetArchitect, FleetCommander, DocMaintainer, Purger.")

        print("\n🛡️ Mode 1: Spec-First")
        print("   > Ask QA to audit @06-Microservices against specs in @02-Business-BDD.")
        
        print("\n🧪 Mode 2: Free-Labs")
        print("   > Ask Developer to build a prototype in @04-Rapid-Prototyping.")
        
        print("\n🛰️ Mode 3: Fleet-Commander")
        print("   > Ask Fleet Commander to sync the ecosystem to the develop branch.")
        
        print("\n🔭 Strategic Oracle")
        print("   > Ask Oracle for a Nexus Pulse on the project trajectory.")
        
        print("\n🔄 Protocols & Maintenance")
        print("   > Ask Sentinel to switch to Mode 2 and update the manual.")
        print("   > Ask DocMaintainer to repair links in the vault and update the MOC.")
        
        print("\n🧹 Cleanup")
        print("   > Ask Purger to audit the vault for redundant files and suggest removals.")
        
        print("\n💾 Session Persistence")
        print("   > \"Restore session state\" (Load context at start)")
        print("   > \"Update AI-Session-State.md with progress\" (Save context at end)")
        
        print("\n🛠️ CLI Utility Commands")
        print("   > /mcp list    (Verify tool availability)")
        print("   > /agents list (See all available squad members)")
        print("   > /help        (Native Gemini CLI help)")

        print("\n💬 Direct Interaction (Tier 1)")
        print("   > [SCAN] Analyze @Ecosystem-Map-MOC.md and suggest next steps.")
        
        print("\n🔑 Keywords & Symbols")
        print("   - [SCAN]   : Mandatory header for every AI response.")
        print("   - @<file> : Use '@' to give the AI a specific file (e.g. @README.md).")
        print("   - !<cmd>  : Use '!' to run terminal commands (e.g. !ls).")
        print("\n-------------------------------------------------\n")

# ### MAIN EXECUTION ###

if __name__ == "__main__":
    helper = MissionHelper()
    helper.print_cheat_sheet()
