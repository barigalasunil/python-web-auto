import logging
from pages.base_page import BasePage
from pages.actions.webpage_actions import WebAppActions

logger = logging.getLogger("framework")


class WatchListPageFYC(BasePage):
    """FYC watchlist page using Playwright page object model."""

    # Locators for the FYC watchlist page (web XPath/CSS selectors)
    locators = {
        "WATCHLIST_TAB": (".//a[contains(@class, 'watchlist-tab')]"),
        "WATCHLIST_PROJECTS": (".//div[contains(@class, 'watchlist-project')]"),
        "ADDED_PROJECT": (".//span[contains(@class, 'added-project')]"),
        "REMOVE_BUTTON": (".//button[contains(@class, 'remove-button')]"),
        "CHRONOLOGICAL_LIST": (".//ol[contains(@class, 'chronological-list')]"),
    }

    def __init__(self, page):
        super().__init__(page)
        self.actions = WebAppActions(page)
        logger.info("WatchListPageFYC initialized")

    def click_on_watchlist(self):
        """Click on watchlist tab."""
        self.actions.wait_for_selector(self.locators["WATCHLIST_TAB"])
        self.actions.click(self.locators["WATCHLIST_TAB"])

    def verify_projects_are_displayed_in_chronological_list(self, project_name):
        """Verify projects are displayed in chronological order."""
        try:
            project = self.page.wait_for_selector(
                f".//li[contains(@class, 'chronological-item')][.//span[contains(text(), '{project_name}')]]", 
                timeout=5000
            )
            return project is not None
        except Exception:
            return False

    def click_on_watchlist_menuoption(self):
        """Click on watchlist menu option."""
        self.actions.wait_for_selector(self.locators["WATCHLIST_TAB"])
        self.actions.click(self.locators["WATCHLIST_TAB"])

    def Remove_watchlist(self):
        """Remove from watchlist."""
        self.actions.wait_for_selector(self.locators["REMOVE_BUTTON"])
        self.actions.click(self.locators["REMOVE_BUTTON"])