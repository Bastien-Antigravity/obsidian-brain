import os
import re

root_dir = "obsidian-brain/02-Business-BDD/02-Behavior-Specs"
hubs_dir = "obsidian-brain/06-Microservices"

domain_map = {
    "config-server": "domain/networking",
    "data-ingestor": "domain/analysis",
    "distributed-config": "domain/networking",
    "enhanced-backtesting": "domain/analysis",
    "flexible-logger": "domain/observability",
    "fundamental-analysis": "domain/analysis",
    "log-server": "domain/observability",
    "market-observer": "domain/analysis",
    "microservice-toolbox": "domain/architecture",
    "notif-server": "domain/interface",
    "ontime-scheduler": "domain/architecture",
    "orderbook-aggregator": "domain/analysis",
    "safe-socket": "domain/networking",
    "sandbox-testing": "domain/architecture",
    "tele-remote": "domain/interface",
    "universal-logger": "domain/observability",
    "web-interface": "domain/interface",
    "technical-analysis": "domain/analysis"
}

def get_hub_link(ms):
    # Try to find the hub file
    for file in os.listdir(hubs_dir):
        if ms.lower() in file.lower() and file.endswith("-Hub.md"):
            return f"[[06-Microservices/{file.replace('.md', '')}|🌐 {ms.capitalize()} Hub]]"
    return None

# First, move root FEAT files to ontime-scheduler if appropriate
root_feats = [f for f in os.listdir(root_dir) if f.startswith("FEAT-") and f.endswith(".md")]
if root_feats:
    os.makedirs(os.path.join(root_dir, "ontime-scheduler"), exist_ok=True)
    for f in root_feats:
        os.rename(os.path.join(root_dir, f), os.path.join(root_dir, "ontime-scheduler", f))

# Process all FEAT files
for root, dirs, files in os.walk(root_dir):
    ms_from_folder = os.path.basename(root)
    if ms_from_folder not in domain_map:
        continue
    
    domain_tag = domain_map[ms_from_folder]
    hub_link = get_hub_link(ms_from_folder)
    
    for file in files:
        if file.startswith("FEAT-") and file.endswith(".md"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            new_lines = []
            in_frontmatter = False
            frontmatter_end = -1
            
            for i, line in enumerate(lines):
                if line.strip() == "---":
                    if not in_frontmatter:
                        in_frontmatter = True
                    else:
                        in_frontmatter = False
                        frontmatter_end = i
                
                if in_frontmatter:
                    if line.startswith("microservice:"):
                        new_lines.append(f"microservice: {ms_from_folder}\n")
                    elif line.startswith("type:"):
                        new_lines.append(f"type: behavior-spec\n")
                    elif line.startswith("tags:"):
                        new_lines.append(line)
                        # We'll add tags later
                    elif line.strip() == "- null":
                        pass # Remove null
                    elif line.strip().startswith("- '#"):
                        new_lines.append(line)
                    else:
                        new_lines.append(line)
                else:
                    new_lines.append(line)
            
            # Insert domain tag if not present
            found_tags = False
            for i, line in enumerate(new_lines):
                if line.startswith("tags:"):
                    new_lines.insert(i+1, f"- {domain_tag}\n")
                    found_tags = True
                    break
            
            # Add backlink after frontmatter if not present
            if hub_link:
                link_line = f"\n*Back-link: {hub_link}*\n"
                if link_line not in "".join(new_lines):
                    new_lines.insert(frontmatter_end + 1, link_line)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)

print("Done processing FEAT files.")
