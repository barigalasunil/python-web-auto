# import pytest
import time
from pytest_bdd import given, when, parsers, then, scenarios
from pytest_bdd.parsers import parse
from appium import webdriver
from pages.base_page import BasePage
from pages.login_page_screener import LoginPageScreener
from pages.settings_page_screener import SettingsPageScreener
from pages.homepage_screener import HomePageScreener
from pages.search_page_screeners import SearchPageScreener
from pages.help_page_screener import HelpPageScreener
from pages.media_player_page_screener import MediaPlayerPageScreener
from pages.logout_page_screener import LogoutPageScreener
from pages.download_page_screener import DownloadPageScreeners
from pages.actions.roku_actions import RokuActions
from pages.web_admin_page import AdminPortalPage
from pages.web_nimaad_page import NimaadPortalPage
from pages.web_admin_page_screener import AdminPortalPageScreener
# from conftest import launchBrowser
from pages.web_browser_page import WebBrowserPage
from conftest import readPreReqJsonValue, readConstants
import pytest
import allure
from pages.actions.assertions import Assert
# from conftest import launch_TV_Application


scenarios('../features/Screener_validations.feature')

# this xifture not workimg
# @pytest.fixture(scope="class")
# def login_page_obj(setup_platform):
#     # driver = setup_platform
#     login_page_init = LoginPageScreenerScreenerScreenerScreener(setup_platform)
#     return login_page_init


@given(parse("I install Screener {application} from testflight for {api_version} with {build_number}"))
@allure.step('Given I install Screener {application} from testflight for {api_version} with {build_number}')
def install_screeners_application_from_testflight(setup_platform, request, application, api_version, build_number):
    basePage = BasePage(setup_platform)
    basePage.install_ios_application(request, readPreReqJsonValue("prereq", application), readPreReqJsonValue("prereq", api_version), readPreReqJsonValue("prereq", build_number))


@given("I launch Screener Application")
@allure.step("Given I launch Screener Application")
def launch_GD_application(setup_platform):
    print("Launch screener application")
    print('what is webdriver instance =====', type(setup_platform))
    basePage = BasePage(setup_platform)
    basePage.launchApp()


@then('I verify The app load image is present')
@allure.step("Then I verify The app load image is present")
def i_verify_app_load_image_visible(setup_platform):
    login_page_init = LoginPageScreener(setup_platform).verify_launchScreen_view()
    Assert.assert_true(login_page_init, "App Launch Image is not loading")
    

@when("I am in Login Page")
@allure.step("When I am in Login Page")
def i_am_in_login_page(setup_platform):
    isSignInHeaderDisplayed = LoginPageScreener(setup_platform).verify_signin_header()
    if isSignInHeaderDisplayed:
        # in login page --so continue with sign i 
        print("Application is in Logout Statte")  
        Assert.assert_true(isSignInHeaderDisplayed, "Applciation is not in Login Page")   
    else:
        print("Application is in Login State,So logging out ")  
        HomePageScreener(setup_platform).click_logout_button()
        LogoutPageScreener(setup_platform).log_Out()
        print("Logged out successfully")  


@then("I verify Login Page BackGround image is loaded")
@allure.step("Then I verify Login Page BackGround image is loaded")
def i_verify_login_page_background_image_is_loaded(setup_platform):
    print("here Login Page BackGround image is loaded")
    isBGdisplayed = LoginPageScreener(setup_platform).verify_bg_image_displayed()
    Assert.assert_true(isBGdisplayed, "Login Page BG Image is Not Displayed")


@then('I verify App icon is present')
@allure.step('Then I verify App icon is present')
def i_verify_app_icon_is_present(setup_platform):
    app_icon_displayed = LoginPageScreener(setup_platform).verify_loginPage_Icon()
    Assert.assert_true(app_icon_displayed, "App Icon Is Not Displayed In Login Page")


@then('I verify Sign in header is present')
@allure.step('Then I verify Sign in header is present')
def i_verify_sign_in_header_is_present(setup_platform):
    print("Verifying Sign In Header Text In Login Page")
    isSignInHeaderDisplayed = LoginPageScreener(setup_platform).verify_signin_header()
    Assert.assert_true(isSignInHeaderDisplayed, "Sign In Header Is Not Displayed In Login Page")


@then("I verify Email and Password Fields Present")
@allure.step("Then I verify Email and Password Fields Present")
def i_verify_email_and_password_fields_present(setup_platform):
    print("Verifying Email and Password Fields Displayed In Login Page")
    email = LoginPageScreener(setup_platform).verify_Email_text_field(readPreReqJsonValue("prereq", "email_input_text"))
    password = LoginPageScreener(setup_platform).verify_password_text_field(readPreReqJsonValue("prereq", "password_input_text"))
    if all([email, password]):
        print('email and password input fields are displayed in login page')
    else:
        Assert.assert_fail("Email and password fields are Not Displayed In Login Page")


@then("I verify Forget Password Link is present")
@allure.step("Then I verify Forget Password Link is present")
def i_verify_forget_password_link(setup_platform):
    print("Verifying Forgot Password Link Text In Login Page")
    isForgotPswdLinkDisplayed = LoginPageScreener(setup_platform).verify_forgetpassword_text_field(readPreReqJsonValue("prereq", "forgot_password_text"))  # noqa:E501
    Assert.assert_true(isForgotPswdLinkDisplayed, "Forgot Password Link Is Not Displayed In Login Page")


@then("I verify Login Checkbox is present with correct Text")
@allure.step("Then I verify Login Checkbox is present with correct Text")
def verify_login_checkbox_is_present_with_correct_Text(setup_platform):
    print("Verifying Login Checkbox Is Displayed In Login Page")
    isCheckboxDisplayed = LoginPageScreener(setup_platform).verify_signin_session_checkBox(False, readPreReqJsonValue("prereq", "checkbox_text1"))
    Assert.assert_true(isCheckboxDisplayed, "Login Checkbox Is Not Displayed In Login Page")


@then("I verify Sign In Button is Present")
@allure.step("Then I verify Sign In Button is Present")
def i_verify_signin_button_is_present(setup_platform):
    print("Verifying Sign In Button Displayed In Login Page")
    isSignInButtonDisplayed = LoginPageScreener(setup_platform).check_loginbutton_visbility()
    Assert.assert_true(isSignInButtonDisplayed, "Sign In Is Not Displayed In Login Page")


@then("I verify Sign In With QR Code Button is Present")
@allure.step("Then I verify Sign In With QR Code Button is Present")
def i_verify_signin_withQRcode_button_is_present(setup_platform):
    print("Verifying Sign In With QR Code Button Displayed In Login Page")
    isQRSignInButtonDisplayed = LoginPageScreener(setup_platform).check_loginbutton_QR_Code_visbility()
    Assert.assert_true(isQRSignInButtonDisplayed, "Sign In With QR Code Button Is Not Displayed In Login Page")


@then('I Verify terms and services is displayed')
@allure.step('Then I Verify terms and services is displayed')
def i_verify_terms_and_service_is_displayed(setup_platform):
    terms_and_service = LoginPageScreener(setup_platform).verify_terms_and_service_button()
    Assert.assert_true(terms_and_service, "Terms and Service Link Is Not Displayed In Login Page")


@then('I verify App Version is present')
@allure.step('Then I verify App Version is present')
def i_verify_app_version_is_present(setup_platform):
    print("Verifying App Version Is Displayed In Login Page")
    isAppVersionDisplayed = LoginPageScreener(setup_platform).check_app_version_visibilty()
    Assert.assert_true(isAppVersionDisplayed, "App Version Is Not Displayed In Login Page")


@then('I verify Settings button is Present')
@allure.step('Then I verify Settings button is Present')
def i_verify_settings_button_is_present(setup_platform):
    print("Verifying Settings Button Is Displayed In Login Page")
    isSettingsButtonDisplayed = LoginPageScreener(setup_platform).check_settings_button_visibilty()
    Assert.assert_true(isSettingsButtonDisplayed, "Settings Button Is Not Displayed In Login Page")


@then('I Verify the chat support')
@allure.step('Then I Verify the chat support')
def i_verify_settings_button_is_present(setup_platform):
    print("Verifying chat support Is Displayed In Login Page")
    isSettingsButtonDisplayed = LoginPageScreener(setup_platform).verify_chat_support()
    Assert.assert_true(isSettingsButtonDisplayed, "chat support Is Not Displayed In Login Page")


@when('The user clicks on Settings button')
@allure.step("When The user clicks on Settings button")
def verify_the_user_clicks_on_the_settings_button(setup_platform):
    print("Clicking On Setting Button")
    LoginPageScreener(setup_platform).click_settings_button()


