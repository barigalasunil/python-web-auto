from appium.webdriver.common.appiumby import AppiumBy
from conftest import readConstants
from pages.actions.android_actions import AndroidActions
from pages.actions.ios_actions import iOSActions
import time

from pages.base_page import BasePage


locators_ipad = {
    "LOGOUT_TXT": (AppiumBy.IOS_PREDICATE, "name CONTAINS[c] 'log out'"),
    "LOGOUT_BTN": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "SIGN OUT"`]'),
    "BACK_BTN": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "BACK"`]')
}


class LogoutPageScreener(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        package_name = readConstants("current_app_package")
        locators_temp = {
            "LOGOUT_TXT": (AppiumBy.ID, f"{package_name}:id/txt_signout"),
            "LOGOUT_BTN": (AppiumBy.ID, f"{package_name}:id/btn_signout"),
            "BACK_BTN": (AppiumBy.ID, f"{package_name}:id/btn_cancle")
        }
        self.locators = locators_temp
        print("modied locator ====", self.locators)

    def log_Out(self):
        if isinstance(self.actions, AndroidActions):  
            Logout_Text = self.actions.is_element_displayed(*self.locators['LOGOUT_TXT'])
            self.actions.click_button(*self.locators['LOGOUT_BTN'])
            return Logout_Text
        elif isinstance(self.actions, iOSActions):
            Logout_Text = self.actions.is_element_displayed(*locators_ipad['LOGOUT_TXT'])
            self.actions.click_button(*locators_ipad['LOGOUT_BTN'])
            return Logout_Text
        else:
            time.sleep(10)
            return self.actions.is_element_displayed("name", "lForgotPassword", "Forgot Password?")
