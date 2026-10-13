import time
from pytest_bdd import given, when, parsers, then, scenarios
from pytest_bdd.parsers import parse
from conftest import readConstants, updateConstantFile
from pages.base_page import BasePage
from pages.login_page_fyc import LoginPageFYC
from pages.settings_page_fyc import SettingsPageFYC
from pages.home_page_fyc import HomePageFYC
from pages.search_page_fyc import SearchPage_FYC
from pages.media_player_page_fyc import MediaPlayerPageFYC
from pages.help_page_fyc import HelpPageFYC
from pages.brand_page_fyc import BrandPageFYC
from pages.web_admin_page_fyc import AdminPortalPageFYC
from pages.web_nimaad_page import NimaadPortalPage
from pages.watchlist_fyc import WatchListPageFYC
from pages.actions.assertions import Assert
import pytest
import allure
from conftest import readPreReqJsonValue
from conftest import load_environments


scenarios('../features/FYC_validations.feature')


@given("I launch FYC App URL")
@allure.step("Given I launch FYC App URL")
def launch_FYC_app_url(page):
    """Launch FYC app URL using Playwright page fixture."""
    base_url = load_environments().get("base_url", "https://dev.example.com")
    page.goto(base_url)
    page.wait_for_selector(".//input[@name='username']")


@given("I launch Admin Server")
@allure.step("Given I launch Admin Server")
def i_launch_admin_server(page, get_admin_server):
    """Launch admin server using Playwright page."""
    webAdminPage = AdminPortalPageFYC(page)
    webAdminPage.launch_admin_webPage_url()


@when("I Login with Admin {client_email}, {internal_email} and {password} Credentails")
@allure.step("When I Login with Admin Credentails")
def i_login_with_admin_credetails(page, client_email, internal_email, password):
    """Login with admin credentials using Playwright page."""
    admin_portal_FYC_navigation = AdminPortalPageFYC(page)
    admin_portal_FYC_navigation.login_to_admin_portal(
        readPreReqJsonValue("prereq", client_email),
        readPreReqJsonValue("prereq", internal_email),
        readPreReqJsonValue("prereq", password)
    )


@given("I navigate to FYC portal")
@allure.step("When I navigate to FYC portal")
def i_navigate_to_FYC_portal(page, get_admin_server):
    """Navigate to FYC portal."""
    admin_portal_FYC_navigation = AdminPortalPageFYC(page)
    admin_portal_FYC_navigation.navigate_To_FYC_Portal(get_admin_server)


@then("I verify FYC App icon is present")
@allure.step("I verify FYC App icon is present")
def i_verify_GD_app_icon_is_present(page):
    """Verify FYC app icon is present."""
    isAppIconDisplayed = LoginPageFYC(page).verify_loginPage_Icon()
    Assert.assert_true(isAppIconDisplayed, "App Icon Is Not Displayed")


@when('I verify by uploading the carousel image')
@allure.step('When I verify by uploading the carousel image')
def adding_carousal_image_in_admin(page):
    """Upload carousel image in admin portal."""
    admin_FYC_navigation = AdminPortalPageFYC(page)
    admin_FYC_navigation.upload_carousel_Image(page)


@when('I verify by deleting the carousel image')
@allure.step('When I verify by deleting the carousel image')
def deleting_carousal_image_in_admin(page):
    """Delete carousel image in admin portal."""
    admin_FYC_navigation = AdminPortalPageFYC(page)
    admin_FYC_navigation.delete_carousel_image(page)


@when('I verify by adding swimlanes')
@allure.step('When I verify by adding swimlanes')
def adding_swimlane_in_admin(page):
    """Add swimlanes in admin portal."""
    admin_FYC_navigation = AdminPortalPageFYC(page)
    admin_FYC_navigation.add_Swimlane(
        page,
        readPreReqJsonValue("prereq", "new_admin_swimlane_name"),
        readPreReqJsonValue("prereq", "no_security_episodic_fyc01")
    )


@when('I verify by editing swimlanes')
@allure.step('When I verify by editing swimlanes')
def edit_added_swimlane_in_admin(page):
    """Edit added swimlane in admin portal."""
    admin_FYC_navigation = AdminPortalPageFYC(page)
    admin_FYC_navigation.edit_swimlane(
        page,
        readPreReqJsonValue("prereq", "fyc_admin_edited_swimlane_name"),
        readPreReqJsonValue("prereq", "no_security_episodic_fyc01")
    )


