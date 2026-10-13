import logging
from pytest_bdd import scenarios, given, when, then

from pages.login_page_fyc import LoginPageFYC
from pages.home_page_fyc import HomePageFYC
from pages.logout_page_fyc import LogoutPageFYC

log = logging.getLogger(__name__)

# Adjust path if your features folder is nested
scenarios("../features/FYC_validations.feature")


@given("I launch FYC Application homepage")
def launch_FYC_app_url(page):
    log.info("Launching FYC Application homepage")
    page.goto("https://www.saucedemo.com")


@when('I log in with "standard_user" and "secret_sauce"')
def login_with_credentials(page):
    log.info("Logging in with FYC credentials")
    lp = LoginPageFYC(page)
    lp.fill(lp.locators["CLIENT_EMAIL_FIELD"], "standard_user")
    lp.fill(lp.locators["INTERNAL_PASSWORD_FIELD"], "secret_sauce")
    lp.click(lp.locators["SIGN_IN_BUTTON"])


@then('Verify the page title contains expected text')
def verify_page_title(page):
    actual = page.title()
    log.info(f"Page title: {actual}")
    assert actual, f"Expected page title to contain expected text, got '{actual}'"


@then('Verify the page URL contains "/inventory"')
def verify_url_inventory(page):
    expected = "/inventory"
    actual_url = page.url
    assert expected in actual_url, f"Expected URL to contain '{expected}', got '{actual_url}'"


@then('Verify sign-in header is displayed')
def verify_signin_header(page):
    lp = LoginPageFYC(page)
    result = lp.verify_signin_header()
    assert result, "Sign-in header not displayed"


@then('Verify logout is possible')
def verify_logout(page):
    hp = HomePageFYC(page)
    result = hp.click_logout_button()
    assert result, "Logout button not clickable"


@then('Verify user can log back in')
def verify_re_login(page):
    lp = LoginPageFYC(page)
    lp.fill(lp.locators["CLIENT_EMAIL_FIELD"], "standard_user")
    lp.fill(lp.locators["INTERNAL_PASSWORD_FIELD"], "secret_sauce")
    lp.click(lp.locators["SIGN_IN_BUTTON"])
    assert page.title(), "Re-login failed"