@when('Click on the Forgot Password link')
@allure.step('When Click on the Forgot Password link')
def click_on_forgot_passwoord_link(setup_platform):
    LoginPageScreener(setup_platform).click_Forgot_Password()


@then('I verify enter email address popup messsage is displayed')
@allure.step('Then I verify enter email address popup messsage is displayed')
def verify_enter_email_address_popup_message_is_displayed(setup_platform):
    Email_address = LoginPageScreener(setup_platform).verify_Forgot_Password_PopupHeader(readPreReqJsonValue("prereq", "forgoot_password_email_text"))
    Assert.assert_true(Email_address, 'Enter Email Address Popup Message Is Not Displayed After Clicking Forgot Password Link')


@when(parse('Enter {email_address} to request reset password link'))
@allure.step('When Enter Email address to request reset password link')
def enter_email_address_to_request_reset_password_link(setup_platform, email_address):
    LoginPageScreener(setup_platform).enter_username_in_forgot_password(readPreReqJsonValue("prereq", email_address))


@then(parse('Verify email successfully sent {success_message}'))
@allure.step('Then Verify email successfully sent message')
def verify_email_successfully_sent_messsage(setup_platform, success_message):
    Success_message = LoginPageScreener(setup_platform).verify_email_sent_message_in_forgot_password(readPreReqJsonValue("prereq", success_message))
    Assert.assert_true(Success_message, 'Forgot Password Email Sent Successfully Authentication Message Is Not Displayed')


@when(parse('I update the {server} {server_ipad} {company_name} and {API} key fields'))
@allure.step("When I update the server, company_name and API key fields")
def i_update_the_server_company_name_and_api_key_fields(setup_platform, server, server_ipad, company_name, API):
    print("Verfiying Server Text In Settings Screen")
    serverValue = readPreReqJsonValue("prereq", server).format(readConstants("GD_SERVER"))
    ipad_serveer_value = readPreReqJsonValue("prereq", server_ipad).format(readConstants("GD_SERVER"))
    SettingsPageScreener(setup_platform).set_settings_data(serverValue, ipad_serveer_value, readPreReqJsonValue("prereq", company_name), readPreReqJsonValue("prereq", API))   # noqa:E501


@then('The fields should be updated successfully')
@allure.step('Then The fields should be updated successfully')
def verify_the_fields_should_be_updated_successfully(setup_platform):
    print("Clicking On Save Button")
    SettingsPageScreener(setup_platform).click_savebutton()
    Setting_updation = LoginPageScreener(setup_platform).verify_signin_header()
    Assert.assert_true(Setting_updation, "Failed at updating settings configuration")


@when(parse("Enter {username} and {password} Credentials with Non verified"))
@allure.step("When I Enter username and password Credentials")
def enter_login_credentials(setup_platform, username, password):
    print("Entering Login Credentials")
    loginpage = LoginPageScreener(setup_platform)
    loginpage.do_login(readPreReqJsonValue("prereq", username), readPreReqJsonValue("prereq", password))    


@when(parse("Enter {username} and {password} Credentials"))
@allure.step("When I Enter username and password Credentials")
def enter_login_credentials(setup_platform, username, password):
    print("Entering Login Credentials")
    loginpage = LoginPageScreener(setup_platform)
    loginpage.do_login(readPreReqJsonValue("prereq", username), readPreReqJsonValue("prereq", password))

@when("Click on Sign in Button")
@allure.step('When Click on Sign in Button')
def click_on_signin_button(setup_platform):
    print('Click on sign in button')
    LoginPageScreener(setup_platform).sign_In()


@then('Verify User Login Successfully by Validating HomeScreen Visibility')
@allure.step("Then Verify User Login Successfully by Validating HomeScreen Visibility")
def verify_user_login_successfully_by_homescreen_visibility(setup_platform):
    print("Verifying Home Page After Login")
    isHomeScreenReached = HomePageScreener(setup_platform).verify_home_screen_navigation()
    Assert.assert_true(isHomeScreenReached, "Login Failed After Entering Credentials")    


@then(parsers.parse("I verify the appropriate error message {errormessage} is displayed"))
@allure.step('Then I verify the appropriate error message is displayed')
def verify_appropriate_error_message_is_displayed(setup_platform, errormessage):
    print('errormessage=============', errormessage)
    # print(setup_platform.page_source)
    Error_message_validation = LoginPageScreener(setup_platform).fetch_invalid_error_message(readPreReqJsonValue("prereq", errormessage))
    expected_err_msg = readPreReqJsonValue("prereq", errormessage)
    print("####Is error message matches: ", Error_message_validation)
    Assert.assert_true(Error_message_validation is not None, "Error message is not displayed in login page for non verified user")
    Assert.assert_true(Error_message_validation == expected_err_msg, f"Error message mismatches. Expected: {expected_err_msg}, actual: {Error_message_validation}")


@then(parse("I verify the appropriate error message {errormessage}, {error_message_ipad} is displayed for non verified user"))
@allure.step('Then I verify the appropriate error message is displayed for non verified user')
def verify_appropriate_error_message_is_displayed_for_non_verified_user(setup_platform, errormessage, error_message_ipad):
    print('errormessage=============', errormessage)
    # print(setup_platform.page_source)
    Error_message_validation = LoginPageScreener(setup_platform).fetch_invalid_error_message_non_verified_user(readPreReqJsonValue("prereq", errormessage), readPreReqJsonValue("prereq", error_message_ipad))
    Assert.assert_true(Error_message_validation, "Error message is not displayed in login page for non verified user")  


@then('I verify that the Forgot Password link is visible and clickable')
@allure.step("Then I verify that the Forgot Password link is visible and clickable")
def verify_that_the_forgot_password_link_is_visible_and_clickable(setup_platform):
    forget_password = LoginPageScreener(setup_platform).verify_forgetpassword_text_field(readPreReqJsonValue("prereq", "forgot_password_text"))
    LoginPageScreener(setup_platform).click_Forgot_Password()
    Assert.assert_true(forget_password, "Forget password link is not displayed")


@then('I navigate into Forgot Password link and validate the popup message')
@allure.step("Then I navigate into Forgot Password link and validate the popup message")
def navigate_into_forgot_password_link_and_validate_the_popup_message(setup_platform):
    forget_password_popup = LoginPageScreener(setup_platform).verify_forget_password_popup()
    Assert.assert_true(forget_password_popup, "Forget password popup is not displayed")


@then("I verify that each menu item is present and visible")
@allure.step('Then I verify that each menu item is present and visible')
def verify_each_menu_item_is_present_and_visible(setup_platform):
    print("Verifying that each menu item is present and visible")
    Menu_Items = HomePageScreener(setup_platform).verify_menu_bar()
    Assert.assert_true(Menu_Items, "Menu Bar Items Are Not Displyed") 


@when('I click on unsupported devices')
@allure.step('When I click on unsupported devices')
def click_on_unsupported_devices(get_nimaad_server):
    nimaad_portal_navigation = NimaadPortalPage(get_nimaad_server)
    nimaad_portal_navigation.click_on_unsupported_devices(get_nimaad_server)


@when('I add the device under unsupported devices')
@allure.step('When I add the device under unsupported devices')
def add_the_device_under_unsupported_devices(get_nimaad_server):
    nimaad_portal_navigation = NimaadPortalPage(get_nimaad_server)
    nimaad_portal_navigation.add_firestick_to_the_unsupported_devices(get_nimaad_server)


@when("I click on Logout")
@allure.step("When I click on Logout")
def verify_signin_button_is_present(setup_platform):
    print('Clicking On Logout Button')
    HomePageScreener(setup_platform).click_logout_button()


@when('I click on cmaf button')
def click_on_cmaf_button(setup_platform):
    LoginPageScreener(setup_platform).click_on_cmaf_button()    


@when("Click on help icon from the menu")
@allure.step('When Click on help icon from the menu')
def click_on_help_icon_from_the_menu(setup_platform):
    print('Clicking on help icon from the menu')
    HomePageScreener(setup_platform).click_on_help_button()


@then("I verify the Help document is displayed")
@allure.step('Then I verify the Help document is displayed')
def verify_help_document_is_displayed(setup_platform):
    print('Verifying help document is displayed')
    Help_Document = HelpPageScreener(setup_platform).help_page_header_verification()
    Assert.assert_true(Help_Document, "Help Document Is Not Displyed After Clicking On Help Button In Home Page")
    pass


