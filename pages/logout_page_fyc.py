import logging
from pages.base_page import BasePage
from pages.actions.webpage_actions import WebAppActions

logger = logging.getLogger("framework")


class LogoutPageFYC(BasePage):
    """FYC logout page using Playwright page object model (web-only).

    Web equivalents of the original iOS Appium logout actions.
    """

    # Locators for the FYC logout page (web XPath/CSS selectors)
    locators = {
        "LOG_OUT_TXT": (".//div[contains(text(), 'Log out')]"),
        "LOG_OUT_BTN": (".//button[contains(text(), 'Log Out')]"),
        "BACK_BTN": (".//button[contains(text(), 'Back')]"),
        "SIGNIN_HEADER": (".//div[contains(@class, 'signin-header')]"),
    }

    def __init__(self, page):
        super().__init__(page)
        self.actions = WebAppActions(page)
        logger.info("LogoutPageFYC initialized (web-only)")

    def log_out(self, expected_content):
        """Log out from the FYC portal (web equivalent)."""
        self.actions.wait_for_selector(self.locators["LOG_OUT_TXT"])
        self.actions.click(self.locators["LOG_OUT_BTN"])
        logger.info("Logout button clicked (web)")
        return True

    def verify_logout_displayed(self):
        """Verify logout text is displayed."""
        try:
            log_out = self.page.wait_for_selector(self.locators["LOG_OUT_TXT"], timeout=3000)
            return log_out is not None
        except TimeoutError:
            return False

    def click_back_button(self):
        """Click back button."""
        self.actions.wait_for_selector(self.locators["BACK_BTN"])
        self.actions.click(self.locators["BACK_BTN"])
        logger.info("Back button clicked (web)")
        return True

    def verify_signin_header(self):
        """Verify sign-in header is displayed."""
        try:
            header = self.page.wait_for_selector(self.locators["SIGNIN_HEADER"], timeout=3000)
            return header is not None
        except TimeoutError:
            return False