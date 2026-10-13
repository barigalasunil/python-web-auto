from appium.webdriver.common.appiumby import AppiumBy


from pages.actions.android_actions import AndroidActions
from pages.actions.ios_actions import iOSActions
from conftest import readPreReqJsonValue
from pages.base_page import BasePage
from pages.logout_page_screener import LogoutPageScreener
import time
from pages.actions.roku_actions import RokuActions

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager

locators = {
    "USERNAME_FIELD": (AppiumBy.ID, 'com.indee.indeestaffsc:id/etMail'),
    "PASSWORD_FIELD": (AppiumBy.ID, 'com.indee.indeestaffsc:id/etPassword'),
    "ACCESS_CODE": (AppiumBy.ID, 'com.indee.indeestaffsc:id/etMail'),
    "LAUNCH_APP_ICON": (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.indee.indeestaffsc:id/frameLogin"]/android.view.ViewGroup[2]/android.view.ViewGroup'),  # noqa:E501
    "LOGIN_PAGE_BG_IMAGE": (AppiumBy.ID, 'com.indee.indeestaffsc:id/contentFrame'),
    "LOGIN_APP_ICON": (AppiumBy.ID, 'com.indee.indeestaffsc:id/ivLogo'),
    "LOGIN_SIGNIN_HEADER": (AppiumBy.ID, 'com.indee.indeestaffsc:id/txt_header'), 
    "LOGIN_EMAIL_LABEL": (AppiumBy.ID, 'com.indee.indeestaffsc:id/etMail'),
    "LOGIN_PASSWORD_LABEL": (AppiumBy.ID, 'com.indee.indeestaffsc:id/etPassword'),
    "LOGIN_FORGET_PASSWORD": (AppiumBy.ID, 'com.indee.indeestaffsc:id/btnForgotPassword'),
    "LOGIN_SIGNIN_SESSION_CHECKBOX": (AppiumBy.ID, 'com.indee.indeestaffsc:id/cbLoggedIn'), 
    "LOGIN_SIGNIN_BUTTON": (AppiumBy.ID, 'com.indee.indeestaffsc:id/btnLogin'), 
    "LOGIN_SIGNIN_WITHQRCODE_BUTTON": (AppiumBy.ID, 'com.indee.indeestaffsc:id/btnLoginQr'), 
    "LOGIN_APP_VERSION": (AppiumBy.ID, 'com.indee.indeestaffsc:id/tvVersion'),
    "LOGIN_SETTINGS_BUTTON": (AppiumBy.ID, 'com.indee.indeestaffsc:id/settings'),               
    "FORGOT_PSWD_POPUP_HEADER": (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]'),  # noqa:E501
    "FORGOT_PSWD_POPUP_TEXT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").textContains("web browser or use our iPad app")'),  # noqa:E501
    "FORGOT_PSWD_GO_BACK_BUTTON": (AppiumBy.ID, "com.indee.indeestaffsc:id/btnGoBack"),
    "QR_SIGNIN_HEADER": (AppiumBy.ID, "com.indee.indeestaffsc:id/textView41"),
    "QR_SIGNIN_URL": (AppiumBy.ID, "com.indee.indeestaffsc:id/textView10"),
    "QR_SIGNIN_CODE": (AppiumBy.ID, "com.indee.indeestaffsc:id/textView12"),
    "QR_SIGNIN_READY_TO_WATCH": (AppiumBy.ID, "com.indee.indeestaffsc:id/textView13"),
    "QR_CODE": (AppiumBy.ID, "com.indee.indeestaffsc:id/imgqrcode"),
    "SIGN_IN_WITH_REMOTE": (AppiumBy.ID, "com.indee.indeestaffsc:id/btnLoginWithRemote"),
    "INVALID_LOGIN_ERROR_MESSAGE": (AppiumBy.ID, "com.indee.indeestaffsc:id/tvError"),
    "USERNAME_QR_LOGIN": (AppiumBy.ID, 'tv-sign-in-email'),
    "PASSWORD_QR_LOGIN": (AppiumBy.ID, 'tv-sign-in-password'),
    "SIGN_IN_QR_LOGIN": (AppiumBy.ID, 'tv-sign-in-button'),
    "CMAF_POPUP_CONTINUE": (AppiumBy.ID, 'com.indee.indeestaffsc:id/btnContinue'),
    "SUCCESSFUL_MESSAGE_QR_LOGIN": (AppiumBy.XPATH, "//div[text()='Sign In Successful']"),
    "INVALID_MESSAGE": (AppiumBy.XPATH, "//div[@id='form-error-message']//small"),
    "PASSWORD_FIELD_BLANK_MESSAGE": (AppiumBy.ID, 'tv-sign-in-password-error-message'),
    "TERMS_OF_SERVICES": (AppiumBy.ID, 'com.indee.indeestaffsc:id/txt_terms'),
    "ERROR_MESSAGE": (AppiumBy.ID, 'com.indee.indeestaffsc:id/errorStrip'),
    "VERIFY_TERMS_AND_CONDITIONS": (AppiumBy.ID, 'com.indee.indeestaffsc:id/linearlayout'),
    "CMAF_POPUP_CONTINUE": (AppiumBy.ID, 'com.indee.indeestaffsc:id/btnContinue'),
    "SELECT_BRAND": (AppiumBy.XPATH, "(//*[@resource-id='com.indee.indeestaffsc:id/imgLogo'])[1]"),
    "ERROR_EXPIRY_PIN": (AppiumBy.ID, 'com.indee.indeestaffsc:id/tvError'),
    "HEADER_LOGO_T&C": (AppiumBy.ID, 'android.widget.ImageView'),
    "ERROR_MESSAGE_VERSION": (AppiumBy.ID, 'com.indee.indeestaffsc:id/tvError'),
    "EMAIL_INPUT_FIELD": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Email")'),
    "CMAF_WARNING_LOGO": (AppiumBy.ID, "com.indee.indeestaffsc:id/infoIcon"),
    "CMAF_WARNING_TEXT": (AppiumBy.ID, "com.indee.indeestaffsc:id/dialog_msg"),
    "CMAF_BUTTON_CONTINUE": (AppiumBy.ID, "com.indee.indeestaffsc:id/btnContinue"),
    "CMAF_ASK_ME_AGAIN": (AppiumBy.ID, 'com.indee.indeestaffsc:id/checkBoxRemindSection'),
    "CMAF_CHECKBOOX": (AppiumBy.ID, "com.indee.indeestaffsc:id/checkboxMark"),
    "CHAT_SUPPORT": (AppiumBy.ID, "com.indee.indeestaffsc:id/txt_chat_support")
}