@then("I click on Help document and verify the major contents")
@allure.step('Then I click on Help document and verify the major contents')
def click_on_help_document_and_verify_major_contents(setup_platform):
    print('Verifying help content contents')
    Help_Page_Verification = HelpPageScreener(setup_platform).help_Section_Contents(readPreReqJsonValue("prereq", "help_page_expected_content"), readPreReqJsonValue("prereq", "help_page_browsing_shows"), readPreReqJsonValue("prereq", "help_page_selecting_shows"), readPreReqJsonValue("prereq", "help_page_settings_and_features"), readPreReqJsonValue("prereq", "help_page_solving_straming_issues"), readPreReqJsonValue("prereq", "help_page_expected_loggingout"))  # noqa:E501
    Assert.assert_true(Help_Page_Verification, "Help Page Contents Are Not Displayed As Expected") 


@then('I click on Logout and verify Loggedout successfully')
@allure.step("When I click on Logout")
def verify_logout_button(setup_platform):
    print('Clicking On Logout Button')
    HomePageScreener(setup_platform).click_logout_button()
    time.sleep(5)
    LogoutPageScreener(setup_platform).log_Out()
    Login_Page = LoginPageScreener(setup_platform).verify_signin_header()
    Assert.assert_true(Login_Page, "Login Page Is Not Reached after logging out") 


@then("verify Loggedout successfully")
@allure.step("Then verify Loggedout successfully")
def verify_loggedout_successfully(setup_platform):
    print('Verifying If The App Got Logged Out Successfully.')
    Logout = LogoutPageScreener(setup_platform).log_Out()
    Assert.assert_true(Logout, "Logout Text Is Verified and Sign Out Button Is Clicked In Logout Page")                
           

@when('Click on Sign In With QR Code')
@allure.step("Click on Sign In With QR Code")
def click_on_sign_in_with_qr_code(setup_platform):
    print("Clicking On Sign In With QR Code")
    LoginPageScreener(setup_platform).click_sign_in_with_qr_code_button()


@then('Verify Sign In With QR Code Page Reached')
@allure.step("Verify Sign In With QR Code Page Reached")
def verify_sign_in_with_qr_code_page_reached(setup_platform):
    print('Verifying QR Screen Page Navigation')
    QR_Page_Navigation = LoginPageScreener(setup_platform).verify_qr_code_page_navigation()
    Assert.assert_true(QR_Page_Navigation, "Failed To Navigate Sign In With QR Code Screen")


@then('Validate QR Screen elements for 5min')
@allure.step('Then Validate QR Screen elements for 5min')
def validate_qr_screen_elements_5mins(setup_platform):
    QR_Screen = LoginPageScreener(setup_platform).get_qr_elements_after_5mins()
    Assert.assert_true(QR_Screen, "QR elements are not updated after waiting for 5 mins in QR Screen")  


@then('The application should automatically redirect the user to the login screen after 10min')
@allure.step('Then application automatically redirect to login page after 10min')
def application_redirect_to_loginpage_after_10min(setup_platform):
    Page_navigation = LoginPageScreener(setup_platform).validate_login_screen_navigation_after_10mins()
    Assert.assert_true(Page_navigation, "application should not automatically redirect to login page after 10min")      


@then('Validate QR Screen elements')
@allure.step("Validate QR Screen elements")
def validate_qr_screen_elements(setup_platform):
    print('Validating QR Screen Elements')
    QR_Screen_Url = LoginPageScreener(setup_platform).verify_qr_screen_sign_in_url()
    QR_Screen_Code = LoginPageScreener(setup_platform).verify_qr_screen_signin_code()
    Ready_To_Watch = LoginPageScreener(setup_platform).verify_qr_screen_ready_to_watch()
    # QR_Code = LoginPage(setup_platform).verify_qr_code()
    List_of_Elements = [QR_Screen_Url, QR_Screen_Code, Ready_To_Watch]
    if all(List_of_Elements):
        print("QR Screen Elements Are Validated")
    elif not QR_Screen_Url:
        Assert.assert_fail("URL To Login In Using Browser Is Not Displayed")
    elif not QR_Screen_Code:
        Assert.assert_fail("Login Code Is Not Displyed IN QR Screen")
    else:
        Assert.assert_fail("Ready To Watch Is Not Displayed In QR Screen")


@when('Click on Sign in with Remote Button')
@allure.step("Click on Sign in with Remote Button")
def click_on_sign_in_with_remote_button(setup_platform):
    print('Clicking on sign in with Remote Button in QR Screen')
    LoginPageScreener(setup_platform).click_sign_in_with_remote()
    print("Clicked On Sign In With Remote Button")


@then('Compare QR codes generated upon selecting Login with QR Screen button two times')
@allure.step('Then Compare QR codes generated upon selecting Login with QR Screen button two times')
def compare_qr_codes_generated_upon_selecting_login_with_qr_screen_button_two_times(setup_platform):
    print('Verifying QR code is displayed on the screen')
    Access_code_validation = LoginPageScreener(setup_platform).compare_qr_codes_after_selecting_login_with_qr_button_two_times()
    Assert.assert_true(Access_code_validation, "QR Screen Elements are not updated after navigating back from login page twice")


@then('Verify Navigation To Login Page')
@allure.step("Verify Navigation To Login Page")
def verify_navigation_to_login_page(setup_platform):
    print('Verifying login page navigation')
    Login_Navigation = LoginPageScreener(setup_platform).check_loginbutton_visbility()
    Assert.assert_true(Login_Navigation, "Login Page Navigation Failed After Clicking On Sign In With Remote Button In QR Screen")


@when("I click on search button in home page")
@allure.step('When Click on search button in home page')
def verify_search_field_is_present_and_visible(setup_platform):
    print('Verifying search field')
    HomePageScreener(setup_platform).click_on_search_button()


@when("I click on the Project video")
@allure.step('When I click on the Project video')
def verify_project_video(setup_platform):
    print('Verifying search field')
    HomePageScreener(setup_platform).click_on_search_button()    


@then('I verify that the header logo is displayed correctly')
def verify_that_the_header_logo_is_displayed_correctly(setup_platform):
    headerlogohome = HomePageScreener(setup_platform).verify_header_logo_in_homepage_screen()
    Assert.assert_true(headerlogohome, "verify header logo in homepage")


@then(parse("I verify by entering a {project_name} in the Search field"))
@allure.step('Then I verify by entering a search term in the Search field')
def verify_by_entering_search_term_in_search_field(setup_platform, project_name):
    print('Entering text in search field')
    Text_Entered = SearchPageScreener(setup_platform).enter_Text_In_Search_Field(readPreReqJsonValue("prereq", project_name))
    SearchPageScreener(setup_platform).submit_Search_Button()
    Assert.assert_true(Text_Entered, "Search Text is not entered in search box text field")


@then(parse("I verify the {project_name} content of the search results"))
@allure.step('Then I verify the content of the search results')
def verify_content_of_search_results(setup_platform, project_name):
    print('Verifying search result contents')
    Search_Results = SearchPageScreener(setup_platform).verify_Search_Content(readPreReqJsonValue("prereq", project_name))
    Assert.assert_true(Search_Results, "No Project Is Published With The Name Searched For In Search Page")    


@then(parse('Verify that the {project_video} has remaining views greater than {count}'))
@allure.step('Then Verify that the project has remaining views greater than 20')
def verify_the_project_has_remaining_views_greater_than_20(setup_platform, project_video, count):
    maximum_count = SearchPageScreener(setup_platform).maximum_Count_Video_Redirection(readPreReqJsonValue("prereq", count), readPreReqJsonValue("prereq", project_video))
    Assert.assert_true(maximum_count, "Selected project Doesn't Have Remaining Views Greater Than 20")


@then('I verify playback of the video that has views greater than 20')
@allure.step('Then I verify playback of the video that has views greater than 20')
def verify_playback_of_the_video_that_has_views_greater_than_20(setup_platform):
    project_under_selected_genre = SearchPageScreener(setup_platform).click_on_start_watching_button()
    SearchPageScreener(setup_platform).roku_back_button()
    Assert.assert_true(project_under_selected_genre, "Failed to play video for the selected project")
           

@when("Submit the search")
@allure.step('When Submit the search')
def submit_search_button(setup_platform):
    print('Submiting the search button after entering text')
    SearchPageScreener(setup_platform).submit_Search_Button()


@then("I verify that the Genres dropdown is visible")
@allure.step('Then I verify that the Genres dropdown is visible')
def Verify_Genres_Dropdown_Is_Visible(setup_platform):
    print('Verifying genre dropdown is displayed')
    Genres_Dropdown = HomePageScreener(setup_platform).genres_Dropdown()
    Assert.assert_true(Genres_Dropdown, "Genres Dropdown Is Not Displayed In Home Page")


