# import pytest
import time
from pytest_bdd import given, when, parsers, then, scenarios
from pytest_bdd.parsers import parse
from appium import webdriver
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.settings_page import SettingsPage
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.help_page import HelpPage
from pages.media_player_page import MediaPlayerPage
from pages.logout_page import LogoutPage
from pages.download_page import DownloadPage
from pages.web_admin_page import AdminPortalPage
from pages.web_nimaad_page import NimaadPortalPage
# from conftest import launchBrowser
from pages.web_browser_page import WebBrowserPage
from conftest import readPreReqJsonValue
import allure
import urllib3
from pages.actions.assertions import Assert
# from conftest import launch_TV_Application
from conftest import readConstants, updateConstantFile
import pytest


scenarios('../features/GD_validations.feature')

# this xifture not workimg
# @pytest.fixture(scope="class")
# def login_page_obj(setup_platform):
#     # driver = setup_platform
#     login_page_init = LoginPage(setup_platform)
#     return login_page_init


@given(parse("I install GD {application} from testflight for {api_version} with {build_number}"))
@allure.step('Given I install GD {application} from testflight for {api_version} with {build_number}')
def install_gd_application_from_testflight(setup_platform, request, application, api_version, build_number):
    basePage = BasePage(setup_platform)
    basePage.install_ios_application(request, readPreReqJsonValue("prereq", application), readPreReqJsonValue("prereq", api_version), readPreReqJsonValue("prereq", build_number))


@given("I launch GD Application")
@allure.step("Given I launch GD Application")
def launch_GD_application(setup_platform):
    print("Launch gd application")
    print('what is webdriver instance =====', type(setup_platform))
    basePage = BasePage(setup_platform)
    basePage.launchApp()


@then('The app load image is present')
@allure.step("Then The app load image is present")
def verify_app_load_image_visible(setup_platform):
    login_page_init = LoginPage(setup_platform).verify_launchScreen_view()
    Assert.assert_true(login_page_init, "App Launch Image is not loading")
    

@when("I am in GD  Login Page")
@allure.step("When I am in GD  Login Page")
def i_am_in_GD_login_page(setup_platform):
    isSignInHeaderDisplayed = LoginPage(setup_platform).verify_signin_header()
    if isSignInHeaderDisplayed:
        # in login page --so continue with sign i 
        print("Application is in Logout Statte")  
       
    else:
        print("Application is in Login State,So logging out ")  
        HomePage(setup_platform).click_logout_button()
        logout_text_value = LogoutPage(setup_platform).log_Out(readPreReqJsonValue("prereq", "log_out"))
        print("Logged out successfully",logout_text_value)  
        


@then("I verify Login Page BackGround image is loaded")
@allure.step("I verify Login Page BackGround image is loaded")
def i_verify_login_page_background_image_is_loaded(setup_platform):
    print("here Login Page BackGround image is loaded")
    isBGdisplayed = LoginPage(setup_platform).verify_bg_image_displayed()
    Assert.assert_true(isBGdisplayed, "Login Page BG Image is Not Displayed")


@then("I verify GD App icon is present")
@allure.step('I verify GD App icon is present')
def i_verify_GD_app_icon_is_present(setup_platform):
    print("Verifying App Icon Is Loaded In Login Page")
    isAppIconDisplayed = LoginPage(setup_platform).verify_loginPage_Icon()
    Assert.assert_true(isAppIconDisplayed, "App Icon Is Not Displayed")


@then("I verify Sign in header is present")
@allure.step("I verify Sign in header is present")
def i_verify_signin_header_is_present(setup_platform):
    print("Verifying Sign In Header Text In Login Page")
    isSignInHeaderDisplayed = LoginPage(setup_platform).verify_signin_header()
    Assert.assert_true(isSignInHeaderDisplayed, "Sign In Header Is Not Displayed In Login Page")


@then("I verify Email and Password Fields Present")
@allure.step("I verify Email and Password Fields Present")
def i_verify_email_and_password_fields_present(setup_platform):
    print("Verifying Email and Password Fields Displayed In Login Page")
    isEmailFieldDisplayed = LoginPage(setup_platform).verify_Email_text_field(readPreReqJsonValue("prereq", "email_input_text"))
    isPasswordFieldDisplayed = LoginPage(setup_platform).verify_password_text_field(readPreReqJsonValue("prereq", "password_input_text"))
    Credentials_Input = [isEmailFieldDisplayed, isPasswordFieldDisplayed]
    print(Credentials_Input)
    if all(Credentials_Input):
        print("Both Email and Password Fields Are Displayed")
    else:
        Assert.assert_fail("Both Email and Password Fields Are Not Displayed")


@then("I verify Forget Password Link is present")
@allure.step("I verify Forget Password Link is present")
def i_verify_forget_password_link(setup_platform):
    print("Verifying Forgot Password Link Text In Login Page")
    isForgotPswdLinkDisplayed = LoginPage(setup_platform).verify_forgetpassword_text_field(readPreReqJsonValue("prereq", "forgot_password_text"))
    Assert.assert_true(isForgotPswdLinkDisplayed, "Forgot Password Link Is Not Displayed In Login Page")


@then(parse("I verify Login Checkbox is present and {checbox_status} and {text}"))
@allure.step("I verify Login Checkbox is present and {checbox_status} and {text}")
def i_verify_login_checkbox_is_present_and_checked(setup_platform, checbox_status, text):
    print("Verifying Login Checkbox Is Displayed In Login Page")
    # expectedCheckBoxStatus = readPreReqJsonValue("prereq", "GD_Login_checkbox_status")
    # expectedCheckBoxText =  readPreReqJsonValue("prereq", "GD_Login_checkbox_text")
    expectedCheckBoxStatus = readPreReqJsonValue("prereq", checbox_status)
    expectedCheckBoxText =  readPreReqJsonValue("prereq", text)
    isCheckboxDisplayed = LoginPage(setup_platform).verify_signin_session_checkBox(expectedCheckBoxStatus, expectedCheckBoxText)
    print("verify_login_checkbox_is_present  ", isCheckboxDisplayed)
    Assert.assert_true(isCheckboxDisplayed, "Login Checkbox Validation  failed Login Page")


@then("I verify Sign In Button is Present")
@allure.step("Then I verify Sign In Button is Present")
def i_verify_signin_button_is_present(setup_platform):
    print("Verifying Sign In Button Displayed In Login Page")
    isSignInButtonDisplayed = LoginPage(setup_platform).check_loginbutton_visbility()
    Assert.assert_true(isSignInButtonDisplayed, "Sign In Is Not Displayed In Login Page")


@when("I click on Logout")
@allure.step("When I click on Logout")
def click_logout(setup_platform):
    print('Clicking On Logout Button')
    HomePage(setup_platform).click_logout_button()
    
@when("I click on Logout from Player")
@allure.step("When I click on Logout from Player")
def click_logout_from_player_screen(setup_platform):
    print('Clicking On Logout Button from Player')
    HomePage(setup_platform).click_logout_button_from_player()


@then("verify Loggedout successfully")
@allure.step("Then verify Loggedout successfully")
def verify_loggedout_successfully(setup_platform):
    print('Verifying If The App Got Logged Out Successfully.')
    Logout_Text = LogoutPage(setup_platform).log_Out(readPreReqJsonValue("prereq", "log_out"))
    
    Assert.assert_true(Logout_Text, "Logout Text Is Verified and Sign Out Button Is Clicked In Logout Page")



@then("Click Signout in Confirmation screen")
@allure.step("Then Click Signout in Confirmation screen")
def click_signout_in_confirmation_screen(setup_platform):
    print('Click Signout in Confirmation screen"')
    LogoutPage(setup_platform).click_logout_on_confirmation_screen()
    

@then("I verify Sign In With QR Code Button is Present")
@allure.step("Then I verify Sign In With QR Code Button is Present")
def verify_signin_withQRcode_button_is_present(setup_platform):
    print("Verifying Sign In With QR Code Button Displayed In Login Page")
    isQRSignInButtonDisplayed = LoginPage(setup_platform).check_loginbutton_QR_Code_visbility()
    Assert.assert_true(isQRSignInButtonDisplayed, "Sign In With QR Code Button Is Not Displayed In Login Page")


@then("I verify App Version is present")
@allure.step("Then I verify App Version is present")
def i_verify_appversion_value_is_present(setup_platform):
    print("Verifying App Version Is Displayed In Login Page")
    isAppVersionDisplayed = LoginPage(setup_platform).check_app_version_visibilty()
    Assert.assert_true(isAppVersionDisplayed, "App Version Is Not Displayed In Login Page")


@then("I verify Settings button is Present")
@allure.step('Then I verify Settings button is Present')
def verify_settings_button_is_present(setup_platform):
    print("Verifying Settings Button Is Displayed In Login Page")
    isSettingsButtonDisplayed = LoginPage(setup_platform).check_settings_button_visibilty()
    Assert.assert_true(isSettingsButtonDisplayed, "Settings Button Is Not Displayed In Login Page")


@when(parse("Enter {username} and {password} Credentials and Login"))
@allure.step("When I Enter username and password Credentials and Login")
def enter_login_credentials(setup_platform, username, password):
    print("Entering Login Credentials")
    loginpage = LoginPage(setup_platform)
    loginpage.do_login(readPreReqJsonValue("prereq", username), readPreReqJsonValue("prereq", password))


@when(parse('Enter {username} and {password} Credentials and Login with Non verified'))
@allure.step('When Enter username and password Credentials and Login with Non verified')
def enter_username_and_password_credentials_and_login_with_non_verified(setup_platform, username, password):
    print("Entering Login Credentials")
    if '{0}' in username:
        username = username.replace('{0}', readPreReqJsonValue("prereq", "gd_valid_user_for_invalid_scenarios"))
    loginpage = LoginPage(setup_platform)
    loginpage.do_login(readPreReqJsonValue("prereq", username), readPreReqJsonValue("prereq", password))


