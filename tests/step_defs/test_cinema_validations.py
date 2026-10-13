import time
from pytest_bdd import given, when, parsers, then, scenarios
from pytest_bdd.parsers import parse
from conftest import readConstants, updateConstantFile
from pages.base_page import BasePage
from pages.login_page_cinema import LoginPageCinema
from pages.settings_page_cinema import SettingsPageCinema
from pages.home_page_cinema import HomePageCinema
from pages.search_page_cinema import SearchPage_Cinema
from pages.media_player_page_cinema import MediaPlayerPageCinema
from pages.help_page import HelpPage
from pages.media_player_page import MediaPlayerPage
from pages.logout_page import LogoutPage
from pages.download_page import DownloadPage
from pages.web_admin_page import AdminPortalPage
# from conftest import launchBrowser
from pages.web_browser_page import WebBrowserPage
import pytest
import allure
from conftest import readPreReqJsonValue
from pages.actions.assertions import Assert


scenarios('../features/Cinema_validations.feature')


@given("I launch Cinema App URL")
@allure.step("Given I launch Cinema App URL")
def launch_cinema_app_url(get_cinema_server):
    print('Logging in with admin credentials')
    admin_portal_GD_navigation = AdminPortalPage(get_cinema_server)
    admin_portal_GD_navigation.launch_cinema_url()


@given(parse("I launch Cinema App URL for {project_URL_link} and fetch Access Code"))
@allure.step("Given I launch Cinema App URL for Password verification and fetch Access Code")
def launch_Cinema_App_URL_for_Password_verification(setup_platform, launchBrowser, project_URL_link):
    print('Logging in with admin credentials')

    webBrowserPage = WebBrowserPage(launchBrowser)
    webBrowserPage.launch_browser_page(readPreReqJsonValue("prereq", project_URL_link))
    time.sleep(4)  
    admin_portal_GD_navigation = AdminPortalPage(webBrowserPage)
    admin_portal_GD_navigation.launch_cinema_url()
    admin_portal_GD_navigation.navigate_to_access_code_section(launchBrowser)
    access_code_validation = admin_portal_GD_navigation.fetch_access_code(launchBrowser)
    updateConstantFile("CINEMA_PIN", access_code_validation)
    print("access code updated in const==", readConstants("CINEMA_PIN"))
    Assert.assert_not_none(access_code_validation, "Access code is not displayed")    


@given("I launch Cinema App URL for Password verification and fetch Access Code")
@allure.step("Given I launch Cinema App URL for Password verification and fetch Access Code")
def launch_Cinema_App_URL_for_Password_verification(setup_platform, launchBrowser):
    print('Logging in with admin credentials')

    webBrowserPage = WebBrowserPage(launchBrowser)
    webBrowserPage.launch_browser_page(readPreReqJsonValue("prereq", "Cinema_URL_password"))
    time.sleep(4)  
    admin_portal_GD_navigation = AdminPortalPage(webBrowserPage)
    admin_portal_GD_navigation.launch_cinema_url()
    admin_portal_GD_navigation.navigate_to_access_code_section(launchBrowser)
    access_code_validation = admin_portal_GD_navigation.fetch_access_code(launchBrowser)
    updateConstantFile("CINEMA_PIN", access_code_validation)
    print("access code updated in const==", readConstants("CINEMA_PIN"))
    Assert.assert_not_none(access_code_validation, "Access code is not displayed")


@given("I launch Cinema App URL for Phone verification and fetch Access Code")
@allure.step("Given I launch Cinema App URL for Phone verification and fetch Access Code")
def launch_Cinema_App_URL_for_Phone_verification(setup_platform, launchBrowser):
    print('Logging in with admin credentials')

    webBrowserPage = WebBrowserPage(launchBrowser)
    webBrowserPage.launch_browser_page(readPreReqJsonValue("prereq", "PhoneNoWM"))
    time.sleep(4)  
    admin_portal_GD_navigation = AdminPortalPage(webBrowserPage)
    admin_portal_GD_navigation.launch_cinema_url()
    admin_portal_GD_navigation.navigate_to_access_code_section(launchBrowser)
    access_code_validation = admin_portal_GD_navigation.fetch_access_code(launchBrowser)
    updateConstantFile("CINEMA_PIN", access_code_validation)
    print("access code updated in const==", readConstants("CINEMA_PIN"))
    Assert.assert_not_none(access_code_validation, "Access code is not displayed") 


@given("I launch Cinema App URL to fetch Access Code with Standard watermark")
@allure.step("Given I launch Cinema App URL to fetch Access Code with Standard watermark")
def launch_Cinema_App_URL_for_standard_watermark_verification(setup_platform, launchBrowser):
    print('Logging in with admin credentials')

    webBrowserPage = WebBrowserPage(launchBrowser)
    webBrowserPage.launch_browser_page(readPreReqJsonValue("prereq", "Cinema_URL_Forensic_watermark"))
    time.sleep(4)  
    admin_portal_GD_navigation = AdminPortalPage(webBrowserPage)
    admin_portal_GD_navigation.launch_cinema_url()
    admin_portal_GD_navigation.navigate_to_access_code_section(launchBrowser)
    access_code_validation = admin_portal_GD_navigation.fetch_access_code(launchBrowser)
    updateConstantFile("CINEMA_PIN", access_code_validation)
    print("access code updated in const==", readConstants("CINEMA_PIN"))
    Assert.assert_not_none(access_code_validation, "Access code is not displayed")