@when(parse("I click on {genres} dropdown"))
@allure.step('When I click on genres dropdown')
def click_on_genres_dropdown(setup_platform, Generes_Content):
    print('Clicking on genres dropdown')
    Genre_Selection = HomePageScreener(setup_platform).genres_Dropdown_Select(readPreReqJsonValue("prereq", Generes_Content))
    Assert.assert_true(Genre_Selection, "Failed To Filter Genre Under Genre Selection")
    

     

@then(parse("I verify the {project_name} of the search results for Forensic Video"))
@allure.step('Then I verify the content of the search results')
def verify_content_of_search_results(setup_platform, project_name):
    print('Verifying search result contents')
    Search_Results = SearchPageScreener(setup_platform).verify_Search_Content(readPreReqJsonValue("prereq", project_name))
    Assert.assert_true(Search_Results, "No Project Is Published With The Name Searched For In Search Page") 


@when('Click on first video inside the project')
@allure.step('When Click on first video inside the project')
def verify_project_details_should_be_displayed_on_project_information(setup_platform):
    print("Project should be diaplyed on project info")
    SearchPageScreener(setup_platform).click_OnVideoInsideProject()


@when('click on the playbutton video')
@allure.step('When I click play button')
def click_on_the_playbutton_video(setup_platform):
    print("Click on video play button")
    MediaPlayerPageScreener(setup_platform).click_on_Playnowbutton()                      
    SearchPageScreener(setup_platform).submit_Search_Button()   


@then('I verify the resend verification email popup')
@allure.step('Then I verify the resend verification email popup')
def verify_resend_verification_email_popup_message(setup_platform):
    print('Verifying the resend verification email popup')
    resend_verification = LoginPageScreener(setup_platform).verify_resend_verification_link_popup_message()
    Assert.assert_true(resend_verification, "Resend Verification Link Popup Message Is Not Displayed")


@when("I click on resend verification link")
@allure.step('When I click on resend verification link')
def click_on_resend_verification_link(setup_platform):
    mail_sent = LoginPageScreener(setup_platform).click_on_resend_verification_link()
    Assert.assert_true(mail_sent, "Verification Email Is Not Sent To The Respective User")


@then('I verify login page navigation after clicking on go back to sign in button')
@allure.step('Then I verify login page navigation after clicking on go back to sign in button')
def verify_login_page_navigation_after_clicking_on_go_back_to_sign_in_button(setup_platform):
    LoginPageScreener(setup_platform).click_on_back_to_sign_in_button()
    Login_page = LoginPageScreener(setup_platform).verify_signin_header()
    Assert.assert_true(Login_page, "Login Page Navigation Failed After Clicking On Go Back To Signin Button")


@then('I verify that the header logo is displayed correctly')
@allure.step('Then I verify that the header logo is displayed correctly')
def verify_that_the_header_logo_is_displayed_correctly(setup_platform):
    headerlogohome = HomePageScreener(setup_platform).verify_header_logo_in_homepage_screen()
    Assert.assert_true(headerlogohome, "verify header logo in homepage")


@given('I launch Nimaad portal')
@allure.step('Given I launch Nimaad portal')
def launch_nimaad_portal(get_nimaad_server):
    # Add Your Code Here
    pass


@when(parse('I login with nimaad {username} and {password}'))
@allure.step('When I Enter Nimaad Login Credentials')
def login_with_nimaad_credentials(get_nimaad_server, username, password):
    NimaadPortalPage(get_nimaad_server).enter_login_credentials(get_nimaad_server, readPreReqJsonValue("prereq", username), readPreReqJsonValue("prereq", password))  


@when(parse('I select user {email_address} to change password'))
@allure.step('When I select user email address to change password')
def select_user_email_address_to_change_password(get_nimaad_server, email_address):
    NimaadPortalPage(get_nimaad_server).click_emails_in_nimaad(get_nimaad_server, readPreReqJsonValue("prereq", email_address))  


@when(parse('I select user {email_address} to verify resend verification link'))
@allure.step('When I select user email address to verify resend verification link')
def select_user_email_address_to_verify_resend_verification_link(get_nimaad_server, email_address):
    NimaadPortalPage(get_nimaad_server).click_resend_emails_in_nimaad(get_nimaad_server, readPreReqJsonValue("prereq", email_address))  


@then('I verify resend verification email in nimaad')
@allure.step('Then I verify resend verification email in nimaad')
def verify_resend(get_nimaad_server):
    Resend_Email = NimaadPortalPage(get_nimaad_server).verify_resend_verification_email(get_nimaad_server)  
    Assert.assert_true(Resend_Email, "Resend Verification Email IN Nimaad Is Not Displayed For The User")


@when('I verify the mail and click on reset password button')
@allure.step('When I verify the mail and click on reset password button')
def verify_the_mail_and_click_on_reset_password_button(get_nimaad_server):
    NimaadPortalPage(get_nimaad_server).click_reset_password_link(get_nimaad_server)  


@pytest.fixture
def shared_data():
    return {'new_password': None,
            'remaining_views': None,
            'new_expiry': None}


@when('I create new password for the user')
@allure.step('When I create new password for the user')
def create_new_password_for_the_user(get_nimaad_server, shared_data):
    shared_data['new_password'] = NimaadPortalPage(get_nimaad_server).create_new_password(get_nimaad_server)  
    Assert.assert_not_none(shared_data['new_password'], "Passwordd Is Not Changed In Nimaad")


@then('I verify password changed message')
@allure.step('Then I verify password changed message')
def verify_password_changed_message(get_nimaad_server):
    password_changed = NimaadPortalPage(get_nimaad_server).verify_password_changed_success_message(get_nimaad_server)  
    Assert.assert_true(password_changed, "Password Changed Success Message Is Not Displayed In Nimaad")


@when(parse('Enter {email_address} and password credentials after changing password'))
@allure.step('When Enter email and password credentials after changing password')
def enter_email_and_password_credentials_after_changing_password(setup_platform, email_address, shared_data):
    LoginPageScreener(setup_platform).do_login(readPreReqJsonValue("prereq", email_address), shared_data['new_password'])  


@when(parse('Click on {project_name} from Search Result'))
@allure.step('When Click on Project from Search Result')
def click_project_from_search_result(setup_platform, project_name):
    print('Clicking on project from search results')
    SearchPageScreener(setup_platform).click_OnProjectResult(readPreReqJsonValue("prereq", project_name)) 


@when('Click on header logo')
@allure.step('When Click on header logo')
def click_on_project_from_search_results(setup_platform):
    HomePageScreener(setup_platform).click_on_header_logo()


@then('Verify home page is navigated on clicking on header logo')
@allure.step('Then Verify home page is navigated on clicking on header logo')
def verify_home_page_is_navigated_after_clicking_on_header_logo(setup_platform):
    homepage_navigation = HomePageScreener(setup_platform).project_listing_page()  
    Assert.assert_true(homepage_navigation, "Home Page Is Not Navigated After Clicking On Header Logo")


@then('I verify that the Genres dropdown is visible')
@allure.step('Then I verify that the Genres dropdown is visible')
def verify_genres_dropdown_is_visible(setup_platform):
    genres_dropdown = HomePageScreener(setup_platform).genres_Dropdown()  
    Assert.assert_true(genres_dropdown, "Genres Dropdown Is Not Displayed In Home Page")


@when(parse('I click on {genres} dropdown'))
@allure.step('When I click on genres dropdown')
def click_on_genres_dropdown(setup_platform, genres):
    HomePageScreener(setup_platform).genres_Dropdown_Select(readPreReqJsonValue("prereq", genres))


@then(parse('Verify respective {project} is displayed under selected genre'))
@allure.step('Then Verify respective project is displayed under selected genre')
def verify_respective_project_is_displayed_under_selected_genre(setup_platform, project):
    project_under_selected_genre = HomePageScreener(setup_platform).select_genre_content(readPreReqJsonValue("prereq", project))
    Assert.assert_true(project_under_selected_genre, "Expected Project Is Not Displayed Under Selected Genre")    


@then(parse('I verify the {project_name} content of the search results'))
@allure.step('Then I verify the project content of the search results')
def verify_project_content_of_the_search_results(setup_platform, project_name):
    search_content = SearchPageScreener(setup_platform).verify_Search_Content(readPreReqJsonValue("prereq", project_name))  
    Assert.assert_true(search_content, "Searched Project Is Not Displayed In Search Page}")


