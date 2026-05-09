#!/usr/bin/env python
# coding:utf-8

import os
from os.path import join as osPathJoin, exists as osPathExists, abspath as osPathAbspath, dirname as osPathDirname
import subprocess as subProcess
import sys
from typing import List, Optional, Tuple

"""
ESSENTIAL PROCESS: Fleet Commander - Mass Git Operations
DATA FLOW: Scans repository folders -> Detects git state -> Commits & Pushes changes
KEY PARAMETERS: 
    - repos: List of repositories to process
    - commit_msg: Standardized commit message
"""

# ### COMPONENT CLASS ###

class FleetCommander:
    Name: str = "FleetCommander"

    def __init__(self, base_path: str, config: Optional[object] = None, logger: Optional[object] = None) -> None:
        self.config = config
        self.logger = logger
        self.base_path: str = base_path
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

    def _log(self, message: str) -> None:
        """Helper to log messages using the injected logger or fallback to print."""
        formatted_msg: str = "{0} : {1}".format(self.Name, message)
        if self.logger and hasattr(self.logger, "info"):
            self.logger.info(formatted_msg)
        else:
            print(formatted_msg)

    # -----------------------------------------------------------------------------------------------

    def _run_command(self, cmd: str, cwd: str) -> Tuple[str, Optional[str]]:
        """Helper to run shell commands within a specific directory."""
        try:
            result = subProcess.run(
                cmd, cwd=cwd, shell=True, 
                capture_output=True, text=True, check=True
            )
            return result.stdout.strip(), None
        except subProcess.CalledProcessError as e:
            return e.stdout.strip(), e.stderr.strip()

    # -----------------------------------------------------------------------------------------------

    def execute_fleet_push(self) -> None:
        """Main execution loop for mass git operations."""
        self._log("Starting Mass Push Operation ---")
        results: List[str] = []

        for repo in self.repos:
            repo_path: str = osPathJoin(self.base_path, repo)
            if not osPathExists(osPathJoin(repo_path, ".git")):
                results.append(f"{repo}: [SKIP] Not a git repository")
                continue

            # 1. Get current branch
            branch, err = self._run_command("git rev-parse --abbrev-ref HEAD", repo_path)
            if err:
                results.append(f"{repo}: [ERROR] Failed to get branch: {err}")
                continue

            # 2. Stage changes
            self._run_command("git add .", repo_path)

            # 3. Check for changes
            status, _ = self._run_command("git status --porcelain", repo_path)
            if not status:
                results.append(f"{repo}: [OK] No changes")
                continue

            # 4. Commit
            _, err = self._run_command(f'git commit -m "{self.commit_msg}"', repo_path)
            if err:
                results.append(f"{repo}: [ERROR] Commit failed: {err}")
                continue

            # 5. Push
            _, err = self._run_command(f"git push origin {branch}", repo_path)
            if err:
                results.append(f"{repo}: [ERROR] Push failed: {err}")
            else:
                results.append(f"{repo}: [SUCCESS] Pushed to {branch}")

        self._log("Summary ---")
        for res in results:
            print(res)

# ### MAIN EXECUTION ###

if __name__ == "__main__":
    # Base path is parent of obsidian-brain
    script_dir: str = osPathDirname(osPathAbspath(__file__))
    base_dir: str = osPathAbspath(osPathJoin(script_dir, "..", ".."))
    commander = FleetCommander(base_dir)
    commander.execute_fleet_push()
