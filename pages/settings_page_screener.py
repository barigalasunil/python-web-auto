from appium.webdriver.common.appiumby import AppiumBy
import time
from pages.actions.android_actions import AndroidActions
from pages.actions.ios_actions import iOSActions
from pages.base_page import BasePage
from conftest import readConstants

locators_ipad = {
    "SERVER_TEXT": (AppiumBy.XPATH, "//XCUIElementTypeTextField[1]"),
    "COMPANY_TEXT": (AppiumBy.XPATH, "//XCUIElementTypeTextField[2]"),
    "APIVERSION_TEXT": (AppiumBy.XPATH, "//XCUIElementTypeTextField[3]"),
    "SAVE_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Back"`]'),
    "BACK_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Save"`]')
}


class SettingsPageScreener(BasePage):

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
                

    def set_settings_data(self, Servertext, server_ipad, companytext, apiversiontext):
        if isinstance(self.actions, AndroidActions):
            print("my server element ===", self.locators)
            self.actions.enter_text(*self.locators['SERVER_TEXT'], Servertext)
            self.actions.enter_text(*self.locators['COMPANY_TEXT'], companytext)
            self.actions.enter_text(*self.locators['APIVERSION_TEXT'], apiversiontext)
        elif isinstance(self.actions, iOSActions):
            self.actions.set_text(*locators_ipad['SERVER_TEXT'], server_ipad)
            self.actions.set_text(*locators_ipad['COMPANY_TEXT'], companytext)
            self.actions.set_text(*locators_ipad['APIVERSION_TEXT'], apiversiontext)
        else:
            time.sleep(3)
            print("Roku actions to settings page")
            self.actions.click_button("Select")
            time.sleep(3)
            self.actions.click_button("Up")
            for i in range(2):
                time.sleep(2)
                self.actions.click_button("Down")
            time.sleep(1)     
            for i in range(95): 
                self.actions.click_button("Select")
            print("what i am settign as server in roku===",Servertext)
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
            self.actions.screenshotAttachment("settingsdata.jpeg")
            self.actions.click_button("Select")
            time.sleep(3)
            # self.actions.click_button("Up")
            # for i in range(2):
            #     time.sleep(2)
            #     self.actions.click_button("Down")
            # time.sleep(2)          
            # for i in range(50): 
            #     self.actions.click_button("Select")
            # time.sleep(2)
                
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
            self.actions.screenshotAttachment("before_save_settingsdata.jpeg")
            self.actions.click_button("Select") 
            self.actions.screenshotAttachment("after_save_settingsdata.jpeg")
            time.sleep(9)  
            self.actions.click_button("Back") 
    
    
