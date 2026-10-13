import os
import datetime
from pathlib import Path

_WORKSPACE = Path(r"D:\Myvi-Web Auto-python").resolve()


def init_run(execution_type: str = "smoke") -> Path:
    """Create and return the active run directory.

    Naming: test-results/YYYY-MM-DD_HH-MM-SS_<type>
    Sub-directories created: logs/, screenshots/, allure-results/, traces/, reports/
    Returns the Path of the new directory.
    """
    ts = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_name = f"{ts}_{execution_type}"
    run_dir = _WORKSPACE / "test-results" / run_name

    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "logs").mkdir(parents=True, exist_ok=True)
    (run_dir / "screenshots").mkdir(parents=True, exist_ok=True)
    (run_dir / "allure-results").mkdir(parents=True, exist_ok=True)
    (run_dir / "traces").mkdir(parents=True, exist_ok=True)
    (run_dir / "reports").mkdir(parents=True, exist_ok=True)

    # persist the run directory path as env var so conftest.py can find it
    os.environ["RUN_DIR"] = str(run_dir)
    os.environ["TEST_RUN_TYPE"] = execution_type
    return run_dir