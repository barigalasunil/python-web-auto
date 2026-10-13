import logging
import sys
from pathlib import Path


def setup_logging(run_dir: Path) -> logging.Logger:
    """Set up an execution-aware logger that writes ONLY to the run directory.

    Creates a logger named 'framework' with a FileHandler pointing at
    run_dir / 'logs' / 'execution.log'.  All other handlers are cleared
    so no output escapes the run folder.
    """
    logger = logging.getLogger("framework")
    logger.setLevel(logging.INFO)
    logger.handlers = []  # clear any root handlers

    log_file = run_dir / "logs" / "execution.log"
    log_file.parent.mkdir(parents=True, exist_ok=True)

    handler = logging.FileHandler(log_file, encoding="utf-8")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Also add a simple ConsoleHandler so pytest -v still shows something
    # (but only at CRITICAL level so it doesn't spam the terminal)
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.CRITICAL)
    console.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(console)

    logger.info(f"Logging initialised – run directory: {run_dir}")
    return logger