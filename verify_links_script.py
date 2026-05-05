import os
import re

def get_all_files(root_dir):
    all_files = {}
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), root_dir)
            all_files[rel_path] = rel_path
            all_files[file] = rel_path
            # Also store without extension for .md files
            if file.endswith('.md'):
                name_no_ext = file[:-3]
                all_files[name_no_ext] = rel_path
                path_no_ext = rel_path[:-3]
                all_files[path_no_ext] = rel_path
    return all_files

def verify_links(root_dir):
    all_files = get_all_files(root_dir)
    broken_links = []
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Find [[Link]]
                links = re.findall(r'\[\[(.*?)\]\]', content)
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
                    if os.path.isdir(os.path.join(root_dir, link_target)):
                        continue
                        
                    broken_links.append((file_path, link))
    
    return broken_links

root = '/Users/imac/Desktop/Bastien-Antigravity/obsidian-brain'
broken = verify_links(root)
if broken:
    print(f"Found {len(broken)} broken links:")
    for f, l in broken:
        print(f"{f}: [[{l}]]")
else:
    print("No broken links found.")
