#!/usr/bin/env python
# coding:utf-8
"""
ESSENTIAL PROCESS:
Converts the human-readable Role-Prompts from the core-kms-brain into 
compatible Gemini CLI agent definitions in the obsidian-brain vault.

DATA FLOW:
1. Scans core-kms-brain/Role-Prompts for markdown files.
2. Extracts agent names from folder prefixes.
3. Injects mandatory YAML frontmatter and the [SCAN] restoration block.
4. Writes the final agent markdown to obsidian-brain/.gemini/agents/.

KEY PARAMETERS:
- source_dir: Path to the raw role prompts.
- target_dir: Path to the generated Gemini agent definitions.
"""

from os import listdir as osListdir, makedirs as osMakedirs
from os.path import dirname as osPathDirname, abspath as osPathAbspath, join as osPathJoin, isdir as osPathIsdir
from glob import glob as globGlob

# -----------------------------------------------------------------------------------------------

def _find_workspace_root() -> str:
    """
    Walk up from this script's location until we find the workspace root.
    """
    current = osPathDirname(osPathAbspath(__file__))
    while current != osPathDirname(current):
        if osPathExists(osPathJoin(current, "Bastien-Antigravity.code-workspace")):
            return current
        if osPathIsdir(osPathJoin(current, "obsidian-brain")) and osPathIsdir(osPathJoin(current, "fleet-operation-brain")):
            return current
        current = osPathDirname(current)
    return osPathAbspath(osPathJoin(osPathDirname(osPathAbspath(__file__)), "..", ".."))

def main() -> None:
    workspace_root = _find_workspace_root()

    # Try standalone clone first, fall back to submodule inside obsidian-brain
    source_dir = osPathJoin(workspace_root, "core-kms-brain", "Role-Prompts")
    if not osPathIsdir(source_dir):
        source_dir = osPathJoin(workspace_root, "obsidian-brain", "07-Core-KMS", "Role-Prompts")
    
    target_dir = osPathJoin(workspace_root, "obsidian-brain", ".gemini", "agents")

    osMakedirs(target_dir, exist_ok=True)

    # Map folder names to clean agent names
    for folder in osListdir(source_dir):
        folder_path = osPathJoin(source_dir, folder)
        if osPathIsdir(folder_path):
            md_files = globGlob(osPathJoin(folder_path, "*.md"))
            if md_files:
                md_file = md_files[0]
                # e.g. "04-QA" -> "qa"
                agent_name = folder.split("-", 1)[1].lower() if "-" in folder else folder.lower()
                
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                yaml_frontmatter = f"""---
name: {agent_name}
description: The {agent_name} persona from the Bastien-Antigravity squad.
---
"""
                
                scan_block = f"""
# 💾 STATE MANAGEMENT RULE (CRITICAL)
Before finishing any major task or concluding a session, you MUST use the `obsidian_vault` tool to append a summary of your actions to the local `AI-Session-State.md` file in the target repository. This acts as our Hard-Stop Context Block to prevent memory loss across sessions.

# 🚨 ATTENTION RESTORATION (SCAN METHOD)
To prevent context degradation, you MUST begin EVERY single response with the following SCAN block:

**[SCAN]**
- Role Adherence (Am I strictly acting as the {agent_name}?): [CHECK/MISSED]
- Source Verification (Did I use `obsidian_vault` to check facts?): [CHECK/MISSED]
- State Management (Will I update `AI-Session-State.md` before stopping?): [CHECK/MISSED]

"""
                
                target_file = osPathJoin(target_dir, f"{agent_name}.md")
                with open(target_file, 'w', encoding='utf-8') as f:
                    f.write(yaml_frontmatter + content + "\n" + scan_block)
                print(f"Created agent: {target_file}")

# -----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
