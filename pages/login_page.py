"""FYC Login Page Object — Playwright POM (web-only).

No Appium, no Roku, no iOS/Android actions. Uses Playwright page selectors.
"""

import logging
from pages.base_page import BasePage

logger = logging.getLogger("login_page")


class LoginPage(BasePage):
    """FYC login page using Playwright page object model."""

    # Locators for the Sauce Demo login page (CSS selectors with data-test attributes)
    locators = {
        "USERNAME_FIELD": "[data-test='username']",
        "PASSWORD_FIELD": "[data-test='password']",
        "LOGIN_BUTTON": "[data-test='login-button']",
        "SIGNIN_HEADER": ".login_logo",
        "PRODUCTS_CONTAINER": "#header_container .title",
    }

    def fill(self, selector: str, value: str):
        """Fill a field with auto-waiting for selector presence."""
        self.page.wait_for_selector(selector, timeout=5000)
        self.page.fill(selector, value)
        logger.info(f"Filled {selector} with {value}")

    def click(self, selector: str):
        """Click a element with auto-waiting."""
        self.page.wait_for_selector(selector, timeout=5000)
        self.page.click(selector)
        logger.info(f"Clicked: {selector}")