@when('I verify by rearranging projects within swimlanes')
@allure.step('When I verify by rearranging projects within swimlanes')
def rearrange_projects_within_swimlane_in_admin(page):
    """Rearrange projects within swimlanes in admin portal."""
    admin_FYC_navigation = AdminPortalPageFYC(page)
    admin_FYC_navigation.rearranging_projects_within_swimlanes(
        page,
        readPreReqJsonValue("prereq", "standard_security_nonepisodic02")
    )


@when('I verify by rearranging swimlanes')
@allure.step('When I verify by rearranging swimlanes')
def rearrange_swimlanes_in_admin(page):
    """Rearrange swimlanes in admin portal."""
    admin_FYC_navigation = AdminPortalPageFYC(page)
    admin_FYC_navigation.reorder_Swimlanes(page)


@when('I verify by removing projects from swimlanes')
@allure.step('When I verify by removing projects from swimlanes')
def remove_projects_within_swimlane_in_admin(page):
    """Remove projects from swimlanes in admin portal."""
    admin_FYC_navigation = AdminPortalPageFYC(page)
    admin_FYC_navigation.remove_project_from_swimlane(
        page,
        readPreReqJsonValue("prereq", "no_security_episodic_fyc01")
    )


@when('I delete the swimlane after removing projects')
@allure.step('When I delete the swimlane after removing projects')
def i_delete_swimlane_in_admin(page):
    """Delete swimlane in admin portal."""
    admin_FYC_navigation = AdminPortalPageFYC(page)
    admin_FYC_navigation.delete_swimlane(page)


@then("I verify Sign In With QR Code Button is Present")
@allure.step("Then I verify Sign In With QR Code Button is Present")
def verify_signin_withQRcode_button_is_present(page):
    """Verify Sign In With QR Code Button is present."""
    isQRSignInButtonDisplayed = LoginPageFYC(page).check_loginbutton_QR_Code_visbility()
    Assert.assert_true(isQRSignInButtonDisplayed, "Sign In With QR Code Button Is Not Displayed In Login Page")


@when('I navigate to the project with maximum count above 20')
@allure.step('When I navigate to the project with maximum count above 20')
def verify_Navigation_To_Project_With_Maximum_Count_Above_20(page):
    """Navigate to project with maximum count above 20."""
    Count_Verification = SearchPage_FYC(page).maximum_Count_Verification(
        readPreReqJsonValue("prereq", "episodic_project1")
    )
    Assert.assert_true(Count_Verification, "Failed At Navigation To Project With Maximum Count Above 20")


@then("I click the playback button to verify that the video starts playing")
@allure.step("Then I click the playback button to verify that the video starts playing")
def verify_video_playback_for_project_with_remaining_views_greater_than_20(page):
    """Verify video playback for project with remaining views."""
    isQRSignInButtonDisplayed = SearchPage_FYC(page).play_video_with_remaining_views_greater_than_20()
    SearchPage_FYC(page).roku_back_button()
    Assert.assert_true(isQRSignInButtonDisplayed, "Video is not played for project with remaining views greater than 20")


@when('I click on the playbutton video')
@allure.step('When I click play button')
def click_on_the_playbutton_video(page):
    """Click play button on video."""
    MediaPlayerPageFYC(page).click_on_Playnowbutton()


@when('I click back from Roku device')
@allure.step('When I click play button')
def click_back_from_roku_device(page):
    """Back button press - web equivalent."""
    # Web equivalent - go back or close current context
    page.go_back()


@when('I play the video to the fullest')
@allure.step('When I play the video to the fullest')
def play_the_video_to_the_fullest(page):
    """Play video to the fullest."""
    Video_Played = MediaPlayerPageFYC(page).play_the_video_to_fullest()
    Assert.assert_true(Video_Played, "failed to play video completely")


@then("I verify that the selected subtitle is displayed correctly during playback")
@allure.step('Then I verify that the selected subtitle is displayed correctly during playback')
def verify_selected_subtitle_displayed_as_expected_during_playback(page):
    """Verify selected subtitle displayed during playback."""
    pass  # Placeholder - subtitle verification in web context


@when('I access the audio track selection options')
@allure.step('When I access the audio track selection options')
def access_audio_track_options(page):
    """Access audio track selection options."""
    # Web equivalent - subtitle/audio selection
    pass


@then('I verify the Help document is displayed')
@allure.step('Then I verify the Help document is displayed')
def verify_help_document_is_displayed(page):
    """Verify help document is displayed."""
    Help_Document = HelpPageFYC(page).help_page_header_verification()
    Assert.assert_true(Help_Document, "Help Document Is Not Displyed After Clicking On Help Button In Home Page")


