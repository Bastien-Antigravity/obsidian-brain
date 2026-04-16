#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Masque dans Obsidian les dossiers ne contenant aucun fichier .md
(directement ou dans leurs sous-dossiers), via génération CSS.

Structure attendue :
Bastien-Antigravity/
├── .obsidian/
├── obsidian-brain/
│   └── 05-Scripts/
│       └── hide_empty_folders.py   <-- ce script
"""

import os
from pathlib import Path

# ==========================================================
# LOCALISATION AUTOMATIQUE
# ==========================================================

SCRIPT_DIR = Path(__file__).resolve().parent

# On remonte de 'obsidian-brain/05-Scripts' vers la racine 'Bastien-Antigravity'
VAULT_ROOT = SCRIPT_DIR.parents[1]

OBSIDIAN_DIR = VAULT_ROOT / ".obsidian"
SNIPPETS_DIR = OBSIDIAN_DIR / "snippets"
CSS_FILE = SNIPPETS_DIR / "hide_empty_folders.css"

# dossiers à ignorer totalement
IGNORE_DIRS = {
    ".obsidian",
    ".git",
    "__pycache__",
    "node_modules",
}

# ==========================================================
# OUTILS
# ==========================================================

def contains_md_recursive(folder: Path) -> bool:
    """
    True si ce dossier contient au moins un .md
    dans lui-même ou n'importe quel sous-dossier.
    """
    for root, dirs, files in os.walk(folder):
        # Ignore technical directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            if file.lower().endswith(".md"):
                return True

    return False


def css_escape(path_str: str) -> str:
    """
    Echappe guillemets pour sélecteur CSS.
    """
    return path_str.replace("\\", "/").replace('"', '\\"')


# ==========================================================
# SCAN
# ==========================================================

folders_to_hide = []

for root, dirs, files in os.walk(VAULT_ROOT):
    root_path = Path(root)

    # ignorer dossiers techniques
    dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

    # ne pas traiter la racine elle-même
    if root_path == VAULT_ROOT:
        continue

    # Si le dossier ne contient aucun .md récursivement, on le masque
    if not contains_md_recursive(root_path):
        rel_path = root_path.relative_to(VAULT_ROOT).as_posix()
        folders_to_hide.append(rel_path)

# ==========================================================
# GENERATION CSS
# ==========================================================

SNIPPETS_DIR.mkdir(parents=True, exist_ok=True)

lines = [
    "/* Fichier généré automatiquement par hide_empty_folders.py */",
    "/* Masque les dossiers ne contenant aucune documentation (.md) dans le sidebar */",
    "",
]

for rel_path in sorted(folders_to_hide):
    safe = css_escape(rel_path)
    # Target both the folder title and its children container
    lines.append(
        f'.nav-folder-title[data-path="{safe}"],'
    )
    lines.append(
        f'.nav-folder-title[data-path="{safe}"] + .nav-folder-children {{ display: none !important; }}'
    )

CSS_FILE.write_text("\n".join(lines), encoding="utf-8")

print(f"CSS généré : {CSS_FILE}")
print(f"Dossiers masqués : {len(folders_to_hide)}")
print("")
print("Dans Obsidian :")
print("Settings > Appearance > CSS Snippets > activer hide_empty_folders.css")
