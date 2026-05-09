#!/usr/bin/env python
# coding:utf-8

import os
import re
from typing import Dict, List, Optional, Tuple

"""
ESSENTIAL PROCESS: Fix Feats - Standardizes FEAT markdown files across the obsidian-brain.
DATA FLOW: Scans specified directories -> Parses frontmatter -> Applies domain tags and backlinks -> Updates files.
KEY PARAMETERS: 
    - root_dir: Path to behavior specs.
    - hubs_dir: Path to microservice hubs.
"""

# ### COMPONENT CLASS ###

class FeatFixer:
    Name: str = "FeatFixer"

    def __init__(self, config: Optional[object] = None, logger: Optional[object] = None) -> None:
        self.config = config
        self.logger = logger
        self.root_dir: str = "obsidian-brain/02-Behavior-Specs"
        self.hubs_dir: str = "obsidian-brain/06-Microservices"
        self.domain_map: Dict[str, str] = {
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

    # -----------------------------------------------------------------------------------------------

    def _get_hub_link(self, ms: str) -> Optional[str]:
        """Try to find the hub file for a given microservice."""
        if not os.path.exists(self.hubs_dir):
            return None
            
        for file in os.listdir(self.hubs_dir):
            if ms.lower() in file.lower() and file.endswith("-Hub.md"):
                return f"[[06-Microservices/{file.replace('.md', '')}|🌐 {ms.capitalize()} Hub]]"
        return None

    # -----------------------------------------------------------------------------------------------

    def _move_root_feats(self) -> None:
        """Move root FEAT files to ontime-scheduler if appropriate."""
        if not os.path.exists(self.root_dir):
            return

        root_feats: List[str] = [f for f in os.listdir(self.root_dir) if f.startswith("FEAT-") and f.endswith(".md")]
        if root_feats:
            target_dir: str = os.path.join(self.root_dir, "ontime-scheduler")
            if not os.path.exists(target_dir):
                os.makedirs(target_dir, exist_ok=True)
            for f in root_feats:
                os.rename(os.path.join(self.root_dir, f), os.path.join(target_dir, f))

    # -----------------------------------------------------------------------------------------------

    def process_feats(self) -> None:
        """Iterates through all FEAT files and applies standardization rules."""
        self._move_root_feats()

        for root, dirs, files in os.walk(self.root_dir):
            ms_from_folder: str = os.path.basename(root)
            if ms_from_folder not in self.domain_map:
                continue
            
            domain_tag: str = self.domain_map[ms_from_folder]
            hub_link: Optional[str] = self._get_hub_link(ms_from_folder)
            
            for file in files:
                if file.startswith("FEAT-") and file.endswith(".md"):
                    self._process_single_file(os.path.join(root, file), ms_from_folder, domain_tag, hub_link)

    # -----------------------------------------------------------------------------------------------

    def _process_single_file(self, file_path: str, ms_from_folder: str, domain_tag: str, hub_link: Optional[str]) -> None:
        """Processes a single FEAT file to update frontmatter and backlinks."""
        with open(file_path, 'r', encoding='utf-8') as f:
            lines: List[str] = f.readlines()
        
        new_lines: List[str] = []
        in_frontmatter: bool = False
        frontmatter_end: int = -1
        
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
                elif line.strip() == "- null":
                    pass # Remove null
                elif line.strip().startswith("- '#"):
                    new_lines.append(line)
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        
        # Insert domain tag if not present
        found_tags: bool = False
        for i, line in enumerate(new_lines):
            if line.startswith("tags:"):
                new_lines.insert(i+1, f"- {domain_tag}\n")
                found_tags = True
                break
        
        # Add backlink after frontmatter if not present
        if hub_link:
            link_line: str = f"\n*Back-link: {hub_link}*\n"
            if link_line not in "".join(new_lines):
                new_lines.insert(frontmatter_end + 1, link_line)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

# ### MAIN EXECUTION ###

if __name__ == "__main__":
    fixer = FeatFixer()
    fixer.process_feats()
    print(f"{FeatFixer.Name} : Done processing FEAT files.")
