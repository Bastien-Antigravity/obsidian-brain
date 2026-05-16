#!/usr/bin/env python
# coding:utf-8
"""
🛡️ SOVEREIGNTY ENGINE (Core Library)
Centralized validation logic for the Bastien-Antigravity Obsidian Brain.
Enforces DocMaintainer and Sentinel rules with high reliability.
"""

import re
from pathlib import Path
from typing import Dict, Set

class Sovereignty:
    # --- Configuration ---
    REQUIRED_YAML = ["microservice", "type", "status"]
    MANDATORY_TAG_ROOTS = ["#type/", "#state/"]
    
    # --- Result Structure ---
    def __init__(self):
        self.errors = []
        self.warnings = []

    def log_error(self, message: str):
        self.errors.append(message)

    def log_warning(self, message: str):
        self.warnings.append(message)

    # --- Validation Methods ---

    def validate_frontmatter(self, content: str, file_name: str) -> bool:
        """Checks for mandatory YAML frontmatter fields."""
        if not content.startswith("---"):
            self.log_error(f"[{file_name}] Missing YAML frontmatter.")
            return False

        parts = content.split("---", 2)
        if len(parts) < 3:
            self.log_error(f"[{file_name}] Malformed YAML frontmatter.")
            return False

        yaml_block = parts[1]
        missing = [f for f in self.REQUIRED_YAML if f"{f}:" not in yaml_block]
        
        for field in missing:
            self.log_error(f"[{file_name}] Missing mandatory field: '{field}'")
            
        return len(missing) == 0

    def validate_taxonomy(self, content: str, file_name: str):
        """Ensures #type/ and #state/ tags are present."""
        for tag_root in self.MANDATORY_TAG_ROOTS:
            if tag_root not in content:
                self.log_warning(f"[{file_name}] Missing recommended taxonomy tag: '{tag_root}'")

    def validate_links(self, content: str, file_name: str, valid_stems: Set[str], valid_paths: Set[str]):
        """Identifies broken [[Links]]."""
        # Extract [[Link]] or [[Link|Alias]]
        links = re.findall(r'\[\[([^|\]]+)(?:\|[^\]]*)?\]\]', content)
        
        for link in links:
            clean_link = link.strip().replace("\\", "/")
            link_stem = Path(clean_link).stem
            
            # Check against stems, full relative paths, or exact filenames
            if clean_link in valid_stems or clean_link in valid_paths or link_stem in valid_stems:
                continue
                
            # If it's a direct file reference with extension
            if any(clean_link.endswith(ext) for ext in [".md", ".json"]):
                # This would need a full file list to be perfect, 
                # for now we flag it if not in paths
                if clean_link not in valid_paths:
                    self.log_error(f"[{file_name}] Broken link: [[{link}]]")
            else:
                # Assume .md if no extension
                if f"{clean_link}.md" not in valid_paths:
                    self.log_error(f"[{file_name}] Broken link: [[{link}]]")

    def validate_telemetry(self, content: str, file_name: str):
        """Ensures Roles have the [SCAN] block."""
        if "Role-" in file_name or "Prompt-" in file_name:
            if "[SCAN]" not in content:
                self.log_error(f"[{file_name}] Role file missing mandatory [SCAN] telemetry block.")

    def validate_utc_mandate(self, content: str, file_name: str):
        """Heuristic check for prohibited local time references."""
        # Very basic check for common local time indicators if they aren't followed by 'UTC' or 'Z'
        # This is a warning-only check as it can have false positives
        local_time_patterns = [
            r'\d{1,2}:\d{2} (AM|PM)(?!.*UTC)',
            r'Local Time',
            r'Heure locale'
        ]
        for pattern in local_time_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                self.log_warning(f"[{file_name}] Potential 'Local Time' detected. Ensure UTC mandate is followed.")

    def validate_session_state(self, content: str, file_name: str):
        """Checks for Mission-ID in session states."""
        if "AI-Session-State" in file_name:
            if not re.search(r'Mission-ID:|Trace-ID:|X-Bastien-Mission-ID', content, re.IGNORECASE):
                self.log_error(f"[{file_name}] Session state entry missing Mission/Trace ID.")

    # --- Orchestration ---

    def audit_file(self, path: Path, valid_stems: Set[str], valid_paths: Set[str]):
        """Runs the full suite against a single file."""
        if not path.suffix == ".md":
            return

        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            file_name = path.name
            
            self.validate_frontmatter(content, file_name)
            self.validate_taxonomy(content, file_name)
            self.validate_links(content, file_name, valid_stems, valid_paths)
            self.validate_telemetry(content, file_name)
            self.validate_utc_mandate(content, file_name)
            self.validate_session_state(content, file_name)
            
        except Exception as e:
            self.log_error(f"Failed to read {path.name}: {str(e)}")

    def auto_fix_file(self, path: Path):
        """Fixes taxonomy issues like missing # on domain tags and injecting #service tags."""
        if not path.suffix == ".md":
            return
            
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            original_content = content
            
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    yaml_block = parts[1]
                    
                    # Fix domain/ missing #
                    yaml_block = re.sub(r'-\s+domain/([^\s\'"\n]+)', r"- '#domain/\1'", yaml_block)
                    yaml_block = re.sub(r'-\s+[\'"]domain/([^\'"]+)[\'"]', r"- '#domain/\1'", yaml_block)
                    
                    # Inject #service tag based on microservice key
                    micro_match = re.search(r'^microservice:\s*([^\n\s]+)', yaml_block, re.MULTILINE)
                    if micro_match:
                        service_name = micro_match.group(1).strip("'\"")
                        if service_name and service_name.lower() != "null":
                            service_tag = f"#service/{service_name}"
                            if "tags:" in yaml_block and service_tag not in yaml_block:
                                yaml_block = re.sub(r'(tags:\s*\n)', r'\1- \'' + service_tag + r'\'\n', yaml_block)
                                
                    if yaml_block != parts[1]:
                        content = f"---{yaml_block}---{parts[2]}"
            
            if content != original_content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                    
        except Exception as e:
            self.log_warning(f"Auto-fix failed for {path.name}: {str(e)}")

    def get_report(self) -> Dict:
        return {
            "errors": self.errors,
            "warnings": self.warnings,
            "success": len(self.errors) == 0
        }

