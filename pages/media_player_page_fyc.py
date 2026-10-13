import logging
from pages.base_page import BasePage
from pages.actions.webpage_actions import WebAppActions

logger = logging.getLogger("framework")


class MediaPlayerPageFYC(BasePage):
    """FYC media player page using Playwright page object model."""

    # Locators for the FYC media player page (web XPath/CSS selectors)
    locators = {
        "PLAY_BUTTON": (".//button[contains(@class, 'play-button')]"),
        "PAUSE_BUTTON": (".//button[contains(@class, 'pause-button')]"),
        "PLAY_PROGRESS_BAR": (".//div[contains(@class, 'play-progress')]"),
        "SUBTITLE_ICON": (".//button[contains(@class, 'subtitle-icon')]"),
        "SUBTITLE_OPTIONS": (".//div[contains(@class, 'subtitle-options')]"),
        "MULTIPLE_SUBTITLES": (".//span[contains(@class, 'subtitle-option')]"),
        "PLAY_PROGRESS": (".//span[contains(@class, 'play-progress-value')]"),
        "VIDEO_CONTAINER": (".//video[contains(@class, 'video-player')]"),
        "FULLSCREEN_BUTTON": (".//button[contains(@class, 'fullscreen')]"),
    }

    def __init__(self, page):
        super().__init__(page)
        self.actions = WebAppActions(page)
        logger.info("MediaPlayerPageFYC initialized")

    def click_on_settings_icon(self, scenario_name=None):
        """Click on settings/icon in video player."""
        self.actions.wait_for_selector(self.locators["SUBTITLE_ICON"])
        self.actions.click(self.locators["SUBTITLE_ICON"])
        return self

    def verify_multiple_subtitles_displayed(self):
        """Verify multiple subtitle options are available."""
        try:
            subtitles = self.page.query_selector_all(self.locators["MULTIPLE_SUBTITLES"])
            return len(subtitles) > 1
        except Exception:
            return False

    def click_on_different_subtitle_option(self, subtitle):
        """Click on a different subtitle option."""
        self.actions.wait_for_selector(f".//span[contains(text(), '{subtitle}')]")
        self.actions.click(f".//span[contains(text(), '{subtitle}')]")
        return self

    def play_the_video_to_fullest(self):
        """Play the video to the fullest extent."""
        self.actions.wait_for_selector(self.locators["PLAY_BUTTON"])
        self.actions.click(self.locators["PLAY_BUTTON"])
        # Wait for playback to start
        self.page.wait_for_selector(self.locators["PLAY_PROGRESS"], timeout=10000)
        return True

    def click_on_Playnowbutton(self):
        """Click play now button."""
        self.actions.wait_for_selector(self.locators["PLAY_BUTTON"])
        self.actions.click(self.locators["PLAY_BUTTON"])

    def verify_selected_subtitle_displayed_as_expected_during_playback(self, subtitle):
        """Verify selected subtitle is displayed correctly during playback."""
        try:
            subtitle_elem = self.page.wait_for_selector(
                f".//span[contains(@class, 'selected-subtitle') and contains(text(), '{subtitle}')]", 
                timeout=5000
            )
            return subtitle_elem is not None
        except Exception:
            return False