@given("I launch Cinema App URL to fetch Access Code with Adjustable watermark")
@allure.step("Given I launch Cinema App URL to fetch Access Code with Adjustable watermark")
def launch_Cinema_App_URL_for_adjustable_watermark_verification(setup_platform, launchBrowser):
    print('Logging in with admin credentials')

    webBrowserPage = WebBrowserPage(launchBrowser)
    webBrowserPage.launch_browser_page(readPreReqJsonValue("prereq", "ForensicOnlyPwd"))
    time.sleep(4)  
    admin_portal_GD_navigation = AdminPortalPage(webBrowserPage)
    admin_portal_GD_navigation.launch_cinema_url()
    admin_portal_GD_navigation.navigate_to_access_code_section(launchBrowser)
    access_code_validation = admin_portal_GD_navigation.fetch_access_code(launchBrowser)
    updateConstantFile("CINEMA_PIN", access_code_validation)
    print("access code updated in const==", readConstants("CINEMA_PIN"))
    Assert.assert_not_none(access_code_validation, "Access code is not displayed")


@given("I launch Cinema App URL to fetch Access Code with Overlay screener watermark")
@allure.step("Given I launch Cinema App URL to fetch Access Code with Overlay screener watermark")
def launch_Cinema_App_URL_for_overlay_watermark_verification(setup_platform, launchBrowser):
    print('Logging in with admin credentials')

    webBrowserPage = WebBrowserPage(launchBrowser)
    webBrowserPage.launch_browser_page(readPreReqJsonValue("prereq", "NoSecurityOverlayWM"))
    time.sleep(4)  
    admin_portal_GD_navigation = AdminPortalPage(webBrowserPage)
    admin_portal_GD_navigation.launch_cinema_url()
    admin_portal_GD_navigation.navigate_to_access_code_section(launchBrowser)
    access_code_validation = admin_portal_GD_navigation.fetch_access_code(launchBrowser)
    updateConstantFile("CINEMA_PIN", access_code_validation)
    print("access code updated in const==", readConstants("CINEMA_PIN"))
    Assert.assert_not_none(access_code_validation, "Access code is not displayed")  


@given("I launch Cinema App URL to fetch Access Code with No security watermark")
@allure.step("Given I launch Cinema App URL to fetch Access Code with No security watermark")
def launch_Cinema_App_URL_for_no_security_watermark_verification(setup_platform, launchBrowser):
    print('Logging in with admin credentials')

    webBrowserPage = WebBrowserPage(launchBrowser)
    webBrowserPage.launch_browser_page(readPreReqJsonValue("prereq", "NoSecurityNoWM"))
    time.sleep(4)  
    admin_portal_GD_navigation = AdminPortalPage(webBrowserPage)
    admin_portal_GD_navigation.launch_cinema_url()
    admin_portal_GD_navigation.navigate_to_access_code_section(launchBrowser)
    access_code_validation = admin_portal_GD_navigation.fetch_access_code(launchBrowser)
    updateConstantFile("CINEMA_PIN", access_code_validation)
    print("access code updated in const==", readConstants("CINEMA_PIN"))
    Assert.assert_not_none(access_code_validation, "Access code is not displayed") 


@given("I launch Cinema App URL to fetch Access Code with Subtitle")
@allure.step("Given I launch Cinema App URL to fetch Access Code with Subtitle")
def launch_Cinema_App_URL_for_subtitle(setup_platform, launchBrowser):
    print('Logging in with admin credentials')

    webBrowserPage = WebBrowserPage(launchBrowser)
    webBrowserPage.launch_browser_page(readPreReqJsonValue("prereq","Cinema_Subtitle"))
    time.sleep(4)  
    admin_portal_GD_navigation = AdminPortalPage(webBrowserPage)
    admin_portal_GD_navigation.launch_cinema_url()
    admin_portal_GD_navigation.navigate_to_access_code_section(launchBrowser)
    access_code_validation = admin_portal_GD_navigation.fetch_access_code(launchBrowser)
    updateConstantFile("CINEMA_PIN", access_code_validation)
    print("access code updated in const==", readConstants("CINEMA_PIN"))
    Assert.assert_not_none(access_code_validation, "Access code is not displayed")                        


@then('The app load image is present')
@allure.step("Then The app load image is present")
def verify_app_load_image_visible(setup_platform):
    login_page_init = LoginPageCinema(setup_platform)
    print('Inside step definition')
    Launch_image = login_page_init.verify_launchScreen_view()
    Assert.assert_true(Launch_image, "App Launch Image is not loading")    


@given("I launch Cinema App URL to fetch Access Code")
@allure.step("Given I launch Cinema App URL to fetch Access Code")
def I_launch_Cinema_App_URL_to_fetch_Access_Code(get_cinema_server):
    print('Logging in with admin credentials')
    print("launchig brwoser ====", type(get_cinema_server))
    admin_portal_Cinema_navigation = AdminPortalPage(get_cinema_server)
    # admin_portal_Cinema_navigation.launch_cinema_url()
    admin_portal_Cinema_navigation.navigate_to_access_code_section(get_cinema_server)
    access_code_validation = admin_portal_Cinema_navigation.fetch_access_code(get_cinema_server)
    updateConstantFile("CINEMA_PIN", access_code_validation)
    print("access code updated in const==", readConstants("CINEMA_PIN"))
    Assert.assert_not_none(access_code_validation, "Access code is not displayed")   