@when('The user clicks on the Settings button')
@allure.step("When The user clicks on the Settings button")
def verify_the_user_clicks_on_the_settings_button(setup_platform):
    print("Clicking On Setting Button")
    LoginPage(setup_platform).click_settings_button()


@when(parse('user update the {server} {server_ipad} {company_name} {API} {API_ipad} and {API_Key} key fields'))
@allure.step("When user update the server, company_name, API version and API key fields")
def user_update_the_server_company_name_and_api_key_fields(setup_platform, server, server_ipad, company_name, API, API_ipad, API_Key):  # noqa:E501
    print("Verfiying Server Text In Settings Screen")
    settingspage = SettingsPage(setup_platform)
    print("passing constant key to rereq json ===", server)
    serverValue = readPreReqJsonValue("prereq", server).format(readConstants("GD_SERVER"))
    ipad_serveer_value = readPreReqJsonValue("prereq", server_ipad).format(readConstants("GD_SERVER"))
    settingspage.set_settings_data(serverValue, ipad_serveer_value, readPreReqJsonValue("prereq", company_name), readPreReqJsonValue("prereq", API), readPreReqJsonValue("prereq", API_ipad), readPreReqJsonValue("prereq", API_Key))  # noqa:E501


@then('The fields should be updated successfully')
@allure.step('Then The fields should be updated successfully')
def verify_the_fields_should_be_updated_successfully(setup_platform):
    print("Clicking On Save Button")
    SettingsPage(setup_platform).click_savebutton()
    Setting_updation = LoginPage(setup_platform).check_app_version_visibilty()
    Assert.assert_true(Setting_updation, "Failed at updating settings configuration")


@then('Verify User Login Successfully')
@allure.step("Then Verify User Login Successfully")
def verify_user_login_successfully(setup_platform):
    print("Verifying Home Page After Login")
    isHomeScreenReached = HomePage(setup_platform).verify_home_screen_navigation()
    Assert.assert_true(isHomeScreenReached, "Login Failed After Entering Credentials")


@then(parse('Enter Credentials {errormessage} Should be Displayed'))
@allure.step("Then Enter Credentials Error Banner Should be Displayed")
def verify_enter_credentials_error_banner_should_be_displayed(setup_platform, errormessage):
    print('Verifying Enter Credentials Error Message in Login Screen')
    Error_Message = LoginPage(setup_platform).fetch_Error_Banner_Msg(readPreReqJsonValue("prereq", errormessage))
    Assert.assert_true(Error_Message, "Email Field Is Blank Error Message Is Not Displayed")


@then('Header Logo Should be Displayed on Home Screen')
@allure.step("Then Header Logo Should be Displayed on Home Screen")
def verify_header_logo_should_be_displayed_on_home_screen(setup_platform):
    print('Validating Header logo on the home screen')
    pass


@then('Each Swimlane Should Display its Respective Projects')
@allure.step("Then Each Swimlane Should Display its Respective Projects")
def verify_each_swimlane_should_display_its_respective_projects(setup_platform):
    print('Verifying project under swimlanes')
    RespectiveProjects = HomePage(setup_platform).verify_swimlanes_respective_project()
    Assert.assert_true(RespectiveProjects, "Each swimlane is not display in respective project")


@when('I close the playback')
@allure.step('I close the playback')
def close_the_playback(setup_platform):
    MediaPlayerPage(setup_platform).close_the_playback()


@then('User Should be able to Play Videos Play For the Selected Project')
@allure.step("Then User Should be able to Play Videos Play For the Selected Project")
def verify_user_should_be_able_to_play_videos_play_for_the_selected_project(setup_platform):
    print('Playing video for selected project')
    selectedvideo = HomePage(setup_platform).play_first_project_in_swimlanes()
    Assert.assert_true(selectedvideo, "User is not able to Play Videos Play For the Selected Project")


@given('reading data for json')
def reading_data_for_prereqjson(load_GD_prereq):
    value = load_GD_prereq('prereq.json', "app_pre_req_execution_id")
    print('value  from json==', value)
    pass


@then('Swimlanes Should be Displayed on the Home Screen')
@allure.step('Then Swimlanes Should be Displayed on the Home Screen')
def verify_swimlanes_displayed(setup_platform):
    print('Verifying Swimlanes on home screen')
    Swimlanes = HomePage(setup_platform).verify_swimlanes_list_in_homescreen()
    Assert.assert_true(Swimlanes, "swimlanes is not display on home screen")


@when(parse('Search for {Episodic_Project} on the HomeScreen'))
@allure.step('When I Search for Episodic Project on the HomeScreen')
def click_on_project_from_homescreen(setup_platform, Episodic_Project):
    print('Searching for the episodic project')
    SearchPage(setup_platform).enter_Text_In_Search_Field(readPreReqJsonValue("prereq", Episodic_Project))
    SearchPage(setup_platform).submit_Search_Button()
    

@then(parse('Project Information {project_synopsys} Should be Displayed'))
@allure.step('Project Information {project_synopsys} Should be Displayed')
def verify_project_information_should_be_displayed(setup_platform, project_synopsys):
    print('Validating project information details')
    SearchPage(setup_platform).click_DetailsTab_Project()
    project_Synopsis_Displayed = SearchPage(setup_platform).verify_Project_Synopsis_Information(readPreReqJsonValue("prereq", project_synopsys))
    Assert.assert_true(project_Synopsis_Displayed, "Project_Synopsis Button Is Not Displayed")


@then(parse('Project {project_cast} and {project_crew} Information Should be Displayed'))
@allure.step('Then Project Cast and Crew Information Should be Displayed')
def verify_project_cast_and_crew_information_should_be_displayed(setup_platform, project_cast, project_crew):
    print('Validating project cast and crew information')
    SearchPage(setup_platform).click_DetailsTab_Project()
    Cast_Crew_Details = SearchPage(setup_platform).verify_Cast_Crew_Title_Displayed(readPreReqJsonValue("prereq", project_cast), readPreReqJsonValue("prereq", project_crew))  # noqa:E501
    Assert.assert_true(Cast_Crew_Details, "Cast And Crew Is Not Displayed As Expected In Project Details Page")


@when('I click left activity on Roku')
@allure.step('When I click left activity on Roku')
def click_left_activity_on_roku(setup_platform):
    print('Clicking on videos tab inside project')
    SearchPage(setup_platform).roku_left()


@when(parse('Click on Project {Video_name}'))
@allure.step('When Click on Project Video')
def click_on_project_video(setup_platform, Video_name):
    print('Clicking on videos tab inside project')
    SearchPage(setup_platform).click_videos_tab_project(click_video_tab=False)
    SearchPage(setup_platform).click_OnVideoInsideProject(readPreReqJsonValue("prereq", Video_name))
    

@then('Video Information Should be Displayed')
@allure.step('Then Video Information Should be Displayed')
def verify_video_information_should_be_displayed(setup_platform):
    print('Verifying Video Information')
    video__Synopsis_Displayed = SearchPage(setup_platform).verify_Video_Synopsis_Information()
    Assert.assert_true(video__Synopsis_Displayed, "Video_Synopsis Section is not available")


@then(parse('Video {video_cast} and {video_crew} Information Should be Displayed'))
@allure.step('Then Video Cast and Crew Information Should be Displayed')
def verify_video_cast_amd_crew_Information_should_be_displayed(setup_platform, video_cast, video_crew):
    print('Verifying cast and crew details in video details page')
    Cast_Crew_Details = SearchPage(setup_platform).verify_Cast_Crew_Title_Displayed(readPreReqJsonValue("prereq", video_cast), readPreReqJsonValue("prereq", video_crew))  # noqa:E501
    Assert.assert_true(Cast_Crew_Details, "Cast And Crew Is Not Displayed As Expected In Video Details Page")


@when(parse('Click on {Episodic_Project} from Search Result'))
@allure.step('When Click on Project from Search Result')
def click_project_from_search_result(setup_platform, Episodic_Project):
    print('Clicking on project from search results')
    SearchPage(setup_platform).click_OnProjectResult(readPreReqJsonValue("prereq", Episodic_Project))


@when(parse('Click on {project_name} from Search Result'))
@allure.step('When Click on project_name from Search Result')
def click_project_from_search_result(setup_platform, Project):
    print('Clicking on project from search results')
    # SearchPage(setup_platform).submit_Search_Button()
    SearchPage(setup_platform).click_OnProjectResult(readPreReqJsonValue("prereq", Project))


@then(parse('Airdate {airdate_value} Should be Displayed on Project Information For The Selected {Video_name}'))
@allure.step('Then Airdate Should be Displayed on Project Information For The Selected Video')
def verify_airdate_should_be_displayed_on_project_information(setup_platform, airdate_value, Video_name):
    print('Verifying airdate displayed in selected project')
    SearchPage(setup_platform).click_videos_tab_project(click_video_tab=False)
    SearchPage(setup_platform).click_OnVideoInsideProject(readPreReqJsonValue("prereq", Video_name))
    Airdate_Value = SearchPage(setup_platform).verify_AirDate_Value(readPreReqJsonValue("prereq", airdate_value))
    Assert.assert_true(Airdate_Value, "Failed TO Verify Air Date Value In The Selected Project")
    

@when(parse('Search for {Non_Episodic_Project} on the HomeScreen'))
@allure.step('When Search for Non-Episodic Project on the HomeScreen')
def search_for_non_episodic_project_on_the_homescreen(setup_platform, Non_Episodic_Project):
    print('Searching for non-episodic project')
    SearchPage(setup_platform).enter_Text_In_Search_Field(readPreReqJsonValue("prereq", Non_Episodic_Project))
    print("Entered project name")
    SearchPage(setup_platform).submit_Search_Button()


