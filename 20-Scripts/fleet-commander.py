#!/usr/bin/env python
# coding:utf-8

import os
import subprocess
import sys

"""
ESSENTIAL PROCESS: Fleet Commander - Mass Git Operations
DATA FLOW: Scans repository folders -> Detects git state -> Commits & Pushes changes
KEY PARAMETERS: 
    - repos: List of repositories to process
    - commit_msg: Standardized commit message
"""

class FleetCommander:
    Name = "FleetCommander"

    def __init__(self, base_path):
        self.base_path = base_path
        self.repos = [
            "data-ingestor", "distributed-config", "docker-deployment", 
            "enhanced-backtesting", "flexible-logger", "fundamental-analysis", 
            "log-server", "market-observer", "microservice-toolbox", 
            "notif-server", "obsidian-brain", "orderbook-aggregator", 
            "safe-socket", "sandbox-testing", "technical-analysis", 
            "tele-remote", "universal-logger", "web-interface"
        ]
        self.commit_msg = "refactor: ecosystem-wide project DNA standardization and modern UI/code architecture"

    def run_command(self, cmd, cwd):
        """Helper to run shell commands within a specific directory."""
        try:
            result = subprocess.run(
                cmd, cwd=cwd, shell=True, 
                capture_output=True, text=True, check=True
            )
            return result.stdout.strip(), None
        except subprocess.CalledProcessError as e:
            return e.stdout.strip(), e.stderr.strip()

    def execute_fleet_push(self):
        print(f"--- {self.Name}: Starting Mass Push Operation ---")
        results = []

        for repo in self.repos:
            repo_path = os.path.join(self.base_path, repo)
            if not os.path.exists(os.path.join(repo_path, ".git")):
                results.append(f"{repo}: [SKIP] Not a git repository")
                continue

            # 1. Get current branch
            branch, err = self.run_command("git rev-parse --abbrev-ref HEAD", repo_path)
            if err:
                results.append(f"{repo}: [ERROR] Failed to get branch: {err}")
                continue

            # 2. Stage changes
            self.run_command("git add .", repo_path)

            # 3. Check for changes
            status, _ = self.run_command("git status --porcelain", repo_path)
            if not status:
                results.append(f"{repo}: [OK] No changes")
                continue

            # 4. Commit
            _, err = self.run_command(f'git commit -m "{self.commit_msg}"', repo_path)
            if err:
                results.append(f"{repo}: [ERROR] Commit failed: {err}")
                continue

            # 5. Push
            _, err = self.run_command(f"git push origin {branch}", repo_path)
            if err:
                results.append(f"{repo}: [ERROR] Push failed: {err}")
            else:
                results.append(f"{repo}: [SUCCESS] Pushed to {branch}")

        print("\n--- Summary ---")
        for res in results:
            print(res)

if __name__ == "__main__":
    # Base path is parent of obsidian-brain
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    commander = FleetCommander(base_dir)
    commander.execute_fleet_push()
