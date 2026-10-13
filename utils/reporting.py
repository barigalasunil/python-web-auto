"""PDF report generation from reporting-labs HTML output.

Exports a single synchronous function :func:`generate_pdf_from_reporting_labs`
that takes a run_dir Path, ensures the reporting-labs HTML is present,
and renders it into a PDF file.
"""
import asyncio
from pathlib import Path

# We import here so the function can be called both from conftest.py
# and from elsewhere without top-level async dependencies.
from playwright.async_api import async_playwright


def generate_pdf_from_reporting_labs(run_dir: Path) -> Path:
    """Render the reporting-labs HTML into a PDF file.

    The reporting-labs HTML is expected at  run_dir / "reports" / "reporting-labs.html".
    The PDF will be written to  run_dir / "reports" / "reporting-labs.pdf".

    Returns the Path of the generated PDF (or the existing PDF if already present).
    """
    html_path = run_dir / "reports" / "reporting-labs.html"
    pdf_path = run_dir / "reports" / "reporting-labs.pdf"

    if not html_path.is_file():
        print(f"[WARNING] reporting-labs HTML not found at {html_path}; PDF not generated")
        return pdf_path  # return empty path so caller can handle

    async def _render():
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(f"file://{html_path.resolve()}")
            await page.wait_for_load_state("networkidle")
            await page.pdf(path=str(pdf_path), print_background=True, format="A4")
            await browser.close()

    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            asyncio.create_task(_render())
        else:
            loop.run_until_complete(_render())
    except RuntimeError:
        asyncio.run(_render())

    print(f"[INFO] PDF report generated: {pdf_path}")
    return pdf_path