@then(parse('Airdate Should not be Displayed on Project Information For The Selected {Video_name}'))
@allure.step('Then Airdate Should not be Displayed on Project Information For The Selected Video')
def verify_airdate_should_not_be_displayed_on_project_information(setup_platform, Video_name):
    print('Verifying absence of airdate in non-episodic project')
    SearchPage(setup_platform).click_videos_tab_project(click_video_tab=False)
    SearchPage(setup_platform).click_OnVideoInsideProject(readPreReqJsonValue("prereq", Video_name))
    status = SearchPage(setup_platform).airDate_Should_Not_Display()
    Assert.assert_true(status, "AirDate is displayed")


@then("I verify that the Forgot Password link is visible and clickable")
@allure.step('Then I verify that the Forgot Password link is visible and clickable')
def verify_forgot_password_link_is_visible_and_clickable(setup_platform):
    print("Verify Forgot Password Link")
    time.sleep(2)
    # unittest.TestCase().assertEqual(forgotPasswordLinkVisibility.verify_Forgot_Password_Link_isDisplayed(), True, "Forgot password Link is not present")
    forgotPasswordLinkVisibility = LoginPage(setup_platform).verify_Forgot_Password_Link_isDisplayed()
    Assert.assert_true(forgotPasswordLinkVisibility, "Forgot password Link is not present")


@when("Click on the Forgot Password link")
@allure.step('When Click on the Forgot Password link')
def click_on_forgot_password_link(setup_platform):
    print('Clicking on forgot password')
    LoginPage(setup_platform).click_Forgot_Password()
    print("Tap on Forgot password Link")


@then(parse("I navigate into Forgot Password link and validate the popup message {forgot_password_text}  and {forgot_password_popup_text}"))
@allure.step('Then I navigate into Forgot Password link and validate the popup message {forgot_password_text}  and {forgot_password_popup_text}')
def verify_naviation_to_forgot_password_link_and_validate_popup_message(setup_platform, forgot_password_text, forgot_password_popup_text):
    print('Validating forgot password popup message')
    popupHeader = LoginPage(setup_platform).verify_Forgot_Password_PopupHeader(readPreReqJsonValue("prereq", "forgot_password_text"))
    print("is poup header matching===", popupHeader)
    
    Assert.assert_true(popupHeader, "Forgot password Text is not matching with {}".format(readPreReqJsonValue("prereq", "forgot_password_text")))
    popUp = LoginPage(setup_platform).verify_Forgot_Password_Popup(readPreReqJsonValue("prereq", "forgot_password_popup_text"))
    Assert.assert_true(popUp, "Forgot password Text is not matching with {}".format(readPreReqJsonValue("prereq", "forgot_password_popup_text")))


@then("I click Go Back Button in FogotPassword popup")
@allure.step('I click Go Back Button in FogotPassword popup')
def click_go_back_button_in_forget_password_popop(setup_platform):
    LoginPage(setup_platform).click_on_forgot_password_go_back_button()
   

@when(parsers.parse('Enter incorrect {username} and {password}'))
@allure.step('When Enter incorrect username and password')
def enter_incorrect_username_and_password(setup_platform, username, password):
    print("login with invalid credetails")
    LoginPage(setup_platform).do_login(readPreReqJsonValue("prereq", username), readPreReqJsonValue("prereq", password))


@when("Click on Sign in Button")
@allure.step('When Click on Sign in Button')
def click_on_signin_button(setup_platform):
    print('Click on sign in button')
    LoginPage(setup_platform).click_sign_In()


@then(parsers.parse("I verify the appropriate error message {errormessage} is displayed"))
@allure.step('Then I verify the appropriate error message is displayed')
def verify_appropriate_error_message_is_displayed(setup_platform, errormessage):
    print('errormessage=============', errormessage)
    # print(setup_platform.page_source)
    Error_message_validation = LoginPage(setup_platform).fetch_invalid_error_message(readPreReqJsonValue("prereq", errormessage))
    Assert.assert_true(Error_message_validation, "Error message is not displayed in login page for non verified user")
    

@then(parsers.parse("I verify the appropriate error message {errormessage} {error_message_ipad} is displayed for Non verified user"))
@allure.step('Then I verify the appropriate error message is displayed for Non verified user')
def verify_appropriate_error_message_is_displayed_non_verified_user(setup_platform, errormessage, error_message_ipad):
    print('errormessage=============', errormessage)
    # print(setup_platform.page_source)
    Error_message_validation = LoginPage(setup_platform).fetch_non_verified_error_message(readPreReqJsonValue("prereq", errormessage), readPreReqJsonValue("prereq", error_message_ipad))
    Assert.assert_true(Error_message_validation, "Error message is not displayed in login page for non verified user")
       

@then("I verify that the Genres dropdown is visible")
@allure.step('Then I verify that the Genres dropdown is visible')
def Verify_Genres_Dropdown_Is_Visible(setup_platform):
    print('Verifying genre dropdown is displayed')
    Genres_Dropdown = HomePage(setup_platform).genres_Dropdown()
    Assert.assert_true(Genres_Dropdown, "Genres Dropdown Is Not Displayed In Home Page")


@when(parse("I click on {genres} dropdown"))
@allure.step('When I click on genres dropdown {genres}')
def click_on_genres_dropdown(setup_platform, genres):
    print('Clicking on genres dropdown', genres)
    Genre_Selection = HomePage(setup_platform).genres_Dropdown_Select(readPreReqJsonValue("prereq", genres))
    Assert.assert_true(Genre_Selection, "Failed To Filter Genre Under Genre Selection")
    

@then(parse("Verify all genres titles are displayed with {expected_project}"))
@allure.step('Then Verify all genres titles are displayed with {expected_project}')
def verify_all_genres_titles_are_displayed(setup_platform, expected_project):
    print('Validating selected genre contents')
    Content_Selection = HomePage(setup_platform).select_genre_content(readPreReqJsonValue("prereq", expected_project))
    print("Content_Selection in verify_all_genres_titles_are_displayed", Content_Selection)
    Assert.assert_true(Content_Selection, "Failed At Selecting Required Project Under Filtered Genres In Home Page")
    

@then("I verify that each menu item is present and visible")
@allure.step('Then I verify that each menu item is present and visible')
def verify_each_menu_item_is_present_and_visible(setup_platform):
    print("Verifying that each menu item is present and visible")
    Menu_Items = HomePage(setup_platform).verify_menu_bar()
    Assert.assert_true(Menu_Items, "Menu Bar Items Are Not Displyed")


@when("I click on help icon from the menu")
@allure.step('When Click on help icon from the menu')
def click_on_help_icon_from_the_menu(setup_platform):
    print('Clicking on help icon from the menu')
    HomePage(setup_platform).click_on_help_button()


@then("I verify the Help document is displayed")
@allure.step('Then I verify the Help document is displayed')
def verify_help_document_is_displayed(setup_platform):
    print('Verifying help document is displayed')
    Help_Document = HelpPage(setup_platform).help_page_header_verification()
    Assert.assert_true(Help_Document, "Help Document Is Not Displyed After Clicking On Help Button In Home Page")


@then(parse("I click on Help document and verify the {help_page_header},{expected_content},{browsing_shows},{selected_shows},{settings_and_features},{streaming_issues},{expecteedd_loggingout} contents"))  # noqa:E501
@allure.step('ThenI click on Help document and verify the {help_page_header} {expected_content} and {selected_shows} and {settings_and_features} and {streaming_issues} and {expecteedd_loggingout} content")')# noqa:E501
def I_click_on_Help_document(setup_platform, help_page_header, expected_content, browsing_shows, selected_shows, settings_and_features, streaming_issues, expecteedd_loggingout): # noqa:E501
    print('Verifying help content contents')
    Help_Page_Verification = HelpPage(setup_platform).help_Section_Contents(readPreReqJsonValue("prereq", expected_content), readPreReqJsonValue("prereq", browsing_shows), readPreReqJsonValue("prereq", selected_shows), readPreReqJsonValue("prereq", settings_and_features), readPreReqJsonValue("prereq", streaming_issues), readPreReqJsonValue("prereq", expecteedd_loggingout))  # noqa:E501
    Assert.assert_true(Help_Page_Verification, "Help Page Contents Are Not Displayed As Expected")
   
@when("I click on search button in home page")
@allure.step('When I Click on search button in home page')
def i_click_on_search_button_on_home_screen(setup_platform):
    print('Verifying search field')
    HomePage(setup_platform).click_on_search_button()

@when("I navigate to search result")
@allure.step('When I navigate to search result')
def i_navigate_to_search_result(setup_platform):
    print('i_navigate_to_search_result')
    HomePage(setup_platform).navigate_to_search_result()


@when("Submit the search")
@allure.step('When Submit the search')
def submit_search_button(setup_platform):
    print('Submiting the search button after entering text')
    SearchPage(setup_platform).submit_Search_Button()


@then(parse("I verify the {project_name} content of the search results"))
@allure.step('Then I verify the content of the search results')
def verify_content_of_search_results(setup_platform, project_name):
    print('Verifying search result contents')
    Search_Results = SearchPage(setup_platform).verify_Search_Content(readPreReqJsonValue("prereq", project_name))
    Assert.assert_true(Search_Results, "No Project Is Published With The Name Searched For In Search Page")
    

@then("I verify the pagination call after receiving search results")
@allure.step('Then I verify the pagination call after receiving search results')
def verify_pagination_call_after_receiving_search_results(setup_platform):
    print('Verifying pagination call after receiving search results')
    Pagination = SearchPage(setup_platform).pagination_Call_Search_Field()
    Assert.assert_true(Pagination, "Pagination Call Is Not Displayed After Receiving Search Results")


