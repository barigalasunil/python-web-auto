import logging
from pytest_bdd import scenarios, given, when, then

from pages.login_page import LoginPage

log = logging.getLogger(__name__)

# Adjust path if your features folder is nested
scenarios("../features/smoke/login.feature")


@given("I launch the Sauce Demo login page")
def launch_sauce_demo_login(page):
    log.info("Launching Sauce Demo login page")
    page.goto("https://www.saucedemo.com")


@when('I log in with "standard_user" and "secret_sauce"')
def login_with_credentials(page):
    log.info("Logging in with standard_user credentials")
    lp = LoginPage(page)
    lp.fill(lp.locators["USERNAME_FIELD"], "standard_user")
    lp.fill(lp.locators["PASSWORD_FIELD"], "secret_sauce")
    lp.click(lp.locators["LOGIN_BUTTON"])


@then('the page title should be "Swag Labs"')
def verify_page_title(page):
    actual = page.title()
    log.info(f"Page title: {actual}")
    assert actual == "Swag Labs", f"Expected title 'Swag Labs', got '{actual}'"


@then('the page URL should contain "/inventory"')
def verify_url_inventory(page):
    expected = "/inventory"
    actual_url = page.url
    log.info(f"Page URL: {actual_url}")
    assert expected in actual_url, f"Expected URL to contain '{expected}', got '{actual_url}'"