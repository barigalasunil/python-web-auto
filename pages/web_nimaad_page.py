from selenium.webdriver.common.by import By
# from pages.actions.webpage_actions import WebAppActions
from pages.actions.android_actions import AndroidActions
from selenium.webdriver.common.keys import Keys
from conftest import readConstants, readPreReqJsonValue
from pages.base_page import BasePage
import time
import random
import string

locators = {
    "VIEW_ENGAGEMENT": (By.XPATH, "//a[contains(text(), 'View engagements')]"),
    "ENGAGEMENT_KEY": (By.XPATH, "//th[@class='field-engagement_key']"),
    "IP_ADDRESS": (By.XPATH, "//td[@class='field-ip_address']"),
    "DEVICE": (By.XPATH, "//td[@class='field-device']"),
    "VIEW_SECONDS": (By.XPATH, "//td[@class='field-seconds_viewed']"),
    "MAX_SECONDS_VIEWED": (By.XPATH, "//td[@class='field-max_second_viewed']"),
    "VIEWTIME": (By.XPATH, "//td[@class='field-viewtime_in_seconds']"),
    "USERNAME": (By.XPATH, "//input[@id='id_username']"),
    "PASSWORD": (By.XPATH, "//input[@id='id_password']"),
    "LOGIN_BUTTON": (By.XPATH, "//input[@value='Log in']"),
    "UNSUPPORTED_DEVICES": (By.XPATH, "//a[@href='/nimad/indee_users/cmafunsupportedtvdevice/']"),
    "BUTTON_ADD_UNSUPPORTED_DEVICES": (By.XPATH, "(//a[@href='/nimad/indee_users/cmafunsupportedtvdevice/add/'])[2]"),
    "SELECT_DEVICE_BUTTON": (By.XPATH, "//select[@id='id_device_type']"),
    "DROPDOWN_DEVICE_SELECTION": (By.XPATH, "//select[@id='id_device_type']/option[text()='Amazon Firestick']"),
    "MODEL_NAME": (By.XPATH, "//input[@id='id_device_model_name']"),
    "DEVICE_MAKE": (By.XPATH, "//input[@id='id_device_make']"),
    "OS_VERSION": (By.XPATH, "//input[@id='id_os_version']"),
    "LOGIN_MESSAGE": (By.XPATH, "//textarea[@id='id_on_login_msg']"),
    "PLAYBACK_MESSAGE": (By.XPATH, "//textarea[@id='id_on_play_required_msg']"),
    "OPTINAL_PLAYACK_MESSAGE": (By.XPATH, "//textarea[@id='id_on_play_optional_msg']"),
    "SAVE_BUTTON": (By.XPATH, "//input[@value='Save']"),
    "SELECT_UNSUPPORTED_DEVICE": (By.XPATH, "(//a[contains(@href, '/nimad/indee_users/cmafunsupportedtvdevice/') and contains(@href, '/change/')])[1]"),
    "DELETE_BUTTON": (By.XPATH, "//a[@class='deletelink']"),
    "CONFIRM_DELETE": (By.XPATH, '//input[@value="Yes, I’m sure"]'),
    "USER_EMAILS": (By.XPATH, "//a[text()='Emails']"),
    "MAIL_LINK": (By.XPATH, "(//tr[td[contains(text(), '{username}')] and td[contains(text(), 'Reset password')]]//th[@class='field-id']/a)[1]"),
    "RESET_MAIL_LINK": (By.XPATH, "(//tr[td[contains(text(), '{username}')] and td[contains(text(), 'Welcome to Indee Screeners')]]//th[@class='field-id']/a)[1]"),
    "RESET_PASSWORDD_MAIL_TEXT": (By.XPATH, "//p[contains(text(), 'A password reset request was generated on Indee')]"),
    "RESET_PASSWORD_LINK": (By.XPATH, "//a[text()='Reset Password']"),
    "CREATE_PASSWORD_HEADER": (By.XPATH, "//div[@id='title-password-mode']"),
    "NEW_PASSWORD_TEXTFIELD": (By.XPATH, "//input[@id='forgot-password-field']"),
    "CONFIRM_PASSWORD_TEXTFIELD": (By.XPATH, "//input[@id='forgot-password-field-reconfirm']"),
    "CONTINUE_BUTTON": (By.XPATH, "//button[@id='continue-button']"),
    "PASSWORD_CHANGED_MESSAGE": (By.XPATH, "//div[text()='Password Created Successfully']"),
    "RESEND_VERIFICATION_EMAIL": (By.XPATH, "//a[text()='Verify Email']"),
    "APPLICATION_MANAGER": (By.XPATH, "//a[text()='Application configurations']"),
    "SEARCHBAR_TEXTFIELD": (By.XPATH, "//input[@id='searchbar']"),
    "SEARCH_SUBMIT_BUTTON": (By.XPATH, "//input[@type='submit' and @value='Search']"),
    "BRAND_SELECTION": (By.XPATH, "//tr[td[contains(text(), 'Valid_Ext_VL{pin}_2025 | FYC')]]//th/a[contains(text(), '{brand} | FYC | paramount')]"),
    "LISTED_ON_WATCH": (By.XPATH, "//input[@type='checkbox' and @id='id_is_listed_on_watch']"),
    "LISTED_APP_MANAGER": (By.XPATH, "//input[@type='checkbox' and @id='id_is_listed_on_app_manager']")
}


class NimaadPortalPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_login_credentials(self, driver, username, password):
        AndroidActions(driver).enter_text(*locators["USERNAME"], username)
        AndroidActions(driver).enter_text(*locators["PASSWORD"], password)
        AndroidActions(driver).click_button(*locators["LOGIN_BUTTON"])

    def click_on_view_engagement(self, driver):
        AndroidActions(driver).click_button(*locators["VIEW_ENGAGEMENT"])

    def verify_engagement_data(self, driver, request):
        platform = request.config.getoption("--platform")
        if platform == "fire_tv":
            device_name = "Amazon Firestick"
        elif platform == "ipad":
            device_name = "iPad"
        else:
            device_name = "Roku"
        Key = AndroidActions(driver).is_element_displayed(*locators['ENGAGEMENT_KEY'])
        AndroidActions(driver).get_text(*locators["IP_ADDRESS"])
        ip_value = AndroidActions(driver).is_element_displayed(*locators["IP_ADDRESS"])
        Device = AndroidActions(driver).get_text(*locators['DEVICE'])
        Device = Device.lower()
        if Device == device_name:
            Device_value = True
        else:
            Device_value = False
        View_seconds = AndroidActions(driver).is_element_displayed(*locators['VIEW_SECONDS'])
        Max_seconds = AndroidActions(driver).is_element_displayed(*locators['MAX_SECONDS_VIEWED'])
        View_time = AndroidActions(driver).is_element_displayed(*locators['VIEWTIME'])
        Engagement_data = [Key, ip_value, Device_value, View_seconds, Max_seconds, View_time]
        if all(Engagement_data):
            return True
        else:
            return False
        
    def click_on_unsupported_devices(self, driver):
        AndroidActions(driver).click_button(*locators["UNSUPPORTED_DEVICES"])

    def add_firestick_to_the_unsupported_devices(self, driver):
        Login_Message = readPreReqJsonValue("prereq", "fyc_unsupported_login_message")
        Playback_Message = readPreReqJsonValue("prereq", "fyc_unsupported_playback_message")
        Optional_Message = readPreReqJsonValue("prereq", "fyc_unsupported_optional_playback_message")
        Model_name = readPreReqJsonValue("prereq", "fyc_unsupported_firetv_model_name")
        Device_make = readPreReqJsonValue("prereq", "fyc_unsupported_firetv_device_make")
        os_version = readPreReqJsonValue("prereq", "fyc_unsupported_firetv_os_version")
        AndroidActions(driver).wait_for_element(*locators['BUTTON_ADD_UNSUPPORTED_DEVICES'])
        AndroidActions(driver).click_button(*locators["BUTTON_ADD_UNSUPPORTED_DEVICES"])
        AndroidActions(driver).click_button(*locators['SELECT_DEVICE_BUTTON'])
        AndroidActions(driver).click_button(*locators['DROPDOWN_DEVICE_SELECTION'])
        AndroidActions(driver).enter_text(*locators['MODEL_NAME'], Model_name)
        AndroidActions(driver).enter_text(*locators["DEVICE_MAKE"], Device_make)
        AndroidActions(driver).enter_text(*locators['OS_VERSION'], os_version)
        AndroidActions(driver).enter_text(*locators['LOGIN_MESSAGE'], Login_Message)
        AndroidActions(driver).enter_text(*locators['PLAYBACK_MESSAGE'], Playback_Message)
        AndroidActions(driver).enter_text(*locators['OPTINAL_PLAYACK_MESSAGE'], Optional_Message)
        time.sleep(10)
        AndroidActions(driver).click_button(*locators['SAVE_BUTTON'])

    def delete_firestick_from_the_unsupported_devices(self, driver):
        AndroidActions(driver).click_button(*locators['SELECT_UNSUPPORTED_DEVICE'])
        Model_name = readPreReqJsonValue("prereq", "fyc_unsupported_firetv_model_name")
        Device_make = readPreReqJsonValue("prereq", "fyc_unsupported_firetv_device_make")
        os_version = readPreReqJsonValue("prereq", "fyc_unsupported_firetv_os_version")
        Model = AndroidActions(driver).validate_text(*locators['MODEL_NAME'], Model_name)
        Make = AndroidActions(driver).validate_text(*locators["DEVICE_MAKE"], Device_make)
        Device_os = AndroidActions(driver).validate_text(*locators['OS_VERSION'], os_version)
        if all([Model, Make, Device_os]):
            AndroidActions(driver).click_button(*locators["DELETE_BUTTON"])
            AndroidActions(driver).click_button(*locators['CONFIRM_DELETE'])
        else:
            print("Device is already removedd from the list of unsupported device")

    def click_emails_in_nimaad(self, driver, user_name):
        AndroidActions(driver).wait_for_element(*locators["USER_EMAILS"])
        AndroidActions(driver).click_button(*locators['USER_EMAILS'])
        user_name = user_name.lower()
        print(user_name)
        by, value = locators['MAIL_LINK']
        formated_value = value.format(username=user_name)
        print(formated_value)
        AndroidActions(driver).wait_for_element(by, formated_value)
        AndroidActions(driver).click_button(by, formated_value)

    def click_resend_emails_in_nimaad(self, driver, user_name):
        AndroidActions(driver).wait_for_element(*locators["USER_EMAILS"])
        AndroidActions(driver).click_button(*locators['USER_EMAILS'])
        user_name = user_name.lower()
        print(user_name)
        by, value = locators['RESET_MAIL_LINK']
        formated_value = value.format(username=user_name)
        print(formated_value)
        AndroidActions(driver).wait_for_element(by, formated_value)
        AndroidActions(driver).click_button(by, formated_value)

    def verify_resend_verification_email(self, driver):
        return AndroidActions(driver).is_element_displayed(*locators['RESEND_VERIFICATION_EMAIL'])

    def click_reset_password_link(self, driver):
        AndroidActions(driver).wait_for_element(*locators["RESET_PASSWORDD_MAIL_TEXT"])
        AndroidActions(driver).wait_for_element(*locators["RESET_PASSWORD_LINK"])
        AndroidActions(driver).click_button(*locators['RESET_PASSWORD_LINK'])

    def create_new_password(self, driver):
        password = []
        password.append(random.choice(string.ascii_uppercase))  
        password.append(random.choice(string.digits))           
        password.append(random.choice(string.punctuation))
        characters = string.ascii_letters + string.digits + string.punctuation
        for i in range(6):
            password.append(random.choice(characters))
        password = ''.join(password)
        print(password)
        AndroidActions(driver).wait_for_element(*locators["CREATE_PASSWORD_HEADER"])
        AndroidActions(driver).enter_text(*locators['NEW_PASSWORD_TEXTFIELD'], password)
        AndroidActions(driver).enter_text(*locators['CONFIRM_PASSWORD_TEXTFIELD'], password)
        AndroidActions(driver).click_button(*locators['CONTINUE_BUTTON'])
        time.sleep(5)
        return password
    
    def verify_password_changed_success_message(self, driver):
        return AndroidActions(driver).is_element_displayed(*locators['PASSWORD_CHANGED_MESSAGE'])
    
    def navigate_to_application_manager_and_search_pin(self, driver, pin):
        AndroidActions(driver).wait_for_element(*locators["APPLICATION_MANAGER"])
        AndroidActions(driver).click_button(*locators['APPLICATION_MANAGER'])
        AndroidActions(driver).enter_text(*locators['SEARCHBAR_TEXTFIELD'], pin)
        AndroidActions(driver).click_button(*locators['SEARCH_SUBMIT_BUTTON'])

    def select_brand_to_enable_pin_configuration(self, driver, brand, pin):
        by, value = locators['BRAND_SELECTION']
        format_value = value.format(pin=pin, brand=brand)
        AndroidActions(driver).wait_for_element(by, format_value)
        AndroidActions(driver).click_button(by, format_value)

    def enable_pin_configuration_and_save(self, driver):
        listed_on_watch = self.driver.find_element(*locators["LISTED_ON_WATCH"])
        listed_on_watch_enabled = listed_on_watch.is_selected()
        if not listed_on_watch_enabled:
            AndroidActions(driver).click_button(*locators["LISTED_ON_WATCH"])
        listed_app_manager = self.driver.find_element(*locators["LISTED_APP_MANAGER"])
        listed_app_manager_enabled = listed_app_manager.is_selected()
        if not listed_app_manager_enabled:
            AndroidActions(driver).click_button(*locators["LISTED_APP_MANAGER"])
        time.sleep(5)
        AndroidActions(driver).click_button(*locators['SAVE_BUTTON'])
        time.sleep(5)

    def diable_pin_configuration_and_save(self, driver):
        listed_on_watch = self.driver.find_element(*locators["LISTED_ON_WATCH"])
        listed_on_watch_enabled = listed_on_watch.is_selected()
        if listed_on_watch_enabled:
            AndroidActions(driver).click_button(*locators["LISTED_ON_WATCH"])
        listed_app_manager = self.driver.find_element(*locators["LISTED_APP_MANAGER"])
        listed_app_manager_enabled = listed_app_manager.is_selected()
        if listed_app_manager_enabled:
            AndroidActions(driver).click_button(*locators["LISTED_APP_MANAGER"])
        time.sleep(5)
        AndroidActions(driver).click_button(*locators['SAVE_BUTTON'])
        time.sleep(5)