@when("Click on video tab in the project page")
@allure.step('When Click on video tab in the project page')
def click_on_video_tab_in_the_project_page(setup_platform):
    print('Clicking on video tab on project page')
    SearchPage(setup_platform).click_videos_tab_project()


@then("I verify that the correct content is displayed under the Videos tab")
@allure.step('Then I verify that the correct content is displayed under the Videos tab')
def verify_correct_content_is_displayed_under_videos_tab(setup_platform):
    print('Verifying video tab contents in project')
    video_tab_contents = SearchPage(setup_platform).verify_video_tab_contents_in_project()
    Assert.assert_true(video_tab_contents, "Expected Contents Are Not Displayed Under Videos Tab")


@then('I verify that the correct content is displayed after auto playback')
def verify_autoplayback_screen(setup_platform):
    Autoplayback = SearchPage(setup_platform).verify_auto_playback()
    Assert.assert_true(Autoplayback, "Expected contents are not displayed after autoplayback")


@when("Click on details tab in the project page")
@allure.step('When Click on details tab in the project page')
def click_on_details_tab_in_the_project_page(setup_platform):
    print('Clicking on details tab on project page')
    SearchPage(setup_platform).click_DetailsTab_Project()


@then("I verify that the correct content is displayed under the Details tab")
@allure.step('Then I verify that the correct content is displayed under the Details tab')
def verify_the_correct_content_is_displayed_under_details_tab(setup_platform):
    print('Verifying content displayed in details tab')
    Details_tab_contents = SearchPage(setup_platform).verify_details_tab_contents_in_project()
    Assert.assert_true(Details_tab_contents, "Expected Contents Are Not Displayed Under Details Tab")


@when('I click back from Roku device')
@allure.step('When I click play button')
def click_back_from_roku_device(setup_platform):
    print("Click on video play button")
    SearchPage(setup_platform).roku_back_button()    


@when(parse('Click on first {video_name} inside the project'))
@allure.step('When Click on first video inside the project')
def verify_project_details_should_be_displayed_on_project_information(setup_platform, video_name):
    print("Project should be diaplyed on project info")
    SearchPage(setup_platform).click_videos_tab_project(click_video_tab=False)
    SearchPage(setup_platform).click_OnVideoInsideProject(readPreReqJsonValue("prereq", video_name))


@then("I verify that the selected project has remaining views greater than 20")
@allure.step('Then I verify that the selected project has remaining views greater than 20')
def verify_the_selected_project_has_remaining_views_greater_than_20(setup_platform):
    print('Clicking on play button to play the video')
    Maximum_Count_Verification = SearchPage(setup_platform).maximum_Count_Video_Redirection(readPreReqJsonValue("prereq", "maximum_count"))
    Assert.assert_true(Maximum_Count_Verification, "Maximum Count For The Video Is Not Greater Than 20")


@when("I should Tap on the video with Overlay watermark")
@allure.step('When I should Tap on the video with Overlay watermark')
def click_on_videos_with_overlay_watermark(setup_platform):
    #watermark related scenario. Need to add screenshot verification.
    pass


@then("I should verify the video playing with standard watermark")
@allure.step('Then I should verify the video playing with standard watermark')
def verify_videos_playing_with_standard_watermark(setup_platform):
    #watermark related scenario. Need to add screenshot verification.
    pass


@when("I should Tap on the video with No watermark Overlay watermark")
@allure.step('When I should Tap on the video with No watermark Overlay watermark')
def click_on_videos_with_no_overlay_watermark(setup_platform):
    #watermark related scenario. Need to add screenshot verification.
    pass


@then("I should verify the video playing with No watermark")
@allure.step('Then I should verify the video playing with No watermark')
def verify_videos_playing_with_no_watermark(setup_platform):
    #watermark related scenario. Need to add screenshot verification.
    pass


@when("I navigate to the page containing the high-resolution image")
@allure.step('When I navigate to the page containing the high-resolution image')
def navigate_to_the_page_containing_high_resolution_image(setup_platform):
    #hi-res image scenario. Need to add screenshot verification.
    pass


@then("I verify that the image is visible on the page and meets the high resolution criteria")
@allure.step('Then I verify that the image is visible on the page and meets the high resolution criteria')
def verify_image_is_visible_on_page_and_meets_the_high_resolution_criteria(setup_platform):
    #hi-res image scenario. Need to add screenshot verification.
    pass


@when("I start the video playback")
@allure.step('When I start the video playback')
def start_the_video_playback(setup_platform):
    print('Playing video for the selected project')
    Start_Video_Playback = HomePage(setup_platform).play_video_for_selected_project()
    Assert.assert_true(Start_Video_Playback, "Failed To Play Video Under Selected Project")


@when("I Tap on the subtitle options menu in the video player")
@allure.step('When I Tap on the subtitle options menu in the video player')
def tap_on_subtitle_option_menu_in_video_player(setup_platform):
    print('Clicking on subtitles option')
    Subtitle_icon = MediaPlayerPage(setup_platform).click_on_settings_icon(scenario_name=None)
    Assert.assert_true(Subtitle_icon, "Failed To Click Subtitle Selection Button")


@then("I verify that multiple subtitle options are available")
@allure.step('Then I verify that multiple subtitle options are available')
def verify_multiple_subtitle_options_are_available(setup_platform):
    print('Verifying multiple subtitles displayed for the video')
    Multiple_Subtitle = MediaPlayerPage(setup_platform).verify_multiple_subtitles_displayed()
    Assert.assert_true(Multiple_Subtitle, "Multiple Subtitle Option Is Displayed")


@when(parse("I select a different {subtitle} option"))
@allure.step('When I select a different subtitle option')
def click_on_different_subtitle_options(setup_platform, subtitle):
    print('Clicking on different subtitle option in the video')
    Subtitle_Selection = MediaPlayerPage(setup_platform).click_on_different_subtitle_option(readPreReqJsonValue("prereq", subtitle))
    Assert.assert_true(Subtitle_Selection, "Different Subtitle Is Selected From Multiple Subtitle Option")
        

@then("I verify that the selected subtitle is displayed correctly during playback")
@allure.step('Then I verify that the selected subtitle is displayed correctly during playback')
def verify_selected_subtitle_displayed_as_expected_during_playback(setup_platform):
    #Screenshot shouldbe added for subtitle selection verification
    pass


@when('Page should navigates to the section where downloadable screeners are listed')
@allure.step('When Page should navigates to the section where downloadable screeners are listed')
def page_should_navigates_to_section_where_downloadable_screeners_are_listed(setup_platform):
    HomePage(setup_platform).click_on_downloads_button()
    Downloads = DownloadPage(setup_platform).verify_project_in_downloads()
    Assert.assert_true(Downloads, "No projects are displayed in downloads")


@when(parse('The user uninstalls the {application} from the device'))
@allure.step('When The user uninstalls the TV application from the device')
def user_uninstalls_the_tv_application_from_the_device(setup_platform, application):
    LoginPage(setup_platform).uninstall_the_app_in_ipad(readPreReqJsonValue("prereq", application))


@when(parse('The user re-installs the {application} on the same device'))
@allure.step('When The user re-installs the TV application on the same device')
def user_reinstalls_the_tv_application_on_the_same_device(setup_platform, application):
    App_reinstall = LoginPage(setup_platform).install_the_app_in_ipad(readPreReqJsonValue("prereq", application))
    Assert.assert_true(App_reinstall, "App is not reinstalled successfully from testflight")


@when('I play the project video')
@allure.step('When I play the project video')
def play_video_for_selected_project(setup_platform):
    print('Play a video for selected project')
    Video_Playback = HomePage(setup_platform).play_video_for_selected_project()
    print(Video_Playback)
    Assert.assert_true(Video_Playback, "Failed To Play Video With Multiple Audio Tracks Under Selected Project")


@when('I access the audio track selection options')
@allure.step('When I access the audio track selection options')
def access_audio_track_selection_options(setup_platform):
    scenario_name = "GD035 :  Verify Playback on Multiple Audio Screeners"
    print('Verifying multiple audio selection option is displayed')
    Settings_icon = MediaPlayerPage(setup_platform).click_on_settings_icon(scenario_name)
    Multiple_Audio = MediaPlayerPage(setup_platform).verify_multiple_audio_selection_displayed()
    if Settings_icon and Multiple_Audio:
        print("Settings Button Is Clicked And Audio Is Selected From List In Media Player Page")
    elif Settings_icon and not Multiple_Audio:
        Assert.assert_fail("Failed At Audio Selection After Clicking Settings Button In Media Player Page")
    else:
        Assert.assert_fail("Settings Button Is Not Selected And Failed To Access Audio Track For The Video Playback")


@when(parse('I select different {audio} tracks during playback'))
@allure.step('When I select different audio tracks during playback')
def select_different_audio_tracks_during_playback(setup_platform, audio):
    print('Selecting differenet audio track during playback')
    Audio_Selection = MediaPlayerPage(setup_platform).click_on_different_audio_option(readPreReqJsonValue("prereq", audio))
    Assert.assert_true(Audio_Selection, "Failed At Audio Selection In Media Player Page")


@when('User Selects a Project From Homescreen')
@allure.step('When User Selects a Project From Homescreen')
def user_selects_project_from_homescreen(setup_platform):
    print('Selecting project from homescreen')
    Project_Selected = HomePage(setup_platform).select_project_from_homepage()
    Assert.assert_true(Project_Selected, "Failed To Select Project From Homescreen")


@then('I verify that the screener plays correctly with the selected audio track')
@allure.step('Then I verify that the screener plays correctly with the selected audio track')
def verify_that_the_screener_plays_correctly_with_the_selected_audio_track(setup_platform):
    #Screenshot should be added for audio track verification
    pass


