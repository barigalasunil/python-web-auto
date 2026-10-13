from appium.webdriver.common.appiumby import AppiumBy
import time
from conftest import readConstants
from pages.actions.android_actions import AndroidActions
from pages.actions.ios_actions import iOSActions
from pages.actions.roku_actions import RokuActions
from pages.base_page import BasePage


locators_ipad = {
    "SERVER_TEXT": (AppiumBy.XPATH, "//XCUIElementTypeTextField[1]"),
    "COMPANY_TEXT": (AppiumBy.XPATH, "//XCUIElementTypeTextField[2]"),
    "APIVERSION_TEXT": (AppiumBy.XPATH, "//XCUIElementTypeTextField[3]"),
    "API_KEY_1": (AppiumBy.XPATH, '//XCUIElementTypeTextField[4]'),
    "API_KEY_2": (AppiumBy.XPATH, '//XCUIElementTypeTextField[5]'),
    "SAVE_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Back"`]'),
    "BACK_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Save"`]'),
    "SERVER_HEADER": (AppiumBy.ACCESSIBILITY_ID, 'Server')
}


class SettingsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        package_name = readConstants("current_app_package")
        locators_temp = {
            "SERVER_TEXT": (AppiumBy.ID, f"{package_name}:id/etServer"),
            "COMPANY_TEXT": (AppiumBy.ID, f"{package_name}:id/etCompanyName"),
            "APIVERSION_TEXT": (AppiumBy.ID, f"{package_name}:id/etAPIVersion"),
            "SAVE_BUTTON": (AppiumBy.ID, f"{package_name}:id/save"),
            "BACK_BUTTON": (AppiumBy.ID, f"{package_name}:id/back")
        }
        self.locators = locators_temp
        print("modied locator ====", self.locators)
   
    def set_settings_data(self, Servertext, server_ipad, companytext, apiversiontext, api_version_ipad, apikey1):
        if isinstance(self.actions, AndroidActions):
            self.actions.enter_text(*self.locators['SERVER_TEXT'], Servertext)
            self.actions.enter_text(*self.locators['COMPANY_TEXT'], companytext)
            self.actions.enter_text(*self.locators['APIVERSION_TEXT'], apiversiontext)
        elif isinstance(self.actions, iOSActions):
            settings_page_reached = self.actions.is_element_displayed(*locators_ipad['SERVER_HEADER'])
            if settings_page_reached:
                self.actions.enter_text(*locators_ipad['SERVER_TEXT'], server_ipad)
                self.actions.enter_text(*locators_ipad['COMPANY_TEXT'], companytext)
                self.actions.enter_text(*locators_ipad['APIVERSION_TEXT'], api_version_ipad)
                self.actions.enter_text(*locators_ipad['API_KEY_1'], apikey1)
                # API_key_2 = self.actions.wait_for_element(*locators_ipad['API_KEY_2'])
                # API_key_2.clear()
                # self.driver.hide_keyboard()
            else:
                print('Settings Page Is Not Reached')
        else:
            time.sleep(3)
            self.actions.screenshotAttachment("settings_before.jpeg")
            print("Roku actions to settings page")
            self.actions.click_button("Select")
            time.sleep(3)
            self.actions.click_button("Up")
            for i in range(2):
                time.sleep(2)
                self.actions.click_button("Down")
            time.sleep(1)     
            for i in range(35): 
                self.actions.click_button("Select")
            self.actions.doRokuSendKeys(server_ipad)
            time.sleep(8)
            self.actions.click_button("Enter")
            time.sleep(3)
            self.actions.click_button("Select")
            self.actions.click_button("Up")
            for i in range(2):
                time.sleep(2)
                self.actions.click_button("Down")
            for i in range(10): 
                time.sleep(1)   
                self.actions.click_button("Select")
            self.actions.doRokuSendKeys(companytext)
            self.actions.click_button("Enter")
            time.sleep(3)
            self.actions.click_button("Select")
            self.actions.click_button("Up")
            for i in range(2):
                time.sleep(2)
                self.actions.click_button("Down")
            for i in range(7): 
                time.sleep(1)   
                self.actions.click_button("Select")

            self.actions.doRokuSendKeys(apiversiontext)
            self.actions.click_button("Enter") 
            time.sleep(3)
            self.actions.click_button("Select")
            time.sleep(3)
            self.actions.click_button("Up")
            for i in range(2):
                time.sleep(2)
                self.actions.click_button("Down")
            time.sleep(2)          
            for i in range(50): 
                self.actions.click_button("Select")
            time.sleep(2)
            self.actions.doRokuSendKeys(apikey1)
            self.actions.screenshotAttachment("settings_after.jpeg")
            self.actions.click_button("Enter") 
            time.sleep(4)
            self.actions.screenshotAttachment("settings_back.jpeg")

    def set_settings_roku(self, Servertext, companytext, apiversiontext, apikey1):
        if isinstance(self.actions, RokuActions):
            time.sleep(3)
            self.actions.screenshotAttachment("settings_before.jpeg")
            print("Roku actions to settings page")
            self.actions.click_button("Select")
            time.sleep(3)
            self.actions.click_button("Up")
            for i in range(2):
                time.sleep(2)
                self.actions.click_button("Down")
            time.sleep(1)     
            for i in range(35): 
                self.actions.click_button("Select")
            self.actions.doRokuSendKeys(Servertext)
            time.sleep(8)
            self.actions.click_button("Enter")
            time.sleep(3)
            self.actions.click_button("Select")
            self.actions.click_button("Up")
            for i in range(2):
                time.sleep(2)
                self.actions.click_button("Down")
            for i in range(10): 
                time.sleep(1)   
                self.actions.click_button("Select")
            self.actions.doRokuSendKeys(companytext)
            self.actions.click_button("Enter")
            time.sleep(3)
            self.actions.click_button("Select")
            self.actions.click_button("Up")
            for i in range(2):
                time.sleep(2)
                self.actions.click_button("Down")
            for i in range(7): 
                time.sleep(1)   
                self.actions.click_button("Select")

            self.actions.doRokuSendKeys(apiversiontext)
            self.actions.click_button("Enter") 
            time.sleep(3)
            self.actions.click_button("Select")
            time.sleep(3)
            self.actions.click_button("Up")
            for i in range(2):
                time.sleep(2)
                self.actions.click_button("Down")
            time.sleep(2)          
            for i in range(50): 
                self.actions.click_button("Select")
            time.sleep(2)
            self.actions.doRokuSendKeys(apikey1)
            self.actions.screenshotAttachment("settings_before_withvaluee.jpeg")
            self.actions.click_button("Enter") 
            self.actions.screenshotAttachment("settings_back.jpeg")
            time.sleep(4)
        else:
            pass            
                
    def click_savebutton(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators['SAVE_BUTTON'])
            time.sleep(5) 
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['SAVE_BUTTON'])
            time.sleep(5)
        else:
            # self.actions.click_button("Down")
            time.sleep(4)
            self.actions.click_button("Select") 
            time.sleep(9)   
    
    