@then(parse("I click on Help document and verify the {expected_content},{browsing_shows},{selected_shows},{settings_and_features},{streaming_issues},{expecteedd_loggingout} contents"))  
@allure.step('Then I click on Help document and verify the {expected_content},{browsing_shows},{selected_shows},{settings_and_features},{streaming_issues},{expecteedd_loggingout} contents')
def I_click_on_Help_document(page, expected_content, browsing_shows, selected_shows, settings_and_features, streaming_issues, expecteedd_loggingout):  
    """Click on help document and verify contents."""
    Help_Page_Verification = HelpPageFYC(page).help_Section_Contents(
        readPreReqJsonValue("prereq", expected_content),
        readPreReqJsonValue("prereq", browsing_shows),
        readPreReqJsonValue("prereq", selected_shows),
        readPreReqJsonValue("prereq", settings_and_features),
        readPreReqJsonValue("prereq", streaming_issues),
        readPreReqJsonValue("prereq", expecteedd_loggingout)
    )
    Assert.assert_true(Help_Page_Verification, "Help Page Contents Are Not Displayed As Expected")


@then('I verify that the Search field is present and visible')
@allure.step('Then I verify that the Search field is present and visible')
def verify_search_field_is_present_and_visible(page):
    """Verify search field is present and visible."""
    search_Field = HomePageFYC(page).verify_Search_Field()
    Assert.assert_true(search_Field, "Search field Not Displayed")


@when(parse("I verify by entering a {project_name} search term in the Search field"))
@allure.step('Then I verify by entering a search term in the Search field')
def verify_by_entering_search_term_in_search_field(page, project_name):
    """Enter search term in search field."""
    fycExecution_Id = readPreReqJsonValue("prereq", "fyc_execution_id")
    project_to_search = readPreReqJsonValue("prereq", project_name) + fycExecution_Id
    HomePageFYC(page).verify_Search_Field()
    SearchPage_FYC(page).enter_Text_In_Search_Field(project_to_search)
    SearchPage_FYC(page).submit_Search_Button()


@then(parse("I validate the availability of carousal by searching using {project_name}"))
@allure.step('I validate the availability of carousal by searching using {project_name}')
def I_validate_the_availability_of_carousal_by_searching_using_carousal_name(page, project_name):
    """Validate availability of carousel by searching."""
    fetched_carousal_projects = readPreReqJsonValue("prereq", project_name)
    for project in fetched_carousal_projects:
        SearchPage_FYC(page).enter_Text_In_Search_Field(readPreReqJsonValue("prereq", project))
        SearchPage_FYC(page).submit_Search_Button()


@when(parse("I verify by entering a {project_name} search term in the Search field for admin"))
@allure.step('Then I verify by entering a search term in the Search field')
def verify_by_entering_search_term_in_search_field_for_admin(page, project_name):
    """Enter search term for admin."""
    fyc_execution_id = readPreReqJsonValue("prereq", "fyc_execution_id")
    project_to_search = readPreReqJsonValue("prereq", project_name) + fyc_execution_id
    print('Entering text in search field')
    SearchPage_FYC(page).enter_Text_In_Search_Field(project_to_search)


@when('Submit the search')
@allure.step('When Submit the search')
def submit_search_button(page):
    """Submit search button."""
    SearchPage_FYC(page).submit_Search_Button()


@then(parse("I verify the content of the search {project_name} results"))
@allure.step('Then I verify the content of the search results')
def verify_content_of_search_results(page, project_name):
    """Verify content of search results."""
    Search_Results = SearchPage_FYC(page).verify_Search_Content(readPreReqJsonValue("prereq", project_name))
    Assert.assert_true(Search_Results, "No Project Is Published With The Name Searched For In Search Page")


@then(parse("I verify the {project_name} of the search results for No security"))
@allure.step('Then I verify the content of the search results')
def verify_content_of_search_results(page, project_name):
    """Verify search results for no security."""
    Search_Results = SearchPage_FYC(page).verify_Search_Content(readPreReqJsonValue("prereq", project_name))
    Assert.assert_true(Search_Results, "No Project Is Published With The Name Searched For In Search Page")


@then(parse("I verify the {project_name} of the search results for Standard Security"))
@allure.step('Then I verify the content of the search results')
def verify_content_of_search_results_standard(page, project_name):
    """Verify search results for standard security."""
    Search_Results = SearchPage_FYC(page).verify_Search_Content(readPreReqJsonValue("prereq", project_name))
    Assert.assert_true(Search_Results, "No Project Is Published With The Name Searched For In Search Page")