@when('I select the option Enter with QR CODE to log in using a URL')
@allure.step('When I select the option Enter with QR CODE to log in using a URL')
def user_selects_the_option_enter_with_qr_code_to_loin_usin_url(setup_platform):
    print('Selecting sign in with QR button in login screen')
    LoginPage(setup_platform).click_sign_in_with_qr_code_button()
    LoginPage(setup_platform).verify_qr_code_page_navigation()


@when('I copy the provided URL and opens it on a secondary device')
@allure.step("When I copy the provided URL and opens it on a secondary device")
def i_copy_the_provided_URL_and_opens_it_on_a_secondary_device(setup_platform, launchBrowser):
    print('executing I copy the provided URL and opens it on a secondary device')
    login_url_from_screen = LoginPage(setup_platform).get_login_url()
    login_access_code = LoginPage(setup_platform).login_access_code()

    print("fetched url from browser----", login_url_from_screen)
    browser = launchBrowser
   
    webBrowserPage = WebBrowserPage(browser)
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


@then(parse("I verify the successful login {message} on the secondary device"))
@allure.step("Then I verify the successful login {message} on the secondary device")
def i_verify_the_successful_login_message_on_the_secondary_device(launchBrowser, message):
    webBrowserPage = WebBrowserPage(launchBrowser)
    successful_login = webBrowserPage.successfull_Login(readPreReqJsonValue("prereq", message))
    Assert.assert_true(successful_login, "Encounted Error while Login via QR Code URL")


@then(parse("verify GD app on the primary device logs in automatically within {duration}"))
@allure.step('Then verify GD app on the primary device logs in automatically within {duration}')
def verify_GD_app_on_the_primary_device_logs_in_automatically_within_duration(setup_platform, duration):
    print('verify_GD_app_on_the_primary_device_logs_in_automatically_within_duration ')
    elementvisibilityWithinTime = HomePage(setup_platform).validate_logged_in_and_home_page_visible_within_timeframe(readPreReqJsonValue("prereq", duration))   # noqa:E501
    #page should get logout even loign duration failes
    HomePage(setup_platform).click_logout_button()
    LogoutPage(setup_platform).log_Out(readPreReqJsonValue("prereq", "log_out"))
    Assert.assert_not_none(elementvisibilityWithinTime, "App Not logged in with in {}".format(readPreReqJsonValue("prereq", duration)))


@then("I verify that the Keep me logged in checkbox is present")
@allure.step('Then I verify that the Keep me logged in checkbox is present')
def verify_keep_me_logged_in_checkbox_is_present(setup_platform):
    print('Verifying keep me logged in checkbox is present')
    LoginPage(setup_platform).verify_signin_session_checkBox(False, "logged in")


@when('Email and Password Fields Are Cleared')
@allure.step('When Email and Password Fields Are Cleared')
def email_and_password_fields_are_cleared(setup_platform):
    print('Clearing email and password field values')
    LoginPage(setup_platform).clear_email_and_password_fields()


@when('Click on Sign In With QR Code')
@allure.step("Click on Sign In With QR Code")
def click_on_sign_in_with_qr_code(setup_platform):
    print("Clicking On Sign In With QR Code")
    LoginPage(setup_platform).click_sign_in_with_qr_code_button()


@then('Verify Sign In With QR Code Page Reached')
@allure.step("Verify Sign In With QR Code Page Reached")
def verify_sign_in_with_qr_code_page_reached(setup_platform):
    print('Verifying QR Screen Page Navigation')
    QR_Page_Navigation = LoginPage(setup_platform).verify_qr_code_page_navigation()
    Assert.assert_true(QR_Page_Navigation, "Failed To Navigate Sign In With QR Code Screen")


@then('Validate QR Screen elements')
@allure.step("Validate QR Screen elements")
def validate_qr_screen_elements(setup_platform):
    print('Validating QR Screen Elements')
    QR_Screen_Url = LoginPage(setup_platform).verify_qr_screen_sign_in_url()
    QR_Screen_Code = LoginPage(setup_platform).verify_qr_screen_signin_code()
    Ready_To_Watch = LoginPage(setup_platform).verify_qr_screen_ready_to_watch()
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
    LoginPage(setup_platform).click_sign_in_with_remote()
    print("Clicked On Sign In With Remote Button")


@then('Verify Navigation To Login Page')
@allure.step("Verify Navigation To Login Page")
def verify_navigation_to_login_page(setup_platform):
    print('Verifying login page navigation')
    Login_Navigation = LoginPage(setup_platform).check_loginbutton_visbility()
    Assert.assert_true(Login_Navigation, "Login Page Navigation Failed After Clicking On Sign In With Remote Button In QR Screen")


@then('I save the changes')
@allure.step('Then I save the changes')
def save_changes(setup_platform):
    #watermark configuration in admin
    pass


@when('I navigate to the video management section')
@allure.step('When I navigate to the video management section')
def navigate_to_video_section(setup_platform):
    #watermark configuration in admin
    pass


@when('I select a video')
@allure.step('When I select a video')
def click_on_video(setup_platform):
    #watermark configuration in admin
    pass


@then('I configure the overlay playback')
@allure.step('Then I configure the overlay playback')
def select_overlay_for_playback(setup_platform):
    #watermark configuration in admin
    pass


@then('I configure the watermark not display')
@allure.step('Then I configure the watermark not display')
def select_watermark_not_display(setup_platform):
    #watermark configuration in admin
    pass


@given('I launch Admin Server')
@allure.step('Given I launch Admin Server')
def i_launch_admin_server(get_admin_server):
    # webAdminPage = AdminPortalPage(get_admin_server)
    # webAdminPage.launch_admin_webPage_url()
    pass


@when('I Login with Admin Credentails')
@allure.step('When I Login with Admin Credentails')
def i_login_with_admin_credetails(get_admin_server):
    print('Logging in with admin credentials')
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)
    admin_portal_GD_navigation.login_to_admin_portal()

# @when('I Login with "{clientUserName}" and "{internaleEmail}" and "{internalePassword}"')
# def i_login_with_clientUserName_and_internaleEmail_and_internalePassword(get_admin_server, clientUserName, internaleEmail, internalePassword):
#     admin_portal_GD_navigation = AdminPortalPage(get_admin_server)        # driver
#     admin_portal_GD_navigation.enter_text(get_admin_server, clientUserName, internaleEmail, internalePassword)


@when('I navigate to Global description portal')
@allure.step('When I navigate to Global description portal')
def i_login_with_admin_credentails(get_admin_server):
    print('Navigating to global description portal')
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)        # driver
    admin_portal_GD_navigation.navigate_To_GD_Portal()


@then('I verify by uploading the carousel image')
@allure.step('Then I verify by uploading the carousel image')
def verify_by_uploading_carosel_image(get_admin_server):
    print('Uploading the carousal image')
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)        # driver
    admin_portal_GD_navigation.upload_Image()


@then('I verify by deleting the carousel image')
@allure.step('Then I verify by deleting the carousel image')
def verify_by_deleting_carousel_image(get_admin_server):
    print('Deleting the carousal image in admin portal')
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)        # driver
    admin_portal_GD_navigation.delete_image(get_admin_server) 


@when('I navigate to projects and Add new project')
@allure.step('when I navigate to projects and Add new project')
def navigate_to_projects_and_add_new_project(get_admin_server):
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)        # driver
    admin_portal_GD_navigation.navigate_to_project_section(get_admin_server)    


@when(parse('I enter the required {Project_Name} {Description} and {Generes_Content} details'))
@allure.step('when I navigate to projects and Add new project')
def enter_the_required_project_details_and_upload_video(get_admin_server, Project_Name, Description, Generes_Content):
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)        # driver
    Project_Name_To_Publish = admin_portal_GD_navigation.enter_details_in_project_section(get_admin_server, readPreReqJsonValue("prereq", Project_Name), readPreReqJsonValue("prereq", Description), readPreReqJsonValue("prereq", Generes_Content))   
    updateConstantFile("Admin_Project_Name", Project_Name_To_Publish)   


@when(parse('I enter the required {video_name} details and upload video'))
@allure.step('when I enter the required video details and upload video')
def enter_the_required_video_details_and_upload_video(get_admin_server, video_name):
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)        # driver
    admin_portal_GD_navigation.enter_details_in_video_section(get_admin_server, readPreReqJsonValue("prereq", video_name))


@when('I navigate to send screeners and publish video')
@allure.step('when I navigate to send screeners and publish video')
def navigate_to_send_screeners_and_publish_video(get_admin_server):
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)        # driver
    admin_portal_GD_navigation.send_screeners_to_publish(get_admin_server)    


@when(parse('I search for the {Project_Name} to Unpublishing'))
@allure.step('when I search for the project to Unpublishing')
def search_for_the_project_to_unpublishing(get_admin_server, Project_Name):
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)        # driver
    admin_portal_GD_navigation.search_project_to_unpublish(get_admin_server, readConstants("Admin_Project_Name"))      


@when(parse('I navigate to the {Project_Name} to Unpublish'))
@allure.step('when I navigate to the {Project_Name} to Unpublish')
def navigate_to_the_project_to_unpublish(get_admin_server, Project_Name):
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)        # driver
    admin_portal_GD_navigation.navigate_to_project_to_unpublish(get_admin_server, readConstants("Admin_Project_Name"))  


@then(parse('I verify that the {Project_Name} is unpublished'))
@allure.step('when I verify that the project is unpublished')
def verify_that_the_project_is_unpublished(get_admin_server, Project_Name):
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)        # driver
    unpublish_verify = admin_portal_GD_navigation.verify_deleted_project(get_admin_server, readConstants("Admin_Project_Name"))    
    Assert.assert_not_none(unpublish_verify, "Project is not get unpublished")      