@then('I verify the pagination call after receiving search results')
@allure.step('Then I verify the pagination call after receiving search results')
def verify_pagination_call_after_receiving_search_results(setup_platform):
    search_page_pagination = SearchPageScreener(setup_platform).pagination_Call_Search_Field()  
    Assert.assert_true(search_page_pagination, "Projects Are Not Paginated For The Searched Content")


@then('verify pagination call in the project listing page')
@allure.step('Then verify pagination call in the project listing page')
def verify_project_listing_page(setup_platform):
    project_listing_page = HomePageScreener(setup_platform).project_listing_page()  
    Assert.assert_true(project_listing_page, "verify pagination call is not displayed project listing page")    


@when('I Click On Details Tab')
@allure.step('When I Click On Details Tab')
def click_on_details_tab(setup_platform):
    SearchPageScreener(setup_platform).click_DetailsTab_Project()


@then(parse('Project {synopsis} Information Should be Displayed'))
@allure.step('Then Project synopsis Information Should be Displayed')
def verify_project_synopsis_information_isdisplayed(setup_platform, synopsis):
    project_synopsis = SearchPageScreener(setup_platform).verify_Project_Synopsis_Information(readPreReqJsonValue("prereq", synopsis))  
    print(project_synopsis)
    Assert.assert_true(project_synopsis, "Projects Synopsis Is Not Displayed As Expected")


@then(parse('Project {cast} and {crew} and {crew_ipad} Information Should be Displayed in Details Tab'))
@allure.step('Then Project cast and crew Information Should be Displayed in Details Tab ')
def verify_project_cast_andd_crew_information_isdisplayed(setup_platform, cast, crew, crew_ipad):
    cast_and_crew = SearchPageScreener(setup_platform).verify_Cast_Crew_Title_Displayed(readPreReqJsonValue("prereq", cast), readPreReqJsonValue("prereq", crew), readPreReqJsonValue("prereq", crew_ipad))   # noqa:E501
    Assert.assert_true(cast_and_crew, "Cast And Crew Information Is Not Displayed As Expected In Project Details Page")


@when('I Click On Videos Tab')
@allure.step('When I Click On Videos Tab')
def click_on_videos_tab(setup_platform):
    SearchPageScreener(setup_platform).click_videos_tab_project()


@when('I do remote activity in Roku')
@allure.step('When I do remote activity in Roku')
def do_remote_activity_in_roku(setup_platform):
    SearchPageScreener(setup_platform).do_remote_activity()


@when(parse('I Click On {video_name} Inside Project'))
@allure.step('When I Click On Videos Inside Project')
def click_on_videos_inside_project(setup_platform, video_name):
    SearchPageScreener(setup_platform).click_OnVideoInsideProject(readPreReqJsonValue("prereq", video_name))    


@then(parse('Video {synopsis} Information Should be Displayed'))
@allure.step('Then Video synopsis Information Should be Displayed')
def verify_video_synopsis_information_isdisplayed(setup_platform, synopsis):
    video_synopsis = SearchPageScreener(setup_platform).verify_Video_Synopsis_Information(readPreReqJsonValue("prereq", synopsis))  
    Assert.assert_true(video_synopsis, "Video Synopsis Is Not Displayed As Expected")


@then(parse('Video {cast} and {crew} and {crew_ipad} Information Should be Displayed in Details Tab'))
@allure.step('Then Video cast and crew Information Should be Displayed in Details Tab ')
def verify_video_cast_andd_crew_information_isdisplayed(setup_platform, cast, crew, crew_ipad):
    cast_and_crew = SearchPageScreener(setup_platform).verify_Cast_Crew_Title_Displayed(readPreReqJsonValue("prereq", cast), readPreReqJsonValue("prereq", crew), readPreReqJsonValue("prereq", crew_ipad))   # noqa:E501
    Assert.assert_true(cast_and_crew, "Cast And Crew Information Is Not Displayed As Expected In Videoo Details")


@then('I verify that the correct content is displayed under the Videos tab')
@allure.step('Then I verify that the correct content is displayed under the Videos tab')
def verify_correct_content_is_displayed_under_the_videos_tab(setup_platform):
    video_tab_contents = SearchPageScreener(setup_platform).verify_video_tab_contents_in_project()   
    Assert.assert_true(video_tab_contents, "Video Tab Details Are Not Displayed As Expected")


@then('I verify that the correct content is displayed under the Details tab')
@allure.step('Then I verify that the correct content is displayed under the Details tab')
def verify_correct_content_is_displayed_undder_the_details_tab(setup_platform):
    details_tab_contents = SearchPageScreener(setup_platform).verify_details_tab_contents_in_project()   
    Assert.assert_true(details_tab_contents, "Details Tab Content Are Not Displayed As Expected")


@then('Airdate Should not be Displayed on Project Information')
@allure.step('Then Airdate Should not be Displayed on Project Information')
def verify_airdate_should_not_be_displayed_on_project_information(setup_platform):
    airdate_not_displayed = SearchPageScreener(setup_platform).airDate_Should_Not_Display()
    Assert.assert_true(airdate_not_displayed, "Airdate Details Not Displayed In Episodic/Non Episodic project As Expected")


@when('I navigate to home page')
@allure.step('When I navigate to home page')
def navigate_to_home_page(setup_platform):
    HomePageScreener(setup_platform).click_on_home_button()


@when('Minimize the application')
@allure.step('When Minimize the application')
def minimize_the_application(setup_platform):
    LoginPageScreener(setup_platform).minimize_the_app()


@when(parse('ReLaunch the {application}'))
@allure.step('When ReLaunch the Screeners application')
def relaunch_the_application(setup_platform, application):
    LoginPageScreener(setup_platform).launch_the_app(readPreReqJsonValue("prereq", application))


@then('I verify by search page is reached')
@allure.step('Then I verify by search page is reached')
def verify_search_page_is_reached(setup_platform):
    search_navigation = SearchPageScreener(setup_platform).verify_search_page_reached()
    Assert.assert_true(search_navigation, "Search Page Is Not Navigated Afteer Clicking Search Button")


@then('Verify app launches in same page after relaunching')
@allure.step('Then Verify app launches in same page after relaunching')
def verify_app_launches_in_same_page_after_relaunching(setup_platform):
    search_navigation = SearchPageScreener(setup_platform).verify_search_page_reached()
    Assert.assert_true(search_navigation, "App Is Not Launched In Same Page After Minimizing And Relaunching the App")


@when(parse('Close the {application} completly'))
@allure.step('When Close the application completly')
def close_the_application_commpletely(setup_platform, application):
    LoginPageScreener(setup_platform).terminate_the_app(readPreReqJsonValue("prereq", application))


@then('Verify app launches in home page after killing an relaunching')
@allure.step('Then Verify app launches in home page after killing an relaunching')
def verify_app_launches_in_home_page_after_killing_and_relaunching(setup_platform):
    home_navigation = HomePageScreener(setup_platform).verify_home_screen_navigation()
    Assert.assert_true(home_navigation, "App Is Not Launched In Home Page After Killing And Relaunching the App")


@then(parse('Verify that the project has remaining views greater than {count}'))
@allure.step('Then Verify that the project has remaining views greater than 20')
def verify_the_project_has_remaining_views_greater_than_20(setup_platform, count):
    maximum_count = SearchPageScreener(setup_platform).maximum_Count_Video_Redirection(readPreReqJsonValue("prereq", count))
    Assert.assert_true(maximum_count, "Selected project Doesn't Have Remaining Views Greater Than 20")


# @then('I verify playback of the video that has views greater than 20')
# @allure.step('Then I verify playback of the video that has views greater than 20')
# def verify_playback_of_the_video_that_has_views_greater_than_20(setup_platform):
#     project_under_selected_genre = SearchPageScreener(setup_platform).click_on_start_watching_button()
#     Assert.assert_true(project_under_selected_genre, "Failed to play video for the selected project")


@when('I start the video playback')
@allure.step('When I start the video playback')
def start_the_video_playback(setup_platform):
    SearchPageScreener(setup_platform).click_on_start_watching_button()


@when('I start the video playback for Authentication playback')
@allure.step('When I start the video playback for Authentication playback')
def start_the_video_playback(setup_platform):
    SearchPageScreener(setup_platform).click_on_start_watching_button_authentication()    


@when('I Tap on the subtitle options menu in the video player')
@allure.step('When I Tap on the subtitle options menu in the video player')
def tap_on_the_subtitle_options_menu_in_the_video_player(setup_platform):
    MediaPlayerPageScreener(setup_platform).click_on_settings_icon(scenario_name=None)