@when('The user clicks on the Settings button')
@allure.step("When The user clicks on the Settings button")
def verify_the_user_clicks_on_the_settings_button(setup_platform):
    print("Clicking On Setting Button")
    LoginPageCinema(setup_platform).click_settings_button()


@when(parse('I update the {server} {company_name} and {API} key fields'))
@allure.step("When I update the server, company_name and API key fields")
def i_update_the_server_company_name_and_api_key_fields(setup_platform, server, company_name, API):
    print("Verfiying Server Text In Settings Screen")
    server_URL = readPreReqJsonValue("prereq", server).format(readConstants("QA_SERVER"))
    SettingsPageCinema(setup_platform).set_settings_data(server_URL, readPreReqJsonValue("prereq", company_name), readPreReqJsonValue("prereq", API))  # noqa:E501
    # settingspage.  # noqa:E50  


@then('The fields should be updated successfully')
@allure.step('Then The fields should be updated successfully')
def verify_the_fields_should_be_updated_successfully(setup_platform):
    print("Clicking On Save Button")
    SettingsPageCinema(setup_platform).click_savebutton()
    Setting_updation = LoginPageCinema(setup_platform).verify_signin_header()
    Assert.assert_true(Setting_updation, "Failed at updating settings configuration")      


@when("I navigate to Access code section")
@allure.step("When I navigate to Access code section")
def navigate_to_access_code_section(get_cinema_server):
    print('Logging in with admin credentials')
    admin_portal_GD_navigation = AdminPortalPage(get_cinema_server)
    admin_portal_GD_navigation.navigate_to_access_code_section(get_cinema_server)  


@then("I verify the access code and fetch the access code")
@allure.step("Then I verify the access code and fetch the access code")
def verify_the_access_code_and_fetch_the_access_code(get_cinema_server):
    print('Logging in with admin credentials')
    admin_portal_GD_navigation = AdminPortalPage(get_cinema_server)
    access_code_validation = admin_portal_GD_navigation.fetch_access_code(get_cinema_server)
    updateConstantFile("CINEMA_PIN", access_code_validation)
    print("access code updated in const==", readConstants("CINEMA_PIN"))
    Assert.assert_not_none(access_code_validation, "Access code is not displayed")  


@when("I launch Cinema Application")
@allure.step("When I launch Cinema Application")
def launch_cinema_application(setup_platform):
    print("Cinema Application Launched")
    print('what is webdriver instance =====', type(setup_platform))
    if isinstance(setup_platform, webdriver.Remote):
        print("Cinema Application Launched")
    elif isinstance(setup_platform, str):
        print("Cinema Application Launched in roku")
        sessionid = setup_platform
        print(" ", sessionid)
        basePage = BasePage(setup_platform)
        basePage.launchApp()
    
        # roku_actions = RokuActions()
        # roku_actions.getActiveChannel(setup_platform)
        # time.sleep(15)
        # roku_actions.doRokuGDLogin() 
                

@when("I relaunch Cinema Application")
@allure.step("When I relaunch Cinema Application")
def relaunch_cinema_application(setup_platform):
    print("Cinema Application Launched")
    print('what is webdriver instance =====', type(setup_platform))
    if isinstance(setup_platform, webdriver.Remote):
        basePage = BasePage(setup_platform)
        basePage.relaunchApp("com.indee.indeestaffsc")
    elif isinstance(setup_platform, str):
        print("Cinema Application Launched in roku")
        sessionid = setup_platform
        print(" ", sessionid)
        basePage = BasePage(setup_platform)
        basePage.launchApp()
    

@given("I launch Cinema Application on Respective platform")
@allure.step("When I launch Cinema Application on Respective platform")
def launch_cinema_application_on_respective_platform(setup_platform):
    print("Cinema Application Launched")
    print('what is webdriver instance =====', type(setup_platform))
    if isinstance(setup_platform, webdriver.Remote):
        print("Cinema Application Launched")
    elif isinstance(setup_platform, str):
        print("Cinema Application Launched in roku")
        sessionid = setup_platform
        print(" ", sessionid)
        basePage = BasePage(setup_platform)
        basePage.launchApp()
    
        # roku_actions = RokuActions()
        # roku_actions.getActiveChannel(setup_platform)
        # time.sleep(15)
        # roku_actions.doRokuGDLogin() 


@when("I am in Login Page")
@allure.step("When I am in Login Page")
def i_am_in_login_page(setup_platform):
    isSignInHeaderDisplayed = LoginPageCinema(setup_platform).verify_signin_header()
    Assert.assert_true(isSignInHeaderDisplayed, "Application is not in Login Page")
    

@then('I verify Login Page BackGround image is loaded')
@allure.step('I verify Login Page BackGround image is loaded')
def i_verify_login_page_background_image(setup_platform):
    print("here Login Page BackGround image is loaded")
    isBGdisplayed = LoginPageCinema(setup_platform).verify_bg_image_displayed()
    Assert.assert_true(isBGdisplayed, "Login Page BG Image is Not Displayed")


