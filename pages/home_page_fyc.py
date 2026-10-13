import logging
from pages.base_page import BasePage
from pages.actions.webpage_actions import WebAppActions

logger = logging.getLogger("framework")


class HomePageFYC(BasePage):
    """FYC home page using Playwright page object model."""

    # Locators for the FYC home page (web XPath/CSS selectors)
    locators = {
        "MENU_BAR": (".//div[contains(@class, 'navbar')]"),
        "MENU_HOME_ICON": (".//button[contains(@class, 'home-icon')]"),
        "MENU_BRAND_ICON": (".//a[contains(@class, 'brand-link')]"),
        "MENU_WATCHLIST_ICON": (".//a[contains(@class, 'watchlist-link')]"),
        "MENU_HELP_ICON": (".//a[contains(@class, 'help-link')]"),
        "MENU_SIGNOUT": (".//a[contains(@class, 'signout-link')]"),
        "HEADER_LOGO": (".//img[contains(@class, 'header-logo')]"),
        "SEARCH_BUTTON": (".//button[contains(@class, 'search-button')]"),
        "SEARCH_BOX_FIELD": (".//input[@placeholder='Search for a title...']"),
        "CAROUSAL_IMAGE": (".//div[contains(@class, 'carousel-image')]"),
        "CAROUSAL_IMAGE_INDICATOR": (".//div[contains(@class, 'carousel-indicator')]//span"),
        "GENRES_TAB": (".//span[contains(text(), 'All Genres')]"),
        "GENRES_DROPDOWN": (".//div[contains(@class, 'genres-dropdown')]"),
        "PROJECT_BANNER": (".//div[contains(@class, 'project-banner')]"),
        "SWIMLANES_LIST": (".//div[contains(@class, 'swimlanes-list')]"),
        "FIRST_SWIMLANE": (".//div[contains(@class, 'swimlane')][1]"),
        "PROJECTS_UNDER_FIRST_SWIMLANE": (".//span[contains(@class, 'project-name')]"),
        "PAGINATION_PROJECT_LISTING": (".//div[contains(@class, 'pagination')]//a"),
        "GENRES_TEXT_SELECTION": (".//span[contains(text(), '{genres}')]"),
        "GENRES_SELECT_DISPLAYED_CONTENT": (".//div[contains(@class, 'genre-content')]"),
        "PROJECT_BANNER_IMAGE": (".//img[contains(@class, 'project-banner-image')]"),
        "SWIMLANE_NAME": (".//span[contains(@class, 'swimlane-name')]"),
    }

    def __init__(self, page):
        super().__init__(page)
        self.actions = WebAppActions(page)
        logger.info("HomePageFYC initialized")

    def verify_menu_bar(self):
        """Verify menu bar is displayed."""
        try:
            menu_bar = self.page.wait_for_selector(self.locators["MENU_BAR"], timeout=3000)
            return menu_bar is not None
        except TimeoutError:
            return False

    def click_on_header_logo(self):
        """Click on header logo."""
        self.actions.wait_for_selector(self.locators["HEADER_LOGO"])
        self.actions.click(self.locators["HEADER_LOGO"])

    def verify_header_logo_in_homepage_screen(self):
        """Verify header logo is displayed on homepage screen."""
        try:
            logo = self.page.wait_for_selector(self.locators["HEADER_LOGO"], timeout=3000)
            return logo is not None
        except TimeoutError:
            return False

    def click_on_Brand_button(self):
        """Click on Brand button."""
        self.actions.wait_for_selector(self.locators["MENU_BRAND_ICON"])
        self.actions.click(self.locators["MENU_BRAND_ICON"])

    def verify_swimlanes_respective_project(self, swimlane_name):
        """Verify swimlanes have respective projects."""
        try:
            swimlane = self.page.wait_for_selector(
                f".//span[contains(@class, 'swimlane-name') and contains(text(), '{swimlane_name}')]", 
                timeout=5000
            )
            return swimlane is not None
        except TimeoutError:
            return False

    def verify_Carousel_view(self):
        """Verify carousel view is displayed."""
        try:
            carousel = self.page.wait_for_selector(self.locators["CAROUSAL_IMAGE"], timeout=3000)
            return carousel is not None
        except TimeoutError:
            return False

    def genres_Dropdown(self):
        """Click on genres dropdown."""
        self.actions.wait_for_selector(self.locators["GENRES_DROPDOWN"])
        self.actions.click(self.locators["GENRES_DROPDOWN"])
        return self

    def genres_Dropdown_Select(self, genres):
        """Select genre from dropdown."""
        # Select the genre by text
        self.actions.wait_for_selector(f".//div[contains(text(), '{genres}')]")
        self.actions.click(f".//div[contains(text(), '{genres}')]")
        return self

    def select_genre_content(self, project_name):
        """Select genre content."""
        try:
            content = self.page.wait_for_selector(
                f".//div[contains(@class, 'project-content') and contains(text(), '{project_name}')]", 
                timeout=5000
            )
            return content is not None
        except TimeoutError:
            return False

    def verify_Search_Field(self):
        """Verify search field is displayed."""
        try:
            search_field = self.page.wait_for_selector(self.locators["SEARCH_BOX_FIELD"], timeout=3000)
            return search_field is not None
        except TimeoutError:
            return False

    def enter_Text_In_Search_Field(self, search_string):
        """Enter text in search field."""
        self.actions.wait_for_selector(self.locators["SEARCH_BOX_FIELD"])
        self.actions.fill(self.locators["SEARCH_BOX_FIELD"], search_string)

    def submit_Search_Button(self):
        """Submit search button."""
        self.actions.wait_for_selector(self.locators["SEARCH_BUTTON"])
        self.actions.click(self.locators["SEARCH_BUTTON"])

    def click_logout_button(self):
        """Click logout button."""
        self.actions.wait_for_selector(self.locators["MENU_SIGNOUT"])
        self.actions.click(self.locators["MENU_SIGNOUT"])

    def genres_Dropdown(self):
        """Click on genres dropdown."""
        self.actions.wait_for_selector(self.locators["GENRES_DROPDOWN"])
        self.actions.click(self.locators["GENRES_DROPDOWN"])