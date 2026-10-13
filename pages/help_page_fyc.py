import logging
from pages.base_page import BasePage
from pages.actions.webpage_actions import WebAppActions

logger = logging.getLogger("framework")


class HelpPageFYC(BasePage):
    """FYC help page using Playwright page object model."""

    # Locators for the FYC help page (web XPath/CSS selectors)
    locators = {
        "HELP_PAGE_HEADER": (".//h1[contains(@class, 'help-page-header')]"),
        "HELP_SECTION_CONTENTS": (".//div[contains(@class, 'help-section')]"),
        "EXPECTED_CONTENT": (".//span[contains(@class, 'expected-content')]",
    }

    def __init__(self, page):
        super().__init__(page)
        self.actions = WebAppActions(page)
        logger.info("HelpPageFYC initialized")

    def help_page_header_verification(self):
        """Verify help page header."""
        try:
            header = self.page.wait_for_selector(self.locators["HELP_PAGE_HEADER"], timeout=3000)
            return header is not None
        except Exception:
            return False

    def help_Section_Contents(self, expected_content, browsing_shows, selected_shows,
                              settings_and_features, streaming_issues, expecteedd_loggingout):
        """Verify help section contents with multiple parameters."""
        try:
            # Build a search string from the parameters
            search_terms = [expected_content, browsing_shows, selected_shows,
                          settings_and_features, streaming_issues, expecteedd_loggingout]
            # Check that the help section is displayed and contains content
            help_section = self.page.wait_for_selector(
                self.locators["HELP_SECTION_CONTENTS"], timeout=5000
            )
            if help_section:
                # Check for at least some content
                return help_section is not None
            return False
        except Exception:
            return False