@then('I verify Cinema App icon is present')
@allure.step('I verify Cinema App icon is present')
def i_verify_cinema_app_icon_is_present(setup_platform):
    print("here Login Page Cinema launch is loaded")
    islaunchicon = LoginPageCinema(setup_platform).verify_cinema_launch_icon()
    Assert.assert_true(islaunchicon, "Cinema launch icon is Not Displayed")


@then('I verify Sign in header is present')
@allure.step('Then I verify Sign in header is present')
def i_verify_sign_in_header_is_present(setup_platform):
    print("Verifying Sign In Header Text In Login Page")
    isSignInHeaderDisplayed = LoginPageCinema(setup_platform).verify_signin_header()
    Assert.assert_true(isSignInHeaderDisplayed, "Sign In Header Is Not Displayed In Login Page")


@then(parse('I verify Access Key field is present with {text}'))
@allure.step('I verify Access Key field is present with {text}')
def verify_access_key_field_is_present(setup_platform, text):
    print("Verifying Access code field is present In Login Page")
    isAccessCodeDisplayed = LoginPageCinema(setup_platform).verify_Access_Code_text_field(readPreReqJsonValue("prereq", text))
    Assert.assert_true(isAccessCodeDisplayed, "AccessCode Is Not Displayed In Login Page")


@then('I verify Enter Button is Present')
@allure.step('I verify Enter Button is Present')
def verify_enter_button_is_present(setup_platform):
    print("Verifying enter Button Displayed In Login Page")
    isSignInButtonDisplayed = LoginPageCinema(setup_platform).check_Enterbutton_visbility()
    Assert.assert_true(isSignInButtonDisplayed, "Enter Button not present in LoginPage ")


@then('I verify App Version is present')
@allure.step('I verify App Version is present')
def i_verify_app_version_is_present(setup_platform):
    print("Verifying App Version Is Displayed In Login Page")
    isAppVersionDisplayed = LoginPageCinema(setup_platform).check_app_version_visibilty()
    Assert.assert_true(isAppVersionDisplayed, "App Version Is Not Displayed In Login Page")


@then('I verify Settings button is Present')
@allure.step('Then Settings button is Present')
def i_verify_settings_button_is_present(setup_platform):
    print("Verifying Settings Button Is Displayed In Login Page")
    isSettingsButtonDisplayed = LoginPageCinema(setup_platform).check_settings_button_visibilty()
    Assert.assert_true(isSettingsButtonDisplayed, "Settings Button Is Not Displayed In Login Page")


@then('Where can I find my access code')
@allure.step('Then Where can I find my access code')
def verify_where_can_i_find_my_access_code_is_present(setup_platform):
    print("Verifying Access code text Is Displayed In Login Page")
    isAccesscodedisplayed = LoginPageCinema(setup_platform).where_can_find_access_code()
    Assert.assert_true(isAccesscodedisplayed, "Where can I find my access code Is Not Displayed In Login Page")


@then('I verify terms and services is displayed')
@allure.step('Then I verify terms and services is displayed')
def verify_terms_and_service_is_displayed(setup_platform):
    termsAndServicesIsDisplayed = LoginPageCinema(setup_platform).terms_Services()
    Assert.assert_true(termsAndServicesIsDisplayed, "Terms and services is not displayed in Login page")



@then('I verify by tapping on Terms and services')
@allure.step('Then I verify by tapping on Terms and services')
def verify_by_tapping_on_termms_and_services(setup_platform):
    termsAndServicesIsDisplayed = LoginPageCinema(setup_platform).tapping_On_Terms_Services()
    print('tap on terms and services')
    Assert.assert_true(termsAndServicesIsDisplayed, "Terms and services is not displayed")


@then('I verify Privacy policy is displayed')
@allure.step('Then I verify Privacy policy is displayed')
def verify_privacy_policy_is_displayed(setup_platform):
    termsAndServicesIsDisplayed = LoginPageCinema(setup_platform).privacy_policy()
    Assert.assert_true(termsAndServicesIsDisplayed, "Privacy policy is not displayed in Login page")


@then('I verify Where can I find my access code field')
@allure.step('Then I verify Where can I find my access code field')
def verify_where_my_access_code_is_displayed(setup_platform):
    termsAndServicesIsDisplayed = LoginPageCinema(setup_platform).where_can_find_access_code()
    Assert.assert_true(termsAndServicesIsDisplayed, "Where my access code is not displayed in Login page")    


@then('I verify by tapping on Privacy policy')
@allure.step('Then I verify by tapping on Privacy policy')
def verify_by_tapping_on_privacy_policy(setup_platform):
    termsAndServicesIsDisplayed = LoginPageCinema(setup_platform).tapping_On_privacy_policy()
    print('tap on terms and services')
    Assert.assert_true(termsAndServicesIsDisplayed, "Privacy policy is not displayed") 

@then('I navigate back to login page')
@allure.step('Then I navigate back to login page')
def navigate_back_to_login_page(setup_platform):
    # LoginPageCinema(setup_platform).navigate_back_to_login_page_from_terms_of_service()
    login_page_displayed = LoginPageCinema(setup_platform).verify_signin_header()
    Assert.assert_true(login_page_displayed, "Login Page Is Not Navigated From Termms Of Service")