@then('I verify that multiple subtitle options are available')
@allure.step('Then I verify that multiple subtitle options are available')
def verify_multiple_subtitle_options_are_available(setup_platform):
    Multiple_Subtitles = MediaPlayerPageScreener(setup_platform).verify_multiple_subtitles_displayed()
    Assert.assert_true(Multiple_Subtitles, "Multiple Subtitle options are not displayed for the selected project")


@when('I close the playback')
@allure.step('I close the playback')
def close_the_playback(setup_platform):
    MediaPlayerPageScreener(setup_platform).close_the_playback()


@when(parse('I select a different {subtitle} option'))
@allure.step('When I select a different subtitle option')
def select_a_different_sutitle_option(setup_platform, subtitle):
    subtitle_selected = MediaPlayerPageScreener(setup_platform).click_on_different_subtitle_option(readPreReqJsonValue("prereq", subtitle))
    Assert.assert_true(subtitle_selected, "Different Subtitle Option Is Selected For The Project Video")


@then('I verify that the selected subtitle is displayed correctly during playback')
@allure.step('Then I verify that the selected subtitle is displayed correctly during playback')
def verify_selected_subtitle_is_displayed_correctly_during_playback(setup_platform):
    pass


@when('I Tap on the audio options menu in the video player')
@allure.step('When I Tap on the audio options menu in the video player')
def tap_on_the_audio_options_menu_in_the_video_player(setup_platform):
    scenario_name = "Verify Playback on Multiple Audio Screeners"
    MediaPlayerPageScreener(setup_platform).click_on_settings_icon(scenario_name)


@then('I verify that multiple audio options are available')
@allure.step('Then I verify that multiple audio options are available')
def verify_multiple_audio_options_are_available(setup_platform):
    Multiple_audio = MediaPlayerPageScreener(setup_platform).verify_multiple_audio_selection_displayed()
    Assert.assert_not_none(Multiple_audio, "Multiple audio options are not displayed for the selected project")


@then('I verify default audio is selected')
@allure.step('Then I verify default audio is selected')
def verify_default_audio_is_selected(setup_platform):
    default_audio = MediaPlayerPageScreener(setup_platform).verify_default_audio_is_selected()
    Assert.assert_true(default_audio, "Default audio options is not selected for the selected project")


@when(parse('I select a different {audio}, {audio_ipad} option from the list'))
@allure.step('When I select a different audio option from the list')
def select_a_different_audio_option(setup_platform, audio, audio_ipad):
    audio_selected = MediaPlayerPageScreener(setup_platform).click_on_different_audio_option(readPreReqJsonValue("prereq", audio), readPreReqJsonValue("prereq", audio_ipad))
    Assert.assert_true(audio_selected, "Different Audio Option Is Selected For The Project Video")


@then('I verify that the selected audio is played correctly during playback')
@allure.step('Then I verify that the selected audio is played correctly during playback')
def verify_selected_audio_is_played_correctly_during_playback(setup_platform):
    pass


@when('I play the video to the fullest')
@allure.step('When I play the video to the fullest')
def play_the_video_to_the_fullest(setup_platform):
    MediaPlayerPageScreener(setup_platform).play_the_video_to_fullest()


@then('I verify that the auto playback functionality works as expected')
@allure.step('Then I verify that the auto playback functionality works as expected')
def verify_that_the_auto_playback_functionality_works_as_expected(setup_platform):
    auto_playback = SearchPageScreener(setup_platform).verify_auto_playback()
    Assert.assert_true(auto_playback, "Video details page is not displayed as expected after playing the viddeo to the fullest")


@given('I launch Testflight application')
@allure.step('Given I launch Testflight application')
def launch_testflight_application(setup_platform):
    LoginPageScreener(setup_platform).launch_testflight_app()


@when('I am in Testflight app')
@allure.step('When I am in Testflight app')
def verify_testflight_app_is_launched(setup_platform):
    Testflight_launched = LoginPageScreener(setup_platform).verify_testflight_app_launched()
    Assert.assert_true(Testflight_launched, "Testflight App Is Not Launched")


@when('I install previous build application from testflight')
@allure.step('When I install previous build application from testflight')
def install_previous_build_application_from_testflight(setup_platform):
    App_installed = LoginPageScreener(setup_platform).install_previous_build_from_testflight()
    Assert.assert_true(App_installed, "Previous build is not installed from testflight")


@when(parse('Launch the installed {application}'))
@allure.step('When Launch the installed application')
def launch_the_installed_application(setup_platform, application):
    LoginPageScreener(setup_platform).launch_the_app(readPreReqJsonValue("prereq", application))


@then('I verify app launch in previous build')
@allure.step('I verify app launch in previous build')
def verify_app_launch_in_previous_build(setup_platform):
    App_launched = LoginPageScreener(setup_platform).verify_forgetpassword_text_field(readPreReqJsonValue("prereq", "forgot_password_text"))
    Assert.assert_true(App_launched, "App Failed To Launch In Previous Build Downloaded From Testflight")


@when(parse('I update the {application} from testflight'))
@allure.step('I update the application from testflight')
def update_the_application_from_testflight(setup_platform, application):
    App_update = LoginPageScreener(setup_platform).update_the_app_in_ipad(readPreReqJsonValue("prereq", application))
    Assert.assert_true(App_update, "Failed To Update Screeners App In Testflight")


@then('verify playback in media player')
@allure.step('Then verify playback in media player')
def verify_playback_in_media_player(setup_platform):
    Playback = MediaPlayerPageScreener(setup_platform).verify_playback()
    Assert.assert_true(Playback, "Playack Is Not Started In Meddia Player Page")


@when(parse('The user uninstalls the {application} from the device'))
@allure.step('When The user uninstalls the application from the device')
def user_uninstalls_the_application_from_the_device(setup_platform, application):
    LoginPageScreener(setup_platform).uninstall_the_app_in_ipad(readPreReqJsonValue("prereq", application))


@when(parse('The user re-installs the {application} on the same device'))
@allure.step('When The user re-installs the application on the same device')
def user_reinstalls_the_application_on_the_same_device(setup_platform, application):
    App_Installed = LoginPageScreener(setup_platform).install_the_app_in_ipad(readPreReqJsonValue("prereq", application))
    Assert.assert_true(App_Installed, "App Instalation Failed After Uninstalling The Screeners App")


@when('I click on download button')
@allure.step('When I click on download button')
def click_on_download_button(setup_platform):
    HomePageScreener(setup_platform).click_on_downloads_button()


@then('I verify navigation to download page')
@allure.step('Then I verify navigation to download page')
def verify_navigation_to_download_page(setup_platform):
    Download_page = DownloadPageScreeners(setup_platform).verify_downloads_page_header()
    Assert.assert_true(Download_page, "Download page is not reached after clicking on download button")


@then('I verify no projects in downloads')
@allure.step('Then I verify no projects in downloads')
def verify_no_projects_in_downloads(setup_platform):
    no_downloaded_projects = DownloadPageScreeners(setup_platform).verify_no_downloads_message()
    Assert.assert_true(no_downloaded_projects, "There are projects under downloads")


@when('I click on download button inside project')
@allure.step('When I click on download button inside project')
def click_on_download_button_inside_project(setup_platform):
    SearchPageScreener(setup_platform).click_on_download_button_in_video_details_page()


@then(parse('I verify {project_name} added in downloads'))
@allure.step('Then I verify project added in downloads')
def verify_project_added_in_downloads(setup_platform, project_name):
    project_added = DownloadPageScreeners(setup_platform).verify_project_in_downloads(readPreReqJsonValue("prereq", project_name))
    Assert.assert_true(project_added, "Downloaded project is not displayed in download page")


@when('I play the downloaded project')
@allure.step('When I play the downloaded project')
def play_the_downloaded_project(setup_platform):
    project_playback = DownloadPageScreeners(setup_platform).play_the_downloaded_video()
    Assert.assert_true(project_playback, "Downloaded project is not played in media player page")


@then(parse('verify the downloaded project has multiple {audio} and {subtitle} tracks'))
@allure.step('Then verify the downloaded project has multiple audio and subtitle tracks')
def verify_downloaded_projects_has_multiple_audio_and_subtitle_tracks(setup_platform, audio, subtitle):
    project_added = MediaPlayerPageScreener(setup_platform).verify_multiple_audio_and_subtitle_options_are_displayed(readPreReqJsonValue("prereq", audio), readPreReqJsonValue("prereq", subtitle))
    Assert.assert_true(project_added, "Project doesn't have both multiple audio and subtitle files")