@then(parse("I verify the {project_name} of the search results for Forensic Video"))
@allure.step('Then I verify the content of the search results')
def verify_content_of_search_results_forensic(page, project_name):
    """Verify search results for forensic video."""
    Search_Results = SearchPage_FYC(page).verify_Search_Content(readPreReqJsonValue("prereq", project_name))
    Assert.assert_true(Search_Results, "No Project Is Published With The Name Searched For In Search Page")


@then(parse("I verify the {project_name} of the search results for watermark Video"))
@allure.step('Then I verify the content of the search results')
def verify_content_of_search_results_watermark(page, project_name):
    """Verify search results for watermark video."""
    Search_Results = SearchPage_FYC(page).verify_Search_Content(readPreReqJsonValue("prereq", project_name))
    Assert.assert_true(Search_Results, "No Project Is Published With The Name Searched For In Search Page")


@then(parse("I verify the {project_name} of the search results for swimlanes for add,delete,update"))
@allure.step('Then I verify the content of the search results')
def verify_content_of_search_results_swimlanes_add_delete_update(page, project_name):
    """Verify search results for swimlanes operations."""
    Search_Results = SearchPage_FYC(page).verify_Search_Content(readPreReqJsonValue("prereq", project_name))
    Assert.assert_true(Search_Results, "No Project Is Published With The Name Searched For In Search Page")


@then(parse("I verify the {project_name} of the search results for swimlane"))
@allure.step('Then I verify the content of the search results')
def verify_content_of_search_results_swimlane(page, project_name):
    """Verify search results for swimlane."""
    Search_Results = SearchPage_FYC(page).verify_Search_Content(readPreReqJsonValue("prereq", project_name))
    Assert.assert_true(Search_Results, "No Project Is Published With The Name Searched For In Search Page")


@then("I verify the pagination call after receiving search results")
@allure.step('Then I verify the pagination call after receiving search results')
def verify_pagination_call_after_receiving_search_results(page):
    """Verify pagination call after receiving search results."""
    Pagination = SearchPage_FYC(page).pagination_Call_Search_Field()
    Assert.assert_true(Pagination, "Pagination Call Is Not Displayed After Receiving Search Results")


@then("I verify that the Genres dropdown is visible")
@allure.step('Then I verify that the Genres dropdown is visible')
def Verify_Genres_Dropdown_Is_Visible(page):
    """Verify genres dropdown is visible."""
    Genres_Dropdown = HomePageFYC(page).genres_Dropdown()
    Assert.assert_true(Genres_Dropdown, "Genres Dropdown Is Not Displayed In Home Page")


@when(parse("I click on {genres} dropdown"))
@allure.step('When I click on genres dropdown')
def click_on_genres_dropdown(page, genres):
    """Click on genres dropdown."""
    Genre_Selection = HomePageFYC(page).genres_Dropdown_Select(readPreReqJsonValue("prereq", genres))
    Assert.assert_true(Genre_Selection, "Failed To Filter Genre Under Genre Selection")


@then(parse("Verify all genres {project_name} titles are displayed"))
@allure.step('Then Verify all genres titles are displayed')
def verify_all_genres_titles_are_displayed(page, project_name):
    """Verify all genres titles are displayed."""
    Content_Selection = HomePageFYC(page).select_genre_content(readPreReqJsonValue("prereq", project_name))
    Assert.assert_true(Content_Selection, "Failed At Selecting Required Project Under Filtered Genres In Home Page")


@then(parse('User should be able to see {project_name} that contains entire string in the project name'))
@allure.step('Then I verify the content of the search results')
def verify_content_of_search_results(page, project_name):
    """Verify user can see project by name."""
    Search_Results = SearchPage_FYC(page).verify_Search_Content(readPreReqJsonValue("prereq", project_name))
    Assert.assert_true(Search_Results, "No Project Is Published With The Name Searched For In Search Page")


@when('I Tap on the subtitle options menu in the video player')
@allure.step('When I Tap on the subtitle options menu in the video player')
def tap_on_subtitle_option_menu_in_video_player(page):
    """Tap on subtitle options menu in video player."""
    Subtitle_icon = MediaPlayerPageFYC(page).click_on_settings_icon(scenario_name=None)
    Assert.assert_true(Subtitle_icon, "Failed To Click Subtitle Selection Button")


@then('I verify that multiple subtitle options are available')
@allure.step('Then I verify that multiple subtitle options are available')
def verify_multiple_subtitle_options_are_available(page):
    """Verify multiple subtitle options are available."""
    Multiple_Subtitle = MediaPlayerPageFYC(page).verify_multiple_subtitles_displayed()
    Assert.assert_true(Multiple_Subtitle, "Multiple Subtitle Option Is Displayed")