@when('I verify by adding swimlanes')
@allure.step('When I verify by adding swimlanes')
def verify_by_adding_swimlanes(get_admin_server):
    print('Adding swimlanes in admin portal')
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)        # driver
    project_name = readPreReqJsonValue("prereq", 'project_with_poster_and_banner') + readPreReqJsonValue("prereq", "app_pre_req_execution_id")
    admin_portal_GD_navigation.add_Swimlane(get_admin_server, readPreReqJsonValue("prereq", "new_admin_swimlane_name"), project_name)


@then('I reorder the swimlanes')
@allure.step('Then I reorder the swimlanes')
def i_login_with_admin_credentails(get_admin_server):
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)        # driver
    admin_portal_GD_navigation.reorder_Swimlanes(get_admin_server)


@then('Compare QR codes generated upon selecting Login with QR Screen button two times')
@allure.step('Then Compare QR codes generated upon selecting Login with QR Screen button two times')
def compare_qr_codes_generated_upon_selecting_login_with_qr_screen_button_two_times(setup_platform):
    print('Verifying QR code is displayed on the screen')
    Access_code_validation = LoginPage(setup_platform).compare_qr_codes_after_selecting_login_with_qr_button_two_times()
    Assert.assert_true(Access_code_validation, "QR Screen Elements are not updated after navigating back from login page twice")


@given('I launch GD URL')
@allure.step('Given I launch GD URL')
def i_login_with_admin_credentails(setup_platform):
    print("I launch the URL")
    LoginPage(setup_platform).launch_URL()


@then('The Carousel View should be visible on the screen')
@allure.step('Then The Carousel View should be visible on the screen')
def carousel_image(setup_platform):
    print("Verifying Carousel View should be visible on the screen")
    carousel_image_display = HomePage(setup_platform).verify_Carousel_view()
    Assert.assert_true(carousel_image_display, "Carousel View should not be visible on the screen")


@then('verify the header logo in the homepage screen')
@allure.step('Then verify the header logo in the homepage screen')
def verify_header_logo(setup_platform):
    print("verify header logo is displayed on the screen")
    header_logo_display = HomePage(setup_platform).verify_header_logo_in_homepage_screen()
    Assert.assert_true(header_logo_display, "verify header logo is not displayed on the screen")


@when(parse('Enter {username} and {password} Credentials with Non verified'))
@allure.step('When Enter Login Credentials with Non verified')
def enter_login_non_verified(setup_platform, username, password):
    print("Entering Non Verified Login Credentials")
    LoginPage(setup_platform).do_login(readPreReqJsonValue("prereq", username), readPreReqJsonValue("prereq", password))


@then('verify pagination call in the project listing page')
@allure.step('Then verify pagination call in the project listing page')
def verify_pagination_project_listing(setup_platform):
    print("pagination call in project listing page should verify")
    project_listing_page = HomePage(setup_platform).verify_pagination_project_listing_page()
    Assert.assert_true(project_listing_page, "pagination call in project listing page should not verify")


@given('Go to GD Application')
@allure.step("Given Go to GD Application")
def go_to_gd_application(setup_platform):
    print('what is webdriver instance =====', type(setup_platform))
    if isinstance(setup_platform, webdriver.Remote):
        print("GD Application Launched")
    else:
        time.sleep(7)
        print("GD Application Launched in roku")
        # roku_actions = RokuActions()
        # roku_actions.getActiveChannel(setup_platform)
        # time.sleep(15)
        # roku_actions.doRokuGDLogin()


@when('I play the video to the fullest')
@allure.step('When I play the video to the fullest')
def play_the_video_to_the_fullest(setup_platform):
    Video_Played = MediaPlayerPage(setup_platform).play_the_video_to_fullest()
    Assert.assert_true(Video_Played, "failed to play video completely")


@when('Click on Project Video in the project')
@allure.step('When Click on Project Video in the project')
def click_on_project_video_in_the_project(setup_platform):
    Video_navigation = SearchPage(setup_platform).click_on_start_watching_button()
    Assert.assert_true(Video_navigation, "Failed to navigate video player after clicking on start watching button")


@then('Validate QR Screen elements for 5min')
@allure.step('Then Validate QR Screen elements for 5min')
def validate_qr_screen_elements_5mins(setup_platform):
    QR_Screen = LoginPage(setup_platform).get_qr_elements_after_5mins()
    Assert.assert_true(QR_Screen, "QR elements are not updated after waiting for 5 mins in QR Screen")


@then(parse("I verify by entering a {project_name} in the Search field"))
@allure.step('Then I verify by entering a search term in the Search field')
def verify_by_entering_search_term_in_search_field(setup_platform, project_name):
    print('Entering text in search field')
    Text_Entered = SearchPage(setup_platform).enter_Text_In_Search_Field(readPreReqJsonValue("prereq", project_name))
    SearchPage(setup_platform).submit_Search_Button()
    Assert.assert_true(Text_Entered, "Search Text is not entered in search box text field")


@then('The application should automatically redirect the user to the login screen after 10min')
@allure.step('Then application automatically redirect to login page after 10min')
def application_redirect_to_loginpage_after_10min(setup_platform):
    Page_navigation = LoginPage(setup_platform).validate_login_screen_navigation_after_10mins()
    Assert.assert_true(Page_navigation, "application should not automatically redirect to login page after 10min")


@then(parse('verify old version {errormessage}'))
@allure.step('Then verify old version errormessage')
def verify_old_version_error_message(setup_platform, errormessage):
    Error_Displayed = LoginPage(setup_platform).old_version_error_messgae(readPreReqJsonValue("prereq", errormessage))
    Assert.assert_true(Error_Displayed, "Update App Error Message Is Not Displayed")


@then('Old version error message should not display')
@allure.step('Then Old version error message should not display')
def old_version_error_message_should_not_display(setup_platform):
    Error_Displayed = LoginPage(setup_platform).verify_old_version_error_message_not_display()
    Assert.assert_true(Error_Displayed, "Update App Error Message Is Displayed")


@when('testing test one')
@allure.step('When testing test one')
def testing_step_one(setup_platform):
    print("testing_step_one")
    Assert.assert_true(True, "Testing step one")


@when('testing step two')
@allure.step('When testing step two')
def testing_step_two(setup_platform):
    print("testing_step_two")
    Assert.assert_fail('Testing step two')


@when('testing step three')
@allure.step('When testing step three')
def testing_step_three(setup_platform):
    print("testing_step_three")
    Assert.assert_fail('Testing step three')


@when('testing step four')
@allure.step('When testing step four')
def testing_step_four(setup_platform):
    print("testing_step_four")
    Assert.assert_fail('Testing step four')


@when('testing step five')
@allure.step('When testing step five')
def testing_step_five(setup_platform):
    print("testing_step_five")
    Assert.assert_fail('Testing step five')


@when('testing step six')
@allure.step('When testing step six')
def testing_step_six(setup_platform):
    print("testing_step_six")
    Assert.assert_fail('Testing step six')


@when('testing step seven')
@allure.step('When testing step seven')
def testing_step_seven(setup_platform):
    print("testing_step_seven")
    Assert.assert_fail('Testing step seven')


@then('I verify Terms and condition button is Present')
@allure.step('Then I verify Terms and condition button is Present')
def i_verify_terms_and_condition_button_is_present(setup_platform):
    print('Verifying Terms and Condition button')
    Termsandcondition = LoginPage(setup_platform).verify_terms_and_service_button()
    Assert.assert_true(Termsandcondition, "Terms and Condition button is not displayed")


@when('Click on terms of service button')
@allure.step('When Click on terms of service button')
def click_on_terms_of_service(setup_platform):
    print('Clicking on Terms and Condition')
    LoginPage(setup_platform).tapping_On_Terms_Services()


@then('Verify terms of service document')
@allure.step('Then verify terms of service document')
def verify_terms_of_service_document(setup_platform):
    print('Verifying Terms Of Service Document')
    Terms_of_service = LoginPage(setup_platform).terms_Services()
    Assert.assert_true(Terms_of_service, "Terms of service document is not displayed")


@then('I navigate into Change Password popup message')
@allure.step('Then I navigate into Change Password popup message')
def verify_navigation_to_Change_password_popup_message(setup_platform):
    print('Verifying Forgot password popup message')
    Forgot_password = LoginPage(setup_platform).verify_Change_Password_PopupHeader(readPreReqJsonValue("prereq", "forgot_password_popup_message"))
    Assert.assert_true(Forgot_password, "Forgot password popup message is not displayed")


@when(parse('Enter {username} in forgot password popup message'))
@allure.step('Enter {username} in forgot password popup message')
def enter_username_in_forgot_password_popup_message(setup_platform, username):
    print('Entering username in Forgot password popup message')
    LoginPage(setup_platform).enter_username_in_forgot_password(readPreReqJsonValue("prereq", username))


@then(parse('I validate {email_sent_message} in forgot password'))
@allure.step('Then I validate email sent message in forgot password')
def validate_email_sent_message_in_forgot_password(setup_platform, email_sent_message):
    print("Verifying Email Sent Authentication message in forgot password popup message")
    Email_Sent = LoginPage(setup_platform).verify_email_sent_message_in_forgot_password(email_sent_message)
    Assert.assert_true(Email_Sent, "Email Sent Authentication message is not displayed after clicking enter button")


@when('I click on done button in forgot password')
@allure.step('When I click on done button in forgot password')
def click_on_done_button_in_forgot_password(setup_platform):
    print("Clicking on done button in forgot password")
    LoginPage(setup_platform).click_on_done_button_in_forgot_password()


@then('I verify login page navigation')
@allure.step('Then I verify login page navigation')
def verify_login_page_navigation(setup_platform):
    print("Verifying Login Page Navigation")
    Login_page = LoginPage(setup_platform).verify_signin_header()
    Assert.assert_true(Login_page, "Login Page Is Not Navigated After Clicking Done Button")


