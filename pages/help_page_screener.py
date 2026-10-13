from appium.webdriver.common.appiumby import AppiumBy
from conftest import readConstants
from pages.actions.android_actions import AndroidActions
from pages.actions.ios_actions import iOSActions
from pages.actions.roku_actions import RokuActions
from pages.base_page import BasePage
import time



locators_ipad = {
    "HELP_PAGE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "helpPage9"`]')
}


class HelpPageScreener(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        package_name = readConstants("current_app_package")
        locators_temp = {
            "HELP_HEADER": (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.widget.TextView"),
            "GETTING_STARTED": (AppiumBy.XPATH, "//android.widget.TextView[@text='Getting Started']"),
            "BROWSING_FOR_SHOWS": (AppiumBy.XPATH, "//android.widget.TextView[@text='Browsing for Shows']"),
            "SELECTING_A_SHOW": (AppiumBy.XPATH, "//android.widget.TextView[@text='Selecting a Show']"),
            "SETTINGS_AND_FEATURES": (AppiumBy.XPATH, "//android.widget.TextView[@text='Settings and Features']"),
            "SOLVING_STREAMING_ISSUES": (AppiumBy.XPATH, "//android.widget.TextView[@text='Solving Streaming Issues']"),
            "LOGGING_OUT": (AppiumBy.XPATH, "//android.widget.TextView[@text='Logging Out']")
        }
        self.locators = locators_temp
        print("modied locator ====", self.locators)
        
    def help_page_header_verification(self):
        if isinstance(self.actions, AndroidActions):    
            return self.actions.is_element_displayed(*self.locators["HELP_HEADER"])
        elif isinstance(self.actions, iOSActions):    
            return self.actions.is_element_displayed(*locators_ipad["HELP_PAGE"])
        elif isinstance(self.actions, RokuActions):
            self.actions.screenshotAttachment("HelpPage.jpeg")
            time.sleep(10)
            return self.actions.is_element_displayed("name", "HelpPage", "")

    def help_Section_Contents(self, ExpectedContent, ExpectedBrowserShowsContent, ExpectedSelectingashow, ExpectedSettingsandfeatures, ExpectedSolvingstramingissues, ExpectedLoggingout):  # noqa:E501
        if isinstance(self.actions, AndroidActions):     
            ActualContent = self.actions.validate_text_contains(*self.locators['GETTING_STARTED'], ExpectedContent)
            ActualBrowserShowsContent = self.actions.validate_text_contains(*self.locators['BROWSING_FOR_SHOWS'], ExpectedBrowserShowsContent)
            ActualSelectingashow = self.actions.validate_text_contains(*self.locators['SELECTING_A_SHOW'], ExpectedSelectingashow)
            ActualSettingsandfeatures = self.actions.validate_text_contains(*self.locators['SETTINGS_AND_FEATURES'], ExpectedSettingsandfeatures)
            ActualSolvingstramingissues = self.actions.validate_text_contains(*self.locators['SOLVING_STREAMING_ISSUES'], ExpectedSolvingstramingissues)
            ActualLoggingout = self.actions.validate_text_contains(*self.locators['LOGGING_OUT'], ExpectedLoggingout)
            Help_Page_Content = [ActualContent, ActualBrowserShowsContent, ActualSelectingashow, ActualSettingsandfeatures, ActualSolvingstramingissues, ActualLoggingout]  # noqa:E501
            self.driver.press_keycode(self.keys['KEYCODE_BACK'])         
            if all(Help_Page_Content):
                return True
            else:
                return False
        elif isinstance(self.actions, RokuActions):  
            # Current_Element = self.actions.fetch_roku_element_by_attr("lDialogTitle", "HELP - PAGE 1/3")
            # Help_Element = self.actions.fetch_element(Current_Element)
            # print("Fetched Element----" + Help_Element)
            # return Help_Element
            # element_Name = "lHelpDialogTitle"
            # text_Value = "HELP - PAGE 1/8"
            # element_Data = self.actions.fetchRokuCurrentPageSourceUsingName(element_Name, text_Value)
            # attrs = element_Data.get('value', {}).get('Attrs', [])
            # text_attr = next((attr['Value'] for attr in attrs if attr['Name']['Local'] == 'text'), None)
            # print("The text present is :" + text_attr)
            self.actions.screenshotAttachment("helpcontent.jpeg")
            self.actions.click_button("Left")
            time.sleep(4)
            return True