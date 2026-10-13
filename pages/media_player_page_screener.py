from appium.webdriver.common.appiumby import AppiumBy

from conftest import readConstants
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
    "SUBTITLE_SELECTION": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "{subtitle_selection}"`]'),
    "VIDEOS_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Videos"`]'),
    "BTN_AUDIO_SELECTION": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Audible Options"`]'),
    "AUDIO_SELECTION_TITLE": (AppiumBy.ACCESSIBILITY_ID, 'Audio Track'),
    "DEFAULT_AUDIO": (AppiumBy.ACCESSIBILITY_ID, 'checkmark'),
    "AUDIO_TRACK_SELECTION": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "{Audio_Selection}"`]'),
    "VIDEO_CONTROLLER": (AppiumBy.ACCESSIBILITY_ID, 'Play/Pause'),
    "PROJECT_CLOSE_BUTTON": (AppiumBy.ACCESSIBILITY_ID, 'Close Button'),
    "2FA_POPUP_HEADER": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Two-Factor Authentication"`]'),
    "POPUP_CLOSE_BUTTON": (AppiumBy.ACCESSIBILITY_ID, "closeMenu"),
    "2FA_PASSWORD_TEXT": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "For enhanced security, we include this step to verify your identity. Please enter your password."`]'),
    "2FA_PASSWORD_INPUT_FIELD": (AppiumBy.XPATH, "//XCUIElementTypeSecureTextField"),
    "UNLOCK_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "UNLOCK"`]'),
    "2FA_PHONE_TEXT": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "For enhanced security, we include this step to verify your identity . You will receive a 6-digit code on your phone via text message."`]'),
    "SELECT_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Select"`]'),
    "ENTER_MOBILE_NUMBER": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`value == "  Enter your phone number"`]'),
    "SEARCH_COUNTRY_CODE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`value == "  Search any country code..."`]'),
    "SELECT_COUNTRY_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "India"`]'),
    "GET_CODE_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "GET CODE"`]'),
    "ENTER_CODE_TEXT": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "We have sent a 6-digit code to your phone via text message. If you haven’t received it, request another one below."`]'),
    "VERIFICATION_CODE": (AppiumBy.ACCESSIBILITY_ID, 'Verification Code'),
    "ENTER_CODDE_INPUT_FIELD": (AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField'),
    "RESEND_CODE_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name contains "Resend code"`]'),
    "APPLICATION": (AppiumBy.CLASS_NAME, 'XCUIElementTypeApplication'),
    "RATE_THE_VIDEO": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "emptyStar"`][5]'),
    "2FA_CLOSE_BUUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "closeCrossImg"`]')
}


