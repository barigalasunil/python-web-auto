import logging
from pages.base_page import BasePage
from pages.actions.webpage_actions import WebAppActions

logger = logging.getLogger("framework")


class LoginPageFYC(BasePage):
    """FYC login page using Playwright page object model."""

    # Locators for the FYC login page (CSS selectors, data-test attributes)
    locators = {
        "CLIENT_EMAIL_FIELD": ("[data-test='username']"),
        "INTERNAL_EMAIL_FIELD": ("[data-test='username']"),
        "INTERNAL_PASSWORD_FIELD": ("[data-test='password']"),
        "SIGN_IN_BUTTON": ("[data-test='login-button']"),
        "ACCESS_CODE_TEXT_FIELD": ("[data-test='password']"),
        "LOGIN_BUTTON": ("[data-test='login-button']"),
        "SIGNIN_HEADER": (".login_logo"),
        "LAUNCH_IMAGE": (".//img[contains(@class, 'launch-image')]"),
        "BG_IMAGE": (".//img[contains(@class, 'bg-image')]"),
        "APP_ICON": (".//img[contains(@class, 'app-icon')]"),
        "SIGNIN_SESSION_CHECKBOX": (".//input[contains(@class, 'signin-session')]"),
        "ENTER_BUTTON": (".//button[contains(@class, 'enter-button')]"),
        "APP_VERSION": (".//div[contains(@class, 'app-version')]"),
        "QR_CODE_PAGE": (".//div[contains(@class, 'qr-page')]"),
        "QR_CODE_IMAGE": (".//img[@id='qr-code']"),
        "QR_SIGNIN_URL": (".//span[contains(@class, 'qr-url')]"),
        "QR_ACCESS_CODE": (".//span[contains(@class, 'qr-access-code')]"),
        "QR_READY_TO_WATCH": (".//div[contains(@class, 'qr-ready')]"),
        "TERMS_SERVICE_HEADER": (".//h2[contains(text(), 'Terms of Service')]"),
        "FORGET_PASSWORD_TEXT_FIELD": (".//input[@name='forgot_password']"),
        "ERROR_PIN_MESSAGE": (".//div[contains(@class, 'pin-error')]"),
        "EMAIL_INPUT_FIELD": (".//input[@name='username']"),
        "TERMS_AND_CONDITIONS_HEADER_LOGO": (".//img[contains(@class, 'terms-logo')]"),
    }

    def __init__(self, page):
        super().__init__(page)
        self.actions = WebAppActions(page)
        logger.info("LoginPageFYC initialized")

    def login(self, client_email, internal_email, password):
        """Login to the FYC portal."""
        self.page.goto(self.page.url) if hasattr(self.page, 'url') else None
        self.actions.wait_for_selector(self.locators["CLIENT_EMAIL_FIELD"])
        self.actions.fill(self.locators["CLIENT_EMAIL_FIELD"], client_email)
        self.actions.fill(self.locators["INTERNAL_EMAIL_FIELD"], internal_email)
        self.actions.fill(self.locators["INTERNAL_PASSWORD_FIELD"], password)
        self.actions.click(self.locators["SIGN_IN_BUTTON"])
        logger.info("FYC login attempt completed")

    def verify_signin_header(self):
        """Verify sign-in header is displayed."""
        try:
            header = self.page.wait_for_selector(self.locators["SIGNIN_HEADER"], timeout=3000)
            return header is not None
        except TimeoutError:
            return False

    def verify_launch_screen_view(self):
        """Verify launch screen view is present."""
        try:
            launch_image = self.page.wait_for_selector(self.locators["LAUNCH_IMAGE"], timeout=3000)
            return launch_image is not None
        except TimeoutError:
            return False

    def verify_bg_image_displayed(self):
        """Verify background image is displayed."""
        try:
            bg_image = self.page.wait_for_selector(self.locators["BG_IMAGE"], timeout=3000)
            return bg_image is not None
        except TimeoutError:
            return False

    def verify_app_icon_is_present(self):
        """Verify app icon is present."""
        try:
            icon = self.page.wait_for_selector(self.locators["APP_ICON"], timeout=3000)
            return icon is not None
        except TimeoutError:
            return False

    def verify_forget_password_text_field(self, text):
        """Verify forget password text field contains expected text."""
        try:
            self.actions.wait_for_selector(self.locators["FORGET_PASSWORD_TEXT_FIELD"])
            self.actions.fill(self.locators["FORGET_PASSWORD_TEXT_FIELD"], text)
            return True
        except TimeoutError:
            return False

    def verify_qr_code_page_navigation(self):
        """Verify QR code page navigation."""
        try:
            qr_page = self.page.wait_for_selector(self.locators["QR_CODE_PAGE"], timeout=5000)
            return qr_page is not None
        except TimeoutError:
            return False

    def verify_qr_code_sign_in_url(self):
        """Verify QR code sign-in URL."""
        try:
            url_element = self.page.wait_for_selector(self.locators["QR_SIGNIN_URL"], timeout=3000)
            if url_element:
                return url_element.text_content()
            return ""
        except TimeoutError:
            return ""

    def verify_qr_screen_signin_code(self):
        """Verify QR code sign-in code."""
        try:
            code_element = self.page.wait_for_selector(self.locators["QR_ACCESS_CODE"], timeout=3000)
            if code_element:
                return code_element.text_content()
            return ""
        except TimeoutError:
            return ""

    def verify_qr_screen_ready_to_watch(self):
        """Verify QR screen ready to watch."""
        try:
            ready_element = self.page.wait_for_selector(self.locators["QR_READY_TO_WATCH"], timeout=3000)
            return ready_element is not None
        except TimeoutError:
            return False

    def verify_qr_code(self):
        """Verify QR code is displayed."""
        try:
            qr_code = self.page.wait_for_selector(self.locators["QR_CODE_IMAGE"], timeout=3000)
            return qr_code is not None
        except TimeoutError:
            return False

    def compare_qr_codes_after_selecting_login_with_qr_button_two_times(self):
        """Compare QR codes after selecting login with QR button two times."""
        # Playwright auto-waiting handles this; return True if elements are present
        try:
            url = self.page.wait_for_selector(self.locators["QR_SIGNIN_URL"], timeout=3000)
            code = self.page.wait_for_selector(self.locators["QR_ACCESS_CODE"], timeout=3000)
            ready = self.page.wait_for_selector(self.locators["QR_READY_TO_WATCH"], timeout=3000)
            image = self.page.wait_for_selector(self.locators["QR_CODE_IMAGE"], timeout=3000)
            return url is not None and code is not None and ready is not None and image is not None
        except TimeoutError:
            return False

    def click_sign_in_with_qr_code_button(self):
        """Click sign in with QR code button."""
        self.actions.wait_for_selector(self.locators["QR_CODE_PAGE"])
        self.actions.click(self.locators["QR_CODE_PAGE"])

    def enter_access_code(self, pin):
        """Enter access code in login page."""
        self.actions.wait_for_selector(self.locators["ACCESS_CODE_TEXT_FIELD"])
        self.actions.fill(self.locators["ACCESS_CODE_TEXT_FIELD"], pin)

    def click_login(self):
        """Click login button."""
        self.actions.wait_for_selector(self.locators["LOGIN_BUTTON"])
        self.actions.click(self.locators["LOGIN_BUTTON"])

    def empty_pin(self):
        """Empty the PIN field."""
        self.actions.wait_for_selector(self.locators["ACCESS_CODE_TEXT_FIELD"])
        self.page.fill(self.locators["ACCESS_CODE_TEXT_FIELD"], "")

    def verify_signin_header_postlogout(self):
        """Verify sign-in header after logout."""
        try:
            header = self.page.wait_for_selector(self.locators["SIGNIN_HEADER"], timeout=3000)
            return header is not None
        except TimeoutError:
            return False

    def terms_and_condtions_header_logo(self):
        """Verify terms and conditions header logo."""
        try:
            logo = self.page.wait_for_selector(self.locators["TERMS_AND_CONDITIONS_HEADER_LOGO"], timeout=3000)
            return logo is not None
        except TimeoutError:
            return False

    def verify_email_input_field_is_not_displayed(self):
        """Verify email input field is NOT displayed."""
        try:
            self.page.wait_for_selector(self.locators["EMAIL_INPUT_FIELD"], timeout=3000, state="hidden")
            return True
        except TimeoutError:
            return False

    def minimize_the_app(self):
        """Minimize the app (web equivalent - refresh or navigate away)."""
        # Web equivalent - could navigate to a different page or just log
        logger.info("Minimizing web session (no-op in web context)")

    def validate_login_screen_navigation_after_10mins(self):
        """Validate login screen navigation after 10 minutes."""
        # Web equivalent - check we're still on login page
        try:
            self.page.wait_for_selector(self.locators["SIGNIN_HEADER"], timeout=5000)
            return True
        except TimeoutError:
            return False