@when('I Click on Login with QR Screen button')
@allure.step('When I Click on Login with QR Screen button')
def click_on_login_with_qr_screen_button(page):
    """Click on login with QR screen button."""
    LoginPageFYC(page).click_sign_in_with_qr_code_button()
    QR_Screen = LoginPageFYC(page).verify_qr_code_page_navigation()
    Assert.assert_true(QR_Screen, "QR Screen Is Not Navigated After Clicking On Login With QR Button")


@then('Compare QR codes generated upon selecting Login with QR Screen button two times')
@allure.step('Then Verify QR Screen elements')
def compare_qr_codes_generated_upon_selecting_login_with_qr_screen_button_two_times(page):
    """Compare QR codes generated upon selecting login with QR screen button two times."""
    QR_Elements_Variation = LoginPageFYC(page).compare_qr_codes_after_selecting_login_with_qr_button_two_times()
    Assert.assert_true(QR_Elements_Variation, "QR Screen Elements Are Not Updated After Selecting Login With QR Screen Button Two Times")


@when('I click on sign in with remote')
@allure.step('When I Click on sign in with remote')
def click_on_sign_in_with_remote(page):
    """Click on sign in with remote."""
    LoginPageFYC(page).click_sign_in_with_remote()


@then('Verify login page navigation')
@allure.step('Then Verify login page navigation')
def verify_login_page_navigation(page):
    """Verify login page navigation."""
    Login_page = LoginPageFYC(page).verify_signin_header()
    Assert.assert_true(Login_page, "Login Page Is Not Navigated After Clicking Sign In With Remote")


@then('Verify QR Screen elements regenerated after 5mins')
@allure.step('Then Verify QR Screen elements regenerated after 5mins')
def verify_qr_screen_elements_regenerated_after_5mins(page):
    """Verify QR screen elements regenerated after 5 minutes."""
    QR_Elements_Regeneration = LoginPageFYC(page).get_qr_elements_after_5mins()
    Assert.assert_true(QR_Elements_Regeneration, "QR Screen Elements Are Not Regenerated After Waiting For 5mins In Login With QR Screen")


@then('The application should automatically redirect the user to the login screen after 10min')
@allure.step('Then The application should automatically redirect the user to the login screen after 10min')
def verify_application_should_automatically_redirect_(page):
    """Verify application auto-redirects to login screen after 10min."""
    Login_Page_navigation = LoginPageFYC(page).validate_login_screen_navigation_after_10mins()
    Assert.assert_true(Login_Page_navigation, "Login Page is Not Navigated After 10mins")


@when(parse("I select a different {subtitle} option"))
@allure.step('When I select a different subtitle option')
def click_on_different_subtitle_options(page, subtitle):
    """Click on different subtitle options."""
    Subtitle_Selection = MediaPlayerPageFYC(page).click_on_different_subtitle_options(readPreReqJsonValue("prereq", subtitle))
    Assert.assert_true(Subtitle_Selection, "Different Subtitle Is Selected From Multiple Subtitle Option")


@then('Verify header logo should not display in P&P and T&C page')
@allure.step('Then I verify that the header logo should not display in P&P and T&C page')
def verify_headerlogo_for_termsandcondition(page):
    """Verify header logo should not display in P&P and T&C page."""
    headerlogoTC = LoginPageFYC(page).terms_and_condtions_header_logo()
    Assert.assert_true(headerlogoTC, "Header logo is displayed in Terms and condition page")


@then('Verify Email Input Field Is Not Present')
@allure.step('Then Verify Email Input Field Is Not Present')
def verify_email_input_field_is_not_present(page):
    """Verify email input field is not present."""
    Email_input = LoginPageFYC(page).verify_email_input_field_is_not_displayed()
    Assert.assert_false(Email_input, "FYC application doesn't have email input field")


@when('Click on add to watchlist button')
@allure.step('When Click on add to watchlist button')
def Click_on_add_to_watchlist_button(page):
    """Click on add to watchlist button."""
    WatchListPageFYC(page).click_on_watchlist()


@when('Click on watchlist tab from menu')
@allure.step('When Click on watchlist tab from menu')
def click_on_watchlist_tab_from_menu(page):
    """Click on watchlist tab from menu."""
    WatchListPageFYC(page).watchlist_menuoption()


