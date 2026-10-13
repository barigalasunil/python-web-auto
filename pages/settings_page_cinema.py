from appium.webdriver.common.appiumby import AppiumBy
from pages.actions.android_actions import AndroidActions
from pages.actions.ios_actions import iOSActions
from pages.actions.roku_actions import RokuActions
import time
from conftest import readConstants

from pages.base_page import BasePage

locators_ipad = {
    "SERVER_TEXT": (AppiumBy.XPATH, "//XCUIElementTypeTextField[1]"),
    "COMPANY_TEXT": (AppiumBy.XPATH, "//XCUIElementTypeTextField[2]"),
    "APIVERSION_TEXT": (AppiumBy.XPATH, "//XCUIElementTypeTextField[3]"),
    "SAVE_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Save"`]'),
    "BACK_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Back"`]')  
}


class SettingsPageCinema(BasePage):

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

    
    def set_settings_data(self, Servertext, companytext, apiversiontext):
        print("launching driver ====", type(self.actions))
        if isinstance(self.actions, AndroidActions):
            self.actions.enter_text(*self.locators['SERVER_TEXT'], Servertext)
            self.actions.enter_text(*self.locators['COMPANY_TEXT'], companytext)
            self.actions.enter_text(*self.locators['APIVERSION_TEXT'], apiversiontext)
        elif isinstance(self.actions, iOSActions):
            self.actions.set_text(*locators_ipad['SERVER_TEXT'], Servertext)
            self.actions.set_text(*locators_ipad['COMPANY_TEXT'], companytext)
            self.actions.set_text(*locators_ipad['APIVERSION_TEXT'], apiversiontext)
        elif isinstance(self.actions, RokuActions):
            time.sleep(3)
            print("Roku actions to settings page")
            self.actions.screenshotAttachment("settings_page.jpeg")
            self.actions.click_button("Select")
            self.actions.click_button("Up")
            self.actions.screenshotAttachment("settings_page_clickup.jpeg")
            for i in range(2):
                time.sleep(2)
                self.actions.click_button("Down")
            for i in range(90): 
                # time.sleep(1)   
                self.actions.click_button("Select")
            self.actions.screenshotAttachment("settings_page_1.jpeg")
            self.actions.doRokuSendKeys(Servertext)
            self.actions.screenshotAttachment("update_setting.jpeg")
            time.sleep(8)
            self.actions.click_button("Enter")
            time.sleep(3)
            self.actions.click_button("Select")
            self.actions.click_button("Up")
            for i in range(2):
                time.sleep(2)
                self.actions.click_button("Down")
            for i in range(35): 
               # time.sleep(1)   
                self.actions.click_button("Select")
            self.actions.doRokuSendKeys(companytext)
            self.actions.screenshotAttachment("update_company.jpeg")
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
            self.actions.screenshotAttachment("Update_API.jpeg")
            self.actions.click_button("Enter") 
            self.actions.screenshotAttachment("out_of_settings.jpeg")

    def set_settings_data_roku(self, Servertext, companytext, apiversiontext):
        if isinstance(self.actions, RokuActions):
            time.sleep(3)
            print("Roku actions to settings page")
            self.actions.screenshotAttachment("settings_page.jpeg")
            self.actions.click_button("Select")
            self.actions.click_button("Up")
            self.actions.screenshotAttachment("settings_page_clickup.jpeg")
            for i in range(2):
                time.sleep(2)
                self.actions.click_button("Down")
            for i in range(90): 
                # time.sleep(1)   
                self.actions.click_button("Select")
            self.actions.screenshotAttachment("settings_page_1.jpeg")
            self.actions.doRokuSendKeys(Servertext)
            self.actions.screenshotAttachment("update_setting.jpeg")
            time.sleep(8)
            self.actions.click_button("Enter")
            time.sleep(3)
            self.actions.click_button("Select")
            self.actions.click_button("Up")
            for i in range(2):
                time.sleep(2)
                self.actions.click_button("Down")
            for i in range(35): 
               # time.sleep(1)   
                self.actions.click_button("Select")
            self.actions.doRokuSendKeys(companytext)
            self.actions.screenshotAttachment("update_company.jpeg")
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
            self.actions.screenshotAttachment("Update_API.jpeg")
            self.actions.click_button("Enter") 
            self.actions.screenshotAttachment("out_of_settings.jpeg")
        else:
            return True    

    def click_savebutton(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators['SAVE_BUTTON'])
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['SAVE_BUTTON'])
        else:
            self.actions.screenshotAttachment("before_clicking_save.jpeg")
            self.actions.click_button("Select")
            time.sleep(10)

    def click_savebutton_roku(self):
        if isinstance(self.actions, RokuActions):
            self.actions.screenshotAttachment("before_clicking_save.jpeg")
            self.actions.click_button("Select")
            time.sleep(10)
        else:
            return True            
    