class MediaPlayerPageScreener(BasePage):
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
            "VIDEOS_BTN": (AppiumBy.ID, f"{package_name}:id/btn_videos"),
            "CMAF_WARNING_LOGO": (AppiumBy.ID, f"{package_name}:id/infoIcon"),
            "CMAF_WARNING_HEADER": (AppiumBy.ID, f"{package_name}:id/dialog_msg"),
            "CMAF_WARNING_TEXT": (AppiumBy.ID, f"{package_name}:id/deviceMsg"),
            "CMAF_GO_BACK_BUTTON": (AppiumBy.ID, f"{package_name}:id/btnGoBack"),
            "ENTER_CODE_TEXT": (AppiumBy.ID, f"{package_name}:id/tvInfo"),
            "VERIFICATION_CODE": (AppiumBy.ID, f"{package_name}:id/etPhoneNumber"),
            "ENTER_CODE_INPUT_FIELD": (AppiumBy.ID, f"{package_name}:id/tvHeader"),
            "UNLOCK_BUTTON": (AppiumBy.ID, f"{package_name}:id/btnControl"),
            "SELECT_BUTTON": (AppiumBy.ID, f"{package_name}:id/imageView_arrow"),
            "SEARCH_COUNTRY_CODE": (AppiumBy.ID, f"{package_name}:id/image_flag"),
            "ENTER_MOBILE_NUMBER": (AppiumBy.ID, f"{package_name}:id/etPhoneNumber"),
            "GET_CODE_BUTTON": (AppiumBy.ID, f"{package_name}:id/btnControl"),
            "MEDIA_PLAYER_CONTROLS": (AppiumBy.ID, f"{package_name}:id/player_view"),
            "AUDIO_DEFAULT": (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.ScrollView/android.widget.LinearLayout/android.widget.CheckedTextView[2]"),
            "2FA_POPUP_HEADER": (AppiumBy.ID, f"{package_name}:id/tvTitle"),
            "2FA_PASSWORD_TEXT": (AppiumBy.ID, f"{package_name}:id/tvInfo"),
            "ENTER_CODDE_INPUT_FIELD": (AppiumBy.ID, f"{package_name}:id/etPhoneNumber"),
            "2FA_PHONE_TEXT": (AppiumBy.ID, f"{package_name}:id/etPhoneNumber")
        
        }
        self.locators = locators_temp
        print("modied locator ====", self.locators)

    def click_on_settings_icon(self, scenario_name):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators['MEDIA_PLAYER_CONTROLS'])
            print('clicked controls')
            try:
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_UP'])
            except Exception:
                pass
            self.actions.is_element_displayed(*self.locators['VIDEO_CONTROLLER'])
            self.actions.click_button(*self.locators['BTN_SETTINGS_SELECTION'])
            print('clicked settings selection')
            try:
                self.actions.click_button(*self.locators['BTN_SETTINGS_SELECTION'])
            except Exception:
                pass
            return self.actions.is_element_displayed(*self.locators['SETTINGS_SELECTION_TITLE'])
        elif isinstance(self.actions, iOSActions):
            if scenario_name == "Verify Playback on Multiple Audio Screeners":
                self.actions.click_button(*locators_ipad['BTN_AUDIO_SELECTION'])
                return self.actions.wait_for_element(*locators_ipad['AUDIO_SELECTION_TITLE'])
            else:
                self.actions.click_button(*locators_ipad['BTN_SUBTITLES_SELECTION'])
                return self.actions.is_element_displayed(*locators_ipad['SUBTITLES_SELECTION_TITLE'])
        else:
            time.sleep(18)
            print("Select the subtitle section")
            self.actions.click_button("Left")
            time.sleep(2)
            self.actions.is_element_displayed("name", "mslVideoDescription", "")
            self.actions.screenshotAttachment("pause.jpeg")
            self.actions.click_button("Select")
            time.sleep(3)
            self.actions.click_button("Info")
            time.sleep(1)
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            # self.actions.click_button("Down")
            time.sleep(1)
            self.actions.click_button("Select")
            time.sleep(1)
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            self.actions.screenshotAttachment("Accesbility.jpeg")
            return True
            
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
            self.actions.click_button("Select")
            time.sleep(3)
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
            format_value = value.format(subtitle_selection=subtitle)
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
            self.actions.click_button("Select")
            self.actions.screenshotAttachment("subtile.jpeg")
            time.sleep(10)
            self.actions.click_button("Back")
            return True

    def verify_multiple_audio_selection_displayed(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators['AUDIO_BUTTON'])
            return self.actions.is_element_displayed(*self.locators['AUDIO_TRACK_SELECTION'])
        elif isinstance(self.actions, iOSActions):
            return self.actions.wait_for_element(*locators_ipad['AUDIO_SELECTION_TITLE'])
        else:
            return True
        
    def verify_default_audio_is_selected(self):
        if isinstance(self.actions, AndroidActions):
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
                # self.actions.click_button("Option")
                time.sleep(5)
                return True
        elif isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad['DEFAULT_AUDIO'])
        else:
            time.sleep(4)
            print("Press back from media player")
            self.actions.click_button("Back")
            return True

    def click_on_different_audio_option(self, audio, audio_ipad):
        if isinstance(self.actions, AndroidActions):
            
            by, value = self.locators['TRACK_SELECTION']
            format_value = value.format(audio)
            self.actions.click_button(by, format_value)
            Default_audio = self.actions.wait_for_element(*self.locators['AUDIO_DEFAULT'])
            Default_audio_selected = Default_audio.get_attribute('checked')
            print(Default_audio_selected)
            if Default_audio_selected:
                return True
            else:
                print("Moved audio is not highlighted ==",Default_audio_selected)
            try:
                self.actions.click_button(*self.locators['TRACK_SELECTION_OK_BUTTON'])
                self.actions.wait_for_element(*self.locators['POPUP_CONTINUE_WATCHING_ICON'], timeout=2)
            except Exception:
                pass
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            return self.actions.is_element_displayed(*self.locators['VIDEO_CONTROLLER'])
        elif isinstance(self.actions, iOSActions):
            by, value = locators_ipad['AUDIO_TRACK_SELECTION']
            format_value = value.format(Audio_Selection=audio_ipad)
            self.actions.click_button(by, format_value)
            Audio_Selected = self.actions.get_element_visibility(*locators_ipad['AUDIO_SELECTION_TITLE'])
            if Audio_Selected:
                return False
            else:
                return True
        else:
            time.sleep(4)
            print("Different audio")
            self.actions.click_button("Info")
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            self.actions.click_button("Select")
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            time.sleep(2)   
            self.actions.click_button("Select")   
            self.actions.click_button("Down")
            time.sleep(2)   
            self.actions.click_button("Select")  
            time.sleep(4)
            self.actions.click_button("Down")
            self.actions.click_button("Select")
            time.sleep(3)
            self.actions.screenshotAttachment("audio.jpeg")
            self.actions.click_button("Back")
            return True 

    def play_the_video_to_fullest(self):
        if isinstance(self.actions, AndroidActions):
            for i in range(20):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
                # self.actions.click_button(*self.locators['"BTN_FORWARD"'])
                time.sleep(60)
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
            Auto_play = False
            for i in range(20):
                try:
                    self.actions.wait_for_element(*locators_ipad["VIDEOS_BUTTON"], timeout=10)
                    print("Genres Tab is displayed in Homepage")
                    Auto_play = True
                    break
                except Exception:
                    pass
            return Auto_play
        else:    
            time.sleep(2)
            print("Start watch button")
            # start_watching_button = self.actions.fetch_Data("lButtonText", "Start Watching")
            # print("Start watch button -------" + start_watching_button)
            # self.actions.click_button("Down")
            # self.actions.click_button("Select")
            self.actions.click_button("Select")
            for i in range(3):
                time.sleep(80)
            return True
        
    def verify_multiple_audio_and_subtitle_options_are_displayed(self, audio, subtitle):
        Subtitle_options = self.actions.is_element_displayed(*locators_ipad['BTN_SUBTITLES_SELECTION'])
        if Subtitle_options:
            self.actions.click_button(*locators_ipad['BTN_SUBTITLES_SELECTION'])
            multiple_subtitle = self.verify_multiple_subtitles_displayed()
            Default = self.actions.is_element_displayed(*locators_ipad['DEFAULT_SUBTITLE'])
            if Default:
                print('Subtitle Is Selected By Default')
            else:
                print('Subtitle is not selected by default')
            by, value = locators_ipad['SUBTITLE_SELECTION']
            format_value = value.format(subtitle_selection=subtitle)
            self.actions.click_button(by, format_value)
        else:
            print("Downloaded project doesn't have subtitle selection options")
            return False
        Audio_options = self.actions.is_element_displayed(*locators_ipad['BTN_AUDIO_SELECTION'])
        if Audio_options:
            self.actions.click_button(*locators_ipad['BTN_AUDIO_SELECTION'])
            multiple_audio_track = self.verify_multiple_audio_selection_displayed()
            by, value = locators_ipad['AUDIO_TRACK_SELECTION']
            format_value = value.format(Audio_Selection=audio)
            self.actions.click_button(by, format_value)
        else:
            print("Downloaded project doesn't have audio selection options")
            return False
        self.actions.click_button(*locators_ipad['PROJECT_CLOSE_BUTTON'])
        if all([multiple_subtitle, multiple_audio_track]):
            return True
        else:
            return False     
            
    def verify_unsupported_error_banner_not_displayed_in_playback(self):
        if isinstance(self.actions, AndroidActions):
            Warning_Logo = self.actions.is_element_displayed(*self.locators['CMAF_WARNING_LOGO'])
            Waring_Header = self.actions.is_element_displayed(*self.locators['CMAF_WARNING_HEADER'])
            Warning_text = self.actions.is_element_displayed(*self.locators['CMAF_WARNING_TEXT'])
            if all([Warning_Logo, Waring_Header, Warning_text]):
                self.actions.click_button(*self.locators['CMAF_GO_BACK_BUTTON'])
                return True
            else:
                return False
        else:
            return True

    def verify_unsupported_error_banner_in_playback(self):
        if isinstance(self.actions, AndroidActions):
            Warning_Logo = self.actions.is_element_displayed(*self.locators['CMAF_WARNING_LOGO'])
            Waring_Header = self.actions.is_element_displayed(*self.locators['CMAF_WARNING_HEADER'])
            Warning_text = self.actions.is_element_displayed(*self.locators['CMAF_WARNING_TEXT'])
            if any([Warning_Logo, Waring_Header, Warning_text]):
                return False
            else:
                return True
        else:
            return True

    def verify_playback(self):
        if isinstance(self.actions, AndroidActions):
            time.sleep(5)
            return self.actions.is_element_displayed(*self.locators['VIDEO_CONTROLLER'])  
        if isinstance(self.actions, iOSActions):
            time.sleep(5)
            return self.actions.is_element_displayed(*locators_ipad['VIDEO_CONTROLLER']) 
        elif isinstance(self.actions, RokuActions):
            return True   
        
    def verify_2fa_password_authentication_popup(self):
        if isinstance(self.actions, iOSActions):
            authentication_popup_header = self.actions.is_element_displayed(*locators_ipad['2FA_POPUP_HEADER'])
            authentication_popup_text = self.actions.is_element_displayed(*locators_ipad['2FA_PASSWORD_TEXT'])
            if all([authentication_popup_header, authentication_popup_text]):
                return True
            else:
                return False
        else:
            return True
                
    def enter_screener_password_in_authentication_popup(self, screener_password):
        if isinstance(self.actions, iOSActions):
            self.actions.enter_text(*locators_ipad['2FA_PASSWORD_INPUT_FIELD'], screener_password)
            self.actions.click_button(*locators_ipad['UNLOCK_BUTTON'])
        else:
            pass

    def verify_2fa_phone_authentication_popup(self):
        if isinstance(self.actions, AndroidActions):
            authentication_popup_header = self.actions.is_element_displayed(*self.locators['2FA_POPUP_HEADER'])
            authentication_popup_text = self.actions.is_element_displayed(*self.locators['2FA_PHONE_TEXT'])
            if all([authentication_popup_header, authentication_popup_text]):
                return True
            else:
                return False
        if isinstance(self.actions, iOSActions):
            authentication_popup_header = self.actions.is_element_displayed(*locators_ipad['2FA_POPUP_HEADER'])
            authentication_popup_text = self.actions.is_element_displayed(*locators_ipad['2FA_PHONE_TEXT'])
            if all([authentication_popup_header, authentication_popup_text]):
                return True
            else:
                return False
        else:
            print("Verify authentication field")
            authentication_popup_header = self.actions.fetch_Data("lDialogTitle", "Two-Factor Authentication")
            authentication_popup_text = self.actions.fetch_Data("lPasswordOrPhoneText", "Phone Number")
            self.actions.screenshotAttachment("phone.jpeg")
            if all([authentication_popup_header, authentication_popup_text]):
                return True
            else:
                return False    
        
    def enter_screener_password_in_authentication_popup(self, screener_password):
        if isinstance(self.actions, iOSActions):
            self.actions.enter_text(*locators_ipad['2FA_PASSWORD_INPUT_FIELD'], screener_password)
            self.actions.click_button(*locators_ipad['UNLOCK_BUTTON'])
        else:
            pass

    def enter_country_code_and_mobile_number_in_authentication_popup(self, country_code, mobile_number):
        if isinstance(self.actions, AndroidActions):
            self.actions.enter_text(*self.locators['ENTER_MOBILE_NUMBER'], mobile_number)
            self.actions.click_button(*self.locators['GET_CODE_BUTTON'])
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['SELECT_BUTTON'])
            self.actions.enter_text(*locators_ipad['SEARCH_COUNTRY_CODE'], country_code)
            self.actions.click_button(*locators_ipad['SELECT_COUNTRY_BUTTON'])
            self.actions.enter_text(*locators_ipad['ENTER_MOBILE_NUMBER'], mobile_number)
            self.actions.click_button(*locators_ipad['GET_CODE_BUTTON'])
        else:
            # self.actions.click_button("Select")
            print("Enter mobile number")
            time.sleep(5)
            for i in range(94):
                self.actions.click_button("Down")
            time.sleep(2)
            self.actions.click_button("Select") 
            time.sleep(2)
            self.actions.click_button("Right")
            self.actions.click_button("Select")
            time.sleep(2)
            self.actions.doRokuSendKeys(mobile_number)
            time.sleep(2)
            self.actions.screenshotAttachment("number.jpeg")
            self.actions.click_button("Select")
            time.sleep(2)
            self.actions.click_button("Down")
            self.actions.click_button("Select")  

    def verify_enter_code_authentication_popup(self):
        if isinstance(self.actions, AndroidActions):
            authentication_popup_header = self.actions.is_element_displayed(*self.locators['2FA_POPUP_HEADER'])
            authentication_popup_text = self.actions.is_element_displayed(*self.locators['ENTER_CODE_TEXT'])
            verification_code = self.actions.is_element_displayed(*self.locators['VERIFICATION_CODE'])
            enter_code = self.actions.is_element_displayed(*self.locators['ENTER_CODDE_INPUT_FIELD'])
            unlock_button = self.actions.is_element_displayed(*self.locators['UNLOCK_BUTTON']) 
            Resend_code = [[authentication_popup_header, authentication_popup_text, verification_code, enter_code, unlock_button]]
            if all(Resend_code):
                return True
            else:
                return False
        elif isinstance(self.actions, iOSActions):
            authentication_popup_header = self.actions.is_element_displayed(*locators_ipad['2FA_POPUP_HEADER'])
            authentication_popup_text = self.actions.is_element_displayed(*locators_ipad['ENTER_CODE_TEXT'])
            verification_code = self.actions.is_element_displayed(*locators_ipad['VERIFICATION_CODE'])
            enter_code = self.actions.is_element_displayed(*locators_ipad['ENTER_CODDE_INPUT_FIELD'])
            resend_code = self.actions.is_element_displayed(*locators_ipad['RESEND_CODE_BUTTON'])
            unlock_button = self.actions.is_element_displayed(*locators_ipad['UNLOCK_BUTTON'])
            Resend_code = [[authentication_popup_header, authentication_popup_text, verification_code, enter_code, resend_code, unlock_button]]
            if all(Resend_code):
                self.actions.click_button(*locators_ipad['2FA_CLOSE_BUUTTON'])
                return True
            else:
                return False
        else:
            time.sleep(3)
            authentication_popup_header = self.actions.fetch_Data("lPasswordOrPhoneText", "Verification Code")
            enter_code = self.actions.fetch_Data("lPlaceHolderText", "Enter your code")   
            self.actions.screenshotAttachment("code.jpeg") 
            if all([authentication_popup_header, enter_code]):
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
        elif isinstance(self.actions, RokuActions):
            time.sleep(5)
            self.actions.click_button("Back")            
        