@then(parse('verify {errormessage_without_entering_pin} without entering pin'))
@allure.step('Then verify this field cannot be empty error message in login page')
def verify_input_field_cannot_be_empty_error_message(setup_platform, errormessage_without_entering_pin):
    emptyerrormessage = LoginPageCinema(setup_platform).verify_empty_error_message(readPreReqJsonValue("prereq", errormessage_without_entering_pin))
    print(emptyerrormessage)
    Assert.assert_true(emptyerrormessage, "Empty error message is not displayed") 


@when("I am in Login Page")
@allure.step("When I am in Login Page")
def i_am_in_login_page(setup_platform):
    print("in Cinema  Applciation LoginScreen")


@when(parse("Enter {invalid_pin} in Login page"))
def enter_Pin_In_Login_Page(setup_platform, invalid_pin):
    LoginPageCinema(setup_platform).enter_Access_Code(readPreReqJsonValue("prereq", invalid_pin))    


@when('Enter AccessCode in Login page')
@allure.step('When Enter AccessCode in Login page')
def enter_pin_in_login_page(setup_platform):
    Access_Code_Value = readConstants("CINEMA_PIN")
    # print("=====readConstants(CINEMA_PIN)" + readConstants("CINEMA_PIN"))
    LoginPageCinema(setup_platform).enter_Access_Code(Access_Code_Value)


@when('I click on the Enter button')
@allure.step('When I click on the Enter button')
def click_on_enter_button(setup_platform):
    print("click on enter button")
    LoginPageCinema(setup_platform).click_login()


@when('I close the app')
@allure.step('When I close the app')
def click_on_close(setup_platform):
    print("click on close button")
    LoginPageCinema(setup_platform).close_the_app()


@then('verify the successfull login')
@allure.step('Then verify the successfull login')
def verify_the_successfull_login(setup_platform):
    header_logo = LoginPageCinema(setup_platform).header_logo()
    Assert.assert_true(header_logo, "Header logo is not displayed")   


@then('I verify the Header logo on Homepage')
@allure.step('Then I verify the Header logo on Homepage')
def verify_the_header_logo_on_homepage(setup_platform):
    header_logo = LoginPageCinema(setup_platform).header_logo()
    Assert.assert_true(header_logo, "Header logo is not displayed") 


@then('I verify project banner in Homepage')
@allure.step('Then I verify project banner in Homepage')
def verify_project_banner_in_homepage(setup_platform):
    project_banner = HomePageCinema(setup_platform).project_banner()
    Assert.assert_true(project_banner, "Project banner is not displayed")


# @then('I verify project poster in Homepage')
# @allure.step('Then I verify project poster in Homepage')
# def verify_project_poster_in_homepage(setup_platform):
#     project_poster = HomePageCinema(setup_platform).project_poster()
#     Assert.assert_true(project_poster, "Project poster is not displayed")


@then('I verify see more button in Homepage')
@allure.step('Then I verify see more button in Homepage')
def verify_see_more_button_in_homepage(setup_platform):
    see_more = HomePageCinema(setup_platform).see_more()
    Assert.assert_true(see_more, "See more button is not displayed")  


@then('I verify the project description')
@allure.step('Then I verify the project description')
def verify_the_project_descriptione(setup_platform):
    see_more = HomePageCinema(setup_platform).project_description()
    Assert.assert_true(see_more, "Project description is not displayed")                    


@then(parse('I verify the {errormessage_invalid_pin} on Loginpage'))
@allure.step('Then I verify the errormessage on Loginpage')
def verify_error_message_on_login_page(setup_platform, errormessage_invalid_pin):
    Error_Message = LoginPageCinema(setup_platform).invalid_Pin_Error_Message(readPreReqJsonValue("prereq", errormessage_invalid_pin))
    Assert.assert_true(Error_Message, "Error Message Is Not Displayed")


@then(parse('I verify the expired pin {error_message_expired_access_code} on the Login'))
@allure.step('Then I verify the errormessage on Loginpage')
def verify_error_message_on_login_page(setup_platform, error_message_expired_access_code):
    Error_Message = LoginPageCinema(setup_platform).invalid_expired_pin_Error_Message(readPreReqJsonValue("prereq", error_message_expired_access_code))
    Assert.assert_true(Error_Message, "Error Message Is Not Displayed")


@then('Verify the first video in the project gets highlighted')
@allure.step('Then Verify the first video in the project gets highlighted')
def verify_first_video_in_project_gets_highlighted(setup_platform):
    # Add Your Code Here
    pass


@when(parse('I click on the project {roku_brandIndex} displayed on Homepage'))
@allure.step('Then  I click on the project displayed on Homepage')
def click_on_the_project_displayed_on_homepage(setup_platform, roku_brandIndex):
    HomePageCinema(setup_platform).click_first_project(roku_brandIndex)
   

@then(parse('I verify the {Expiry_date_and_time} displayed on project data'))
@allure.step('Then  I verify the expire')
def verify_expiry_date_and_time_on_project(setup_platform, Expiry_date_and_time):
    remaining_views = HomePageCinema(setup_platform).expiry_date_time(readPreReqJsonValue("prereq", Expiry_date_and_time))
    Assert.assert_true(remaining_views, "Expire label is not displayed")     


