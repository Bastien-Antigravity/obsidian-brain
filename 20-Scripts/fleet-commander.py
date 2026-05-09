#!/usr/bin/env python
# coding:utf-8
"""
ESSENTIAL PROCESS: Fleet Commander - Mass Git Operations
DATA FLOW: Scans repository folders -> Detects git state -> Commits & Pushes changes
KEY PARAMETERS: 
    - repos: List of repositories to process
    - commit_msg: Standardized commit message
"""

import os
from os.path import join as osPathJoin, exists as osPathExists, abspath as osPathAbspath, dirname as osPathDirname
import subprocess as subProcess
import sys
import argparse
from typing import List, Optional, Tuple

# Standardize terminal output encoding for Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except (AttributeError, Exception):
        pass

# ### COMPONENT CLASS ###

class FleetCommander:
    Name: str = "FleetCommander"

    def __init__(self, base_path: str, config: Optional[object] = None, logger: Optional[object] = None, dry_run: bool = False) -> None:
        self.config = config
        self.logger = logger
        self.base_path: str = base_path
        self.dry_run: bool = dry_run
        self.repos: List[str] = [
            "config-server", "data-ingestor", "distributed-config", "docker-deployment", 
            "enhanced-backtesting", "flexible-logger", "fundamental-analysis", 
            "log-server", "market-observer", "microservice-toolbox", 
            "notif-server", "obsidian-brain", "orderbook-aggregator", 
            "safe-socket", "sandbox-testing", "technical-analysis", 
            "tele-remote", "universal-logger", "web-interface",
            "obsidian-brain/01-Strategic-Nexus", "obsidian-brain/02-Business-BDD",
            "obsidian-brain/03-Tech-Stack", "obsidian-brain/04-Rapid-Prototyping",
            "obsidian-brain/05-Fleet-Operation", "obsidian-brain/07-Core-KMS"
        ]
        self.commit_msg: str = "refactor: ecosystem-wide project DNA standardization and modern UI/code architecture"

    # -----------------------------------------------------------------------------------------------

    def _log(self, message: str, level: str = "info") -> None:
        """Helper to log messages using the injected logger or fallback to print."""
        icons = {"info": "[i]", "success": "[+]", "warning": "[!]", "error": "[X]", "step": "[>]"}
        icon = icons.get(level, "[?]")
        formatted_msg: str = f"{icon} {self.Name} : {message}"
        
        if self.logger and hasattr(self.logger, level):
            getattr(self.logger, level)(formatted_msg)
        else:
            print(formatted_msg)

    def _step(self, repo: str, action: str) -> None:
        """Verbose step indicator."""
        print(f"    {repo.ljust(35)} | {action}...")

    # -----------------------------------------------------------------------------------------------

    def _run_command(self, cmd: str, cwd: str) -> Tuple[str, Optional[str]]:
        """Helper to run shell commands within a specific directory."""
        if self.dry_run and any(x in cmd for x in ["push", "commit", "add"]):
            return f"[DRY-RUN] Executing: {cmd}", None
            
        try:
            result = subProcess.run(
                cmd, cwd=cwd, shell=True, 
                capture_output=True, text=True, check=True
            )
            return result.stdout.strip(), None
        except subProcess.CalledProcessError as e:
            return e.stdout.strip() or "No stdout", e.stderr.strip() or "No stderr"

    # -----------------------------------------------------------------------------------------------

    def execute_fleet_push(self) -> None:
        """Main execution loop for mass git operations."""
        mode_str = " (DRY RUN MODE)" if self.dry_run else ""
        self._log(f"Starting Mass Push Operation{mode_str} ---", "info")
        
        # Pre-flight check
        git_ver, err = self._run_command("git --version", self.base_path)
        if err:
            self._log(f"Git not found! {err}", "error")
            return
        self._log(f"Using {git_ver}", "success")

        results: List[str] = []

        for repo in self.repos:
            repo_path: str = osPathJoin(self.base_path, repo)
            self._log(f"Processing repository: {repo}", "info")
            
            if not osPathExists(repo_path):
                results.append(f"{repo}: [SKIP] Path does not exist")
                continue

            if not osPathExists(osPathJoin(repo_path, ".git")):
                results.append(f"{repo}: [SKIP] Not a git repository")
                continue

            # 1. Get current branch
            self._step(repo, "Detecting branch")
            branch, err = self._run_command("git rev-parse --abbrev-ref HEAD", repo_path)
            if err or branch == "HEAD":
                # Handle detached HEAD or errors
                branch, err = self._run_command("git branch --show-current", repo_path)
                if not branch or branch == "HEAD":
                    self._log(f"{repo} is in detached HEAD. Falling back to 'develop'.", "warning")
                    branch = "develop"
            
            self._step(repo, f"Active branch: {branch}")

            # 2. Stage changes
            self._step(repo, "Staging changes (git add .)")
            self._run_command("git add .", repo_path)

            # 3. Check for changes
            self._step(repo, "Checking status")
            status, _ = self._run_command("git status --porcelain", repo_path)
            if not status:
                self._step(repo, "No changes detected")
                results.append(f"{repo}: [OK] No changes")
                continue

            # 4. Commit
            self._step(repo, f"Committing changes: {self.commit_msg[:30]}...")
            out, err = self._run_command(f'git commit -m "{self.commit_msg}"', repo_path)
            if err:
                self._log(f"{repo} commit failed: {err}", "error")
                results.append(f"{repo}: [ERROR] Commit failed")
                continue

            # 5. Push
            self._step(repo, f"Pushing to origin {branch}")
            out, err = self._run_command(f"git push origin {branch}", repo_path)
            if err:
                self._log(f"{repo} push failed: {err}", "error")
                results.append(f"{repo}: [ERROR] Push failed")
            else:
                success_msg = "[DRY-RUN] Simulated push" if self.dry_run else f"[SUCCESS] Pushed to {branch}"
                self._log(f"{repo} {success_msg.lower()}", "success")
                results.append(f"{repo}: {success_msg}")

        print("\n" + "="*80)
        self._log("FINAL FLEET SUMMARY", "info")
        print("="*80)
        for res in results:
            print(res)

# ### MAIN EXECUTION ###

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FleetCommander - Mass Git Operations")
    parser.add_argument("--dry-run", action="store_true", help="Simulate operations without making changes")
    args = parser.parse_args()

    # Base path is parent of obsidian-brain
    script_dir: str = osPathDirname(osPathAbspath(__file__))
    base_dir: str = osPathAbspath(osPathJoin(script_dir, "..", ".."))
    
    commander = FleetCommander(base_dir, dry_run=args.dry_run)
    commander.execute_fleet_push()
