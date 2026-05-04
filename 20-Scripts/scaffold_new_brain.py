#!/usr/bin/env python3
import os
import shutil
import subprocess
from pathlib import Path

def main():
    print("\n🏗️  Bastien-Antigravity: Ecosystem Scaffolder")
    print("-------------------------------------------")
    
    target_name = input("Enter new project name (e.g. quantum-finance): ").strip()
    if not target_name:
        print("❌ Error: Project name is required.")
        return
        
    target_path = Path(input(f"Enter destination path [default: ../{target_name}]: ").strip() or f"../{target_name}")
    
    if target_path.exists():
        print(f"❌ Error: Path {target_path} already exists.")
        return

    print(f"\n🚀 Fabricating '{target_name}' at {target_path.absolute()}...")

    # 1. Create Folder Structure
    folders = [
        "00-AI-Orchestration",
        "01-Strategic-Nexus",
        "02-Business-BDD",
        "03-Tech-Stack",
        "04-Rapid-Prototyping",
        "05-Fleet-Operation",
        "06-Microservices",
        "07-Core-KMS/Role-Prompts",
        "10-State-and-Tasks",
        "20-Scripts"
    ]
    
    for folder in folders:
        (target_path / folder).mkdir(parents=True, exist_ok=True)

    # 2. Copy "DNA" (Scripts and Role Prompts)
    current_dir = Path(__file__).resolve().parent.parent
    
    print("🧬 Copying AI Squad DNA...")
    shutil.copytree(current_dir / "07-Core-KMS/Role-Prompts", target_path / "07-Core-KMS/Role-Prompts", dirs_exist_ok=True)
    shutil.copytree(current_dir / "20-Scripts", target_path / "20-Scripts", dirs_exist_ok=True)

    # 3. Create Template Files
    print("📝 Generating Project Compass...")
    
    gemini_md = f"""# 🌌 Project: {target_name}

## 📐 Project DNA
This repository follows the Bastien-Antigravity 2-Digit Standard.

## 🤖 AI Interaction Rules
1. Always use the `obsidian_vault` tool.
2. Every response must begin with a **[SCAN]** block.
3. Update `AI-Session-State.md` before concluding a task.
"""
    with open(target_path / "GEMINI.md", 'w') as f:
        f.write(gemini_md)

    with open(target_path / "README.md", 'w') as f:
        f.write(f"# 🧠 {target_name.replace('-', ' ').title()}\n\nNew Bastien-Antigravity Ecosystem.\n")

    # Copy User Manual
    if (current_dir / "User-Manual.md").exists():
        shutil.copy(current_dir / "User-Manual.md", target_path / "User-Manual.md")

    # 4. Initialize Mode Manual
    mode_content = "active_mode: 1\n\n# Mode Manual\n1: Spec-First\n2: Free-Labs\n3: Fleet-Commander\n"
    (target_path / "00-AI-Orchestration/MODE-MANUAL.md").write_text(mode_content)

    # 5. Run Agent Conversion in the new project
    print("🤖 Baking the AI Squad into the new ecosystem...")
    subprocess.run(["python3", "20-Scripts/convert_agents.py"], cwd=target_path)

    print(f"\n✅ SUCCESS! Your new Command Center is ready at: {target_path.absolute()}")
    print(f"👉 To start: cd {target_path} && python3 20-Scripts/start_squad.py\n")

if __name__ == "__main__":
    main()
