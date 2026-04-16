import os
import sys
import subprocess
from pathlib import Path

def get_repos(root_dir):
    """Finds all root-level directories that look like they contain microservices."""
    repos = []
    for item in Path(root_dir).iterdir():
        if item.is_dir() and not item.name.startswith('.') and item.name != "prompt":
            # Just simple check: does it have a language folder or target config?
            if (item / "go.mod").exists() or (item / "go").exists() or \
               (item / "Cargo.toml").exists() or (item / "rust").exists() or \
               (item / "requirements.txt").exists() or (item / "python").exists():
                repos.append(item)
    return repos

def run_all(action, root_dir):
    repos = get_repos(root_dir)
    print(f"=== Bastien Orchestrator: Discovered {len(repos)} repositories ===")
    
    make_script = Path(__file__).parent / "Build-Wrapper.py"
    if not make_script.exists():
        print("Error: Build-Wrapper.py engine missing from .scripts/")
        sys.exit(1)

    failures = []
    
    for repo in repos:
        print(f"\n--- Processing {repo.name} ---")
        try:
            # We call the Build-Wrapper script to handle the cross-platform stuff
            subprocess.run([sys.executable, str(make_script), action, str(repo)], check=True)
        except subprocess.CalledProcessError:
            failures.append(repo.name)

    print("\n=== Orchestration Summary ===")
    if not failures:
        print(f"SUCCESS: All {len(repos)} repositories passed '{action}' phase.")
    else:
        print(f"FAILURE: The following repos failed during '{action}': {', '.join(failures)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python Multi-Repo-Validator.py <build|test>")
        sys.exit(1)
        
    action = sys.argv[1]
    
    # Run from the root workspace directory
    current_dir = Path(__file__).resolve().parent.parent
    run_all(action, str(current_dir))