@then('Verify Sign In With QR Code Page Reached')
@allure.step("Verify Sign In With QR Code Page Reached")
def verify_sign_in_with_qr_code_page_reached(setup_platform):
    print('Verifying QR Screen Page Navigation')
    QR_Page_Navigation = LoginPage(setup_platform).verify_qr_code_page_navigation()
    Assert.assert_true(QR_Page_Navigation, "Failed To Navigate Sign In With QR Code Screen")


@then('verify Carousel image autoscroll')
@allure.step('Then verify Carousel image autoscroll')
def verify_carousel_image_autoscroll(setup_platform):
    print('verifying Autoscroll functionality of carousal image')
    Auto_Scroll = HomePage(setup_platform).verify_carousel_autoscroll_functionality()
    Assert.assert_true(Auto_Scroll, "Autoscroll of Carousel images are not displayed")


@when('Click on header logo in Homescreen')
@allure.step('When Click on header logo in Homescreen')
def click_on_header_logo_in_homescreen(setup_platform):
    print('Clicking on header logo')
    HomePage(setup_platform).click_on_header_logo()


@then('Verify navigation to top in Homescreen')
@allure.step('Then Verify navigation to top in Homescreen')
def verify_navigation_to_top_in_homescreen(setup_platform):
    print("Verifying Home Screen Navigation To Top")
    carousel_image = HomePage(setup_platform).verify_Carousel_view()
    Assert.assert_true(carousel_image, "App is not navigated to top after clicking on header logo")


@when('I click on carousel image')
@allure.step('When I click on carousel image')
def click_on_carousel_image(setup_platform):
    print('Clicking on carousel image')
    HomePage(setup_platform).click_on_carousel_image()


@then('I verify that the linked project to carousel image is loaded')
@allure.step('Then I verify that the linked project to carousel image is loaded')
def verify_that_the_linked_project_to_carousel_image_is_loaded(setup_platform):
    print('Verification of project linked to carousel image')
    Linked_project = HomePage(setup_platform).verify_linked_project_in_carousel_image()
    Assert.assert_true(Linked_project, "No Projects Are Linked To Carousel images in home page")


@when('I Click on download button')
@allure.step('When I Click on download button')
def click_on_download_button(setup_platform):
    print('Clicking on download button')
    HomePage(setup_platform).click_on_downloads_button()


@then('I verify navigation to download page')
@allure.step('Then I verify navigation to download page')
def verify_navigation_to_download_page(setup_platform):
    print('Verify Download page navigation')
    Download_page = DownloadPage(setup_platform).verify_downloads_page_header()
    Assert.assert_true(Download_page, "Download is not reached after clicking on downloads button")


@then('I verify no projects in downloads')
@allure.step('Then I verify no projects in downloads')
def verify_no_projects_in_downloads(setup_platform):
    print('Verify No projects in Download page')
    Download_page = DownloadPage(setup_platform).verify_no_downloads_message()
    Assert.assert_true(Download_page, "No projects displayed in downlaods page")


@when('I click on home button from menu')
@allure.step('When I click on home button from menu')
def click_on_home_button_from_menu(setup_platform):
    print('Clicking on download button')
    HomePage(setup_platform).click_on_home_button()


@when('I download the project video')
@allure.step('When I download the project video')
def download_the_project_video(setup_platform):
    print('Downloading project video')
    Downloading = SearchPage(setup_platform).click_on_download_button_in_video_details_page()
    Assert.assert_true(Downloading, "Project is not started to download after clicking download button in videos details page")


@then(parse('I verify {project_name} added in downloads'))
@allure.step('Then I verify project name added in downloads')
def verify_project_added_in_downloads(setup_platform, project_name):
    print('Verify projects added in Download page')
    Download_page = DownloadPage(setup_platform).verify_project_in_downloads(readPreReqJsonValue("prereq", project_name))
    Assert.assert_true(Download_page, "No projects displayed in downlaods page")


@when('I play the downloaded project')
@allure.step('When I play the downloaded project')
def play_the_downloaded_project(setup_platform):
    print('playback of downloaded videos')
    Project_playing = DownloadPage(setup_platform).play_the_downloaded_video()
    Assert.assert_true(Project_playing, "Project playback is not started playing")


@when('I select the project to delete')
@allure.step('When I select the project to delete')
def select_the_project_to_delete(setup_platform):
    print('Selecting the project to delete')
    Project_selected = DownloadPage(setup_platform).select_project_to_delete()
    Assert.assert_true(Project_selected, "Project is not selected to delete")


@when('I delete the downloaded project by clicking on confirm delete')
@allure.step('When I delete the downloaded project by clicking on confirm delete')
def delete_the_downloaded_project_by_clicking_on_confirm_delete(setup_platform):
    print('Deleting the project in downloads')
    DownloadPage(setup_platform).click_on_delete_button()
    Project_deleted = DownloadPage(setup_platform).verify_and_handle_confirm_delete_popup()
    Assert.assert_true(Project_deleted, "Project is not deleted from downloads")


@then(parse('I verify {project_name} is deleted from downloads'))
@allure.step('Then I verify project is deleted from downloads')
def verify_project_deleted_from_downloads(setup_platform, project_name):
    print('Verify projects added in Download page')
    Download_page = DownloadPage(setup_platform).verify_project_in_downloads(readPreReqJsonValue("prereq", project_name))
    Assert.assert_false(Download_page, "No projects displayed in downlaods page")


@when('I minimize the app')
@allure.step('When I minimize the app')
def minimiize_the_app(setup_platform):
    print('Minimizing the app')
    LoginPage(setup_platform).minimize_the_app()


@when(parse('I launch the {application} app'))
@allure.step('When I launch the GD application')
def launch_the_application(setup_platform, application):
    print('Relaunchiing the app')
    LoginPage(setup_platform).launch_the_app(readPreReqJsonValue("prereq", application))


@then('I verify app launches in the same screen')
@allure.step('Then I verify app launches in the same screen')
def verify_app_launches_in_the_same_screen(setup_platform):
    print('Verifying app launch in the same screen')
    Search_page = SearchPage(setup_platform).verify_search_page_reached()
    Assert.assert_true(Search_page, "App is not launched in the same screen")


@then('I verify search page is reached')
@allure.step('Then I verify search page is reached')
def verify_search_page_is_reached(setup_platform):
    print('Verifying search page is reached')
    Search_page = SearchPage(setup_platform).verify_search_page_reached()
    Assert.assert_true(Search_page, "Search page is not reached after clicking search button in menu")


@when(parse('I kill the {application} app'))
@allure.step('When I kill the GD application')
def kill_the_app(setup_platform, application):
    print('Minimizing the app')
    LoginPage(setup_platform).terminate_the_app(readPreReqJsonValue("prereq", application))


@then('I verify app launches in the homescreen')
@allure.step('Then I verify app launches in the homescreen')
def verify_search_page_is_reached(setup_platform):
    print('Verifying search page is reached')
    App_launch = HomePage(setup_platform).verify_home_screen_navigation()
    Assert.assert_true(App_launch, "App lauched successfully after killing and relaunching app")


@given('I launch Nimaad portal')
@allure.step('Given I launch Nimaad portal')
def launch_nimaad_portal(get_nimaad_server):
    # Add Your Code Here
    pass


@when('I click on view Engagement table')
@allure.step('When I click on view engagement table')
def click_on_view_engagement_table(get_nimaad_server):
    NimaadPortalPage(get_nimaad_server).click_on_view_engagement(get_nimaad_server)


@then('I verify the project view and device data')
@allure.step("Then I verify the project view and device data")
def verify_the_project_view_and_device_data(get_nimaad_server, request):
    Engagement_data = NimaadPortalPage(get_nimaad_server).verify_engagement_data(get_nimaad_server, request)
    Assert.assert_true(Engagement_data, "Engagement data is not reflecting as expected in nimaad")


@when(parse('I login with nimaad {username} and {password}'))
@allure.step('When I Enter Nimaad Login Credentials')
def login_with_nimaad_credentials(get_nimaad_server, username, password):
    NimaadPortalPage(get_nimaad_server).enter_login_credentials(readPreReqJsonValue("prereq", get_nimaad_server), readPreReqJsonValue("prereq", username), readPreReqJsonValue("prereq", password))  


@then(parse('I verify by entering a {project_name}, {project_name_ipad} in the Search field'))
@allure.step('Then I verify by eentering project name in search input field')
def verify_entering_project_name_in_search_field(setup_platform, project_name, project_name_ipad):
    print('Entering text in search field')
    print(project_name)
    print(project_name_ipad)
    Text_Entered = SearchPage(setup_platform).enter_Text_In_Search_Input_Field(readPreReqJsonValue("prereq", project_name), readPreReqJsonValue("prereq", project_name_ipad))
    SearchPage(setup_platform).submit_Search_Button()
    Assert.assert_true(Text_Entered, "Search Text is not entered in search box text field")


@then(parse('Verify deleted {swimlane} is not displayed in the app'))
@allure.step('Then Verify deleted {swimlane} is not displayed in the app')
def verify_deleted_swimlane_is_not_displayed_in_the_app(setup_platform, swimlane):
    print('Verifying swimlane deleted in the app')
    Swimlane_deleted = HomePage(setup_platform).verify_deleted_swimlane_is_not_displayed_in_app(readPreReqJsonValue("prereq", swimlane))
    Assert.assert_true(Swimlane_deleted, "App lauched successfully after killing and relaunching app")


@then('Verify unpublished project is not displayed in the app')
@allure.step('Then Verify unpublished project is not displayed in the app')
def verify_unpublished_project_is_not_displayed_in_the_app(setup_platform):
    print('Verifying swimlane deleted in the app')
    No_project = SearchPage(setup_platform).verify_no_results_in_search_page()
    Assert.assert_true(No_project, "Project is not unpublished in the admmin app")


