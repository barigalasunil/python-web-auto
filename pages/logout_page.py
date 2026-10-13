from appium.webdriver.common.appiumby import AppiumBy
from conftest import readConstants
from pages.actions.android_actions import AndroidActions
from pages.actions.ios_actions import iOSActions
from pages.actions.roku_actions import RokuActions
import time

from pages.base_page import BasePage

# locators1 = {
#     "LOGOUT_TXT": (AppiumBy.ID, "com.indee.gd:id/txt_logout_header"),
#     "LOGOUT_BTN": (AppiumBy.ID, "com.indee.gd:id/btn_signout"),
#     "BACK_BTN": (AppiumBy.ID, "com.indee.gd:id/btn_cancle")
# }

locators_ipad = {
    "LOGOUT_TXT": (AppiumBy.IOS_PREDICATE, "name CONTAINS[c] 'log out'"),
    "LOGOUT_BTN": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "SIGN OUT"`]'),
    "BACK_BTN": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "BACK"`]')
}

locators = {}

class LogoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        package_name = readConstants("current_app_package")
        locators_temp = {
            "LOGOUT_TXT": (AppiumBy.ID, f"{package_name}:id/txt_logout_header"),
            "LOGOUT_BTN": (AppiumBy.ID, f"{package_name}:id/btn_signout"),
            "BACK_BTN": (AppiumBy.ID, f"{package_name}:id/btn_cancle")
        }
        self.locators = locators_temp
        print("modied locator ====", self.locators)
        
    def click_logout_on_confirmation_screen(self):
        if isinstance(self.actions, AndroidActions):  
            self.actions.click_button(*self.locators['LOGOUT_BTN'])
           
        elif isinstance(self.actions, iOSActions):
           
            self.actions.click_button(*locators_ipad['LOGOUT_BTN'])
           
        elif isinstance(self.actions, RokuActions):
            # self.actions.screenshotAttachment("before_sign_out_confirmatin.jpeg")
            # time.sleep(5)
            # self.actions.click_button("Up")
            # time.sleep(1)
            # self.actions.click_button("Select")
            self.actions.screenshotAttachment("after_sign_out_confirmatin.jpeg")
     
    def log_Out(self, ExpectedContent):
        if isinstance(self.actions, AndroidActions):  
            Logout_Text = self.actions.validate_text_contains(*self.locators['LOGOUT_TXT'], ExpectedContent)
            self.actions.click_button(*self.locators['LOGOUT_BTN'])
            return Logout_Text
        elif isinstance(self.actions, iOSActions):
            Logout_Text = self.actions.is_element_displayed(*locators_ipad['LOGOUT_TXT'])
            self.actions.click_button(*locators_ipad['LOGOUT_BTN'])
            return Logout_Text
        else:
            time.sleep(10)
            return self.actions.is_element_displayed("name", "lForgotPassword", "Forgot Password?")
