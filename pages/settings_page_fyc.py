import logging
from pages.base_page import BasePage
from pages.actions.webpage_actions import WebAppActions

logger = logging.getLogger("framework")


class SettingsPageFYC(BasePage):
    """FYC settings page using Playwright page object model."""

    # Locators for the FYC settings page (web XPath/CSS selectors)
    locators = {
        "SETTINGS_HEADER": (".//h2[contains(@class, 'settings-header')]"),
        "SERVER_URL_FIELD": (".//input[@name='server']"),
        "COMPANY_NAME_FIELD": (".//input[@name='company']"),
        "API_KEY_FIELD": (".//input[@name='api_key']"),
        "SAVE_BUTTON": (".//button[contains(@class, 'save-button')]"),
        "SIGN_IN_HEADER": (".//div[contains(@class, 'signin-header')]"),
    }

    def __init__(self, page):
        super().__init__(page)
        self.actions = WebAppActions(page)
        logger.info("SettingsPageFYC initialized")

    def set_settings_data(self, serverURL, company_name, API, API_ipad=None):
        """Set settings data on the settings page."""
        self.actions.wait_for_selector(self.locators["SERVER_URL_FIELD"])
        self.actions.fill(self.locators["SERVER_URL_FIELD"], serverURL)
        self.actions.fill(self.locators["COMPANY_NAME_FIELD"], company_name)
        self.actions.fill(self.locators["API_KEY_FIELD"], API)
        self.actions.wait_for_selector(self.locators["SAVE_BUTTON"])
        self.actions.click(self.locators["SAVE_BUTTON"])

    def click_savebutton(self):
        """Click save button."""
        self.actions.wait_for_selector(self.locators["SAVE_BUTTON"])
        self.actions.click(self.locators["SAVE_BUTTON"])

    def verify_signin_header(self):
        """Verify sign-in header is displayed."""
        try:
            header = self.page.wait_for_selector(self.locators["SIGN_IN_HEADER"], timeout=3000)
            return header is not None
        except Exception:
            return False