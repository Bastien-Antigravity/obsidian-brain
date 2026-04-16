import sys
import os
import subprocess
from pathlib import Path

def run_cmd(cmd, cwd):
    print(f"[{cwd}] Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd)
    if result.returncode != 0:
        print(f"Error: Command failed with exit code {result.returncode}")
        sys.exit(result.returncode)

def detect_and_run(target_action, root_dir):
    root_path = Path(root_dir).resolve()
    if not root_path.exists():
        print(f"Error: Directory {root_dir} does not exist.")
        sys.exit(1)

    print(f"=== bastien_make: {target_action} on {root_path.name} ===")

    # 1. Rust Detection
    if (root_path / "Cargo.toml").exists() or (root_path / "rust" / "Cargo.toml").exists():
        rust_dir = root_path / "rust" if (root_path / "rust").exists() else root_path
        if target_action == "build":
            run_cmd(["cargo", "build"], str(rust_dir))
        elif target_action == "test":
            run_cmd(["cargo", "test"], str(rust_dir))

    # 2. Go Detection
    if (root_path / "go.mod").exists() or (root_path / "go" / "go.mod").exists():
        go_dir = root_path / "go" if (root_path / "go").exists() else root_path
        if target_action == "build":
            run_cmd(["go", "build", "./..."], str(go_dir))
        elif target_action == "test":
            run_cmd(["go", "test", "./..."], str(go_dir))

    # 3. Python Detection
    if (root_path / "requirements.txt").exists() or (root_path / "python").exists():
        py_dir = root_path / "python" if (root_path / "python").exists() else root_path
        if target_action == "build":
            # Just do a compile syntax check for Python "builds"
            run_cmd([sys.executable, "-m", "compileall", "."], str(py_dir))
        elif target_action == "test":
            # Default to pytest if it exists, else just unittest
            try:
                run_cmd([sys.executable, "-m", "pytest"], str(py_dir))
            except Exception:
                run_cmd([sys.executable, "-m", "unittest", "discover"], str(py_dir))

    print(f"=== {target_action} completed ===")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python bastien_make.py <build|test> <repo_dir>")
        sys.exit(1)
        
    action = sys.argv[1]
    target = sys.argv[2]
    
    if action not in ["build", "test"]:
        print("Unsupported action. Use build or test.")
        sys.exit(1)
        
    detect_and_run(action, target)