@then(parse('I verify the {Remaining_views} displayed on project'))
@allure.step('I verify the {Remaining_views} displayed on project')
def verify_remaining_views_on_project(setup_platform, Remaining_views):
    remaining_views = HomePageCinema(setup_platform).remaining_views_project(readPreReqJsonValue("prereq", Remaining_views))
    Assert.assert_true(remaining_views, "Remaining view is not displayed") 


@then('I verify the watch now button is displayed on project')
@allure.step('Then  I verify the watch now button is displayed on project')
def verify_the_watch_now_button_is_displayed_on_project(setup_platform):
    watch_now_button = HomePageCinema(setup_platform).watch_now_button()
    Assert.assert_true(watch_now_button, "Watch Now button views is not displayed")


@then('I verify the successfull playbacks')
@allure.step('Then  I verify the successfull playback')
def verify_the_watch_now_button_is_displayed_on_project(setup_platform, shared_data):
    sucessfull_playback = HomePageCinema(setup_platform).verify_successfull_playback(shared_data['remaining_views'])
    Assert.assert_true(sucessfull_playback, "Video not played")     


@then('Verify synopsis in episodic project is displayed')
@allure.step('Then  Verify synopsis in episodic project is displayed')
def verify_synopsis_in_episodic_project_is_displayed(setup_platform):
    synopsis = HomePageCinema(setup_platform).episodic_synopsis()
    Assert.assert_true(synopsis, "Episodic synopsis is not displayed") 


@then('Verify multiple episodic project is displayed')
@allure.step('Then  Verify multiple episodic project is displayed')
def verify_multiple_episodi_project_is_displayed(setup_platform):
    mulitiple_episodes = HomePageCinema(setup_platform).mulitiple_episodes()
    Assert.assert_true(mulitiple_episodes, "Multiple episodic is not displayed")     


@then('Verify season number in episodic project is displayed')
@allure.step('Then  Verify season number in episodic project is displayed')
def verify_season_number_in_episodic_project_is_displayed(setup_platform):
    season_number = HomePageCinema(setup_platform).season_number()
    Assert.assert_true(season_number, "Season number is not displayed")      


@then('Verify the video duration visibility on projects')
@allure.step('Then  Verify season number in episodic project is displayed')
def verify_season_number_in_episodic_project_is_displayed(setup_platform):
    duration_video = HomePageCinema(setup_platform).duration_video()
    Assert.assert_true(duration_video, "Video duration is not displayed")      


@then('Verify episodic number in episodic project is displayed')
@allure.step('Then  Verify season number in episodic project is displayed')
def verify_episodic_number_in_episodic_project_is_displayed(setup_platform):
    episodic_number = HomePageCinema(setup_platform).episodic_number()
    Assert.assert_true(episodic_number, "Episodic number is inco")  

@pytest.fixture
def shared_data():
    return {'remaining_views': None,
            }


@when('I click on the Watch now button')
@allure.step('When  I click on the Watch now button')
def click_on_the_authenticate_and_play_button(setup_platform, shared_data):
    HomePageCinema(setup_platform).click_authenticate_button()
    shared_data['remaining_views'] = HomePageCinema(setup_platform).remaining_views_count()


@when(parse('I enter the {password} and submits'))
@allure.step('When  I enter the password and submit')
def enter_the_password_and_submit(setup_platform, password):
    HomePageCinema(setup_platform).enter_password_and_authenticate(password)  


@when('I enter the password and submits')
@allure.step('When  I enter the password and submit')
def enter_the_password_and_submit(setup_platform):
    HomePageCinema(setup_platform).enter_password_and_authenticate()  


@when(parse('I enter the valid {phone_number}'))
@allure.step('When  I enter the valid phone number and submit')
def enter_the_valid_phone_number_and_submit(setup_platform, phone_number):
    print("Entering phone number")
    HomePageCinema(setup_platform).enter_phone_number(phone_number) 


@when('I enter the otp')
@allure.step('When  I enter the otp')
def enter_the_otp(setup_platform):
    print("Entering otp")
    HomePageCinema(setup_platform).enter_otp()   


@then(parse('I verify the {invalid_password_error_message} on the OTP section'))
@allure.step('When  I verify the <invalid_password_error_message> on the OTP section')
def verify_the_invalid_password_error_message_on_the_OTP_section(setup_platform, invalid_password_error_message):
    HomePageCinema(setup_platform).enter_invalid_password_and_authenticate(readPreReqJsonValue("prereq", invalid_password_error_message))        
      

@then(parse('I verify the {invalid_password_error_message} on the OTP sections OTP'))
@allure.step('When  I verify the <invalid_password_error_message> on the OTP section')
def verify_the_invalid_password_error_message_on_the_OTP_section(setup_platform, invalid_password_error_message):
    HomePageCinema(setup_platform).enter_invalid_password_and_authenticate_OTP(readPreReqJsonValue("prereq", invalid_password_error_message))


@when(parse('I enter the {invalid_password} and submit'))
@allure.step('When  I enter the <invalid_password> and submit')
def enter_the_invalid_password_and_submit(setup_platform, invalid_password):
    HomePageCinema(setup_platform).enter_invalid_password_and_authenticate(readPreReqJsonValue("prereq", invalid_password))  


