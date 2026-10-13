import logging
from datetime import datetime

logger = logging.getLogger("framework")


class WebAppActions:
    """Web action layer using Playwright page object model."""

    def __init__(self, page):
        self.page = page
        logger.info("WebAppActions initialized with Playwright page")

    def wait_for_selector(self, selector, timeout=5000):
        """Wait for a selector to be visible."""
        self.page.wait_for_selector(selector, timeout=timeout / 1000)  # Playwright uses seconds
        logger.info(f"Selector visible: {selector}")
        return self

    def click(self, selector):
        """Click on an element."""
        self.page.click(selector)
        logger.info(f"Clicked: {selector}")
        return self

    def click_no_wait(self, selector):
        """Click on an element without waiting."""
        self.page.click(selector)
        logger.info(f"Clicked (no wait): {selector}")
        return self

    def fill(self, selector, value):
        """Fill an input field with a value.
        
        Uses page.locator() which supports both CSS and XPath selectors.
        """
        self.page.locator(selector).fill(value)
        logger.info(f"Filled {selector} with {value}")
        return self

    def get_text(self, selector):
        """Get text content of an element."""
        text = self.page.text_content(selector)
        logger.info(f"Got text from {selector}: {text}")
        return text

    def get_attribute(self, selector, attribute):
        """Get an attribute value of an element."""
        return self.page.get_attribute(selector, attribute)

    def press(self, selector, key):
        """Press a key in an element."""
        self.page.click(selector)
        self.page.keyboard.press(key)
        logger.info(f"Pressed {key} on {selector}")
        return self

    def screenshot(self, path=None):
        """Take a screenshot."""
        if path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = f"screenshots/{timestamp}.png"
        self.page.screenshot(path=path)
        logger.info(f"Screenshot saved to {path}")
        return self

    def hover(self, selector):
        """Hover over an element."""
        self.page.hover(selector)
        logger.info(f"Hovered over: {selector}")
        return self

    def select_option(self, selector, option_value):
        """Select an option from a dropdown."""
        self.page.select_option(selector, label=option_value)
        logger.info(f"Selected option: {option_value} from {selector}")
        return self

    def get_dialog(self):
        """Handle JavaScript dialogs."""
        # Playwright auto-handles dialogs with on_dialog callback
        return None