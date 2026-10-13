import logging
from pathlib import Path

logger = logging.getLogger("framework")


class BasePage:
    """Base page object for web automation using Playwright."""

    def __init__(self, page):
        self.page = page
        logger.info("BasePage initialized with Playwright page object")

    def goto(self, url):
        """Navigate to a URL."""
        self.page.goto(url)
        logger.info(f"Navigated to {url}")

    def wait_for_selector(self, selector, timeout=5000):
        """Wait for a selector to be visible."""
        self.page.wait_for_selector(selector, timeout=timeout)
        logger.info(f"Selector visible: {selector}")

    def click(self, selector):
        """Click on an element."""
        self.page.click(selector)
        logger.info(f"Clicked: {selector}")

    def fill(self, selector, value):
        """Fill an input field with a value."""
        self.page.fill(selector, value)
        logger.info(f"Filled {selector} with {value}")

    def get_text(self, selector):
        """Get text content of an element."""
        return self.page.text_content(selector)

    def screenshot(self, path=None):
        """Take a screenshot."""
        if path is None:
            path = f"screenshots/{time.strftime('%Y%m%d_%H%M%S')}.png"
        self.page.screenshot(path=path)
        logger.info(f"Screenshot saved to {path}")

    def get_title(self):
        """Get page title."""
        return self.page.title()

    def get_url(self):
        """Get current URL."""
        return self.page.url