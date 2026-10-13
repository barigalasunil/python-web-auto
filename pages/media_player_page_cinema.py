from appium.webdriver.common.appiumby import AppiumBy
from pages.actions.android_actions import AndroidActions
from pages.actions.ios_actions import iOSActions
from pages.actions.roku_actions import RokuActions
from pages.base_page import BasePage
import time
from conftest import readConstants, readPreReqJsonValue

locators_ipad = {
    "VIDEO_CONTROLLER": (AppiumBy.ACCESSIBILITY_ID, 'Play/Pause'),
    "SUBTITLES_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Legible Options"`]'),
    "SUTITLES_HEADER": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Subtitles"`]'),
    "SUBTITLE_TRACKS": (AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell'),
    "DEFAULT_SUBTITLE": (AppiumBy.ACCESSIBILITY_ID, 'checkmark'),
    "SUBTITLE_SELECTION": (AppiumBy.XPATH, '(//XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeButton)[1]'),
    "PLAY_NOW_BUTTON": (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton'),
    "CLOSE_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "closeMenu"`]'),
    "AUDIO_BUTTON": (AppiumBy.ACCESSIBILITY_ID, 'Audible Options'),
    "AUDIO_TRACK_HEADER": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Audio Track"`]'),
    "AUDIO_TRACKS_SELECTION": (AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeButton'),
    "DEFAULT_AUDIO": (AppiumBy.ACCESSIBILITY_ID, 'checkmark'),
    "MULTIPLE_AUDIIO_COLLECTION": (AppiumBy.CLASS_NAME, 'XCUIElementTypeCollectionView')
}


class MediaPlayerPageCinema(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        package_name = readConstants("current_app_package")
        locators_temp = {
            "BTN_REWIND": (AppiumBy.ACCESSIBILITY_ID, 'Rewind'),
            "BTN_FORWARD": (AppiumBy.ACCESSIBILITY_ID, 'Fast forward'),
            "BTN_PAUSE": (AppiumBy.ACCESSIBILITY_ID, 'Pause'),
            "BTN_SUBTITLES_SELECTION": (AppiumBy.ID, 'com.indee.gd:id/exo_closed_caption'),
            "SUBTITLE_TRACK_SELECTION": (AppiumBy.ID, f'{package_name}:id/exo_track_selection_view'),
            "SUBTITLE_SELECTION": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.CheckedTextView").textContains("None")'),
            "SUBTITLE_CANCEL_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").textContains("CANCEL")'),
            "SUBTITLE_OK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").textContains("OK")'),
            "BTN_SETTINGS_SELECTION": (AppiumBy.ID, f'{package_name}:id/exo_audio'),
            "SETTINGS_SELECTION_TITLE": (AppiumBy.XPATH, '//androidx.appcompat.app.ActionBar.Tab[@content-desc="Text"]'),
            "AUDIO_BUTTON": (AppiumBy.ACCESSIBILITY_ID, 'Audio'),
            "TEXT_BUTTON": (AppiumBy.ACCESSIBILITY_ID, 'Text'),
            "AUDIO_TRACK_SELECTION": (AppiumBy.ID, f'{package_name}:id/exo_track_selection_view'),
            "TRACK_SELECTION": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.CheckedTextView").textContains("None")'),
            "TRACK_SELECTION_CANCEL_BUTTON": (AppiumBy.ID, f'{package_name}:id/track_selection_dialog_cancel_button'),
            "TRACK_SELECTION_OK_BUTTON": (AppiumBy.ID, f'{package_name}:id/track_selection_dialog_ok_button'),
            "PLAYING_NOW_POPUP": (AppiumBy.ID, 'com.indee.gd:id/img_playnow_popup'),
            "POPUP_CONTINUE_WATCHING_ICON": (AppiumBy.ID, f'{package_name}:id/exo_play'),
            "POPUP_YOUR_WATCHING": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").textContains("You’re watching")'),
            "VIDEOS_BTN": (AppiumBy.ID, f'{package_name}:id/btn_videos'),
            "VIDEO_PLAY_BUTTON": (AppiumBy.ID, f'{package_name}:id/exo_play'),
            "SUBTITLE_SECTION": (AppiumBy.XPATH, '//androidx.appcompat.app.ActionBar.Tab[@content-desc="Text"]'),
            "MULTIPLE_SUBTITLE": (AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="{}"]'),
            "SINGLE_SUBTITLE": (AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Auto"]'),
            "AUDIO_DEFAULT": (AppiumBy.XPATH, "//android.widget.CheckedTextView[@text='Auto']"),
            "VIDEO_CONTROLLER": (AppiumBy.ID, f"{package_name}:id/llController")
        }
        self.locators = locators_temp
        print("modied locator ====", self.locators)

    def click_on_settings_icon(self, scenario_name):
        if isinstance(self.actions, AndroidActions):
            print('Inside settings click fn')
            try:
                self.actions.click_button(*self.locators['POPUP_CONTINUE_WATCHING_ICON'])
            except Exception:
                pass
            print('About to click down keywords')
            for i in range(3):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            print('Gonna click settings btn')
            self.actions.click_button(*self.locators['BTN_SETTINGS_SELECTION'])
            try:
                print('Clicking settings btn twice')
                self.actions.click_button(*self.locators['BTN_SETTINGS_SELECTION'])
            except Exception:
                pass
            # self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            # self.actions.click_button(*self.locators['SETTINGS_SELECTION_TITLE'])
        elif isinstance(self.actions, iOSActions):
            if scenario_name:
                self.actions.click_button(*locators_ipad['AUDIO_BUTTON'])
                return self.actions.is_element_displayed(*locators_ipad['AUDIO_TRACK_HEADER'])
            else:
                self.actions.click_button(*locators_ipad['SUBTITLES_BUTTON'])
                return self.actions.is_element_displayed(*locators_ipad['SUTITLES_HEADER'])
        elif isinstance(self.actions, RokuActions):
            time.sleep(2)
            self.actions.screenshotAttachment("reachSettings.jpeg")
            print("Select the subtitle section")
            self.actions.click_button("Left")
            time.sleep(2)
            self.actions.is_element_displayed("name", "mslVideoDescription", "")
            self.actions.screenshotAttachment("pause.jpeg")
            self.actions.click_button("Select")
            time.sleep(3)
            self.actions.click_button("Info")
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            self.actions.click_button("Select")
            self.actions.click_button("Down")
            self.actions.screenshotAttachment("reachedSettings.jpeg")
            return True
                 
    def verify_multiple_subtitles_displayed(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators['TEXT_BUTTON'])
            return self.actions.is_element_displayed(*self.locators['SUBTITLE_TRACK_SELECTION'])
        elif isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad['SUBTITLE_TRACKS'])
        elif isinstance(self.actions, RokuActions):
            time.sleep(20)
            self.actions.screenshotAttachment("multiple_subtitles_1.jpeg")
            self.actions.click_button("Info")
            time.sleep(2)
            self.actions.click_button("Down")
            time.sleep(2)
            self.actions.click_button("Down")
            time.sleep(2)
            self.actions.click_button("Select")
            time.sleep(2)
            self.actions.click_button("Down")
            time.sleep(2)
            self.actions.click_button("Select")
            time.sleep(2)
            self.actions.click_button("Down")
            time.sleep(2)
            self.actions.click_button("Select")
            time.sleep(2)
            self.actions.screenshotAttachment("subtitle.jpeg")
            self.actions.click_button("Info")
            self.actions.screenshotAttachment("after_info.jpeg")
            time.sleep(2)
            return True
        
    def click_on_different_subtitle_option(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators['SUBTITLE_SELECTION'])
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
            self.actions.click_button(*locators_ipad['SUBTITLE_SELECTION'])
            subtitles_popup = self.actions.is_element_displayed(*locators_ipad['SUTITLES_HEADER'])
            return not subtitles_popup
        else:
            print('pass')
            
    def verify_multiple_audio_selection_displayed(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators['AUDIO_BUTTON'])
            return self.actions.is_element_displayed(*self.locators['AUDIO_TRACK_SELECTION'])
        elif isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad['MULTIPLE_AUDIIO_COLLECTION'])

    def click_on_different_audio_option(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators['TRACK_SELECTION'])
            self.actions.click_button(*self.locators['TRACK_SELECTION_OK_BUTTON'])
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['AUDIO_TRACKS_SELECTION'])
        elif isinstance(self.actions, RokuActions):
            self.actions.screenshotAttachment("diff_audio.jpeg")
            print("Need to add code")
            time.sleep(1)
            self.actions.click_button("Down")
            time.sleep(2)
            self.actions.click_button("Down")
            self.actions.click_button("Select")
            time.sleep(2)
            self.actions.click_button("Down")
            time.sleep(2)
            self.actions.screenshotAttachment("navigation.jpeg")
            time.sleep(2)
            self.actions.click_button("Select")
            time.sleep(2)
            self.actions.click_button("Down")
            time.sleep(2)
            self.actions.click_button("Select")
            self.actions.screenshotAttachment("audio.jpeg")
            time.sleep(2)
              
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
                time.sleep(10)
                try:
                    self.actions.click_button(*locators_ipad['CLOSE_BUTTON'])
                except Exception:
                    pass
                Play_now_button = self.actions.get_element_visibility(*locators_ipad['PLAY_NOW_BUTTON'])
                if Play_now_button:
                    return True
                else:
                    pass
            return False
        elif isinstance(self.actions, RokuActions):
            #for i in range(20):
            #    self.actions.click_button("Right")
               
            #self.actions.click_button("Ok")
            time.sleep(20)
            return True
        
    def click_on_Playnowbutton(self):
        if isinstance(self.actions, AndroidActions):
            time.sleep(5)
            # self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            self.actions.click_button(*self.locators['VIDEO_PLAY_BUTTON'])
            # try:
            #     print('Clicking twice')
            #     self.actions.click_button(*self.locators['VIDEO_PLAY_BUTTON'])
            # except Exception:
            #     pass
        elif isinstance(self.actions, iOSActions):
            self.actions.swipe('down')
            self.actions.click_button(*locators_ipad['PLAY_NOW_BUTTON'])
        elif isinstance(self.actions, iOSActions):
            self.actions.screenshotAttachment("beforeclick_on_Playnow.jpeg")
            try:
                time.sleep(4)
                self.actions.click_button("Select")
                time.sleep(15)
                self.actions.screenshotAttachment("aftrclick_on_Playnow.jpeg")
                time.sleep(1)
            except Exception:
                pass
            
    def verify_playback(self):
        if isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad['VIDEO_CONTROLLER'])
        
    def single_subtitle(self):
        if isinstance(self.actions, AndroidActions):
            return self.actions.is_element_displayed(*self.locators['SINGLE_SUBTITLE'])
        
    def verify_default_audio_is_selected(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators['SUBTITLE_SECTION'])
            self.actions.is_element_displayed(*self.locators['SINGLE_SUBTITLE'])
            Default_audio = self.actions.wait_for_element(*self.locators['AUDIO_DEFAULT'])
            if Default_audio:
                Default_audio_selected = Default_audio.get_attribute('checked')
                print(Default_audio_selected)
                if Default_audio_selected:
                    return True
                else:
                    print('Default Audio Is Not Selected')
                    return False
            else:
                print('Default Audio Is Not Displayed')
                time.sleep(4)
                self.actions.click_button("Option")
                time.sleep(15)
                return True
        elif isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad['DEFAULT_AUDIO']) 
        
    def verify_multiple_subtitle(self):
        if isinstance(self.actions, AndroidActions):
            print("Subtitle section====")
            self.actions.click_button(*self.locators['SUBTITLE_SECTION'])
            subtitle = readPreReqJsonValue("prereq", "cinema_subtitle")
            by, value = self.locators['MULTIPLE_SUBTITLE']
            format_value = value.format(subtitle)
            return self.actions.is_element_displayed(by, format_value)
        
    def click_multiple_subtitle(self, subtitle):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators['SUBTITLE_SECTION'])
            by, value = self.locators['MULTIPLE_SUBTITLE']
            format_value = value.format(subtitle)
            self.actions.click_button(by, format_value)
            self.actions.click_button(*self.locators['SUBTITLE_OK_BUTTON'])
            return self.actions.is_element_displayed(*self.locators['VIDEO_CONTROLLER'])
        else:
            return True

