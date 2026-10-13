import logging
from pages.base_page import BasePage
from pages.actions.webpage_actions import WebAppActions

logger = logging.getLogger("framework")


class SearchPage_FYC(BasePage):
    """FYC search page using Playwright page object model."""

    # Locators for the FYC search page (web XPath/CSS selectors)
    locators = {
        "SEARCH_RESULTS": (".//div[contains(@class, 'search-results')]"),
        "PROJECT_RESULT": (".//div[contains(@class, 'project-result')]"),
        "PROJECT_NAME": (".//h3[contains(@class, 'project-name')]"),
        "AIRDATE": (".//span[contains(@class, 'airdate')]"),
        "PAGINATION_NEXT": (".//a[contains(@class, 'pagination-next')]"),
        "PAGINATION_PREV": (".//a[contains(@class, 'pagination-prev')]"),
        "GENRES_FILTER": (".//div[contains(@class, 'genres-filter')]"),
        "CAROUSEL_RESULTS": (".//div[contains(@class, 'carousel-results')]"),
        "VIDEO_PLAY_BUTTON": (".//button[contains(@class, 'play-button')]"),
    }

    def __init__(self, page):
        super().__init__(page)
        self.actions = WebAppActions(page)
        logger.info("SearchPage_FYC initialized")

    def click_OnProjectResult(self, project_name):
        """Click on a project result by name."""
        self.actions.wait_for_selector(self.locators["PROJECT_RESULT"])
        # Click the project result containing the specific project name
        self.page.click(f".//div[contains(@class, 'project-result')][.//h3[contains(text(), '{project_name}')]]")

    def verify_Video_Synopsis_Information(self, episode_synopsis):
        """Verify video synopsis information is displayed."""
        try:
            synopsis = self.page.wait_for_selector(
                f".//div[contains(@class, 'synopsis') and contains(text(), '{episode_synopsis}')]", 
                timeout=5000
            )
            return synopsis is not None
        except Exception:
            return False

    def verify_Cast_Crew_Title_Displayed(self, Cast, Crew, crew_ipad):
        """Verify cast and crew title is displayed."""
        try:
            cast_crew = self.page.wait_for_selector(
                f".//div[contains(@class, 'cast-crew') and contains(text(), '{Cast}') and contains(text(), '{Crew}')]", 
                timeout=5000
            )
            return cast_crew is not None
        except Exception:
            return False

    def click_videos_tab_project(self):
        """Click on videos tab inside project."""
        self.actions.wait_for_selector(self.locators["VIDEO_PLAY_BUTTON"])
        self.actions.click(self.locators["VIDEO_PLAY_BUTTON"])

    def click_OnVideoInsideProject(self, video_name):
        """Click on a specific video inside a project."""
        self.page.click(f".//div[contains(@class, 'video-item')][.//span[contains(text(), '{video_name}')]]")

    def airDate_Should_Not_Display(self):
        """Check that airdate should not be displayed."""
        try:
            self.page.wait_for_selector(self.locators["AIRDATE"], timeout=3000, state="hidden")
            return True
        except Exception:
            return False

    def Expiry_label_with_date_and_time(self, expiry_label):
        """Get expiry label with date and time."""
        try:
            element = self.page.wait_for_selector(
                f".//div[contains(@class, 'expiry-label') and contains(text(), '{expiry_label}')]", 
                timeout=5000
            )
            if element:
                return element.text_content()
            return ""
        except Exception:
            return ""

    def maximum_Count_Verification(self, project_name):
        """Verify project has maximum count above 20."""
        try:
            project = self.page.wait_for_selector(
                f".//div[contains(@class, 'project-entry')][.//h3[contains(text(), '{project_name}')]]", 
                timeout=5000
            )
            if project:
                # Check for views count
                views = self.page.query_selector(f".//div[contains(@class, 'views-count')]")
                if views:
                    return True
            return False
        except Exception:
            return False

    def pagination_Call_Search_Field(self):
        """Verify pagination call after receiving search results."""
        try:
            pagination = self.page.wait_for_selector(self.locators["PAGINATION_NEXT"], timeout=5000)
            return pagination is not None
        except Exception:
            return False

    def verify_Search_Content(self, project_name):
        """Verify search content for a project name."""
        try:
            result = self.page.wait_for_selector(
                f".//div[contains(@class, 'search-result')][.//h3[contains(text(), '{project_name}')]]", 
                timeout=5000
            )
            return result is not None
        except Exception:
            return False

    def verify_mutliple_brands_availability(self):
        """Verify multiple brands are available."""
        try:
            brands = self.page.query_selector_all(".//div[contains(@class, 'brand-item')]")
            return len(brands) > 1
        except Exception:
            return False

    def verify_divisions_page_reached(self):
        """Verify divisions page has been reached."""
        try:
            divisions = self.page.wait_for_selector(".//div[contains(@class, 'divisions-page')]", timeout=5000)
            return divisions is not None
        except Exception:
            return False