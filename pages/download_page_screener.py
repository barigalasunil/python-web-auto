from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.actions.ios_actions import iOSActions


locators_ipad = {
    "DOWNLOADS_HEADER": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Downloads"`]'),
    "WARNING_ICON": (AppiumBy.ACCESSIBILITY_ID, 'warning'),
    "NO_DOWNLOADS_HEADER": (AppiumBy.ACCESSIBILITY_ID, 'You have no downloaded titles.'),
    "NO_DOWNLOADS_TEXT": (AppiumBy.ACCESSIBILITY_ID, 'Look for the  icon, on any title page to start downloading.'),
    "NO_DOWNLOADS_NOTE": (AppiumBy.IOS_PREDICATE, "name CONTAINS[c] 'Note:'"),
    "PROJECT_NAME": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name contains "{project_name}"`]'),
    "SELECT_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Select"`]'),
    "DELETE_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "  Delete"`]'),
    "CANCEL_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Cancel"`]'),
    "UNSELECTED_ICON": (AppiumBy.ACCESSIBILITY_ID, 'unselectedCell icon'),
    "SELECTED_ICON": (AppiumBy.ACCESSIBILITY_ID, 'selectedCell icon'),
    "DELETE_POPUP_HEADER": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Delete downloaded video?"`]'),
    "POPUP_TEXT": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "This video will be deleted from this device. You can download it again later if the title is still available."`]'),  # noqa:E501
    "POPUP_DELETE_BUTTON": (AppiumBy.IOS_PREDICATE, 'name == "DELETE" AND label == "DELETE" AND type == "XCUIElementTypeButton"'),
    "POPUP_CANCEL_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "CANCEL"`]'),
    "DONWLOAD_PLAY_BUTTON": (AppiumBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell'),
    "VIDEO_CONTROLLER": (AppiumBy.ACCESSIBILITY_ID, 'Play/Pause')
}


class DownloadPageScreeners(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_downloads_page_header(self):
        if isinstance(self.actions, iOSActions):
            return self.actions.get_element_visibility(*locators_ipad['DOWNLOADS_HEADER'])
        else:
            return True
    
    def verify_no_downloads_message(self):
        if isinstance(self.actions, iOSActions):
            Warning_icon = self.actions.is_element_displayed(*locators_ipad['WARNING_ICON'])
            No_downloads_header = self.actions.is_element_displayed(*locators_ipad['NO_DOWNLOADS_HEADER'])
            No_downloads_text = self.actions.is_element_displayed(*locators_ipad['NO_DOWNLOADS_TEXT'])
            No_downloads_note = self.actions.is_element_displayed(*locators_ipad['NO_DOWNLOADS_NOTE'])
            No_downloads_elements = [Warning_icon, No_downloads_header, No_downloads_text, No_downloads_note]
            if all(No_downloads_elements):
                return True
            else:
                return False
        else:
            return True
        
    def verify_project_in_downloads(self, project_name):
        if isinstance(self.actions, iOSActions):
            by, value = locators_ipad["PROJECT_NAME"]
            format_value = value.format(project_name=project_name)
            Project_added = self.actions.validate_text_contains(by, format_value, project_name)
            return Project_added
        else:
            return True
        
    def select_project_to_delete(self):
        if isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['SELECT_BUTTON'])
            self.actions.click_button(*locators_ipad['UNSELECTED_ICON'])
            return self.actions.is_element_displayed(*locators_ipad['SELECTED_ICON'])
        else:
            return True
        
    def click_on_delete_button(self):
        if isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['DELETE_BUTTON'])
        else:
            return True

    def verify_and_handle_confirm_delete_popup(self):
        if isinstance(self.actions, iOSActions):
            Popup_header = self.actions.is_element_displayed(*locators_ipad['DELETE_POPUP_HEADER'])
            Popup_text = self.actions.is_element_displayed(*locators_ipad['POPUP_TEXT'])
            if all([Popup_header, Popup_text]):
                self.actions.click_button(*locators_ipad['POPUP_DELETE_BUTTON'])
                try:
                    self.actions.tap(*locators_ipad['POPUP_DELETE_BUTTON'])
                except Exception:
                    pass
                
                return True
            else:
                return False
        else:
            return True
        
    def play_the_downloaded_video(self):
        if isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['DONWLOAD_PLAY_BUTTON'])
            Video_play = self.actions.is_element_displayed(*locators_ipad['VIDEO_CONTROLLER'])
            if Video_play:
                return True
            else:
                print('Project playback is not started after clicking play button in downloads page')
                return False
        else:
            return True
        