@then(parse('Added {project_name} should display in chronological order'))
@allure.step('Then Added {project_name} should display in chronological order')
def added_project_should_display_in_chronological_order(page, project_name):
    """Added project should display in chronological order."""
    Watchlist_added = WatchListPageFYC(page).verify_projects_are_displayed_in_chronological_list(
        readPreReqJsonValue("prereq", project_name)
    )
    Assert.assert_true(Watchlist_added, "Added project is displayed in chronological order under watchlist tab")


@when('Click on remove from watchlist button')
@allure.step('When Click on remove from watchlist button')
def click_on_remove_from_watchlist_button(page):
    """Click on remove from watchlist button."""
    WatchListPageFYC(page).Remove_watchlist()


@then(parse('Verify removed {project_name} should not display in watchlist'))
@allure.step('Then Verify removed {project_name} should not display in watchlist')
def verify_removed_project_should_not_display_in_watchlist(page, project_name):
    """Verify removed project should not display in watchlist."""
    Watchlist_removed = WatchListPageFYC(page).removed_project_shouldnot_display_watchlist(
        readPreReqJsonValue("prereq", project_name)
    )
    Assert.assert_true(Watchlist_removed, "Removed project is displayed in chronological order under watchlist tab")


@then('I verify that the header logo is displayed correctly')
@allure.step('Then I verify that the header logo is displayed correctly')
def verify_that_the_header_logo_is_displayed_correctly(page):
    """Verify that the header logo is displayed correctly."""
    headerlogohome = HomePageFYC(page).verify_header_logo_in_homepage_screen()
    Assert.assert_true(headerlogohome, "verify header logo in homepage")


@given('I launch Admin Server')
@allure.step('Given I launch Admin Server')
def i_launch_admin_server(get_admin_server):
    """Launch admin server - placeholder."""
    print('Inside Admin')
    pass


@when(parse('I Login with Admin {client_email}, {internal_email} and {password} Credentails'))
@allure.step('When I Login with Admin Credentails')
def i_login_with_admin_credetails(get_admin_server, client_email, internal_email, password):
    """Login with admin credentials."""
    print('Logging in with admin credentials')
    admin_portal_FYC_navigation = AdminPortalPageFYC(get_admin_server)
    admin_portal_FYC_navigation.login_to_admin_portal(
        readPreReqJsonValue("prereq", client_email),
        readPreReqJsonValue("prereq", internal_email),
        readPreReqJsonValue("prereq", password)
    )


@when('I navigate to FYC portal')
@allure.step('When I navigate to FYC portal')
def i_login_with_admin_credentails(get_admin_server):
    """Navigate to FYC portal."""
    print('Navigating to global description portal')
    admin_portal_FYC_navigation = AdminPortalPageFYC(get_admin_server)
    admin_portal_FYC_navigation.navigate_To_FYC_Portal(get_admin_server)


@then("I verify FYC App icon is present")
@allure.step('I verify FYC App icon is present')
def i_verify_GD_app_icon_is_present(get_admin_server):
    """Verify FYC app icon is present."""
    print("Verifying App Icon Is Loaded In Login Page")
    isAppIconDisplayed = LoginPageFYC(get_admin_server).verify_loginPage_Icon()
    Assert.assert_true(isAppIconDisplayed, "App Icon Is Not Displayed")


@when('I verify by uploading the carousel image')
@allure.step('When I verify by uploading the carousel image')
def adding_carousal_image_in_admin(get_admin_server):
    """Upload carousel image in admin portal."""
    print('Uploaing carousel image in admin portal')
    admin_FYC_navigation = AdminPortalPageFYC(get_admin_server)
    admin_FYC_navigation.upload_carousel_Image(get_admin_server)


@when('I verify by deleting the carousel image')
@allure.step('When I verify by deleting the carousel image')
def deleting_carousal_image_in_admin(get_admin_server):
    """Delete carousel image in admin portal."""
    print('Uploaing carousel image in admin portal')
    admin_FYC_navigation = AdminPortalPageFYC(get_admin_server)
    admin_FYC_navigation.delete_carousel_image(get_admin_server)


@when('I verify by adding swimlanes')
@allure.step('When I verify by adding swimlanes')
def adding_swimlane_in_admin(get_admin_server):
    """Add swimlanes in admin portal."""
    print('Adding swimlanes in admin portal')
    admin_FYC_navigation = AdminPortalPageFYC(get_admin_server)
    admin_FYC_navigation.add_Swimlane(
        get_admin_server,
        readPreReqJsonValue("prereq", "new_admin_swimlane_name"),
        readPreReqJsonValue("prereq", "no_security_episodic_fyc01")
    )