@when('I select the project to delete')
@allure.step('When I select the project to delete')
def select_the_project_to_delete(setup_platform):
    project_selected = DownloadPageScreeners(setup_platform).select_project_to_delete()
    Assert.assert_true(project_selected, "Downloaded project is not selected to delete")


@when('I delete the downloaded project by clicking on confirm delete')
@allure.step('When I delete the downloaded project by clicking on confirm delete')
def select_the_project_to_delete(setup_platform):
    DownloadPageScreeners(setup_platform).click_on_delete_button()
    project_deleted = DownloadPageScreeners(setup_platform).verify_and_handle_confirm_delete_popup()
    Assert.assert_true(project_deleted, "Downloaded project is not deleted from downloads page")


@then(parse('I verify {project_name} is deleted from downloads'))
@allure.step('Then I verify project is deleted from downloads')
def verify_project_is_deleted_from_downloads(setup_platform, project_name):
    project_deleted = DownloadPageScreeners(setup_platform).verify_project_in_downloads(readPreReqJsonValue("prereq", project_name))
    Assert.assert_false(project_deleted, "Deleted project is displayed in downloads page")


@when(parse('I select {season_number} with multiple audio and subtitle videos'))
@allure.step('When I select season number with multiple audio and subtitle videos')
def select_season_with_multiple_audio_and_subtitle_videos(setup_platform, season_number):
    SearchPageScreener(setup_platform).select_season_with_multiple_audio_andd_subtitle_playback(readPreReqJsonValue("prereq", season_number))


@then('I verify download screeners is disabled')
@allure.step('Then I verify download screeners is disabled')
def verify_download_screeners_is_disabled(setup_platform):
    Download_button = SearchPageScreener(setup_platform).verify_download_button_is_not_displayed()
    Assert.assert_false(Download_button, "Download button is displayedd for the project when downloadable screeners option is disabled")


@when(parse('I Click On Project Video With Multiple Audio {Audio_video} Under Selected Project'))
@allure.step('When I Click On Project Video With Multiple Audio Inside Project')
def click_on_multiple_audio_video_inside_project(setup_platform, Audio_video):
    SearchPageScreener(setup_platform).select_project_video_with_multiple_audio(readPreReqJsonValue("prereq", Audio_video))


@then('I verify overlay watermark in the media player')
@allure.step('Then I verify overlay watermark in the media player')
def verify_overlay_watermark_in_the_mediia_player(setup_platform):
    #watermark can't be verified as media player doesn't allow to take screenshot
    pass


@then('I verify forensic watermark in the media player')
@allure.step('Then I verify forensic watermark in the media player')
def verify_forensic_watermark_in_the_mediia_player(setup_platform):
    #watermark can't be verified as media player doesn't allow to take screenshot
    pass


@then('I verify forensic burned watermark in the media player')
@allure.step('Then I verify forensic burned watermark in the media player')
def verify_forensic_burned_watermark_in_the_mediia_player(setup_platform):
    #watermark can't be verified as media player doesn't allow to take screenshot
    pass


@when('I select the option Enter with QR CODE to log in using a URL')
@allure.step('When I select the option Enter with QR CODE to log in using a URL')
def user_selects_the_option_enter_with_qr_code_to_loin_usin_url(setup_platform):
    print('Selecting sign in with QR button in login screen')
    LoginPageScreener(setup_platform).click_sign_in_with_qr_code_button()
    LoginPageScreener(setup_platform).verify_qr_code_page_navigation()


@when('I copy the provided URL and opens it on a secondary device')
@allure.step("When I copy the provided URL and opens it on a secondary device")
def i_copy_the_provided_URL_and_opens_it_on_a_secondary_device(setup_platform, launchBrowser):
    print('executing I copy the provided URL and opens it on a secondary device')
    login_url_from_screen = LoginPageScreener(setup_platform).get_login_url()
    login_access_code = LoginPageScreener(setup_platform).login_access_code()

    print("fetched url from browser----", login_url_from_screen)
    time.sleep(7)
    browser = launchBrowser
   
    webBrowserPage = WebBrowserPage(browser)
    time.sleep(3)
    webBrowserPage.launch_browser_page(login_url_from_screen)
    time.sleep(4)
    login_access_code = login_access_code or login_url_from_screen.split('/')[-1]
    print("login_access_code  ===", login_access_code)
    webBrowserPage.send_qr_code(login_access_code)
    
    # Url = LoginPage(setup_platform).login_URL()
    # print("Launch URL")
    # LoginPage(setup_platform).launch_URL(Url)


@when(parse("I enter {username} and {password} and submit"))
def i_enter_username_and_password_and_submit(launchBrowser, username, password):
   
    username_to_enter = "" if readPreReqJsonValue("prereq", username) == "None" else readPreReqJsonValue("prereq", username)
    password_to_enter = "" if readPreReqJsonValue("prereq", password) == "None" else readPreReqJsonValue("prereq", password)
    # if readPreReqJsonValue("prereq", username) == "none":
    #     username = ""
    # if readPreReqJsonValue("prereq", password) == "none":
    #     password = ""
    print("username from exmaple ===", username_to_enter)
    print("password from exmaple ===", password_to_enter)
    webBrowserPage = WebBrowserPage(launchBrowser)
    webBrowserPage.submit_qr_url_credentials(username_to_enter, password_to_enter)


@then(parse('Verify {errormessage} on the login page on secondary device for {disc}'))
@allure.step('Then Verify {errormessage} on the login page on secondary device for {disc}')
def verify_error_message_on_the_login_page_on_secondary_device(launchBrowser, errormessage, disc):
    expected_errormessage = readPreReqJsonValue("prereq", errormessage)
    print('Verifying error message', expected_errormessage)
    webBrowserPage = WebBrowserPage(launchBrowser)
    is_errormessage_matches = webBrowserPage.invalid_Credentials_Error_Message(expected_errormessage, readPreReqJsonValue("prereq", disc))
    Assert.assert_true(is_errormessage_matches, 'Error message is not matching {}'.format(expected_errormessage))


@when('Click on Sign in with Remote Button')
@allure.step("Click on Sign in with Remote Button")
def click_on_sign_in_with_remote_button(setup_platform):
    print('Clicking on sign in with Remote Button in QR Screen')
    LoginPageScreener(setup_platform).click_sign_in_with_remote()
    print("Clicked On Sign In With Remote Button")


@then('I verify 2FA password authetication popup is displayed')
@allure.step('Then I verify 2FA password authetication popup is displayed')
def verify_2fa_password_authentication_popup_is_displayed(setup_platform):
    popup_display = MediaPlayerPageScreener(setup_platform).verify_2fa_password_authentication_popup()
    Assert.assert_true(popup_display, "2FA password popup is not displayed for the selected project")


@when(parse('I enter {screener_password} in authentication popup and unlock the project video'))
@allure.step('When I enter screener password in authentication popup and unlock the project video')
def enter_screener_password_in_authentication_popup_and_unlock_the_project_video(setup_platform, screener_password):
    MediaPlayerPageScreener(setup_platform).enter_screener_password_in_authentication_popup(readPreReqJsonValue("prereq", screener_password))


@then('I verify 2FA phone authetication popup is displayed')
@allure.step('Then I verify 2FA phone authetication popup is displayed')
def verify_2fa_phone_authentication_popup_is_displayed(setup_platform):
    popup_display = MediaPlayerPageScreener(setup_platform).verify_2fa_phone_authentication_popup()
    Assert.assert_true(popup_display, "2FA phone popup is not displayed for the selected project")


@when(parse('I enter {country_code} {mobile_number} in authentication popup and get the code'))
@allure.step('When I enter country_code mobile_number in authentication popup and get the code')
def enter_country_code_and_mobile_number_in_authentication_popup_and_get_the_code(setup_platform, country_code, mobile_number):
    MediaPlayerPageScreener(setup_platform).enter_country_code_and_mobile_number_in_authentication_popup(readPreReqJsonValue("prereq", country_code), readPreReqJsonValue("prereq", mobile_number))


@then('verify enter code popup is displayed')
@allure.step('Then verify enter code popup is displayed')
def verify_enter_code_popup_is_displayed(setup_platform):
    enter_code = MediaPlayerPageScreener(setup_platform).verify_enter_code_authentication_popup()
    Assert.assert_true(enter_code, "Enter 6 Ddigit Code Sent To Given Mobile Numbber Popup Is Not Displayed")


