from appium.webdriver.common.appiumby import AppiumBy

from conftest import readConstants, readPreReqJsonValue
from pages.actions.android_actions import AndroidActions
from pages.base_page import BasePage
from pages.actions.android_actions import AndroidActions
from pages.actions.ios_actions import iOSActions
from pages.actions.roku_actions import RokuActions
import time


locators_ipad = {
    "BTN_SUBTITLES_SELECTION": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Legible Options"`]'),
    "SUBTITLES_SELECTION_TITLE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Subtitles"`]'),
    "SUBTITLE_TRACK_SELECTION": (AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell'),
    "DEFAULT_SUBTITLE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "checkmark"`]'),
    "SUBTITLE_SELECTION": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "{}"`]'),
    "VIDEOS_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Videos"`]'),
    "BTN_AUDIO_SELECTION": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Audible Options"`]'),
    "AUDIO_SELECTION_TITLE": (AppiumBy.ACCESSIBILITY_ID, 'Audio Track'),
    "DEFAULT_AUDIO": (AppiumBy.ACCESSIBILITY_ID, 'checkmark'),
    "AUDIO_TRACK_SELECTION": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "{}"`]'),
    "PROJECT_CLOSE_BUTTON": (AppiumBy.ACCESSIBILITY_ID, 'Close Button'),
    "POPUP_CLOSE_BUTTON": (AppiumBy.ACCESSIBILITY_ID, "closeMenu"),
    "APPLICATION": (AppiumBy.CLASS_NAME, 'XCUIElementTypeApplication'),
    "RATE_THE_VIDEO": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "emptyStar"`][5]')
}


class MediaPlayerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        package_name = readConstants("current_app_package")
        locators_temp = {
            "VIDEO_CONTROLLER": (AppiumBy.ID, f"{package_name}:id/llController"),
            "BTN_REWIND": (AppiumBy.ACCESSIBILITY_ID, 'Rewind'),
            "BTN_FORWARD": (AppiumBy.ACCESSIBILITY_ID, 'Fast forward'),
            "BTN_PAUSE": (AppiumBy.ACCESSIBILITY_ID, 'Pause'),
            "BTN_SUBTITLES_SELECTION": (AppiumBy.ID, f"{package_name}:id/exo_closed_caption"),
            "SUBTITLE_HEADER": (AppiumBy.ID, f"{package_name}:id/alertTitle"),
            "SUBTITLE_TRACK_SELECTION": (AppiumBy.ID, f"{package_name}:id/exo_track_selection_view"),
            "SUBTITLE_SELECTION": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.CheckedTextView").textContains("{}")'),
            "SUBTITLE_CANCEL_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").textContains("CANCEL")'),
            "SUBTITLE_OK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").textContains("OK")'),
            "BTN_SETTINGS_SELECTION": (AppiumBy.ID, f"{package_name}:id/exo_audio"),
            "SETTINGS_SELECTION_TITLE": (AppiumBy.ID, f"{package_name}:id/title"),
            "AUDIO_BUTTON": (AppiumBy.ACCESSIBILITY_ID, 'Audio'),
            "TEXT_BUTTON": (AppiumBy.ACCESSIBILITY_ID, 'Text'),
            "AUDIO_TRACK_SELECTION": (AppiumBy.ID, f"{package_name}:id/exo_track_selection_view"),
            "TRACK_SELECTION": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.CheckedTextView").textContains("{}")'),
            "TRACK_SELECTION_CANCEL_BUTTON": (AppiumBy.ID, f"{package_name}:id/track_selection_dialog_cancel_button"),
            "TRACK_SELECTION_OK_BUTTON": (AppiumBy.ID, f"{package_name}:id/track_selection_dialog_ok_button"),
            "VIDEO_TIMELINE": (AppiumBy.ID, f"{package_name}:id/llTimeline"),
            "VIDEO_DURATION": (AppiumBy.ID, f"{package_name}:id/exo_duration"),
            "VIDEO_PROGRESS": (AppiumBy.ID, f"{package_name}:id/exo_progress"),
            "VIDEO_POSITION": (AppiumBy.ID, f"{package_name}:id/exo_position"),
            "PLAYING_NOW_POPUP": (AppiumBy.ID, f"{package_name}:id/img_playnow_popup"),
            "POPUP_CONTINUE_WATCHING_ICON": (AppiumBy.ID, f"{package_name}:id/btn_detail_playnow"),
            "POPUP_TIME_LEFT": (AppiumBy.ID, f"{package_name}:id/txt_detail_duration"),
            "POPUP_YOUR_WATCHING": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").textContains("You’re watching")'),
            "POPUP_VIDEO_NAME": (AppiumBy.ID, f"{package_name}:id/txt_detail_title"),
            "POPUP_VIDEO_TITLE": (AppiumBy.ID, f"{package_name}:id/txt_video_title"),
            "POPUP_VIDEO_DESC": (AppiumBy.ID, f"{package_name}:id/txt_detail_desc"),
            "VIDEOS_BTN": (AppiumBy.ID, f"{package_name}:id/btn_videos") 
            
        }
        self.locators = locators_temp
        print("modied locator ====", self.locators)



    def click_on_settings_icon(self, scenario_name):
        if isinstance(self.actions, AndroidActions):
            try:
                self.actions.wait_for_element(*self.locators['POPUP_CONTINUE_WATCHING_ICON'], timeout=5)
            except Exception:
                pass
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            self.actions.click_button(*self.locators['BTN_SETTINGS_SELECTION'])
            try:
                self.actions.click_button(*self.locators['BTN_SETTINGS_SELECTION'])
            except Exception:
                pass
            return self.actions.is_element_displayed(*self.locators['SETTINGS_SELECTION_TITLE'])
        elif isinstance(self.actions, iOSActions):
            if scenario_name == "GD035 :  Verify Playback on Multiple Audio Screeners":
                self.actions.click_button(*locators_ipad['BTN_AUDIO_SELECTION'])
                return self.actions.wait_for_element(*locators_ipad['AUDIO_SELECTION_TITLE'])
            else:
                self.actions.click_button(*locators_ipad['BTN_SUBTITLES_SELECTION'])
                return self.actions.is_element_displayed(*locators_ipad['SUBTITLES_SELECTION_TITLE'])
        else:
            time.sleep(4)
            print("Select the subtitle section")
            self.actions.click_button("Left")
            time.sleep(2)
            isVideoDescription = self.actions.is_element_displayed("name", "mslVideoDescription", "")
            if isVideoDescription:
                self.actions.screenshotAttachment("pause.jpeg")
                self.actions.click_button("Select")
                time.sleep(3)
                self.actions.click_button("Info")
                time.sleep(3)
                self.actions.click_button("Down")
                self.actions.click_button("Down")
                time.sleep(3)
                self.actions.click_button("Select")
                time.sleep(3)
                self.actions.click_button("Down")
                self.actions.screenshotAttachment("Subtile.jpeg")
                return True
            else:
                return False
                
            
    
    def close_the_playback(self):
        if isinstance(self.actions, AndroidActions):
            for i in range(2):
                self.driver.back()
        elif isinstance(self.actions, iOSActions):
            for i in range(2):
                try:
                    try:
                        self.actions.click_button(*locators_ipad['PROJECT_CLOSE_BUTTON'])
                    except Exception:
                        pass
                    self.actions.click_button(*locators_ipad['POPUP_CLOSE_BUTTON'])
                    try:
                        self.actions.click_button(*locators_ipad['RATE_THE_VIDEO'])
                    except Exception:
                        pass
                except Exception:
                    self.actions.click_button(*locators_ipad['APPLICATION'])
        else:
            print("Inside roku")
            time.sleep(5)
            self.actions.click_button("Back")            
                
    def verify_multiple_subtitles_displayed(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators['TEXT_BUTTON'])
            return self.actions.is_element_displayed(*self.locators['SUBTITLE_TRACK_SELECTION'])
        elif isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad['SUBTITLE_TRACK_SELECTION'])
        else:
            self.actions.click_button("Select")
            self.actions.click_button("Down")
            self.actions.screenshotAttachment("subtitle.jpeg")
            self.actions.screenshotAttachment("subtitle.jpeg")
            self.actions.click_button("Select")
            return True

    def click_on_different_subtitle_option(self, subtitle):
        if isinstance(self.actions, AndroidActions):
            by, value = self.locators['SUBTITLE_SELECTION']
            format_value = value.format(subtitle)
            self.actions.click_button(by, format_value)
            self.actions.click_button(*self.locators['SUBTITLE_OK_BUTTON'])
            try:
                self.actions.wait_for_element(*self.locators['POPUP_CONTINUE_WATCHING_ICON'], timeout=2)
            except Exception:
                pass
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            return self.actions.is_element_displayed(*self.locators['VIDEO_CONTROLLER'])
        elif isinstance(self.actions, iOSActions):
            Default = self.actions.is_element_displayed(*locators_ipad['DEFAULT_SUBTITLE'])
            if Default:
                print('Subtitle Is Selected By Default')
            else:
                print('Subtitle is not selected by default')
            by, value = locators_ipad['SUBTITLE_SELECTION']
            format_value = value.format(subtitle)
            self.actions.click_button(by, format_value)
            subtitles_popup = self.actions.is_element_displayed(*locators_ipad['SUBTITLES_SELECTION_TITLE'])
            return not subtitles_popup
        else:
            time.sleep(4)
            print("Select the subtitle section")
            self.actions.click_button("Info")
            time.sleep(3)
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            time.sleep(3)
            self.actions.click_button("Select")
            time.sleep(3)
            self.actions.click_button("Down")
            self.actions.click_button("Select")
            self.actions.click_button("Down")
            self.actions.screenshotAttachment("Screenshot.jpeg")
            self.actions.click_button("Select")
            self.actions.screenshotAttachment("afterselect.jpeg")
            return True

    def verify_multiple_audio_selection_displayed(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators['AUDIO_BUTTON'])
            return self.actions.is_element_displayed(*self.locators['AUDIO_TRACK_SELECTION'])
        elif isinstance(self.actions, iOSActions):
            return self.actions.wait_for_element(*locators_ipad['AUDIO_SELECTION_TITLE'])
        else:
            return True

    def click_on_different_audio_option(self, audio):
        if isinstance(self.actions, AndroidActions):
            by, value = self.locators['TRACK_SELECTION']
            format_value = value.format(audio)
            self.actions.click_button(by, format_value)
            self.actions.click_button(*self.locators['TRACK_SELECTION_OK_BUTTON'])
            try:
                self.actions.wait_for_element(*self.locators['POPUP_CONTINUE_WATCHING_ICON'], timeout=2)
            except Exception:
                pass
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            return self.actions.is_element_displayed(*self.locators['VIDEO_CONTROLLER'])
        elif isinstance(self.actions, iOSActions):
            audio = readPreReqJsonValue("prereq", "gd_audio_selection_ipad")
            by, value = locators_ipad['AUDIO_TRACK_SELECTION']
            format_value = value.format(audio)
            self.actions.click_button(by, format_value)
            Audio_Selected = self.actions.get_element_visibility(*locators_ipad['AUDIO_SELECTION_TITLE'])
            if Audio_Selected:
                return False
            else:
                return True
        else:
            self.actions.click_button("Down")   
            self.actions.click_button("Select")   
            self.actions.click_button("Down") 
            self.actions.screenshotAttachment("audio.jpeg")  
            self.actions.click_button("Select") 
            time.sleep(5) 
            return True 

    def play_the_video_to_fullest(self):
        if isinstance(self.actions, AndroidActions):
            for i in range(20):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
                # self.actions.click_button(*self.locators['"BTN_FORWARD"'])
                time.sleep(20)
                try:
                    self.actions.wait_for_element(*self.locators['POPUP_CONTINUE_WATCHING_ICON'], timeout=2)
                except Exception:
                    pass
                Video_Button = self.actions.wait_for_element(*self.locators["VIDEOS_BTN"], timeout=2)
                print(Video_Button)
                if Video_Button:
                    return True
                else:
                    pass
            return False
        elif isinstance(self.actions, iOSActions):
            for i in range(20):
                try:
                    self.actions.is_element_displayed(*locators_ipad['SUBTITLES_SELECTION_TITLE'])
                except Exception:
                    pass
                Video_Button = self.actions.wait_for_element(*locators_ipad["VIDEOS_BUTTON"], timeout=2)
                print(Video_Button)
                if Video_Button:
                    return True
                else:
                    pass
            return False
        elif isinstance(self.actions, RokuActions):
            time.sleep(2)
            print("Start watch button")
            self.actions.screenshotAttachment("beforestartplay.jpeg")
            # start_watching_button = self.actions.fetch_Data("lButtonText", "Start Watching")
            # print("Start watch button -------" + start_watching_button)
            # self.actions.click_button("Down")
            # self.actions.click_button("Select")
            self.actions.click_button("Select")
            time.sleep(5)
            self.actions.screenshotAttachment("playingvideo.jpeg")
            # self.actions.click_button("Left")
            time.sleep(5)
            self.actions.is_element_displayed("name", "mslVideoDescription", "")
            time.sleep(2)
            
            self.actions.click_button("Select")
            time.sleep(5)
            self.actions.screenshotAttachment("Playign_video1_1.jpeg")
            self.actions.click_button("Select")
            time.sleep(10)
            self.actions.screenshotAttachment("pause.jpeg")
            time.sleep(3)
            time.sleep(10)
            return True
            
