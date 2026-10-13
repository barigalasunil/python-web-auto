import logging
from pages.base_page import BasePage
from pages.actions.webpage_actions import WebAppActions

logger = logging.getLogger("framework")


class BrandPageFYC(BasePage):
    """FYC brand page using Playwright page object model."""

    # Locators for the FYC brand page (web XPath/CSS selectors)
    locators = {
        "DIVISIONS_PAGE": (".//div[contains(@class, 'divisions-page')]"),
        "BRAND_ITEMS": (".//div[contains(@class, 'brand-item')]"),
        "SELECT_A_BRAND_TITLE": (".//h2[contains(text(), 'Select a brand')]"),
        "MULTIPLE_BRANDS": (".//span[contains(text(), 'Multiple Brands')]"),
        "SEARCH_FIELD": (".//input[@placeholder='Search']"),
    }

    def __init__(self, page):
        super().__init__(page)
        self.actions = WebAppActions(page)
        logger.info("BrandPageFYC initialized")

    def verify_mutliple_brands_availability(self):
        """Verify multiple brands are available."""
        try:
            brands = self.page.query_selector_all(self.locators["BRAND_ITEMS"])
            return len(brands) > 1
        except Exception:
            return False

    def verify_divisions_page_reached(self):
        """Verify divisions page has been reached."""
        try:
            divisions = self.page.wait_for_selector(self.locators["DIVISIONS_PAGE"], timeout=5000)
            return divisions is not None
        except Exception:
            return False

    def verify_select_a_brand_title(self):
        """Verify Select a brand title is displayed."""
        try:
            title = self.page.wait_for_selector(self.locators["SELECT_A_BRAND_TITLE"], timeout=3000)
            return title is not None
        except Exception:
            return False

    def verify_mutliple_brands_availability(self):
        """Verify multiple brands are available."""
        try:
            brands = self.page.query_selector_all(self.locators["BRAND_ITEMS"])
            return len(brands) > 1
        except Exception:
            return False

    def help_page_header_verification(self):
        """Verify help page header."""
        try:
            header = self.page.wait_for_selector(".//h1[contains(@class, 'help-page-header')]", timeout=3000)
            return header is not None
        except Exception:
            return False

    def help_Section_Contents(self, expected_content, browsing_shows, selected_shows,
                              settings_and_features, streaming_issues, expecteedd_loggingout):
        """Verify help section contents."""
        try:
            # Check for expected content
            content_elem = self.page.wait_for_selector(
                f".//div[contains(@class, 'help-content') and contains(text(), '{expected_content}')]", 
                timeout=5000
            )
            return content_elem is not None
        except Exception:
            return False

    def select_brand_option_admin(self):
        """Select brand option for admin."""
        self.actions.wait_for_selector(self.locators["SELECT_A_BRAND_TITLE"])
        self.actions.click(self.locators["SELECT_A_BRAND_TITLE"])

    def select_brand_option(self, brand, roku_brandIndex):
        """Select brand option (web equivalent)."""
        # Web equivalent - select by brand name
        self.actions.wait_for_selector(f".//span[contains(text(), '{brand}')]")
        self.actions.click(f".//span[contains(text(), '{brand}')]")

    def select_brand_option_based_on_text(self, brand_with_text, roku_brandIndex):
        """Select brand option based on text (web equivalent)."""
        self.actions.wait_for_selector(f".//div[contains(text(), '{brand_with_text}')]")
        self.actions.click(f".//div[contains(text(), '{brand_with_text}')]")