@then(parse('I verify the {invalid_password_error_message} playback'))
@allure.step('Then  I verify the <invalid_password_error_message> playback')
def verify_the_invalid_password_error_message_playback(setup_platform, invalid_password_error_message):
    error_message = HomePageCinema(setup_platform).verify_error_message_playback(readPreReqJsonValue("prereq", invalid_password_error_message))
    Assert.assert_true(error_message, "Incorrect password message is not get displayed")                 


@then('I logout from the application and verify logged out')
@allure.step('Then  I logout from the application and verify logged out')
def logout_from_the_application_and_verify_logged_out(setup_platform):
    logged_out = LoginPageCinema(setup_platform).verify_logged_out() 
    Assert.assert_true(logged_out, "Application not get logged out")  


@then('I verify the single subtitle on playback')
@allure.step('Then  I verify the single subtitle on playback')
def verify_the_single_subtitle_on_playback(setup_platform):
    print("Single subtitle")
    single_subtitle = MediaPlayerPageCinema(setup_platform).single_subtitle() 
    Assert.assert_true(single_subtitle, "Single subtitle is not displayed")  


@then('I verify the single subtitle on playback')
@allure.step('Then  I verify the single subtitle on playback')
def verify_the_single_subtitle_on_playback(setup_platform):
    single_subtitle = MediaPlayerPageCinema(setup_platform).single_subtitle() 
    Assert.assert_true(single_subtitle, "Single subtitle is not displayed") 


@then('I verify the default subtitle got selected')
@allure.step('Then  I verify the default subtitle got selected')
def verify_the_default_subtitle_got_selected(setup_platform):
    default_subtitle = MediaPlayerPageCinema(setup_platform).verify_default_audio_is_selected() 
    Assert.assert_true(default_subtitle, "Default subtitle is not selected")  


@then('I verify the multiple subtitle on playback')
@allure.step('Then  I verify the multiple subtitle on playback')
def verify_the_multiple_subtitle_on_playback(setup_platform):
    multiple_subtitle = MediaPlayerPageCinema(setup_platform).verify_multiple_subtitle() 
    Assert.assert_true(multiple_subtitle, "Multiple subtitle is not displayed")   


@then(parse('I verify by selecting the different {subtitle}'))
@allure.step('Then  I verify by selecting the different subtitle')
def verify_the_different_subtitle_on_playback(setup_platform, subtitle):
    multiple_subtitle = MediaPlayerPageCinema(setup_platform).click_multiple_subtitle(readPreReqJsonValue("prereq", subtitle))
    Assert.assert_true(multiple_subtitle, "Multiple subtitle is not displayed")          


@then('I navigate back to the home using navigate back option')
@allure.step('Then  I navigate back to the home using navigate back option')
def navigate_back_to_the_home_using_navigate_back_option(setup_platform):
    LoginPageCinema(setup_platform).navigate_back_until_app_close() 


@then('I navigate back to the home using Home option')
@allure.step('Then  I navigate back to the home using Home option')
def navigate_back_to_the_home_using_Home_option(setup_platform):
    LoginPageCinema(setup_platform).navigate_using_home_button()     


@then('I verify the launch page')
@allure.step('Then  I verify the launch page')
def verify_the_launch_page(setup_platform):
    sign_in = LoginPageCinema(setup_platform).verify_signin_header()  
    print("sign_in  buttomn visible ===", sign_in)
    Assert.assert_true(sign_in, "Launch to the login page Failed,SignIn Button not visible")  
           

@when('I navigate to the menu')
@allure.step('When I navigate to the menu')
def navigate_to_the_menu(setup_platform):
    # Add Your Code Here
    pass


@when('I click on the Logout button')
@allure.step('When I click on the Logout button')
def click_on_the_logout_button(setup_platform):
    # Add Your Code Here
    pass


@then('I should be redirected to the Login page')
@allure.step('Then I should be redirected to the Login page')
def verify_navigation_to_login_page(setup_platform):
    # Add Your Code Here
    pass


@when(parse('I re-enter the same {access_code} within 5 minutes of code expiry'))
@allure.step('When I re-enter the same access code within 5 minutes of code expiry')
def enter_same_access_code_within_5mins_of_code_expiry(setup_platform, access_code):
    # Add Your Code Here
    pass


@then('I should be logged in successfully if the access code is still valid')
@allure.step('Then I should be logged in successfully if the access code is still valid')
def verify_user_logged_in_successfully_if_the_access_code_is_still_valid(setup_platform):
    # Add Your Code Here
    pass


@then(parse('I verify that the header logo,project poster,banner,see more button,{Project_description}'))
def verify_that_the_header_logo_is_displayed_correctly(setup_platform, Project_description):
    headerlogohome = HomePageCinema(setup_platform).verify_header_logo_in_homepage_screen(readPreReqJsonValue("prereq", Project_description))
    Assert.assert_true(headerlogohome, "verify header logo in homepage")


@then('I verify the Project Description')
@allure.step('Then I verify the Project Description')
def verify_the_project_description(setup_platform):
    # Add Your Code Here
    pass


@when('Click on the video')
@allure.step('When Click on the video')
def click_on_the_video(setup_platform):
    # Add Your Code Here
    pass