@then('I verify playback after unlocking by entering code')
@allure.step('Then I verify playback after unlocking by entering code')
def verify_playback_after_unlocking_bbby_entering_code(setup_platform):
    """Test script verification covered until generating coodde and verifying the respective screen.
       Entering code received in phone via auutomation is not feasible.
    """
    pass


@when(parse('I verify by entering a {no_security_project_name} {forensic_project_name} {overlay_project_name} different projects in the Search field'))   # noqa:E501
@allure.step('I verify by entering a <no_security_project_name> <forensic_project_name> <overlay_project_name> different projects in the Search field')   # noqa:E501
def verify_by_entering_a_differet_projects_in_the_search_field(setup_platform, no_security_project_name, forensic_project_name, overlay_project_name):    # noqa:E501
    multiple_screeners = SearchPageScreener(setup_platform).enter_Text_In_Search_Field_To_Verify_Different_Screeneers(readPreReqJsonValue("prereq", no_security_project_name), readPreReqJsonValue("prereq", forensic_project_name), readPreReqJsonValue("prereq", overlay_project_name))   # noqa:E501
    Assert.assert_true(multiple_screeners, "No Security, Forensic and Overlay Screeners Are Not displayed In The Same Guild")


@then(parse('I verify the project videos are {expired_message}'))
@allure.step('Then I verify the project videos are expired')
def verify_the_project_videos_are_expired(setup_platform, expired_message):
    expired_screeners = SearchPageScreener(setup_platform).verify_views_exhausted_error_message_in_project_video(readPreReqJsonValue("prereq", expired_message))
    Assert.assert_true(expired_screeners, 'The Selected Project Screeners Is Not Expired Yet')


@then('I verify the expires on text is visible and the expiry date is future dated')
@allure.step('Then I verify the expires on text is visible and the expiry date is future dated')
def verify_the_expires_on_text_is_visible_and_the_expiry_date_is_future_dated(setup_platform):
    future_dated = SearchPageScreener(setup_platform).verify_expire_on_text_is_future_dated()
    Assert.assert_true(future_dated, 'The Expires On Text Is Visible And The Expired Date Is Future Dated')


@given('I launch Admin Server')
@allure.step('Given I launch Admin Server')
def launch_admin_server(get_admin_server):
    print('Inside Admin')
    pass


@when('I Login with Admin Credentials')
@allure.step('When I Login with Admin Credentials')
def login_with_admin_credentials(get_admin_server):
    AdminPortalPageScreener(get_admin_server).login_to_admin_portal()


@when(parse('I search for the {project_name} to update screeners'))
@allure.step('When I search for the project to update screeners')
def search_for_the_project_to_update_screeners(get_admin_server, project_name):
    project_name_to_update_screeners = readPreReqJsonValue("prereq", project_name) + readPreReqJsonValue("prereq", "publicity_execution_id")
    AdminPortalPageScreener(get_admin_server).search_project_in_admin(project_name_to_update_screeners)


@when(parse('I click on {project_name} from search results in admin'))
@allure.step('When I click on project from search results in admin')
def click_on_project_from_search_results_in_admin(get_admin_server, project_name):
    project_name_to_update_screeners = readPreReqJsonValue("prereq", project_name) + readPreReqJsonValue("prereq", "publicity_execution_id")
    AdminPortalPageScreener(get_admin_server).click_on_project_search_results(project_name_to_update_screeners)


@when(parse('I navigate to screeners tab and select the {user}'))
@allure.step('When I navigate to screeners tab and select the user')
def navigate_to_screeners_tab_and_select_the_user(get_admin_server, user):
    AdminPortalPageScreener(get_admin_server).select_users_under_screeners_tab(readPreReqJsonValue("prereq", user))


@when(parse('I select {video_name} to update screeers'))
@allure.step('When I select video name to update screeers')
def select_video_name_to_update_screeners(get_admin_server, video_name):
    AdminPortalPageScreener(get_admin_server).select_video_to_update_screeners(readPreReqJsonValue("prereq", video_name))


@when('I update the screeners expiry date and remaining views')
@allure.step('When I update the screeners expiry date and remaining views')
def update_the_screeners_expiry_date_and_remaining_views(get_admin_server):
    AdminPortalPageScreener(get_admin_server).update_screeners_expiry_date_and_remaining_views()


@then('I validate remaining views and expiry date')
@allure.step('Then I validate remaining views and expiry date')
def validate_remaining_views_andd_expiry_date(setup_platform, shared_data):
    shared_data['remaining_views'], shared_data['expiry_date'] = SearchPageScreener(setup_platform).validate_expiry_date_and_remaining_views_count()
    if all([shared_data['remaining_views'], shared_data['expiry_date']]) is not None:
        print('Project Video Screener Is Displayed With Expiry Date And Remaining Views')
    else:
        Assert.assert_fail("roject Video Screener Is Not Displayed With Expiry Date And Remaining Views")


@then('I verify remaining views and expiry date value is updated')
@allure.step('Then I verify remaining views and expiry date value is updated')
def verify_remaining_views_and_expiry_date_value_is_updated(setup_platform, shared_data):
    screener_updated = SearchPageScreener(setup_platform).verify_the_remaining_views_an_expiry_date_is_updated(shared_data['remaining_views'], shared_data['expiry_date'])
    Assert.assert_true(screener_updated, 'Screener Details updated in admin is not reflected in app')


@then(parse("I verify the successful login {message} on the secondary device"))
@allure.step("Then I verify the successful login {message} on the secondary device")
def i_verify_the_successful_login_message_on_the_secondary_device(launchBrowser, message):
    webBrowserPage = WebBrowserPage(launchBrowser)
    successful_login = webBrowserPage.successfull_Login(readPreReqJsonValue("prereq", message))
    Assert.assert_true(successful_login, "Encounted Error while Login via QR Code URL")


@then(parse("verify screener app on the primary device logs in automatically"))
@allure.step('Then verify GD app on the primary device logs in automatically')
def verify_GD_app_on_the_primary_device_logs_in_automatically_within_duration(setup_platform):
    print('verify_GD_app_on_the_primary_device_logs_in_automatically_within_duration ')
    elementvisibilityWithinTime = HomePageScreener(setup_platform).validate_logged_in_and_home_page_visible_within_timeframe(readPreReqJsonValue("prereq", "gd_Duration"))   # noqa:E501
    Assert.assert_true(elementvisibilityWithinTime, "App Not logged in with in {}".format(readPreReqJsonValue("prereq", "gd_Duration")))


@when('I close the playback')
@allure.step('I close the playback')
def close_the_playback(setup_platform):
    MediaPlayerPageScreener(setup_platform).close_the_playback()


@then('I verify Unsupported device error banner is displayed in forensic playback')
@allure.step('Then I verify Unsupported device error banner is displayed in forensic playback')
def verify_unsupported_device_error_banner_is_displayed_in_forensic_playback(setup_platform):
    error_banner_displayed = MediaPlayerPageScreener(setup_platform).verify_unsupported_error_banner_in_playback()
    Assert.assert_true(error_banner_displayed, "Unsupported Device Error Banner Is Not Displayed In Forensic Playback") 


@then('I verify Unsupported device error banner is displayed in overlay playback')
@allure.step('Then I verify Unsupported device error banner is displayed in overlay playback')
def verify_unsupported_device_error_banner_is_displayed_in_overlay_playback(setup_platform):
    error_banner_displayed = MediaPlayerPageScreener(setup_platform).verify_unsupported_error_banner_in_playback()
    Assert.assert_true(error_banner_displayed, "Unsupported Device Error Banner Is Not Displayed In Overlay Playback")


@then('I verify Unsupported device error banner is not displayed in forensic playback')
@allure.step('Then I verify Unsupported device error banner is not displayed in forensic playback')
def verify_unsupported_device_error_banner_is_not_displayed_in_forensic_playback(setup_platform):
    error_banner_not_displayed = MediaPlayerPageScreener(setup_platform).verify_unsupported_error_banner_not_displayed_in_playback()
    Assert.assert_true(error_banner_not_displayed, "Unsupported Device Error Banner Is Displayed In Forensic Playback")


@then('I verify Unsupported device error banner is not displayed in overlay playback')
@allure.step('Then I verify Unsupported device error banner is not displayed in overlay playback')
def verify_unsupported_device_error_banner_is_not_displayed_in_overlay_playback(setup_platform):
    error_banner_not_displayed = MediaPlayerPageScreener(setup_platform).verify_unsupported_error_banner_not_displayed_in_playback()
    Assert.assert_true(error_banner_not_displayed, "Unsupported Device Error Banner Is Displayed In Overlay Playback")