locators_ipad = {
    "USERNAME_FIELD": (AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField'),
    "PASSWORD_FIELD": (AppiumBy.CLASS_NAME, 'XCUIElementTypeSecureTextField'),
    "LAUNCH_APP_ICON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage'),    # noqa:E501
    "LOGIN_PAGE_BG_IMAGE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage'),  # noqa:E501
    "LOGIN_APP_ICON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage'),  # noqa:E501
    "LOGIN_SIGNIN_HEADER": (AppiumBy.ACCESSIBILITY_ID, 'Sign in'),                        
    "LOGIN_FORGET_PASSWORD": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Forgot Password?"`]'),
    "LOGIN_CHECKBOX_ENABLED": (AppiumBy.ACCESSIBILITY_ID, 'checkedBox'),
    "LOGIN_CHECKBOX_DISABLED": (AppiumBy.ACCESSIBILITY_ID, 'uncheckedBox'),
    "LOGIN_SIGNIN_SESSION_CHECKBOX": (AppiumBy.IOS_PREDICATE, "name CONTAINS[c] 'Keep me signed in'"),
    "LOGIN_SIGNIN_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "SIGN IN"`]'),       
    "LOGIN_ENTER_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "ENTER"`]'),
    "TERMS_OF_SERVICE_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Read our Terms of Service  "`]'),
    "LOGIN_APP_VERSION": (AppiumBy.IOS_PREDICATE, 'name Contains "V "'),
    "LOGIN_SETTINGS_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Settings"`]'),
    "LOGIN_CHATBOX_BUTTON": (AppiumBy.ACCESSIBILITY_ID, 'chatsupport'),
    "TERMS_OF_CONDITION_DOCUMENT": (AppiumBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[8]/XCUIElementTypeImage'),  
    "ENTER_PIN_ERROR_MESSAGE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name contains "{error_message}"`]'),
    "INVALID_PIN_ERROR_MESSAGE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name contains "{error_message}"`]'),
    "EXPIRED_PIN_ERROR_MESSAGE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name contains "{error_message}"`]'),
    "EMAIL_INPUT_FIELD": (AppiumBy.IOS_PREDICATE, "name CONTAINS[c] 'Email'"),
    "HEADER_LOGO": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage'),  # noqa:E501
    "OLD_VERSION_ERROR_MESSAGE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name contains "{error_message}"`]'),
    "TESTFLIGHT_APP_NAME": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Screeners Testing App"`]'),
    "LOGIN_SETTINGS_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Settings"`]'),                                                  
    "FORGOT_PSWD_POPUP_HEADER": (AppiumBy.ACCESSIBILITY_ID, 'Enter your email to reset your password'),  
    "FORGOT_PSWD_EMAIL_TEXTFIELD": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`value == " Enter your email address"`]'),  # noqa:E501
    "FORGOT_PSWD_GO_BACK_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "  GO BACK"`]'),
    "FORGOT_PSWD_ENTER_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "ENTER"`]'),
    "FORGOT_PSWD_EMAIL_SENT_MSG": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "An email containing the password reset link has been sent to your email ID."`]'),  # noqa:E501
    "FORGOT_PSWD_DONE_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "DONE"`]'),
    "TERMS_OF_SERVICES": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Read our Terms of Service  "`]'),
    "TERMS_OF_SERVICE_DOC": (AppiumBy.CLASS_NAME, 'XCUIElementTypeTable'),
    "TERMS_OF_SERVICE_BACK_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "backImg"`]'),
    "ERROR_MESSAGE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "You are using an older version of this app. Update the app to continue."`]'),  # noqa:E501
    "INVALID_LOGIN_ERROR_MESSAGE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "{error_message}"`]'),  # noqa:E501
    "EMPTY_CREDENTIALS_ERROR_MESSAGE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Invalid credentials. Contact support@indee.tv for assistance."`]'),  # noqa:E501
    "TESTFLIGHT_APP_INSTALL": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Install"`]'),
    "TESTFLIGHT_APPOPEN": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Open"`]'),
    "TESTFLIGHT": (AppiumBy.CLASS_NAME, 'XCUIElementTypeApplication'),
    "PREVIOUS_BUILD": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name contains "Previous Builds"`]'),
    "PREVIOUS_BUILD_SELECTION": (AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton'),   # noqa:E501
    "INSTALL_PREVIOUS_BUILD": (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther//XCUIElementTypeButton[@name="Install"][1]'),   # noqa:E501
    "OPEN_PREVIOUUS_BUILD": (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther//XCUIElementTypeButton[@name="Open"][1]'),   # noqa:E501
    "TESTFLIGHT_APP_UPDATE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "UPDATE"`]'),
    "API_ERROR_MESSAGE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "{error_message}"`]'),
    "FORGOT_PSWD_EMAIL_SENT_DONE_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "DONE"`]'),
    "CHAT_SUPPORT": (AppiumBy.ACCESSIBILITY_ID, "chatsupport"),
    "RESEND_VERIFICATION_HEADER": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "{}"`]'), 
    "RESEND_VERIFICATION_EMAIL_TEXT": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name contains "{}"`]'), 
    "RESEND_VERIFICATION_MESSAGE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "{}"`]'),  
    "RESEND_VERIFICATION_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "RESEND VERIFICATION LINK"`]'),
    "GO_BACT_TO_SIGNIN_BUTTON": (AppiumBy.XPATH, '//XCUIElementTypeButton[2]'),
    "OLDER_BUILD_INSTALL_POPUP": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Install"`][5]'),
    "NO_THANKS_CRASH_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "No Thanks"`]')
}