@when('I verify by editing swimlanes')
@allure.step('When I verify by editing swimlanes')
def edit_added_swimlane_in_admin(get_admin_server):
    """Edit added swimlane in admin portal."""
    print('Editing swimlanes in admin portal')
    admin_FYC_navigation = AdminPortalPageFYC(get_admin_server)
    admin_FYC_navigation.edit_swimlane(
        get_admin_server,
        readPreReqJsonValue("prereq", "fyc_admin_edited_swimlane_name"),
        readPreReqJsonValue("prereq", "no_security_episodic_fyc01")
    )


@when('I verify by rearranging projects within swimlanes')
@allure.step('When I verify by rearranging projects within swimlanes')
def rearrange_projects_within_swimlane_in_admin(get_admin_server):
    """Rearrange projects within swimlanes in admin portal."""
    print('Rearranging projects within swimlanes in admin portal')
    admin_FYC_navigation = AdminPortalPageFYC(get_admin_server)
    admin_FYC_navigation.rearranging_projects_within_swimlanes(
        get_admin_server,
        readPreReqJsonValue("prereq", "standard_security_nonepisodic02")
    )


@when('I verify by rearranging swimlanes')
@allure.step('When I verify by rearranging swimlanes')
def rearrange_swimlanes_in_admin(get_admin_server):
    """Rearrange swimlanes in admin portal."""
    print('Rearranging swimlanes in admin portal')
    admin_FYC_navigation = AdminPortalPageFYC(get_admin_server)
    admin_FYC_navigation.reorder_Swimlanes(get_admin_server)


@when('I verify by removing projects from swimlanes')
@allure.step('When I verify by removing projects from swimlanes')
def remove_projects_within_swimlane_in_admin(get_admin_server):
    """Remove projects from swimlanes in admin portal."""
    print('Removing projects from swimlanes in admin portal')
    admin_FYC_navigation = AdminPortalPageFYC(get_admin_server)
    admin_FYC_navigation.remove_project_from_swimlane(
        get_admin_server,
        readPreReqJsonValue("prereq", "no_security_episodic_fyc01")
    )


@when('I delete the swimlane after removing projects')
@allure.step('When I delete the swimlane after removing projects')
def i_login_with_admin_credentails(get_admin_server):
    """Delete swimlane in admin portal."""
    print('Deleting swimlanes in admin portal')
    admin_FYC_navigation = AdminPortalPageFYC(get_admin_server)
    admin_FYC_navigation.delete_swimlane(get_admin_server)


@then("I verify Sign In With QR Code Button is Present")
@allure.step("Then I verify Sign In With QR Code Button is Present")
def verify_signin_withQRcode_button_is_present(setup_platform):
    """Verify Sign In With QR Code Button is present."""
    print("Verifying Sign In With QR Code Button Displayed In Login Page")
    isQRSignInButtonDisplayed = LoginPageFYC(setup_platform).check_loginbutton_QR_Code_visbility()
    Assert.assert_true(isQRSignInButtonDisplayed, "Sign In With QR Code Button Is Not Displayed In Login Page")


@when("I navigate to the project with maximum count above 20")
@allure.step('When I navigate to the project with maximum count above 20')
def verify_Navigation_To_Project_With_Maximum_Count_Above_20(get_admin_server):
    """Navigate to project with maximum count above 20."""
    print('Navigating to the project with remaing views count greater than 20')
    Count_Verification = SearchPage_FYC(get_admin_server).maximum_Count_Verification(
        readPreReqJsonValue("prereq", "episodic_project1")
    )
    Assert.assert_true(Count_Verification, "Failed At Navigation To Project With Maximum Count Above 20")


@then("I click the playback button to verify that the video starts playing")
@allure.step("Then I click the playback button to verify that the video starts playing")
def verify_video_playback_for_project_with_remaining_views_greater_than_20(get_admin_server):
    """Verify video playback."""
    print("Verifying playback for video with remaining views greater than 20")
    isQRSignInButtonDisplayed = SearchPage_FYC(get_admin_server).play_video_with_remaining_views_greater_than_20()
    SearchPage_FYC(get_admin_server).roku_back_button()
    Assert.assert_true(isQRSignInButtonDisplayed, "Video is not played for project with remaining views greater than 20")


@when('click on the playbutton video')
@allure.step('When I click play button')
def click_on_the_playbutton_video(get_admin_server):
    """Click play button."""
    print("Click on video play button")
    MediaPlayerPageFYC(get_admin_server).click_on_Playnowbutton()


