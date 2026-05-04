import os
import glob

source_dir = "/Users/imac/Desktop/Bastien-Antigravity/obsidian-brain/07-Core-KMS/Role-Prompts"
target_dir = "/Users/imac/Desktop/Bastien-Antigravity/obsidian-brain/.gemini/agents"

os.makedirs(target_dir, exist_ok=True)

# Map folder names to clean agent names
for folder in os.listdir(source_dir):
    folder_path = os.path.join(source_dir, folder)
    if os.path.isdir(folder_path):
        md_files = glob.glob(os.path.join(folder_path, "*.md"))
        if md_files:
            md_file = md_files[0]
            # e.g. "04-QA" -> "qa"
            agent_name = folder.split("-", 1)[1].lower() if "-" in folder else folder.lower()
            
            with open(md_file, 'r') as f:
                content = f.read()
            
            # Grant shell access to agents that need it
            shell_agents = ["developer", "fleetcommander", "qa", "purger", "orchestrator"]
            tools_list = ""
            if agent_name in shell_agents:
                tools_list = "\ntools:\n  - shell"

            yaml_frontmatter = f"""---
name: {agent_name}
description: The {agent_name} persona from the Bastien-Antigravity squad.{tools_list}
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
            
            target_file = os.path.join(target_dir, f"{agent_name}.md")
            with open(target_file, 'w') as f:
                f.write(yaml_frontmatter + content + "\n" + scan_block)
            print(f"Created agent: {target_file}")