class LoginPageScreener(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # USERNAME_FIELD = (AppiumBy.ID, 'com.indee.indeestaffsc:id/etMail')
    # PASSWORD_FIELD = (AppiumBy.ID, 'com.indee.indeestaffsc:id/etPassword')
    # LAUCH_APP_ICON = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.indee.indeestaffsc:id/frameLogin"]/android.view.ViewGroup[2]/android.view.ViewGroup')  # noqa:E501
    # LOGIN_PAGE_BG_IMAGE = (AppiumBy.ID, 'com.indee.indeestaffsc:id/iv_bg_login')
    # LOGIN_APP_ICON = (AppiumBy.ID, 'com.indee.indeestaffsc:id/ivLogo')
    # LOGIN_SIGNIN_HEADER = (AppiumBy.ID, 'com.indee.indeestaffsc:id/txt_header')
    # LOGIN_EMAIL_LABEL = (AppiumBy.ID, 'com.indee.indeestaffsc:id/etMail')
    # LOGIN_PASSWORD_LABEL = (AppiumBy.ID, 'com.indee.indeestaffsc:id/etPassword')
    # LOGIN_FORGET_PASSWORD = (AppiumBy.ID, 'com.indee.indeestaffsc:id/btnForgotPassword')
    # LOGIN_SIGNIN_WITHQRCODE_BUTTON = (AppiumBy.ID, 'com.indee.indeestaffsc:id/btnLoginQr')
    # LOGIN_APP_VERSION = (AppiumBy.ID, 'com.indee.indeestaffsc:id/tvVersion')
    # LOGIN_SETTINGS_BUTTON = (AppiumBy.ID, 'com.indee.indeestaffsc:id/settings')
    # FORGOT_PSWD_POPUP_HEADER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").textContains("Forgot Password?")')  # noqa:E501
    # FORGOT_PSWD_POPUP_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").textContains("web browser or use our iPad app")')  # noqa:E501
    # FORGOT_PSWD_GO_BACK_BUTTON = (AppiumBy.ID, "com.indee.indeestaffsc:id/btnGoBack")
    # QR_SIGNIN_HEADER = (AppiumBy.ID, "com.indee.indeestaffsc:id/textView41")
    # QR_SIGNIN_URL = (AppiumBy.ID, "com.indee.indeestaffsc:id/textView10")
    # QR_SIGNIN_CODE = (AppiumBy.ID, "com.indee.indeestaffsc:id/textView12")
    # QR_SIGNIN_READY_TO_WATCH = (AppiumBy.ID, "com.indee.indeestaffsc:id/textView13")
    # QR_CODE = (AppiumBy.ID, "com.indee.indeestaffsc:id/imgqrcode")
    # SIGN_IN_WITH_REMOTE = (AppiumBy.ID, "com.indee.indeestaffsc:id/btnLoginWithRemote")
    # INVALID_LOGIN_ERROR_MESSAGE = (AppiumBy.ID, "com.indee.indeestaffsc:id/tvError")
    # USERNAME_QR_LOGIN = (AppiumBy.ID, 'tv-sign-in-email')
    # PASSWORD_QR_LOGIN = (AppiumBy.ID, 'tv-sign-in-password')
    # SIGN_IN_QR_LOGIN = (AppiumBy.ID, 'tv-sign-in-button')
    # SUCCESSFULL_MESSAGE_QR_LOGIN = (AppiumBy.XPATH, "//div[text()='Sign In Successful']")
    # INVALID_MESSAGE = (AppiumBy.XPATH, "//div[@id='form-error-message']//small")
    # PASSWORD_FIELD_BLANK_MESSAGE = (AppiumBy.ID, 'tv-sign-in-password-error-message')

    def verify_launchScreen_view(self):
        if isinstance(self.actions, AndroidActions):
            return self.actions.is_element_displayed(*locators['LAUNCH_APP_ICON'])
        elif isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad['LAUNCH_APP_ICON'])
        else:
            return True

    def verify_bg_image_displayed(self):
        if isinstance(self.actions, AndroidActions):
            try:
                return self.actions.is_element_displayed(*locators['LOGIN_PAGE_BG_IMAGE'])
            except Exception:
                pass
        elif isinstance(self.actions, iOSActions):
            Bg_image = self.actions.is_element_displayed(*locators_ipad['LOGIN_PAGE_BG_IMAGE'])
            return Bg_image
        else: 
            time.sleep(17)
            self.actions.screenshotAttachment("background.jpeg")
            return self.actions.is_element_displayed("name", "pBackground", "")
        
    def verify_loginPage_Icon(self):
        try: 
            if isinstance(self.actions, AndroidActions):
                return self.actions.is_element_displayed(*locators['LOGIN_APP_ICON'])
            elif isinstance(self.actions, iOSActions):
                App_Icon = self.actions.is_element_displayed(*locators_ipad['LOGIN_APP_ICON'])
                return App_Icon
            else:
                print("Login page logo")
                self.actions.screenshotAttachment("logo.jpeg")
                return self.actions.is_element_displayed("name", "pLogo", "")
        except Exception:
            pass
        
    def verify_signin_header(self):
        if isinstance(self.actions, AndroidActions):
            return self.actions.is_element_displayed(*locators['LOGIN_SIGNIN_HEADER'])
        elif isinstance(self.actions, iOSActions):
            try:
                self.actions.click_button(*locators_ipad['NO_THANKS_CRASH_BUTTON'])
            except Exception:
                pass
            return self.actions.is_element_displayed(*locators_ipad['LOGIN_SIGNIN_HEADER'])
        elif isinstance(self.actions, RokuActions): 
            time.sleep(20)
            
           # status = self.actions.is_element_displayed("name", "lPlaceHolderText", "Enter your access code")
           # print("access code", status)
           # return status
            self.actions.screenshotAttachment("Signin.jpeg")
            return self.actions.is_element_displayed("name", "lSignIn", "Sign in")
        
    def verify_Email_text_field(self, emailText):
        if isinstance(self.actions, AndroidActions):
            textVisibility = self.actions.get_element_visibility(*locators["LOGIN_EMAIL_LABEL"])
            if (textVisibility):
                print('Email field is present and validate right text')
                return self.actions.validate_text_contains(*locators['LOGIN_EMAIL_LABEL'], emailText)
            print('textVisibility == for email field validation', textVisibility)
            return textVisibility
        if isinstance(self.actions, iOSActions):
            textVisibility = self.actions.get_element_visibility(*locators_ipad["USERNAME_FIELD"])
            if (textVisibility):
                print('Email field is present and validate right text')
                return self.actions.validate_text_contains(*locators_ipad['USERNAME_FIELD'], emailText)
            print('textVisibility == for email field validation', textVisibility)
            return textVisibility
        elif isinstance(self.actions, RokuActions):
            self.actions.screenshotAttachment("email.jpeg")
            return self.actions.is_element_displayed("name", "lPlaceHolderText", "Enter your email address")

    def verify_password_text_field(self, passwordText):
        if isinstance(self.actions, AndroidActions):
            textVisibility = self.actions.get_element_visibility(*locators['LOGIN_PASSWORD_LABEL'])
            print(textVisibility)
            if (textVisibility):
                print('password field is present and validate right text')
                return self.actions.validate_text(*locators['LOGIN_PASSWORD_LABEL'], passwordText)
            print('textVisibility == for password validation', textVisibility)
            return (textVisibility)
        elif isinstance(self.actions, iOSActions):
            textVisibility = self.actions.get_element_visibility(*locators_ipad['PASSWORD_FIELD'])
            if textVisibility:
                print('email field is present and validate right text')
                return self.actions.validate_text_contains(*locators_ipad['PASSWORD_FIELD'], passwordText)
            print('textVisibility == for password validation', textVisibility)
            return textVisibility
        else:
            return True

    def verify_forgetpassword_text_field(self, forgetPasswordText):
        if isinstance(self.actions, AndroidActions):   
            textVisibility = self.actions.get_element_visibility(*locators['LOGIN_FORGET_PASSWORD'])
            if (textVisibility):
                print('forgetpassword_ field is present and validate right text')
                return self.actions.validate_text(*locators['LOGIN_FORGET_PASSWORD'], forgetPasswordText)
            print('textVisibility == for forgetpassword_ validation', textVisibility)
            return (textVisibility)
        elif isinstance(self.actions, iOSActions):
            textVisibility = self.actions.get_element_visibility(*locators_ipad['LOGIN_FORGET_PASSWORD'])
            if (textVisibility):
                print('forgetpassword_ field is present and validate right text')
                return self.actions.validate_text_contains(*locators_ipad['LOGIN_FORGET_PASSWORD'], forgetPasswordText)
            print('textVisibility == for forgetpassword_ validation', textVisibility)
            return (textVisibility)
        else:
            time.sleep(17)
            forget_password_text = readPreReqJsonValue("prereq","forgot_password_text")
            forget_password = self.actions.fetch_Data("lForgotPassword", forget_password_text)
            if forgetPasswordText == forget_password:
                return True
            else:
                return False
        
    def verify_forget_password_popup(self):
        if isinstance(self.actions, AndroidActions):
            Popup = self.actions.is_element_displayed(*locators["FORGOT_PSWD_POPUP_HEADER"])
            self.actions.click_button(*locators["FORGOT_PSWD_GO_BACK_BUTTON"])
            self.actions.click_button(*locators["FORGOT_PSWD_GO_BACK_BUTTON"])
            return Popup
        elif isinstance(self.actions, iOSActions):
            Popup = self.actions.is_element_displayed(*locators_ipad["FORGOT_PSWD_POPUP_HEADER"])
            self.actions.click_button(*locators_ipad["FORGOT_PSWD_GO_BACK_BUTTON"])
            return Popup
        elif isinstance(self.actions, RokuActions):
            time.sleep(3)
            self.actions.screenshotAttachment("Signin.jpeg")
            text_to_validate = readPreReqJsonValue("prereq", "screener_forget_password_text")
            Forget_password = self.actions.is_element_displayed("name", "lPageText", text_to_validate)
            time.sleep(2)
            self.actions.click_button("Back")
            self.actions.click_button("Up")
            self.actions.click_button("Up")
            return Forget_password      
                           
    def verify_signin_session_checkBox(self, checboxStatus, sessionDays):
        if isinstance(self.actions, AndroidActions):
            actualcheckBoxStatus = self.actions.is_checkbox_checked(*locators['LOGIN_SIGNIN_SESSION_CHECKBOX'])
            if (actualcheckBoxStatus == checboxStatus):
                print('Login Checkbox Is Displayed And The Status is As Expected')
                print(checboxStatus)
                print(sessionDays)
                return self.actions.validate_text_contains(*locators['LOGIN_SIGNIN_SESSION_CHECKBOX'], sessionDays)
            else:
                return (actualcheckBoxStatus == checboxStatus)
        elif isinstance(self.actions, iOSActions):
            if checboxStatus:
                Checkbox_Enabled = self.actions.get_element_visibility(*locators_ipad['LOGIN_CHECKBOX_ENABLED'])
                if Checkbox_Enabled:
                    print('Login Checkbox Is Displayed And The Status is As Expected')
                    return self.actions.validate_text_contains(*locators_ipad['LOGIN_SIGNIN_SESSION_CHECKBOX'], sessionDays)
                else:
                    print('Checkbox is Disabled')
                    return False
            else:
                Checkbox_Disabled = self.actions.get_element_visibility(*locators_ipad['LOGIN_CHECKBOX_DISABLED'])
                if Checkbox_Disabled:
                    print('Login Checkbox Is Displayed And The Status is As Expected')
                    return self.actions.validate_text_contains(*locators_ipad['LOGIN_SIGNIN_SESSION_CHECKBOX'], sessionDays)
                else:
                    print('Checkbox is Enabled')
                    return False
        elif isinstance(self.actions, RokuActions):
            self.actions.screenshotAttachment("sessiondays.jpeg")
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, sessionDays, False, "", "", False, "")
            status = self.actions.is_text_available(data, sessionDays)
            return status
        
    def enter_Access_Code(self, accesscode):
        accesscode = "Valid_Pin" + accesscode
        if isinstance(self.actions, AndroidActions):
            print('Inside Android actions block')
            print(accesscode)
            self.actions.is_element_displayed(*locators["ACCESS_CODE"])
            self.actions.enter_text(*locators["ACCESS_CODE"], accesscode)
        elif isinstance(self.actions, iOSActions):
            self.actions.enter_text(*locators_ipad["ACCESS_CODE"], accesscode)
        else:
            time.sleep(8)
            self.actions.click_button("Select")
            time.sleep(4)
            self.actions.doRokuSendKeys(accesscode)
            self.actions.screenshotAttachment("accesscode.jpeg")
            self.actions.click_button("Enter")
            time.sleep(3)
        
    def verify_terms_and_service_button(self):
        if isinstance(self.actions, iOSActions):   
            return self.actions.is_element_displayed(*locators_ipad['TERMS_OF_SERVICES'])
        else:
            return True

    def verify_chat_support(self):
        # if isinstance(self.actions, AndroidActions):   
        #     return True
        #     # return self.actions.is_element_displayed(*locators['CHAT_SUPPORT'])
        if isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad['CHAT_SUPPORT'])
        else:
            return True    

    def enter_password(self, password):
        if isinstance(self.actions, AndroidActions):   
            self.actions.enter_text(*locators['PASSWORD_FIELD'], password)
        elif isinstance(self.actions, iOSActions):
            self.actions.enter_text(*locators_ipad["ACCESS_CODE"], password)
        else:
            time.sleep(8)
            self.actions.click_button("Select")
            time.sleep(4)
            self.actions.doRokuSendKeys(password)
            self.actions.screenshotAttachment("password.jpeg")
            self.actions.click_button("Enter")
            time.sleep(3)
           
    def click_login(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*locators['LOGIN_SIGNIN_BUTTON'])
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['LOGIN_SIGNIN_BUTTON'])
        else:
            self.actions.click_button("Select")
            time.sleep(8)
            # self.actions.click_button("Down")
            # time.sleep(1)
            # self.actions.click_button("Down")
            # time.sleep(1)  
            # self.actions.click_button("Select")
            # time.sleep(1)             

    def do_login(self, username, password):
        if '{0}' in username:
            username = username.replace('{0}', readPreReqJsonValue("prereq", "publicity_execution_id")) + "@gmail.com"
        if isinstance(self.actions, AndroidActions):
            self.actions.enter_text(*locators['LOGIN_EMAIL_LABEL'], username)
            self.actions.enter_text(*locators['LOGIN_PASSWORD_LABEL'], password)
            self.actions.click_button(*locators['LOGIN_SIGNIN_SESSION_CHECKBOX'])
            self.verify_signin_session_checkBox(True, "Keep me signed in")
            print("Login Button Text: ", self.actions.get_element_text(locators['LOGIN_SIGNIN_BUTTON']))
            self.actions.click_button(*locators['LOGIN_SIGNIN_BUTTON'])
        elif isinstance(self.actions, iOSActions):
            self.actions.enter_text(*locators_ipad['USERNAME_FIELD'], username)
            self.actions.enter_text(*locators_ipad['PASSWORD_FIELD'], password)
            self.verify_signin_session_checkBox(False, readPreReqJsonValue("prereq", "checkbox_text"))
            self.actions.click_button(*locators_ipad['LOGIN_SIGNIN_BUTTON'])
        else:
            time.sleep(17)
            print("Enter credentials=====")
            self.actions.click_button("Select")
            self.actions.doRokuSendKeys(username)
            self.actions.screenshotAttachment("username.jpeg")
            self.actions.click_button("Enter")
            self.actions.click_button("Select")
            self.actions.doRokuSendKeys(password)
            self.actions.click_button("Enter")
            self.actions.click_button("Select")
            self.actions.screenshotAttachment("password.jpeg")
            self.actions.click_button("Enter")
            self.actions.screenshotAttachment("afterenter.jpeg")

    def check_loginbutton_visbility(self):
        if isinstance(self.actions, AndroidActions):
            return self.actions.is_element_displayed(*locators['LOGIN_SIGNIN_BUTTON'])
        elif isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad["LOGIN_SIGNIN_BUTTON"])
        elif isinstance(self.actions, RokuActions):
            self.actions.screenshotAttachment("loginbutton.jpeg")
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "ENTER", False, "", "", False, "")
            status = self.actions.is_text_available(data, "ENTER")
            return status
            # return self.actions.is_element_displayed("name", "lButtonText", "ENTER")
        
    def check_loginbutton_QR_Code_visbility(self):
        if isinstance(self.actions, AndroidActions):
            return self.actions.is_element_displayed(*locators['LOGIN_SIGNIN_WITHQRCODE_BUTTON'])
        elif isinstance(self.actions, iOSActions):
            print('QR Code feeature iis not applicable for ipad')
            return True
        elif isinstance(self.actions, RokuActions):
            self.actions.screenshotAttachment("QRCode.jpeg")
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "SIGN IN WITH QR CODE", False, "", "", False, "")
            status = self.actions.is_text_available(data, "SIGN IN WITH QR CODE")
            # return self.actions.is_element_displayed("name", "lButtonText", "SIGN IN WITH QR CODE")
            return status
        
    def check_app_version_visibilty(self):
        if isinstance(self.actions, AndroidActions):
            return self.actions.is_element_displayed(*locators['LOGIN_APP_VERSION'])
        elif isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad['LOGIN_APP_VERSION'])
        else:  # for ruku 
            return self.actions.is_element_displayed("name", "lVersion", "")

    def check_settings_button_visibilty(self):
        if isinstance(self.actions, AndroidActions):
            return self.actions.is_element_displayed(*locators['LOGIN_SETTINGS_BUTTON'])
        elif isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad['LOGIN_SETTINGS_BUTTON'])
        elif isinstance(self.actions, RokuActions):
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "SETTINGS", False, "", "", False, "")
            status = self.actions.is_text_available(data, "SETTINGS")
            return status
           # return self.actions.is_element_displayed("name", "lButtonText", "SETTINGS")
        
    def click_settings_button(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*locators['LOGIN_SETTINGS_BUTTON'])
            print("Button Clicked")
            time.sleep(10)
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['LOGIN_SETTINGS_BUTTON'])
            print("Button Clicked")
            time.sleep(10)
        elif isinstance(self.actions, RokuActions):
            time.sleep(15)
            for i in range(8):      
                self.actions.click_button("Down")
            time.sleep(5)
            self.actions.click_button("Select")                  

    def verify_Forgot_Password_Link_isDisplayed(self):
        return self.actions.is_element_displayed(*locators['LOGIN_FORGET_PASSWORD'], timeout=10)

    def click_Forgot_Password(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*locators['LOGIN_FORGET_PASSWORD'])
            try:
                self.actions.click_button(*locators['LOGIN_FORGET_PASSWORD'])
            except Exception:
                pass
            print("Button Clicked")
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['LOGIN_FORGET_PASSWORD'])
            print("Button Clicked")
        elif isinstance(self.actions, RokuActions):
            self.actions.screenshotAttachment("clickforgetpassord")
            for i in range(2): 
                time.sleep(1)     
                self.actions.click_button("Down")
            self.actions.click_button("Select")  
            self.actions.screenshotAttachment("after_clickforgetpassord") 

    def verify_Forgot_Password_PopupHeader(self, PopUpHeaderText):
        if isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad['FORGOT_PSWD_POPUP_HEADER'])
        else:
            return True

    def verify_Forgot_Password_Popup(self, PopUpText):
        print("Verifying Forgot password popup is displayed")
        return self.actions.validate_text_contains(*locators['FORGOT_PSWD_POPUP_TEXT'], PopUpText)

    def click_on_forgot_password_go_back_button(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*locators['FORGOT_PSWD_GO_BACK_BUTTON'])
        elif isinstance(self.actions, RokuActions):
            self.actions.screenshotAttachment("goback.jpeg") 
            self.actions.is_element_displayed("name", "lButtonText", "GO BACK")
            self.actions.click_button("Select")

    def enter_username_in_forgot_password(self, username):
        if isinstance(self.actions, iOSActions):
            print("Entering username in forgot password")
            self.actions.enter_text(*locators_ipad['FORGOT_PSWD_EMAIL_TEXTFIELD'], username)
            self.actions.click_button(*locators_ipad['FORGOT_PSWD_ENTER_BUTTON'])
            try:
                self.actions.click_button(*locators_ipad['FORGOT_PSWD_ENTER_BUTTON'])
            except Exception:
                pass
        else:
            pass

    def verify_email_sent_message_in_forgot_password(self, success_message):
        if isinstance(self.actions, iOSActions):
            Success_message = self.actions.validate_text_contains(*locators_ipad['FORGOT_PSWD_EMAIL_SENT_MSG'], success_message)
            self.actions.click_button(*locators_ipad['FORGOT_PSWD_EMAIL_SENT_DONE_BUTTON'])
            for i in range(3):
                login_page_navigation = self.actions.is_element_displayed(*locators_ipad['LOGIN_SIGNIN_HEADER'])
                if login_page_navigation:
                    break
                else:
                    self.actions.click_button(*locators_ipad['FORGOT_PSWD_EMAIL_SENT_DONE_BUTTON'])
            return Success_message
        else:
            return True
    
    def click_on_done_button_in_forgot_password(self):
        if isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['FORGOT_PSWD_DONE_BUTTON'])
            for i in range(3):
                login_page_navigation = self.actions.is_element_displayed(*locators_ipad['LOGIN_SIGNIN_HEADER'])
                if login_page_navigation:
                    break
                else:
                    self.actions.click_button(*locators_ipad['FORGOT_PSWD_DONE_BUTTON'])
        else:
            pass

    def do_login_With_Invalid_Credentials(self, username, password):
        self.actions.is_element_displayed(*locators['LOGIN_EMAIL_LABEL'])
        self.actions.enter_text(*locators['LOGIN_EMAIL_LABEL'], username)
        self.actions.enter_text(*locators['LOGIN_PASSWORD_LABEL'], password)

    def fetch_invalid_error_message(self, errormessage):
        if isinstance(self.actions, AndroidActions):
            return self.actions.get_element_text(locators['INVALID_LOGIN_ERROR_MESSAGE'])
            # return self.actions.get_text(*locators['INVALID_LOGIN_ERROR_MESSAGE'])
        elif isinstance(self.actions, iOSActions):
            by, value = locators_ipad["ENTER_PIN_ERROR_MESSAGE"]
            default_format_value = value.format(error_message=errormessage)
            self.actions.click_button(*locators_ipad['LOGIN_SIGNIN_BUTTON'])
            Error_Message = self.actions.is_element_displayed(by, default_format_value)
            return Error_Message
        else:
            time.sleep(6)
            invalid_credentials = self.actions.is_element_displayed("name", "message", "")
            time.sleep(3)
            for i in range(4):
                time.sleep(1)
                self.actions.click_button("Up")
            time.sleep(3)    
            self.actions.click_button("Select")
            time.sleep(4)
            self.actions.click_button("Up") 
            self.actions.click_button("Down") 
            time.sleep(5)
            self.actions.click_button("Down") 
            for i in range(40):
                self.actions.click_button("Select")
            time.sleep(2) 
            self.actions.click_button("Down") 
            self.actions.click_button("Down")   
            self.actions.click_button("Select")
            time.sleep(3)  
            self.actions.click_button("Down")
            self.actions.click_button("Select")
            time.sleep(3)
            self.actions.click_button("Up")
            self.actions.click_button("Down") 
            self.actions.click_button("Down") 
            for i in range(40):
                self.actions.click_button("Select")
            time.sleep(2) 
            self.actions.click_button("Down") 
            self.actions.click_button("Down")   
            self.actions.click_button("Select")
            time.sleep(3) 
            self.actions.click_button("Up")
            time.sleep(3) 
            return invalid_credentials 
        
    def fetch_invalid_error_message_non_verified_user(self, error_message, error_message_ipad):
        if isinstance(self.actions, AndroidActions):   
            return self.actions.validate_text(*locators['INVALID_LOGIN_ERROR_MESSAGE'], error_message)
        elif isinstance(self.actions, iOSActions):
            by, value = locators_ipad["ENTER_PIN_ERROR_MESSAGE"]
            default_format_value = value.format(error_message=error_message_ipad)
            self.actions.click_button(*locators_ipad['LOGIN_SIGNIN_BUTTON'])
            Error_Message = self.actions.is_element_displayed(by, default_format_value)
            return Error_Message
        else:
            time.sleep(6)
            invalid_credentials = self.actions.is_element_displayed("name", "message", "")
            time.sleep(3)
            for i in range(4):
                time.sleep(1)
                self.actions.click_button("Up")
            time.sleep(3)    
            self.actions.click_button("Select")
            time.sleep(4)
            self.actions.click_button("Up") 
            self.actions.click_button("Down") 
            time.sleep(5)
            self.actions.click_button("Down") 
            for i in range(40):
                self.actions.click_button("Select")
            time.sleep(2) 
            self.actions.click_button("Down") 
            self.actions.click_button("Down")   
            self.actions.click_button("Select")
            time.sleep(3)  
            self.actions.screenshotAttachment("settings.jpeg")
            self.actions.click_button("Down")
            self.actions.click_button("Select")
            time.sleep(3)
            self.actions.click_button("Up")
            self.actions.click_button("Down") 
            self.actions.click_button("Down") 
            for i in range(40):
                self.actions.click_button("Select")
            time.sleep(2) 
            self.actions.click_button("Down") 
            self.actions.click_button("Down")   
            self.actions.click_button("Select")
            time.sleep(3) 
            self.actions.screenshotAttachment("settings.jpeg")
            self.actions.click_button("Up")
            time.sleep(3) 
            return invalid_credentials 

    def sign_In(self):
        if isinstance(self.actions, AndroidActions):  
            self.actions.click_button(*locators['LOGIN_SIGNIN_BUTTON'])
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['LOGIN_SIGNIN_BUTTON'])

    def clear_email_and_password_fields(self):
        Email_Field = self.actions.wait_for_element(*locators['LOGIN_EMAIL_LABEL'])
        Email_Field.clear()
        Password_Field = self.actions.wait_for_element(*locators['LOGIN_PASSWORD_LABEL'])
        Password_Field.clear()

    def click_sign_in_with_qr_code_button(self):
        if isinstance(self.actions, AndroidActions):   
            self.actions.is_element_displayed(*locators['LOGIN_SIGNIN_WITHQRCODE_BUTTON'])
            self.actions.click_button(*locators['LOGIN_SIGNIN_WITHQRCODE_BUTTON'])
            try:
                self.actions.click_button(*locators['LOGIN_SIGNIN_WITHQRCODE_BUTTON'])
            except Exception:
                pass
                print("Button Clicked")
        elif isinstance(self.actions, RokuActions):
            time.sleep(14)
            for i in range(5):      
                self.actions.click_button("Down")
                time.sleep(4)
            self.actions.click_button("Select") 
            self.actions.screenshotAttachment("QRcode.jpeg")
        else:
            pass

    def check_loginbutton_visbility(self):
        if isinstance(self.actions, AndroidActions):
            return self.actions.is_element_displayed(*locators['LOGIN_SIGNIN_BUTTON'])
        elif isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad['LOGIN_SIGNIN_BUTTON'])
        else:
            return self.actions.is_element_displayed("name", "lSignIn", "Sign in")                         

    def verify_qr_code_page_navigation(self):
        if isinstance(self.actions, AndroidActions): 
            try:  
                self.actions.wait_for_element(*locators['LOGIN_FORGET_PASSWORD'], timeout=10)
            except Exception:
                pass
            return self.actions.is_element_displayed(*locators['QR_SIGNIN_HEADER'])
        elif isinstance(self.actions, RokuActions):
            return self.actions.is_element_displayed("name", "lSignIn", "Sign in with QR code")
        else:
            return True
    
    def verify_qr_screen_sign_in_url(self):
        if isinstance(self.actions, AndroidActions): 
            return self.actions.is_element_displayed(*locators['QR_SIGNIN_URL'])
        elif isinstance(self.actions, RokuActions):
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", False, "", True, "name", "mslFirstInstruction", False, "")
            firstInstruction = self.actions.is_text_available(data, "mslFirstInstruction") 
            self.actions.screenshotAttachment("url.jpeg")
            return firstInstruction
        else:
            return True
           
    def verify_qr_screen_signin_code(self):
        if isinstance(self.actions, AndroidActions): 
            return self.actions.is_element_displayed(*locators['QR_SIGNIN_CODE'])
        elif isinstance(self.actions, RokuActions):
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", False, "", True, "name", "mslSecondInstruction", False, "")
            secondInstruction = self.actions.is_text_available(data, "mslSecondInstruction") 
            return secondInstruction
        else:
            return True
        
    def verify_qr_screen_ready_to_watch(self):
        if isinstance(self.actions, AndroidActions): 
            return self.actions.is_element_displayed(*locators['QR_SIGNIN_READY_TO_WATCH'])
        elif isinstance(self.actions, RokuActions):
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", False, "", True, "name", "mslThirdInstruction", False, "")
            thirdInstruction = self.actions.is_text_available(data, "mslThirdInstruction") 
            return thirdInstruction
        else:
            return True
        
    def verify_qr_code(self):
        if isinstance(self.actions, AndroidActions): 
            return self.actions.is_element_displayed(*locators['QR_CODE'])
        elif isinstance(self.actions, RokuActions):
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", False, "", True, "name", "loginCode", False, "")
            loginCode = self.actions.is_text_available(data, "loginCode") 
            return loginCode
        else:
            return True

    def click_sign_in_with_remote(self):
        if isinstance(self.actions, AndroidActions): 
            self.actions.click_button(*locators['SIGN_IN_WITH_REMOTE'])
        elif isinstance(self.actions, RokuActions):
            time.sleep(3)
            self.actions.click_button("Select")
            self.actions.screenshotAttachment("remote.jpeg")
            time.sleep(3)
            
    def get_login_url(self):
        if isinstance(self.actions, AndroidActions): 
            fetched_text = self.actions.get_text(*locators['QR_SIGNIN_URL'])
            return fetched_text
        elif isinstance(self.actions, RokuActions):
            time.sleep(18)
            print("--------Before---------")
            currentElement = self.actions.fetch_element_with_parent_name_arrtributes("name", "linkUrl", "text", "")
            print("--------After---------")
            myURL = self.actions.fetch_data_from_json(currentElement)
            print("fetched qr code url ====", myURL) 
            return myURL
        else:
            return True
        
    def login_access_code(self):
        if isinstance(self.actions, AndroidActions): 
            print("Getting access code")
        elif isinstance(self.actions, RokuActions):  
            time.sleep(4)
            # access_code = self.actions.fetch_element_with_parent_name_arrtributes("name", "mslSecondInstruction", "index", "1")
            access_code = self.actions.fetch_element(False, "", "", False, "", "", False, "", False, "", True, "name", "loginCode", False, "")
            time.sleep(4)
            access_code_fetch = self.actions.fetch_data_from_json(access_code)
            print("access code ----" + access_code_fetch) 
            return access_code_fetch  
        else:
            return True
        
    def get_login_code(self):
        fetched_text = self.actions.get_text(*locators['QR_SIGNIN_CODE'])
        return fetched_text

    def get_qr_elements_after_5mins(self):
        if isinstance(self.actions, AndroidActions):
            QR_Screen_Url_1 = self.get_login_url()
            QR_Screen_Code_1 = self.get_login_code()
            print(QR_Screen_Code_1)
            print(QR_Screen_Url_1)
            for i in range(10):
                time.sleep(30)
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            print('Waiting for 5mins in QR Screen')
            QR_Screen_Url_2 = self.get_login_url()
            QR_Screen_Code_2 = self.get_login_code()
            print(QR_Screen_Code_2)
            print(QR_Screen_Url_2)
            if (QR_Screen_Url_1 != QR_Screen_Url_2) and (QR_Screen_Code_1 != QR_Screen_Code_2):
                print('QR Screen Elements updated after 5mins')
                return True
            else:
                return False
        elif isinstance(self.actions, RokuActions):
            QR_Screen_Url_1 = self.get_login_url()
            qr_code_page_element = self.actions.fetch_element(False, "", "", False, "", "", False, "", False, "", True, "name", "loginCode", False, "")
            QR_Screen_Code_1 = self.actions.fetch_data_from_json(qr_code_page_element)
            self.actions.screenshotAttachment("firsturl.jpeg")
            print("QR code ----" + QR_Screen_Code_1)
            for i in range(10):
                time.sleep(30)
                self.actions.click_button("Down")
            print('Waiting for 5mins in QR Screen')
            QR_Screen_Url_2 = self.get_login_url()
            qr_code_page_element = self.actions.fetch_element(False, "", "", False, "", "", False, "", False, "", True, "name", "loginCode", False, "")
            QR_Screen_Code_2 = self.actions.fetch_data_from_json(qr_code_page_element)
            print("QR code ----" + QR_Screen_Code_2)
            self.actions.screenshotAttachment("secondurl.jpeg")
            self.actions.click_button("Select")
            if (QR_Screen_Url_1 != QR_Screen_Url_2) and (QR_Screen_Code_1 != QR_Screen_Code_2):
                print('QR Screen Elements Changed after 5mins')
                return True
            else:
                return False
        else:
            return True
            
    def compare_qr_codes_after_selecting_login_with_qr_button_two_times(self):
        if isinstance(self.actions, AndroidActions):
            QR_Screen_Url_1 = self.get_login_url()
            QR_Screen_Code_1 = self.get_login_code()
            print(QR_Screen_Code_1)
            print(QR_Screen_Url_1)
            self.actions.click_button(*locators['SIGN_IN_WITH_REMOTE'])
            print('Navigating back to login screen')
            self.click_sign_in_with_qr_code_button()
            self.verify_qr_code_page_navigation()
            QR_Screen_Url_2 = self.get_login_url()
            QR_Screen_Code_2 = self.get_login_code()
            print(QR_Screen_Code_2)
            print(QR_Screen_Url_2)
            if (QR_Screen_Url_1 != QR_Screen_Url_2) and (QR_Screen_Code_1 != QR_Screen_Code_2):
                print('QR Screen Elements updated after 5mins')
                return True
            else:
                return False
        elif isinstance(self.actions, RokuActions):
            qr_code_page_element = self.actions.fetch_element(False, "", "", False, "", "", False, "", False, "", True, "name", "loginCode", False, "")
            qr_code_one = self.actions.fetch_data_from_json(qr_code_page_element)
            print("QR code ----" + qr_code_one)
            self.actions.click_button("Select")
            for i in range(6):      
                self.actions.click_button("Down")
                time.sleep(4)
            self.actions.click_button("Select") 
            time.sleep(3) 
            qr_code_page_element = self.actions.fetch_element(False, "", "", False, "", "", False, "", False, "", True, "name", "loginCode", False, "")
            qr_code_two = self.actions.fetch_data_from_json(qr_code_page_element)
            print("QR code ----" ,qr_code_two)
            self.actions.click_button("Select")
            if (qr_code_one != qr_code_two) and (qr_code_one != qr_code_two):
                print('QR Screen Elements updated after clicking on sign in with remote and navigating back to login page')
                return True
            else:
                return False
        else:
            return True

    # def launch_URL(self):
    #     url = self.login_URL()
    #     self.actions.open_url(url)
    #     Element = self.driver.find_element(*locators['QR_SIGNIN_URL'])
    #     URLtext = Element.text
    #     print(URLtext)
    #     return URLtext

    # def launch_URL(self, URLtext):
    #     self.driver = self.driver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    #     self.driver.get(URLtext)
   
    # def qr_Invalid_Credentilas_Field(self, username, password):
    #     self.actions.wait_for_element(*locators['USERNAME_QR_LOGIN'], username)
    #     self.actions.enter_text(*locators['USERNAME_QR_LOGIN'], username)
    #     self.actions.enter_text(*locators['PASSWORD_QR_LOGIN'], password)
    #     self.actions.click_button(*locators['SIGN_IN_QR_LOGIN'])

    # def qr_Credentials_With_Invalid_Password(self, username, invalidpassword):
    #     self.actions.wait_for_element(*locators['USERNAME_QR_LOGIN'], username)
    #     self.actions.enter_text(*locators['USERNAME_QR_LOGIN'], username)
    #     self.actions.enter_text(*locators['PASSWORD_QR_LOGIN'], invalidpassword)
    #     self.actions.click_button(*locators['SIGN_IN_QR_LOGIN'])

    # def qr_Login_Without_Password(self, username):
    #     self.actions.wait_for_element(*locators['USERNAME_QR_LOGIN'], username)
    #     self.actions.enter_text(*locators['USERNAME_QR_LOGIN'], username)
    #     self.actions.click_button(*locators['SIGN_IN_QR_LOGIN'])

    # def invalid_Credentials_Error_Message(self, errormessage):
    #     return self.actions.validate_text(*locators['INVALID_LOGIN_ERROR_MESSAGE'], errormessage)

    # def password_Blank_Error_Message(self, message):
    #     return self.actions.validate_text(*locators['PASSWORD_FIELD_BLANK_MESSAGE'], message)

    def qr_First_Sign_Code(self):
        FirstAccesscode = self.driver.find_element(*locators['QR_SIGNIN_CODE']).text
        return FirstAccesscode
    
    def qr_Second_Sign_Code(self):
        SecondAccesscode = self.driver.find_element(*locators['QR_SIGNIN_CODE']).text
        return SecondAccesscode
    
    def qr_Validate_Sign_Code(self, FirstAccesscode, SecondAccesscode):
        if FirstAccesscode != SecondAccesscode:
            return True
        else:
            return False
        
    def terms_Services(self):
        if isinstance(self.actions, AndroidActions):
            return self.actions.is_element_displayed(*locators['TERMS_OF_SERVICES'])
        elif isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad['TERMS_OF_SERVICE_BUTTON'])
        else:
            print("handled in different method")
            pass
        
    def terms_and_condtions_header_logo(self):
        if isinstance(self.actions, AndroidActions):
            statusValue = False
            try:
                self.actions.wait_for_element(*locators['HEADER_LOGO_T&C'])
                self.actions.is_element_displayed(*locators['HEADER_LOGO_T&C']) 
                statusValue = False
            except Exception:
                statusValue = True
            return statusValue
        elif isinstance(self.actions, iOSActions):
            statusValue = False
            try:
                self.actions.wait_for_element(*locators_ipad['HEADER_LOGO'])
                statusValue = False
            except Exception:
                statusValue = True
            print(statusValue)
            return statusValue
        else:
            statusValue = False
            try:
                data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "logo", False, "", "", False, "")
                original_AirDateLabel = self.actions.is_text_available(data, "logo")
                statusValue = original_AirDateLabel
                statusValue = False
            except Exception:
                statusValue = True
            return statusValue
            
    def tapping_On_Terms_Services(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*locators['TERMS_OF_SERVICES'])
            try:
                self.actions.click_button(*locators['TERMS_OF_SERVICES'])
            except Exception:
                pass
            return self.actions.is_element_displayed(*locators['VERIFY_TERMS_AND_CONDITIONS'])
        if isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['TERMS_OF_SERVICE_BUTTON'])
            time.sleep(5)
            Terms_of_service = self.actions.wait_for_element(*locators_ipad['TERMS_OF_CONDITION_DOCUMENT'])   #displayed value of element is False, hence used the method wait for element
            if Terms_of_service:
                return True
            else:
                return False
        else:
            for i in range(4):      
                self.actions.click_button("Down")
                time.sleep(4)
            self.actions.click_button("Select")
            self.actions.screenshotAttachment("termsconditions.jpeg")
            time.sleep(4)
            return self.actions.is_element_displayed("name", "lDialogTitle", "TERMS OF SERVICE - PAGE 1/8")
            
    def validate_login_screen_navigation_after_10mins(self):
        if isinstance(self.actions, AndroidActions):
            for i in range(20):
                time.sleep(30)
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_UP'])
            Page_navigation = self.check_app_version_visibilty()
            return Page_navigation
        elif isinstance(self.actions, RokuActions):
            for i in range(20):
                time.sleep(30)
                self.actions.click_button("Up")
            
            self.actions.screenshotAttachment("url.jpeg")
            # self.actions.click_button("Select")
            time.sleep(5)
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "QR CODE", False, "", "", False, "")
            status = self.actions.is_text_available(data, "QR CODE")
            return status
        else:
            return True
                   
    def invalid_Pin_Error_Message(self, errormessage):
        if isinstance(self.actions, AndroidActions):
            return self.actions.validate_text_contains(*locators['ERROR_MESSAGE'], errormessage)
        elif isinstance(self.actions, iOSActions):
            by, value = locators_ipad["INVALID_PIN_ERROR_MESSAGE"]
            default_format_value = value.format(error_message=errormessage)
            self.actions.click_button(*locators_ipad['LOGIN_ENTER_BUTTON'])
            Invalid_Error_Message = self.actions.validate_text_contains(by, default_format_value, errormessage)
            return Invalid_Error_Message
        else:
            return self.actions.is_element_displayed("name", "message", "Invalid credentials. For assistance, contact support@indee.tv.")
        
    def pin_Error_Message(self, errormessage):
        return self.actions.validate_text_contains(*locators['ERROR_MESSAGE'], errormessage)
    
    def verify_old_version_error_message_not_display(self, errormessage):
        if isinstance(self.actions, AndroidActions):
            Error_Message = self.actions.get_element_visibility(*locators["ERROR_MESSAGE_VERSION"])
            if Error_Message:
                return False
            else:
                return True  
        elif isinstance(self.actions, iOSActions):
            by, value = locators_ipad["OLD_VERSION_ERROR_MESSAGE"]
            default_format_value = value.format(error_message=errormessage)
            Error_Message = self.actions.get_element_visibility(by, default_format_value)
            if Error_Message:
                return False
            else:
                return True
        else:
            statusValue = False
            try:
                data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, errormessage, False, "", "", False, "")
                original_AirDateLabel = self.actions.is_text_available(data, errormessage)
                statusValue = original_AirDateLabel
                statusValue = False
            except Exception:
                statusValue = True
            return statusValue    
        

    def select_brand_option(self):
        self.actions.click_button(*locators['SELECT_BRAND'])

    def verify_expiry_pin(self, errormessage):
        if isinstance(self.actions, AndroidActions):
            return self.actions.validate_text_contains(*locators['ERROR_EXPIRY_PIN'], errormessage)
        elif isinstance(self.actions, iOSActions):
            by, value = locators_ipad["EXPIRED_PIN_ERROR_MESSAGE"]
            default_format_value = value.format(error_message=errormessage)
            self.actions.click_button(*locators_ipad['LOGIN_ENTER_BUTTON'])
            Invalid_Error_Message = self.actions.validate_text_contains(by, default_format_value, errormessage)
            return Invalid_Error_Message
        else:
            return self.actions.is_element_displayed("name", "message", "Invalid credentials. For assistance, contact support@indee.tv.")
         
    def select_checkbox(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*locators['LOGIN_SIGNIN_SESSION_CHECKBOX'])
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['LOGIN_CHECKBOX_DISABLED'])
            Checkbox = self.actions.is_element_displayed(*locators_ipad['LOGIN_CHECKBOX_ENABLED'])
            if Checkbox:
                print('Checkbbox is enabled')
            else:
                print('Checkbox is not enabled')
        else:
            self.actions.click_button("Down")
            time.sleep(2)
            self.actions.click_button("Select")
     
    def old_version_error_messgae(self, errormessage):
        if isinstance(self.actions, AndroidActions):
            print(errormessage)
            return self.actions.validate_text_contains(*locators['ERROR_MESSAGE_VERSION'], errormessage)
        elif isinstance(self.actions, iOSActions):
            by, value = locators_ipad["OLD_VERSION_ERROR_MESSAGE"]
            default_format_value = value.format(error_message=errormessage)
            Old_version_error = self.actions.validate_text_contains(by, default_format_value, errormessage)
            return Old_version_error
        else:
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, errormessage, False, "", "", False, "")
            errorMsgstatus = self.actions.is_text_available(data, errormessage)
            self.actions.screenshotAttachment("oldversion.jpeg")
            return errorMsgstatus
        
    def verify_email_input_field_is_not_displayed(self):
        if isinstance(self.actions, AndroidActions):
            Email_field = self.actions.is_element_displayed(*locators['EMAIL_INPUT_FIELD'])
            return Email_field
        elif isinstance(self.actions, iOSActions):
            Email_field = self.actions.is_element_displayed(*locators_ipad['EMAIL_INPUT_FIELD'])
            return Email_field
        else:
            return True
        
    def minimize_the_app(self):
        if isinstance(self.actions, iOSActions):
            self.driver.background_app(10)
            print('App Miinimized successfully')
        else:
            pass

    def launch_the_app(self, application):
        if isinstance(self.actions, iOSActions):
            self.driver.activate_app(application)
            print('App launched successfully')
        else:
            pass

    def terminate_the_app(self, application):
        if isinstance(self.actions, iOSActions):
            self.driver.terminate_app(application)
            print('App terminated successfully')
        else:
            pass

    def uninstall_the_app_in_ipad(self, application):
        if isinstance(self.actions, iOSActions):
            self.driver.remove_app(application)
            print('App Unsinstalled Successfully')
        else:
            pass

    def install_the_app_in_ipad(self, application):
        if isinstance(self.actions, iOSActions):
            self.driver.activate_app("com.apple.TestFlight")
            print('App Unsinstalled Successfully')
            time.sleep(15)
            testflight_locator = self.actions.is_element_displayed(*locators_ipad['TESTFLIGHT'])
            if testflight_locator:
                print('Testflight opened successfully')
                fyc_app_locator = self.actions.wait_for_element(*locators_ipad['TESTFLIGHT_APP_NAME'])  #is_element_displayed returns false
                if fyc_app_locator:
                    self.actions.click_button(*locators_ipad['TESTFLIGHT_APP_NAME'])
                    self.actions.click_button(*locators_ipad['TESTFLIGHT_APP_INSTALL'])
                    time.sleep(15)
                    app_open_locator = self.actions.is_element_displayed(*locators_ipad["TESTFLIGHT_APPOPEN"])
                    if app_open_locator:
                        print('App is Installed Successfully')
                        self.driver.activate_app(application)
                        return True
                    else:
                        print('App is not installed in TestFlight')
                        return False
                else:
                    print('FYC appliication is not displayed in testflight')
                    return False
            else:
                print('testflight is not launched')
                return False
        else:
            return True
        
    def verify_api_failure_error_message_is_displayed(self, error_message):
        if isinstance(self.actions, AndroidActions):
            return self.actions.validate_text_contains(*locators['API_ERROR_MESSAGE'], error_message)
        elif isinstance(self.actions, iOSActions):
            by, value = locators_ipad["API_ERROR_MESSAGE"]
            default_format_value = value.format(error_message=error_message)
            api_error_message = self.actions.validate_text_contains(by, default_format_value, error_message)
            return api_error_message
        else:
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, error_message, False, "", "", False, "")
            errorMsgstatus = self.actions.is_text_available(data, error_message)
            return errorMsgstatus
        
    def launch_testflight_app(self):
        if isinstance(self.actions, iOSActions):
            self.driver.activate_app("com.apple.TestFlight")
            print('App Unsinstalled Successfully')
        else:
            pass

    def verify_testflight_app_launched(self):
        if isinstance(self.actions, iOSActions):
            testflight_locator = self.actions.is_element_displayed(*locators_ipad['TESTFLIGHT'])
            if testflight_locator:
                print('Testflight opened successfully')
                return True
            else:
                return False
        else:
            return True
        
    def install_previous_build_from_testflight(self):
        if isinstance(self.actions, iOSActions):
            fyc_app_locator = self.actions.wait_for_element(*locators_ipad['TESTFLIGHT_APP_NAME'])  #is_element_displayed returns false
            if fyc_app_locator:
                self.actions.click_button(*locators_ipad['TESTFLIGHT_APP_NAME'])
                previous_build = self.actions.wait_for_element(*locators_ipad['PREVIOUS_BUILD'])
                previous_build.click()
                try:
                    previous_build = self.actions.wait_for_element(*locators_ipad['PREVIOUS_BUILD'])
                    previous_build.click()
                except Exception:
                    pass
                self.actions.click_button(*locators_ipad['PREVIOUS_BUILD_SELECTION'])
                self.actions.click_button(*locators_ipad['INSTALL_PREVIOUS_BUILD'])
                try:
                    popup_install = self.actions.wait_for_element(*locators_ipad['OLDER_BUILD_INSTALL_POPUP'])
                    print(popup_install)
                    popup_install.click()
                except Exception:
                    pass
                time.sleep(15)
                App_Installed = self.actions.is_element_displayed(*locators_ipad['OPEN_PREVIOUUS_BUILD'])
                return App_Installed
            else:
                print('FYC appliication is not displayed in testflight')
                return False
        else:
            return True

    def update_the_app_in_ipad(self, application):
        if isinstance(self.actions, iOSActions):
            self.driver.activate_app("com.apple.TestFlight")
            print('App Unsinstalled Successfully')
            time.sleep(15)
            testflight_locator = self.actions.is_element_displayed(*locators_ipad['TESTFLIGHT'])
            if testflight_locator:
                print('Testflight opened successfully')
                fyc_app_locator = self.actions.wait_for_element(*locators_ipad['TESTFLIGHT_APP_NAME'])  #is_element_displayed returns false
                if fyc_app_locator:
                    self.actions.click_button(*locators_ipad['TESTFLIGHT_APP_NAME'])
                    self.actions.click_button(*locators_ipad['TESTFLIGHT_APP_UPDATE'])
                    time.sleep(15)
                    app_open_locator = self.actions.is_element_displayed(*locators_ipad["TESTFLIGHT_APPOPEN"])
                    if app_open_locator:
                        print('App is Updated Successfully')
                        self.driver.terminate_app(application)
                        self.driver.activate_app(application)
                        return True
                    else:
                        print('App is not updated in TestFlight')
                        return False
                else:
                    print('FYC appliication is not displayed in testflight')
                    return False
            else:
                print('testflight is not launched')
                return False
        else:
            return True
        
    def verify_unsupported_error_banner_in_login_page(self):
        if isinstance(self.actions, AndroidActions):
            Error_icon = self.actions.is_element_displayed(*locators['CMAF_WARNING_LOGO'])
            Error_msg = self.actions.is_element_displayed(*locators['CMAF_WARNING_TEXT'])
            Continue_Button = self.actions.is_element_displayed(*locators['CMAF_BUTTON_CONTINUE'])
            Ask_me_again = self.actions.is_element_displayed(*locators['CMAF_ASK_ME_AGAIN'])
            checkbox = self.actions.is_element_displayed(*locators['CMAF_CHECKBOOX'])
            Cmaf_warning = [Error_icon, Error_msg, Continue_Button, Ask_me_again, checkbox]
            if all(Cmaf_warning):
                return True
            else:
                return False
        else:
            return True
        
    def verify_unsupported_error_banner_not_displayed_in_login_page(self):
        if isinstance(self.actions, AndroidActions):
            Error_icon = self.actions.is_element_displayed(*locators['CMAF_WARNING_LOGO'])
            Error_msg = self.actions.is_element_displayed(*locators['CMAF_WARNING_TEXT'])
            Continue_Button = self.actions.is_element_displayed(*locators['CMAF_BUTTON_CONTINUE'])
            Ask_me_again = self.actions.is_element_displayed(*locators['CMAF_ASK_ME_AGAIN'])
            checkbox = self.actions.is_element_displayed(*locators['CMAF_CHECKBOOX'])
            Cmaf_warning = [Error_icon, Error_msg, Continue_Button, Ask_me_again, checkbox]
            if any(Cmaf_warning):
                return False
            else:
                return True
        else:
            return True

    def click_on_cmaf_button(self):
        if isinstance(self.actions, AndroidActions):
            try:
                self.actions.click_button(*locators['CMAF_POPUP_CONTINUE'])   
            except Exception:
                pass
        elif isinstance(self.actions, iOSActions):
            pass        

    def verify_resend_verification_link_popup_message(self):
        if isinstance(self.actions, iOSActions):
            resend_email_header = readPreReqJsonValue("prereq", "resend_verification_email_header")
            resend_email_text = readPreReqJsonValue("prereq", "resend_email_text")
            resend_email_message = readPreReqJsonValue("prereq", "resend_email_messsage")
            by, value = locators_ipad["RESEND_VERIFICATION_HEADER"]
            format_value = value.format(resend_email_header)
            Header = self.actions.is_element_displayed(by, format_value)
            by, value = locators_ipad["RESEND_VERIFICATION_EMAIL_TEXT"]
            format_value = value.format(resend_email_text)
            Acknowledgement = self.actions.is_element_displayed(by, format_value)
            by, value = locators_ipad["RESEND_VERIFICATION_MESSAGE"]
            format_value = value.format(resend_email_message)
            Send_again = self.actions.is_element_displayed(by, format_value)
            if all([Header, Acknowledgement, Send_again]):
                return True
            else:
                return False
        else:
            return True

    def click_on_resend_verification_link(self):
        if isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['RESEND_VERIFICATION_BUTTON'])
            return self.verify_resend_verification_link_popup_message()
        else:
            return True

    def click_on_back_to_sign_in_button(self):
        if isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['GO_BACT_TO_SIGNIN_BUTTON'])
            time.sleep(5)
            for i in range(3):
                login_page_navigation = self.actions.is_element_displayed(*locators_ipad['LOGIN_SIGNIN_HEADER'])
                if login_page_navigation:
                    break
                else:
                    self.actions.click_button(*locators_ipad['GO_BACT_TO_SIGNIN_BUTTON'])
                    time.sleep(5)
        else:
            pass
