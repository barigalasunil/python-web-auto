#!/usr/bin/env python
"""Entry point for Playwright smoke/sanity/regression runs."""
import os
import sys
from pathlib import Path

# Ensure the workspace root is on the Python path despite the spaces in the path
WORKSPACE = Path(r"D:\Myvi-Web Auto-python").resolve()
if str(WORKSPACE) not in sys.path:
    sys.path.insert(0, str(WORKSPACE))

# Ensure workspace is CWD-aware for conftest.py base_url fixture
os.chdir(WORKSPACE)

from pytest import main as pytest_main
from utils.artifact_manager import init_run
from utils.logger import setup_logging

def main():
    run_type = sys.argv[1] if len(sys.argv) > 1 else "smoke"
    run_dir = init_run(f"smoke_{run_type}")
    logger = setup_logging(run_dir)
    logger.info(f"Starting {run_type} run, dir={run_dir}")

    # Change CWD to the run directory so reporting-labs writes there
    # reporting-labs defaults to writing to CWD/reporting-labs/
    orig_cwd = os.getcwd()
    os.chdir(run_dir)

    try:
        # Run ONLY the smoke test file
        test_path = WORKSPACE / "steps" / "login_steps.py"
        args = ["--tb=short", str(test_path), "-k", run_type]
        sys.exit(pytest_main(args))
    finally:
        os.chdir(orig_cwd)

if __name__ == "__main__":
    main()