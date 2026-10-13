import os
import json
import logging
import shutil
import time
from pathlib import Path
from datetime import datetime

import pytest
from playwright.sync_api import sync_playwright

# ── Run‐directory liveness ──────────────────────────────────────────────
RUN_DIR = Path(os.getenv("RUN_DIR", "")).resolve()


def get_run_dir() -> Path:
    """Return the active run directory, creating it on first call."""
    if RUN_DIR and RUN_DIR.is_dir():
        return RUN_DIR
    base = Path(os.getenv("TEST_RESULTS_DIR", "test-results")).resolve()
    base.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    choice = base / f"{ts}_smoke"
    choice.mkdir(parents=True, exist_ok=True)
    return choice


def pytest_configure(config):
    run_dir = get_run_dir()

    # Ensure all artifact directories exist inside the run folder
    os.makedirs(run_dir / "logs", exist_ok=True)
    os.makedirs(run_dir / "screenshots", exist_ok=True)
    os.makedirs(run_dir / "traces", exist_ok=True)
    os.makedirs(run_dir / "allure-results", exist_ok=True)
    os.makedirs(run_dir / "reports", exist_ok=True)

    # ── 1. Execution Log ──────────────────────────────────────────────
    run_log = run_dir / "logs" / f"execution_{datetime.now():%Y%m%d_%H%M%S}.log"
    run_handler = logging.FileHandler(run_log)
    run_handler.setLevel(logging.INFO)
    run_formatter = logging.Formatter(
        "%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)"
    )
    run_handler.setFormatter(run_formatter)
    logger = logging.getLogger("framework")
    logger.setLevel(logging.INFO)
    logger.handlers = []  # Clear any existing handlers
    logger.addHandler(run_handler)

    # ── 2. Errors Log ─────────────────────────────────────────────────
    errors_log = run_dir / "logs" / f"errors_{datetime.now():%Y%m%d_%H%M%S}.log"
    errors_handler = logging.FileHandler(errors_log)
    errors_handler.setLevel(logging.ERROR)
    errors_handler.setFormatter(run_formatter)
    logger.addHandler(errors_handler)

    # ── 3. Dynamically override pytest paths to STRICTLY use run_dir ────
    config.option.alluredir = str(run_dir / "allure-results")
    config.option.htmlpath = str(run_dir / "reports" / "report.html")
    config.option.self_contained_html = True

    # Store run_dir for the sessionfinish hook
    config.run_dir = run_dir


@pytest.fixture(scope="function")
def page(request):
    """Playwright fixture – launches Chromium headless and yields a page."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # ── SauceDemo URL (public website, no auth required) ────────────
        base_url = "https://www.saucedemo.com"
        context = browser.new_context(base_url=base_url)
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Save screenshot on test failure."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            run_dir = get_run_dir()
            safe_name = report.nodeid.replace("::", "_").replace("/", "_").replace("[", "_").replace("]", "_")
            screenshot_dir = run_dir / "screenshots" / "failed"
            screenshot_dir.mkdir(parents=True, exist_ok=True)
            screenshot = screenshot_dir / f"{safe_name}.png"
            page.screenshot(path=str(screenshot), full_page=True)


# WORKSPACE ROOT – where reporting-labs writes its output by default
_WORKSPACE = Path(r"D:\Myvi-Web Auto-python")


def pytest_sessionfinish(session, exitstatus):
    """Generate all reports after all tests finish.

    1. Wait for test completions and file writes.
    2. Move reporting-labs HTML/PDF from workspace root to the run directory.
    3. Delete the root-level reporting-labs/ folder to keep workspace clean.
    4. Generate PDF from the reporting-labs HTML if it doesn't already exist.
    """
    run_dir = getattr(session.config, "run_dir", None)
    if not run_dir:
        return

    # ── Wait a moment for OS/processes to flush all files ────────────────
    time.sleep(3.0)

    # ── 1. Move reporting-labs HTML from workspace root to run directory ───
    src_html = _WORKSPACE / "reporting-labs" / "index.html"
    dst_html = run_dir / "reports" / "reporting-labs.html"

    if src_html.is_file():
        dst_html.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(src_html), str(dst_html))
        print(f"[INFO] Copied reporting-labs HTML to: {dst_html}")
    else:
        print("[INFO] No reporting-labs HTML found at workspace root")

    # ── 2. Move reporting-labs PDF from workspace root to run directory ────
    src_pdf = _WORKSPACE / "reporting-labs" / "report.pdf"
    dst_pdf = run_dir / "reports" / "reporting-labs.pdf"

    if src_pdf.is_file():
        dst_pdf.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(src_pdf), str(dst_pdf))
        print(f"[INFO] Copied reporting-labs PDF to: {dst_pdf}")
    else:
        print("[INFO] No reporting-labs PDF found at workspace root – will generate from HTML")

    # ── 3. Delete the root-level reporting-labs/ folder ─────────────────
    root_reporting = _WORKSPACE / "reporting-labs"
    if root_reporting.is_dir():
        shutil.rmtree(root_reporting)
        print(f"[INFO] Removed root-level reporting-labs/ folder")

    # ── 3.5 Generate PDF from reporting-labs HTML (if PDF not already there) ─
    if not dst_pdf.is_file() and dst_html.is_file():
        print("[INFO] Generating PDF from reporting-labs HTML...")
        async def _render():
            import asyncio
            from playwright.async_api import async_playwright
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                pg = await browser.new_page()
                await pg.goto(f"file://{dst_html.resolve()}")
                await pg.wait_for_load_state("networkidle")
                await pg.pdf(path=str(dst_pdf), print_background=True, format="A4")
                await browser.close()

        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                asyncio.create_task(_render())
            else:
                loop.run_until_complete(_render())
        except RuntimeError:
            asyncio.run(_render())
        print(f"[INFO] PDF generated: {dst_pdf}")

    # ── 4. Verify all expected reports exist ────────────────────────────
    expected_files = [
        run_dir / "reports" / "report.html",        # pytest-html
        run_dir / "reports" / "reporting-labs.html", # reporting-labs HTML
        run_dir / "reports" / "reporting-labs.pdf",  # reporting-labs PDF
    ]
    for f in expected_files:
        if f.is_file():
            print(f"[INFO] Found: {f.name}")
        else:
            print(f"[WARNING] Missing: {f.name}")

    print(f"[INFO] Session finish complete – run dir: {run_dir}")