@then(parse('Verify added {swimlane} is displayed in the app'))
@allure.step('Then Verify added swimlane is displayed in the app')
def verify_added_swimlane_is_displayed_in_the_app(setup_platform, swimlane):
    print('Verifying swimlane added in the app')
    Swimlane_added = HomePage(setup_platform).verify_added_swimlane_is_displayed_in_app(readPreReqJsonValue("prereq", swimlane))
    Assert.assert_true(Swimlane_added, "Swimlane added in admin is not reflected in the application")


@when('I verify by editing swimlanes')
@allure.step('When I verify by editing swimlanes')
def verify_by_editing_swimlanes(get_admin_server):
    print('Adding swimlanes in admin portal')
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)
    project_name = readPreReqJsonValue("prereq", 'episodic_with_poster_and_banner') + readPreReqJsonValue("prereq", "app_pre_req_execution_id")      
    admin_portal_GD_navigation.edit_swimlane(get_admin_server, project_name, readPreReqJsonValue("prereq", "fyc_admin_edited_swimlane_name"))


@then(parse('Verify edited {swimlane} is displayed in the app'))
@allure.step('Then Verify edited swimlane is displayed in the app')
def verify_edited_swimlane_is_displayed_in_the_app(setup_platform, swimlane):
    print('Verifying swimlane edited in the app')
    Swimlane_added = HomePage(setup_platform).verify_added_swimlane_is_displayed_in_app(readPreReqJsonValue("prereq", swimlane))
    Assert.assert_true(Swimlane_added, "Swimlane edited in admin is not reflected in the application")


@when('I verify by rearranging projects within swimlanes')
@allure.step('When I verify by rearranging projects within swimlanes')
def rearrange_projects_within_swimlane_in_admin(get_admin_server):
    print('Rearranging projects within swimlanes in admin portal')
    admin_FYC_navigation = AdminPortalPage(get_admin_server)     
    project_name = readPreReqJsonValue("prereq", 'episodic_with_poster_and_banner') + readPreReqJsonValue("prereq", "app_pre_req_execution_id") 
    admin_FYC_navigation.rearranging_projects_within_swimlanes(get_admin_server, project_name)


@when('I verify by rearranging swimlanes')
@allure.step('When I verify by rearranging swimlanes')
def verify_by_rearranging_swimlanes(get_admin_server):
    print('Rearrangiing swimlanes in admin portal')
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)        
    admin_portal_GD_navigation.reorder_Swimlanes(get_admin_server)


@then(parse('Verify rearranged {swimlane} is displayed in the app'))
@allure.step('Then Verify rearranged swimlane is displayed in the app')
def verify_rearranged_swimlane_is_displayed_in_the_app(setup_platform, swimlane):
    print('Verifying swimlane edited in the app')
    Swimlane_added = HomePage(setup_platform).verify_rearranged_swimlane_is_displayed_in_app(readPreReqJsonValue("prereq", swimlane))
    Assert.assert_true(Swimlane_added, "Swimlane edited in admin is not reflected in the application")


@when(parse('I search for the {Project_Name} to publish'))
@allure.step('when I search for the project to publish')
def search_for_the_project_to_publish(get_admin_server, Project_Name):
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)        # driver
    admin_portal_GD_navigation.search_project_to_publish(get_admin_server, readConstants("Admin_Project_Name"))      


@when(parse('I navigate to the {Project_Name} to publish'))
@allure.step('when I navigate to the {Project_Name} to publish')
def navigate_to_the_project_to_publish(get_admin_server, Project_Name):
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)        # driver
    admin_portal_GD_navigation.navigate_to_project_to_publish(get_admin_server, readConstants("Admin_Project_Name"))


@then(parse('I verify {projects} within swimlane is rearranged'))
@allure.step('Then I verify projects within swimlane is rearranged')
def verify_projects_within_swimlane_is_rearranged(setup_platform, projects):
    Swimlane_added = HomePage(setup_platform).verify_projects_within_swimlane_is_rearranged_in_app(readPreReqJsonValue("prereq", projects))
    Assert.assert_true(Swimlane_added, "Swimlane edited in admin is not reflected in the application")


@when('I verify by removing projects from swimlanes')
@allure.step('When I verify by removing projects from swimlanes')
def verify_by_removing_projects_from_swimlanes(get_admin_server):
    print('Rearrangiing swimlanes in admin portal')
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)     
    project_name = readPreReqJsonValue("prereq", 'episodic_with_poster_and_banner') + readPreReqJsonValue("prereq", "app_pre_req_execution_id") 
    admin_portal_GD_navigation.remove_project_from_swimlane(get_admin_server, project_name)


@when('I delete the swimlane after removing projects')
@allure.step('When I delete the swimlane after removing projects')
def delete_the_swimlane_after_removing_projects(get_admin_server):
    print('Deleting swimlanes in admin portal')
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)        
    admin_portal_GD_navigation.delete_swimlane(get_admin_server)


@when('I click on cmaf button')
@allure.step('When I click on cmaf button')
def click_on_cmaf_button(setup_platform):
    print("click unsupoted device popup")
    LoginPage(setup_platform).click_on_cmaf_button()


@when(parse('Enter {username} and {password} Credentials and Login with Non verified'))
@allure.step('When Enter username and password Credentials and Login with Non verified')
def enter_username_and_password_credentials_and_login_with_non_verified(setup_platform, username, password):
    loginpage = LoginPage(setup_platform)
    loginpage.do_login(readPreReqJsonValue("prereq", username), readPreReqJsonValue("prereq", password))    



@then(parse('I verify by uploading the carousel image {imagefile}'))
@allure.step('Then I verify by uploading the carousel image {imagefile}')
def verify_by_uploading_carosel_image(get_admin_server, imagefile):
    print('Uploading the carousal image')
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)        # driver
    admin_portal_GD_navigation.upload_Image(imagefile)


@then('I verify by deleting the carousel image')
@allure.step('Then I verify by deleting the carousel image')
def verify_by_deleting_carousel_image(get_admin_server):
    print('Deleting the carousal image in admin portal')
    admin_portal_GD_navigation = AdminPortalPage(get_admin_server)        # driver
    admin_portal_GD_navigation.delete_image(get_admin_server)




@then('verify Carousel image deleted in app')
@allure.step('Then verify Carousel image deleted in app')
def verify_carousel_image_deleted_in_app(setup_platform):
    carousel_deleted = HomePage(setup_platform).verify_carousel_image_deleted_in_admin_is_reflected_in_app()
    Assert.assert_false(carousel_deleted, "Carousel image deleted in admin is not reflected in app")


@then('verify Carousel image added in app')
@allure.step('Then verify Carousel image added in app')
def verify_carousel_image_added_in_app(setup_platform):
    carousel_added = HomePage(setup_platform).verify_carousel_image_deleted_in_admin_is_reflected_in_app()
    Assert.assert_true(carousel_added, "Carousel image deleted in admin is not reflected in app")




@when(parse('Enter {username} and {password} Credentials and Login with Non verified'))
@allure.step('When Enter username and password Credentials and Login with Non verified')
def enter_username_and_password_credentials_and_login_with_non_verified(setup_platform, username, password):
    loginpage = LoginPage(setup_platform)
    loginpage.do_login(readPreReqJsonValue("prereq", username), readPreReqJsonValue("prereq", password))


@when(parse('user update the {server} {company_name} {API} and {API_Key} key fields in roku'))
@allure.step("When user update the server, company_name, API version and API key fields")
def user_update_the_server_company_name_and_api_key_fields(setup_platform, server, company_name, API, API_Key):  # noqa:E501
    print("Verfiying Server Text In Settings Screen")
    LoginPage(setup_platform).click_settings_roku()
    settingspage = SettingsPage(setup_platform)
    print("passing constant key to rereq json ===", server)
    serverValue = readPreReqJsonValue("prereq", server).format(readConstants("GD_SERVER"))
    settingspage.set_settings_roku(serverValue, readPreReqJsonValue("prereq", company_name), readPreReqJsonValue("prereq", API), readPreReqJsonValue("prereq", API_Key))  # noqa:E501     


@then(parse("I verify by entering a {project_name} in the Search field for pulished project"))
@allure.step('Then I verify by entering a {project_name} in the Search field for pulished project')
def verify_by_entering_search_term_in_search_field_for_published_project(setup_platform, project_name):
    print('Entering text in search field')
    Text_Entered = SearchPage(setup_platform).enter_Text_In_Search_Field(readConstants("Admin_Project_Name"))
    SearchPage(setup_platform).submit_Search_Button()
    Assert.assert_true(Text_Entered, "Search Text is not entered in search box text field")


@then(parse("I verify the {project_name} content of the search results for published project"))
@allure.step('Then I verify the {project_name} content of the search results for published project')
def verify_content_of_search_results(setup_platform, project_name):
    print('Verifying search result contents')
    Search_Results = SearchPage(setup_platform).verify_Search_Content(readConstants("Admin_Project_Name"))
    Assert.assert_true(Search_Results, "No Project Is Published With The Name Searched For In Search Page")


@then(parse("I verify by entering a {project_name} in the Search field for unpublished projects"))
@allure.step('Then I verify by entering a {project_name} in the Search field for unpulished project')
def verify_by_entering_search_term_in_search_field_for_published_project(setup_platform, project_name):
    print('Entering text in search field')
    Text_Entered = SearchPage(setup_platform).enter_Text_In_Search_Field(readConstants("Admin_Project_Name"))
    # SearchPage(setup_platform).submit_Search_Button()
    Assert.assert_true(Text_Entered, "Search Text is not entered in search box text field")