@then(parse('Project {Cast} and {Crew} Information Should be Displayed'))
@allure.step('Then Project Cast and Crew Information Should be Displayed')
def verify_project_cast_and_crew_information_should_be_displayed(setup_platform, Cast, Crew):
    print('Validating project cast and crew information')
    Cast_Crew_Details = SearchPage_Cinema(setup_platform).verify_Cast_Crew_Title_Displayed(readPreReqJsonValue("prereq", Cast), readPreReqJsonValue("prereq", Crew))  # noqa:E501
    Assert.assert_true(Cast_Crew_Details, "Cast And Crew Is Not Displayed As Expected In Project Details Page")


@then('Verify that the menu on the Home Page is displayed correctly')
@allure.step('Then Verify that the menu on the Home Page is displayed correctly')
def verify_menu_on_the_home_page_is_displayed_correctly(setup_platform):
    # Add Your Code Here
    pass


@when('I click on search button in home page')
@allure.step('When I click on search button in home page')
def click_on_search_button_in_home_page(setup_platform):
    # Add Your Code Here
    pass


@then(parse('I verify by entering a {project_name} in the Search field'))
@allure.step('Then I verify by entering a project name in the Search field')
def verify_by_entering_project_name_in_search_field(setup_platform, project_name):
    # Add Your Code Here
    pass


@when('Click on Project from Search Result')
@allure.step('When Click on Project from Search Result')
def click_on_project_from_search_result(setup_platform):
    # Add Your Code Here
    pass



@when('I Tap on the subtitle options menu in the video player')
@allure.step('When I Tap on the subtitle options menu in the video player')
def tap_on_subtitle_option_menu_in_video_player(setup_platform):
    print('Clicking on subtitles option')
    # MediaPlayerPageCinema(setup_platform).click_on_Playnowbutton()
    time.sleep(3)
    MediaPlayerPageCinema(setup_platform).click_on_settings_icon(scenario_name=None)



@then('I verify that multiple subtitle options are available')
@allure.step('Then I verify that multiple subtitle options are available')
def verify_multiple_subtitle_options_are_available(setup_platform):
    # Add Your Code Here
    pass


@when('I select a different subtitle option')
@allure.step('When I select a different subtitle option')
def select_a_different_subtitle_option(setup_platform):
    # Add Your Code Here
    pass


@then('I verify that the selected subtitle is displayed correctly during playback')
@allure.step('Then I verify that the selected subtitle is displayed correctly during playback')
def verify_selected_subtitle_is_displayed_correctly_during_playback(setup_platform):
    # Add Your Code Here
    pass


@when('I am on the 2FA pop-up screen')
@allure.step('When I am on the 2FA pop-up screen')
def user_receives_2fa_popup_screen(setup_platform):
    # Add Your Code Here
    pass


@when('I enter an invalid OTP code')
@allure.step('When I enter an invalid OTP code')
def enter_an_invalid_otp_code(setup_platform):
    # Add Your Code Here
    pass


@when('I click on the Verify button')
@allure.step('When I click on the Verify button')
def click_on_verify_button(setup_platform):
    # Add Your Code Here
    pass


@then(parse('I should see invalid otp {errormessage}'))
@allure.step('Then I should see invalid otp error messsage')
def verify_invalid_otp_error_message(setup_platform, errormessage):
    # Add Your Code Here
    pass


@when('I press the Back button on the TV remote')
@allure.step('When I press the Back button on the TV remote')
def press_back_button_on_tv_remote(setup_platform):
    # Add Your Code Here
    pass


@then('I should be navigated back to the devices home page')
@allure.step('Then I should be navigated back to the devices home page')
def verify_navigation_back_to_devices_home_page(setup_platform):
    # Add Your Code Here
    pass


@when('I try to relaunch the Cinema Application from the home page')
@allure.step('When I try to relaunch the Cinema Application from the home page')
def relaunch_the_cinema_application_from_the_hoome_page(setup_platform):
    # Add Your Code Here
    pass


@then('The Cinema Application should launch successfully')
@allure.step('Then The Cinema Application should launch successfully')
def verify_cinema_application_should_launch_successfully(setup_platform):
    # Add Your Code Here
    pass


@when('I click on cmaf button')
def click_on_cmaf_button(setup_platform):
    LoginPageCinema(setup_platform).click_on_cmaf_button()


@then('verify the signin button')
def verify_the_sign_button(setup_platform):
    LoginPageCinema(setup_platform).verify_signin_button()


@then('I verify the screener has projects')
def verify_the_screener_projects_in_homepage(setup_platform):
    LoginPageCinema(setup_platform).verify_the_homepage()
    

@then('I click on close button')
def click_on_close_button(setup_platform):
    LoginPageCinema(setup_platform).click_on_close()


@then('I click on ok button and navigate back')
def click_on_ok(setup_platform):
    LoginPageCinema(setup_platform).click_on_ok()


@when(parse('User update the {server} {company_name} and {API} key fields in roku'))
@allure.step("When I update the server, company_name and API key fields")
def i_update_the_server_company_name_and_api_key_fields(setup_platform, server, company_name, API):
    LoginPageCinema(setup_platform).click_settings_roku()
    settingspage = SettingsPageCinema(setup_platform)
    serverURL = readPreReqJsonValue("prereq", server)
    serverURLValue = serverURL.format(readConstants("QA_SERVER"))
    
    settingspage.set_settings_data_roku(serverURLValue, readPreReqJsonValue("prereq", company_name), readPreReqJsonValue("prereq", API)) 
    settingspage.click_savebutton_roku()    
    