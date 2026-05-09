import os
import re

root_dir = "obsidian-brain/02-Business-BDD/02-Behavior-Specs"
mapping = {}

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.startswith("FEAT-") and file.endswith(".md"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                match = re.search(r'microservice:\s*(.*)', content)
                if match:
                    ms = match.group(1).strip()
                    if ms not in mapping:
                        mapping[ms] = []
                    mapping[ms].append(file.replace(".md", ""))

for ms, feats in mapping.items():
    print(f"[{ms}]")
    for feat in feats:
        print(f"  - {feat}")

