#!/usr/bin/env python
# coding:utf-8
"""
ESSENTIAL PROCESS:
Verifies the integrity of internal [[Links]] within the Obsidian vault by 
mapping all available files and directories.

DATA FLOW:
1. Crawls the vault to build a dictionary of all files (with and without extensions).
2. Parses every .md file for [[Link]] patterns.
3. Normalizes link targets by removing aliases and anchors.
4. Validates existence against the file map and disk directories.
5. Reports all broken links to the terminal.

KEY PARAMETERS:
- VAULT_ROOT: The target directory for link verification.
"""

from os import walk as osWalk
from os.path import relpath as osPathRelpath, join as osPathJoin, isdir as osPathIsdir, dirname as osPathDirname, abspath as osPathAbspath
from re import findall as reFindall
from typing import Dict, List, Tuple
from sys import stdout as sysStdout

# Standardize terminal output encoding for Windows
if sysStdout.encoding != 'utf-8':
    try:
        sysStdout.reconfigure(encoding='utf-8')
    except (AttributeError, Exception):
        pass

# ### HELPERS ###

def get_all_files(root_dir: str) -> Dict[str, str]:
    """
    Builds a map of all files in the vault to support various linking styles.
    """
    all_files = {}
    for root, dirs, files in osWalk(root_dir):
        for file in files:
            rel_path = osPathRelpath(osPathJoin(root, file), root_dir)
            all_files[rel_path] = rel_path
            all_files[file] = rel_path
            # Also store without extension for .md files
            if file.endswith('.md'):
                name_no_ext = file[:-3]
                all_files[name_no_ext] = rel_path
                path_no_ext = rel_path[:-3]
                all_files[path_no_ext] = rel_path
    return all_files

# -----------------------------------------------------------------------------------------------

def verify_links(root_dir: str) -> List[Tuple[str, str]]:
    """
    Scans markdown files for broken internal links.
    """
    all_files = get_all_files(root_dir)
    broken_links = []
    
    for root, dirs, files in osWalk(root_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = osPathJoin(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Find [[Link]]
                links = reFindall(r'\[\[(.*?)\]\]', content)
                for link in links:
                    # Remove alias and anchor
                    link_target = link.split('|')[0].split('#')[0]
                    if not link_target.strip():
                        continue
                        
                    # Normalize path
                    link_target = link_target.lstrip('/')
                    
                    if link_target in all_files:
                        continue
                    
                    # Check if it's a directory (Obsidian sometimes links to folders)
                    if osPathIsdir(osPathJoin(root_dir, link_target)):
                        continue
                        
                    broken_links.append((file_path, link))
    
    return broken_links

# -----------------------------------------------------------------------------------------------

def main() -> None:
    """
    Entry point for the link verification script.
    """
    # Resolve root relative to script location
    vault_root = osPathAbspath(osPathDirname(__file__))
    
    broken = verify_links(vault_root)
    if broken:
        print("Found {0} broken links:".format(len(broken)))
        for f, l in broken:
            print("{0}: [[{1}]]".format(f, l))
    else:
        print("No broken links found.")

# -----------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
