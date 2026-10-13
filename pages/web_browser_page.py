from pages.actions.webpage_actions import WebAppActions
from pages.base_page import BasePage
# from conftest import launchBrowser
from selenium.webdriver.common.by import By
from pages.actions.android_actions import AndroidActions
import time
from conftest import readPreReqJsonValue
from pages.base_page import BasePage
from pages.login_page import LoginPage

locators = {
    'USERNAME_QR_LOGIN': (By.XPATH, "//input[@name='Email']"),
    'INVALID_MESSAGE': (By.ID, "form-error-message"),
    'PASSWORD_FIELD_BLANK_MESSAGE': (By.ID, 'tv-sign-in-password-error-message'),
    'PASSWORD_QR_LOGIN': (By.ID, "tv-sign-in-password"),
    'SIGN_IN_QR_LOGIN': (By.ID, "tv-sign-in-button"),
    'SUCCESSFULL_MESSAGE_QR_LOGIN': (By.ID, "email-send-success-message"),
    'EMPTY_PASSWORD_ERROR_MESSAGE': (By.ID, "tv-sign-in-password-error-message"),
    'EMPTY_USERNAME_ERROR_MESSAGE': (By.ID, "tv-sign-in-email-error-message"),
    'LOGIN_ACCCESS_CODE': (By.ID, "tv-sign-in-tv-code")
}


class WebBrowserPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
       
    def launch_browser_page(self, url):
        # self.actions = WebAppActions(self.driver)
        WebAppActions(self.driver).launch_browser_url(self.driver, url)
        print("browser launched with URL ", url)
    
    # def qr_Invalid_Credentilas_Field(self, username, password):
    #     self.actions.wait_for_element(self.locator['USERNAME_QR_LOGIN'], username)
    #     self.actions.enter_text(self.locator['USERNAME_QR_LOGIN'], username)
    #     self.actions.enter_text(self.locator['PASSWORD_QR_LOGIN'], password)
    #     self.actions.click_button(self.locator['SIGN_IN_QR_LOGIN'])

    def send_qr_code(self, fetched_access_code):
        print("fetch code----" + fetched_access_code)
        WebAppActions(self.driver).enter_text(*locators['LOGIN_ACCCESS_CODE'], fetched_access_code)
       

    def submit_qr_url_credentials(self, username, password):
        print("self.locator['USERNAME_QR_LOGIN']   ===", locators['USERNAME_QR_LOGIN'])
        if '{0}' in username:
            username = username.replace('{0}', readPreReqJsonValue("prereq", "publicity_execution_id")) + "@gmail.com"
        print("username   in page===", username)
        print("password   in page", password)
        time.sleep(8)
        Username = WebAppActions(self.driver).wait_for_element(*locators['USERNAME_QR_LOGIN'])
        print(Username)
        WebAppActions(self.driver).enter_text(*locators['USERNAME_QR_LOGIN'], username)
        print('entered username')
        time.sleep(4)
        WebAppActions(self.driver).enter_text(*locators['PASSWORD_QR_LOGIN'], password)
        print('entered password')   
        WebAppActions(self.driver).click_button(*locators['SIGN_IN_QR_LOGIN'])
    
    def invalid_Credentials_Error_Message(self, errormessage, desc):
        print("validatign for ===", errormessage)
        return self.actions.validate_text(*locators[desc], errormessage)

    def successfull_Login(self, message):
        print("validate success login message as ", message)
        return self.actions.validate_text(*locators['SUCCESSFULL_MESSAGE_QR_LOGIN'], message)
    