@when('I click back from Roku device')
@allure.step('When I click play button')
def click_back_from_roku_device(get_admin_server):
    """Click back from Roku device."""
    print("Click on video play button")
    SearchPage_FYC(get_admin_server).roku_back_button()


@when('I play the video to the fullest')
@allure.step('When I play the video to the fullest')
def play_the_video_to_the_fullest(get_admin_server):
    """Play video to the fullest."""
    print('Inside play video function')
    Video_Played = MediaPlayerPageFYC(get_admin_server).play_the_video_to_fullest()
    Assert.assert_true(Video_Played, "failed to play video completely")


@then("I verify that the selected subtitle is displayed correctly during playback")
@allure.step('Then I verify that the selected subtitle is displayed correctly during playback')
def verify_selected_subtitle_displayed_as_expected_during_playback(get_admin_server):
    """Verify selected subtitle displayed during playback."""
    pass


@when(parse("I select a different {subtitle} option"))
@allure.step('When I select a different subtitle option')
def click_on_different_subtitle_options(get_admin_server, subtitle):
    """Click on different subtitle options."""
    print('Clicking on different subtitle option in the video')
    Subtitle_Selection = MediaPlayerPageFYC(get_admin_server).click_on_different_subtitle_options(
        readPreReqJsonValue("prereq", subtitle)
    )
    Assert.assert_true(Subtitle_Selection, "Different Subtitle Is Selected From Multiple Subtitle Option")


@then('Verify header logo should not display in P&P and T&C page')
@allure.step('Then I verify that the header logo should not display in P&P and T&C page')
def verify_headerlogo_for_termsandcondition(get_admin_server):
    """Verify header logo should not display in P&P and T&C page."""
    headerlogoTC = LoginPageFYC(get_admin_server).terms_and_condtions_header_logo()
    Assert.assert_true(headerlogoTC, "Header logo is displayed in Terms and condition page")


@then('Verify Email Input Field Is Not Present')
@allure.step('Then Verify Email Input Field Is Not Present')
def verify_email_input_field_is_not_present(get_admin_server):
    """Verify email input field is not present."""
    Email_input = LoginPageFYC(get_admin_server).verify_email_input_field_is_not_displayed()
    Assert.assert_false(Email_input, "FYC application doesn't have email input field")


@when('Click on add to watchlist button')
@allure.step('When Click on add to watchlist button')
def Click_on_add_to_watchlist_button(get_admin_server):
    """Click on add to watchlist button."""
    WatchListPageFYC(get_admin_server).click_on_watchlist()


@when('Click on watchlist tab from menu')
@allure.step('When Click on watchlist tab from menu')
def click_on_watchlist_tab_from_menu(get_admin_server):
    """Click on watchlist tab from menu."""
    WatchListPageFYC(get_admin_server).watchlist_menuoption()


@then(parse('Added {project_name} should display in chronological order'))
@allure.step('Then Added {project_name} should display in chronological order')
def added_project_should_display_in_chronological_order(get_admin_server, project_name):
    """Added project should display in chronological order."""
    Watchlist_added = WatchListPageFYC(get_admin_server).verify_projects_are_displayed_in_chronological_list(
        readPreReqJsonValue("prereq", project_name)
    )
    Assert.assert_true(Watchlist_added, "Added project is displayed in chronological order under watchlist tab")


@when('Click on remove from watchlist button')
@allure.step('When Click on remove from watchlist button')
def click_on_remove_from_watchlist_button(get_admin_server):
    """Click on remove from watchlist button."""
    WatchListPageFYC(get_admin_server).Remove_watchlist()


@then(parse('Verify removed {project_name} should not display in watchlist'))
@allure.step('Then Verify removed {project_name} should not display in watchlist')
def verify_removed_project_should_not_display_in_watchlist(get_admin_server, project_name):
    """Verify removed project should not display in watchlist."""
    Watchlist_removed = WatchListPageFYC(get_admin_server).removed_project_shouldnot_display_watchlist(
        readPreReqJsonValue("prereq", project_name)
    )
    Assert.assert_true(Watchlist_removed, "Removed project is displayed in chronological order under watchlist tab")


@then('I verify that the header logo is displayed correctly')
@allure.step('Then I verify that the header logo is displayed correctly')
def verify_that_the_header_logo_is_displayed_correctly(get_admin_server):
    """Verify that the header logo is displayed correctly."""
    headerlogohome = HomePageFYC(get_admin_server).verify_header_logo_in_homepage_screen()
    Assert.assert_true(headerlogohome, "verify header logo in homepage")