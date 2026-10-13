import logging
from pages.base_page import BasePage
from pages.actions.webpage_actions import WebAppActions

logger = logging.getLogger("framework")


class LoginPageCinema(BasePage):
    """Cinema login page using Playwright page object model."""

    # Locators for the cinema login page
    locators = {
        "CLIENT_EMAIL_FIELD": (".//input[@name='username']" ),
        "INTERNAL_EMAIL_FIELD": (".//input[@name='staff']"),
        "INTERNAL_PASSWORD_FIELD": (".//input[@name='password']"),
        "SIGN_IN_BUTTON": (".//button[@class='sign-in-button']"),
    }

    def __init__(self, page):
        super().__init__(page)
        self.actions = WebAppActions(page)
        logger.info("LoginPageCinema initialized")

    def login(self, client_email, internal_email, password):
        """Login to the cinema portal."""
        self.page.goto(self.page.url) if hasattr(self.page, 'url') else None
        self.actions.wait_for_selector(self.locators["CLIENT_EMAIL_FIELD"])
        self.actions.fill(self.locators["CLIENT_EMAIL_FIELD"], client_email)
        self.actions.fill(self.locators["INTERNAL_EMAIL_FIELD"], internal_email)
        self.actions.fill(self.locators["INTERNAL_PASSWORD_FIELD"], password)
        self.actions.click(self.locators["SIGN_IN_BUTTON"])
        logger.info("Login attempt completed")

    def verify_signin_header(self):
        """Verify sign-in header is displayed."""
        # Check for the sign-in header element
        try:
            header = self.page.wait_for_selector("//div[contains(@class, 'signin-header')]", timeout=3000)
            return header is not None
        except Exception:
            return False

    def verify_launch_screen_view(self):
        """Verify launch screen view is present."""
        try:
            launch_image = self.page.wait_for_selector("//img[contains(@class, 'launch-image')]", timeout=3000)
            return launch_image is not None
        except Exception:
            return False

    def verify_bg_image_displayed(self):
        """Verify background image is displayed."""
        try:
            bg_image = self.page.wait_for_selector("//body//img[contains(@class, 'bg-image')]", timeout=3000)
            return bg_image is not None
        except Exception:
            return False

    def verify_cinema_launch_icon(self):
        """Verify cinema launch icon is present."""
        try:
            icon = self.page.wait_for_selector("//img[contains(@class, 'cinema-icon')]", timeout=3000)
            return icon is not None
        except Exception:
            return False

    def verify_signin_header_is_displayed(self):
        """Verify sign in header text is displayed."""
        try:
            header = self.page.wait_for_selector("//h2[contains(text(), 'Sign In')]", timeout=3000)
            return header is not None
        except Exception:
            return False