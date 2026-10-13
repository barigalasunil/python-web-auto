@FYCAppValidations
Feature: FYC Sanity Feature


@FYCRegression @Adminscript @PinConfiguration @FYCipad @Healthcheck @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck
Scenario Outline:  FY000: Disable Pin Configuration In Nimaad
    Given I launch nimaad link  
    When  I login with valid <username> and <password> credentials
    And   I navigate to application configuration and search for the <pin>
    And   I select <brand> to disable <pin> configuration
    And   I disable pin configuration and save it
    Examples:
        | username        | password        | pin              | brand |
        | nimaad_username | nimaad_password | fyc_execution_id | fyc_admin_brand_selection |

@FYCRegression @FYCipad @Healthcheck 
Scenario Outline: FY001: Install Application From TestFlight
    Given  I install FYC <application> from testflight for <api_version> with <build_number>
    Examples:
        | application     | api_version                | build_number     | 
        | fyc_app_name    | fyc_api_version_to_install | fyc_build_number | 


@FYCRegression @TC-2158 @TC-2157 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCFireStick2 @Healthcheck @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1 @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY002: Update settings in the TV application
    Given I launch FYC Application
    When  I am in Login Page
    When  The user clicks on the Settings button
    When  I update the <server> <server_ipad> <company_name> <API> and <API_ipad> key fields
    Then  The fields should be updated successfully
    Examples:
        | server     | server_ipad         | company_name     | API             | API_ipad             |
        | fyc_server | fyc_server_url_ipad | fyc_company_name | fyc_API_version | fyc_API_ipad_version |


@FYCRegression @TC-2150 @TC-2151 @TC-2152 @TC-2153 @TC-2154 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @Healthcheck @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline: FY003: Launch app and validate login screen elements 
    Given I launch FYC Application
    Then  I verify The app load image is present
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    Then  I verify Login Page BackGround image is loaded
    Then  I verify FYC App icon is present
    Then  I verify Sign in header is present
    Then  I verify Access Key field is present
    Then  I verify Enter Button is Present
    Then  I verify Sign In With QR Code Button is Present
    Then  I verify terms and services is displayed
    Then  I verify Chatbox is present
    Then  I verify App Version <API> is present 
    Then  I verify Settings button is Present
    Then  I verify Keep me Login Checkbox is present and checked with <sign_in_session> text
    Examples:
        | sign_in_session   | API            | server    | company_name     | API             |               
        |  checkbox_text1 | fyc_API_version | fyc_server  | fyc_company_name | fyc_API_version |  

 

@FYCRegression @TC-2161 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY004: Verify Terms and Conditions
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    Then  I verify terms and services is displayed
    Then  I verify by tapping on Terms and services
    Then  I navigate back to login page
    Examples:
        | server      | company_name     | API             |                
        | fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegressionin @TC-2162 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY005: Verify Error Message without entering Pin
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    And   I click on the Enter button without entering a Pin
    Then  verify <errormessage>, <error_message_ipad> This field cannot be empty
    Examples:
        | errormessage                       | error_message_ipad                | server    | company_name     | API             |              
        | fyc_empty_login_input_field_error1 | fyc_empty_login_input_field_error | fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2163 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY006: Verify and Validate Login with Invalid pin
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    Then  I verify the <errormessage> on Loginpage
    Examples:
        | pin                     | errormessage          | server    | company_name     | API             |              
        | inactive_internal_token | fyc_invalid_pin_error |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2164 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY007: Verify and Validate Login with Expired pin 
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    Then  I verify expired pin <errormessage>
    Examples:
        | pin                    | errormessage          | server    | company_name     | API             |              
        | expired_internal_token | fyc_invalid_pin_error |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2168 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY008: Verify and Validate User Login Functionality
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    Then  Verify Division page is displayed    
    When  I select <brand> or <roku_brandIndex> options
    Then  Verify that the menu on the Home Page is displayed correctly
    Then  I click on Logout and verify Loggedout successfully
    Examples:
         | pin                  | brand                 | roku_brandIndex  | server    | company_name     | API             |              
         | fyc_execution_id     | fyc_brand_with_poster | 1                |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2187 @TC-2186 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY009: Verify Menu in home page and items
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    When  I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    Then  Verify that the menu on the Home Page is displayed correctly
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                  | brand                 | roku_brandIndex | server    | company_name     | API             |              
        | fyc_execution_id     | fyc_brand_with_poster | 1               |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2174 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY010: Verify Brand option functionality
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  Click on Brand icon from the menu
    Then  Verify Division page is displayed
    When  I select <brand> or <roku_brandIndex> options
    Then  Verify that the menu on the Home Page is displayed correctly
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                  | brand                 | roku_brandIndex | server    | company_name     | API             |              
        | fyc_execution_id     | fyc_brand_with_poster | 1               |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2173 @TC-2172 @TC-2171 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY011: Verify Brands in Divisions Page
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    Then  Verify Division page is displayed
    Then  Verify more than one brand name is displayed in division page
    Then  Division Header logo should display with Select a brand text label
    When  I select <brand> or <roku_brandIndex> options
    Then  Header Logo should be displayed on the top left corner of the screen
    When  I navigate to home page
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                    | brand                 | roku_brandIndex | server    | company_name     | API             |              
        | fyc_execution_id     | fyc_brand_with_poster | 1               |fyc_server  | fyc_company_name | fyc_API_version | 



@FYCRegression @TC-2199 @TC-2198 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY012: Verify the Search field in Homepage Menu bar  
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    Then  I verify the content of the search <project_name> results
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin              | brand                 | project_name                   |  roku_brandIndex | server    | company_name     | API             |              
        | fyc_execution_id | fyc_brand_with_poster | no_security_nonepisodic_fyc01  | 1                |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2200 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY013: Validate search result should displays the  project that contains entire string
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    When  Search for Project with any three characters <search_string> 
    Then  User should be able to see <project_name> that contains entire string in the project name 
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin               | brand                 | search_string     |  project_name    |  roku_brandIndex | server    | company_name     | API             |              
        | fyc_execution_id  | fyc_brand_with_poster | search_substring  |  episodic_project1  | 1             |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2203 @TC-2202 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY014: Verify Cast and crew info in Project Page and video
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    When  Click on Project <video_name>
    Then  Video Information <episode_synopsis> Should be Displayed
    Then  Video <Cast> and <Crew>, <crew_ipad> Information Should be Displayed
    Then  I click on Logout and verify Loggedout successfully
    Examples: 
        | pin               | brand                 | project_name       | Cast                 | Crew                 | roku_brandIndex | crew_ipad        | server    | company_name     | API               | episode_synopsis | video_name |          
        | fyc_execution_id  | fyc_brand_with_poster | episodic_project2  | project_crew_lengthy | project_cast_lengthy | 1              | project_cast_ipad | fyc_server  | fyc_company_name | fyc_API_version | episode_synopsis | multiple_audio_video |


@FYCRegression @TC-2178 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY015: Verify Carousel image in home page
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    Then  Carousel Image should be displayed on Top of Homepage Page
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                  | brand                 | roku_brandIndex | server    | company_name     | API             |              
        | fyc_execution_id     | fyc_brand_with_poster | 1               |  fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2181 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY016: Verify videos in Swimlanes
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    Then  Verify expected <swimlaneName> is displayed with <project_name> in the app
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                  | brand                 | roku_brandIndex  | server    | company_name     | API             | swimlaneName| project_name |         
        | fyc_execution_id     | fyc_brand_with_poster | 2                |fyc_server  | fyc_company_name | fyc_API_version | swimlane1 | no_security_nonepisodic_fyc01 |


@FYCRegression @TC-2201 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY017: Verify the Pagination call Search field  
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    Then  I verify the pagination call after receiving search results
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin              | brand                 | project_name       | roku_brandIndex | server    | company_name     | API             |              
        | fyc_execution_id | fyc_brand_with_poster | episodic_project2  | 1               |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2219 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY018: Verify and validate pagination call in the project listing page
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    Then  verify pagination call in the project listing page
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                  | brand                 | roku_brandIndex | server    | company_name     | API             |              
        | fyc_execution_id     | fyc_brand_with_poster | 1               |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2220 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY019: Verify Pagination in Screener Listing Room
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    Then  I verify that <pagination>, <poster>, <play_button>, <name>, <expiry> and <remaining_views> is displayed under the Videos tab
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                  |  brand                 | project_name        | pagination        | poster       | play_button | name | expiry | remaining_views | roku_brandIndex | server    | company_name     | API             |              
        | fyc_execution_id     |  fyc_brand_with_poster | episodic_project2   | Videos_Pagination | Video_Poster | Play_Button | Name | Expiry | Remaining_Views | 1               |fyc_server  | fyc_company_name | fyc_API_version | 
   

@FYCRegression @TC-2269 @FYCRoku @FYCFireStick @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY020: Verify login page navigation from login with QR screen after 10mins
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  I Click on Login with QR Screen button
    Then  Verify Sign In With QR Code Page Reached
    Then  The application should automatically redirect the user to the login screen after 10min
    Examples:
    | server    | company_name     | API             |              
    |fyc_server  | fyc_company_name | fyc_API_version | 
    

@FYCRegression @TC-2210 @TC-2209 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline: FY021: Verify Expiry label with date and time display
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    Then  Observe the <Expiry_label> Remaining Views on the project with date and time
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin               | brand                 | project_name      | Expiry_label    | roku_brandIndex  | server    | company_name     | API             |              
        | fyc_execution_id  | fyc_brand_with_poster | episodic_project2 | Expiry_Date_FYC | 1                 |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2206 @TC-2205 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY022: Validate Airdate Information on Episodic Content
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    Then  <Airdate> Should be Displayed on Project Information For The selected <video>
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                  |  brand                 | project_name      | Airdate       | roku_brandIndex | server    | company_name     | API              | video |
        | fyc_execution_id     |  fyc_brand_with_poster | episodic_project2 | Fyc_airdate   |   1             |fyc_server  | fyc_company_name | fyc_API_version | 5_1_audio_channel_video_s3_key |


@FYCRegression @TC-2208 @TC-2207 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY023: Validate Airdate Information No Displayed on Non-Episodic Content
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    Then  Airdate Should not be Displayed on Project Information For The selected <video>
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                  |  brand                 | project_name                    | roku_brandIndex  | server    | company_name     | API              | video |            
        | fyc_execution_id     |  fyc_brand_with_poster | no_security_nonepisodic_fyc01   | 1                |fyc_server  | fyc_company_name | fyc_API_version | Test_4k |


@FYCRegression @TC-2159 @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY024: Verify Header Logo on Privacy Policy and Terms & Conditions Pages
    Given I launch FYC Application
    When  I am in Login Page
    Then  I verify terms and services is displayed
    Then  I verify by tapping on Terms and services
    Then  I verify that the header logo should not display in P&P and T&C page
    Then  I navigate back to login page 



@FYCRegression @TC-2270 @FYCRoku @FYCFireStick @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY025: Verify Login with remote Functionality
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  I Click on Login with QR Screen button
    Then  Verify QR Screen elements
    When  I Click on sign in with remote
    Then  Verify login page navigation
    Examples:
    | server    | company_name     | API             |              
    |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2218 @TC-2217 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline: FY026: Verify Auto Playback Functionality
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    Then  <Airdate> Should be Displayed on Project Information For The selected <video>
    When  click on the playbutton video 
    When  I play the video to the fullest
    And   I click back from Roku device
    Then  I verify auto playback functionality 
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin               | brand                 | project_name      | Airdate      | roku_brandIndex  | server     | company_name     | API             | video |              
        | fyc_execution_id  | fyc_brand_with_poster | episodic_project2 | Fyc_airdate  |  1               |fyc_server  | fyc_company_name | fyc_API_version | 5_1_audio_channel_video_s3_key |


@FYCRegression @TC-2204 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY027: Verify and Validate the Details Tab on Videos Listing page
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    When  Click on details tab in the project page
    Then  I verify that the correct <project_name> <project_Description> content is displayed under the Details tab    
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                  |  brand                 | project_name      | project_Description      | roku_brandIndex  | server    | company_name     | API             |              
        | fyc_execution_id     |  fyc_brand_with_poster | episodic_project1 | project_description_data | 1               |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2223 @TC-2222 @TC-2221 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline: FY028: Verify and Validate the playback with Switching subtitle
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    And   Click on <video> inside the project
    And   click on the playbutton video
    And   I Tap on the subtitle options menu in the video player  
    Then  I verify that multiple subtitle options are available
    When  I select a different <subtitle> option
    And   I click back from Roku device
    Then  I verify that the selected subtitle is displayed correctly during playback
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully   
    # last testcase not able to take screen shot- kept pending
    Examples:
        | pin                  |  brand                 | project_name       | subtitle |  roku_brandIndex  | server    | company_name     | API              | video |          
        | fyc_execution_id     |  fyc_brand_with_poster | episodic_project2  | select_subtitle | 1          |fyc_server  | fyc_company_name | fyc_API_version | multiple_audio_video |


@FYCRegression @TC-2229 @TC-2228 @TC-2227 @TC-2226 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY029: Verify Playback on Multiple Audio Screeners
    Given  I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> <project_name_ipad> search term with multiple audio in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    When  Click on <video> inside the project
    When  click on the playbutton video
    When  I access the audio track selection options
    Then  I verify the default audio is selected
    When  I select different <audio> tracks during playback
    And   I click back from Roku device
    Then  I verify that the screener plays correctly with the selected audio track
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    #Screenshot should be added for audio track verification
    Examples:
        | pin                  |  brand                 | project_name       |  project_name_ipad  | audio               | roku_brandIndex  | server    | company_name     | API             |  video |           
        | fyc_execution_id     |  fyc_brand_with_poster | episodic_project2  |  episodic_project2  | fyc_audio_selection | 1                |fyc_server  | fyc_company_name | fyc_API_version | 5_1_audio_channel_video_s3_key |


@FYCRegression @TC-2267 @FYCRoku @FYCFireStick @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY030: Verify new QR code generated each time login with QR screen is selected
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  I Click on Login with QR Screen button
    Then  Compare QR codes generated upon selecting Login with QR Screen button two times
    Examples:
    | server    | company_name     | API             |              
    |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2268 @FYCRoku @FYCFireStick @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY031: Verify new QR code generation after 5 mins
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  I Click on Login with QR Screen button
    Then  Verify QR Screen elements regenerated after 5mins
    Examples:
    | server    | company_name     | API             |              
    |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2213 @TC-2212 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY032: Verify and Validate the maximum count in remaining views
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    And   Click on <video> inside the project
    And   I navigate to the project with maximum count above 20
    Then  I click the playback button to verify that the video starts playing  
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully 
    Examples:
        | pin                  |  brand                 | project_name         | roku_brandIndex  | server     | company_name     | API             | video |           
        | fyc_execution_id     |  fyc_brand_with_poster | episodic_project2    | 1                |fyc_server  | fyc_company_name | fyc_API_version | 5_1_audio_channel_video_s3_key |


@FYCRegression @TC-2196 @TC-2195 @TC-2194 @TC-2193 @TC-2192 @FYCRoku @FYCipad @FYCFireStick @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY033: Verify adding and removing projects in watchlist
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    When  Click on Video Tab To Add To WatchList
    And   Click on add to watchlist button
    And   Click on watchlist tab from menu
    Then  Added <project_name> should display in chronological order
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    When  Click on remove from watchlist button
    When  Click on watchlist tab from menu
    Then  Verify removed <project_name> should not display in watchlist
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                  |  brand                 | project_name  | roku_brandIndex | server    | company_name     | API             |              
        | fyc_execution_id     |  fyc_brand_with_poster | episodic_project2     | 1       |fyc_server  | fyc_company_name | fyc_API_version | 



@FYCRegression @TC-2189 @FYCRoku @FYCipad @FYCFireStick @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY034: Verify the genres dropdown in Homepage
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Genres dropdown is visible
    When  I click on <genres> dropdown
    Then  Verify all genres <project_name> titles are displayed 
    Then  I click on Logout and verify Loggedout successfully  
    Examples:
        | pin                  | brand                 | genres | project_name         | roku_brandIndex  | server    | company_name     | API             |              
        | fyc_execution_id     | fyc_brand_with_poster | project_action_genre | episodic_project2 | 1     |fyc_server  | fyc_company_name | fyc_API_version | 
        


@FYCRegression @TC-2177 @FYCipad @FYCFireStick @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY035: Verify Header Logo Functionality on iPad
    Given I launch FYC Application
    When  I am in Login Page
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the header logo is displayed correctly
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    When  I Click on header logo
    Then  I verify that the app navigates to homescreen
    Then  I click on Logout and verify Loggedout successfully    
    Examples:
        | pin                  |  brand                 | project_name                | roku_brandIndex |
        | fyc_execution_id     |  fyc_brand_with_poster | episodic_project2           | 1               |


@FYCRegression @TC-2176 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY036: Verify Header Logo
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the header logo is displayed correctly
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                  | brand                 | roku_brandIndex | server    | company_name     | API             |              
        | fyc_execution_id     | fyc_brand_with_poster | 1               |fyc_server  | fyc_company_name | fyc_API_version | 
        
@FYCRegression @TC-2155  @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY037: Verify login page doesn't have email field
    Given I launch FYC Application
    When  I am in Login Page
    Then  Verify Email Input Field Is Not Present  


@FYCRegression @TC-2230  @FYCRoku @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY038: Verify resume timestamp on the media player
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    When  Click on <video> inside the project
    When  click on the playbutton video
    And   CLick on forward and pause the playback
    Then  Verify resume timestamp on the playback 
    When  I close the media player
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin              | brand                 | project_name         | roku_brandIndex | server    | company_name     | API               | video |          
        | fyc_execution_id | fyc_brand_with_poster | episodic_project2    | 1                |fyc_server  | fyc_company_name | fyc_API_version | 5_1_audio_channel_video_s3_key |



@FYCRegression @TC-2175 @FYCRoku @FYCipad 
Scenario Outline:  FY039: Verify resume timestamp for same project on different brands
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    When  Click on <video> inside the project
    When  click on the playbutton video
    And   CLick on forward and pause the playback
    Then  Verify time left on the resume timestamp
    When  I close the media player
    When  Click on Brand icon from the menu
    When  I select different <brand_with_text> or <roku_brandIndex1> brand
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    When  Click on <video> inside the project
    When  click on the playbutton video
    And   CLick on forward and pause the playback
    Then  Verify time left on the resume timestamp updated on the different brand
    When  I close the media player 
    When  I close the playback 
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin              | brand                 | brand1          | project_name                  | roku_brandIndex | server     | company_name     | API             | brand_with_text           | roku_brandIndex1 | video |         
        | fyc_execution_id | fyc_brand_with_poster | fyc_admin_brand | no_security_nonepisodic_fyc01 | 1               |fyc_server  | fyc_company_name | fyc_API_version | fyc_admin_brand_selection | 4 | Test_4k |



@FYCRegression @TC-2242 @TC-2231 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY040: Verify By Playing Video From No Security Section
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field for admin
    When  Submit the search
    Then  I verify the <project_name> of the search results for No security
    When  Click on <project_name> from Search Result
    When  Click on <video> inside the project
    When  click on the playbutton video
    And   I click back from Roku device
    Then  I verify no watermark is displayed during playback
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully   
    # Episodic01KFPUYEPIAC
    Examples:
        | pin               |  brand                 | project_name               | roku_brandIndex | server    | company_name     | API               | video |             
        | fyc_execution_id  |  fyc_brand_with_poster | no_security_episodic_fyc01 |    1             |fyc_server  | fyc_company_name | fyc_API_version | video_name_one_usg_episodic |


@FYCRegression @TC-2156 @FYCRoku1 @FYCFireStick2 @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1 @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline:  FY041: Check if Keep me logged is enabled
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    Then  click and verify the keep me login Checkbox
    Examples:
    | server    | company_name     | API             |              
    |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2188 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick1 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck1 @FYCUnSupportedDeviceCheck1
Scenario Outline:  FY042: Verify the Help section in Homepage Menu bar
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    When  I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    When  Click on help icon from the menu
    Then  I verify the Help document is displayed 
    Then  I click on Help document and verify the <expected_content>,<browsing_shows>,<selected_shows>,<settings_and_features>,<streaming_issues>,<expecteedd_loggingout> contents
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                  | brand                 |  expected_content          | browsing_shows           | selected_shows           | settings_and_features           | streaming_issues                  | expecteedd_loggingout         |  roku_brandIndex | server    | company_name     | API             |              
        | fyc_execution_id     | fyc_brand_with_poster |help_page_expected_content  | help_page_browsing_shows_Fyc | help_page_selecting_shows| help_page_settings_and_features | help_page_solving_straming_issues | help_page_expected_loggingout | 1      |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2232 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline:  FY043: Verify By Playing Video From Standard Security Section
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field for admin
    When  Submit the search
    Then  I verify the <project_name> of the search results for Standard Security
    When  Click on <project_name> from Search Result
    When  Click on <video> inside the project
    When  click on the playbutton video
    And   I click back from Roku device
    Then  I verify standard watermark is displayed during playback
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully   
    Examples:
        | pin               |  brand                 | project_name                 | roku_brandIndex  | server    | company_name     | API             | video |             
        | fyc_execution_id  |  fyc_brand_with_poster | standard_security_episodic01 |    1             |fyc_server  | fyc_company_name | fyc_API_version | 5_1_audio_channel_video_s3_key |


@FYCRegression @TC-2241 @TC-2234 @TC-2233 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick2 @FYCSupportedDeviceCheck @FYCSupportedDeviceCheck2
Scenario Outline:  FY044: Verify Forensic Video is working as expected and watermark
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field for admin
    When  Submit the search
    Then  I verify the <project_name> of the search results for Forensic Video
    When  Click on <project_name> from Search Result
    When  Click on <video> inside the project
    When  click on the playbutton video
    And   I click back from Roku device
    Then  I verify forensic watermark is displayed during playback
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    #AB_Security_episodic01": Episodic05
    Examples:
        | pin               |  brand                 | project_name           | roku_brandIndex | server    | company_name     | API             |  video |            
        | fyc_execution_id  |  fyc_brand_with_poster | AB_Security_episodic01 | 1                |fyc_server  | fyc_company_name | fyc_API_version | Test_4k |


@FYCRegression @TC-2240 @TC-2235 @FYCRoku @FYCFireStick @FYCipad @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline:  FY045: Verify Appearance of watermark throughout the video
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field for admin
    When  Submit the search
    Then  I verify the <project_name> of the search results for watermark Video
    When  Click on <project_name> from Search Result
    When  Click on <video> inside the project
    When  click on the playbutton video
    And   I click back from Roku device
    Then  I verify standard watermark is displayed during playback
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    # standard_security_nonepisodic06": "NonEpisodic09"
    Examples:
        | pin               |  brand                 | project_name            | roku_brandIndex  | server    | company_name     | API             | video |             
        | fyc_execution_id  |  fyc_brand_with_poster | standard_security_nonepisodic06 |    1     |fyc_server  | fyc_company_name | fyc_API_version | 5_1_audio_channel_video_s3_key |

    
@FYCRegression @TC-2245 @FYCRoku @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCSupportedDeviceCheck2 
Scenario Outline: FY046: Verify castlabs video with subtitle playback
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field for admin
    When  Submit the search
    When  Click on <project_name> from Search Result
    When  Click on <video> inside the project
    When  click on the playbutton video
    And   I Tap on the subtitle options menu in the video player  
    Then  I verify that multiple subtitle options are available
    When  I select a different <subtitle> option
    And   I click back from Roku device
    Then  I verify that the selected subtitle is displayed correctly during playback 
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully  
    # last testcase not able to take screen shot- kept pending
    Examples:
        | pin                  | brand                 |  project_name              | subtitle |     roku_brandIndex   | server    | company_name     | API             |  video |            
        | fyc_execution_id     | fyc_brand_with_poster | AB_Security_nonepisodic01  | french_subtitle |  1              |fyc_server  | fyc_company_name | fyc_API_version | Test_4k |



@FYCRegression @TC-2243 @FYCRoku @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCSupportedDeviceCheck2 
Scenario Outline: FY047: Verify castlabs on video playback
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    When  Click on <video> inside the project
    When  click on the playbutton video
    And   I click back from Roku device
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                  |  brand                 | project_name       |   roku_brandIndex    | server    | company_name     | API             |  video |           
        | fyc_execution_id     |  fyc_brand_with_poster | AB_Security_nonepisodic01  | 1            |fyc_server  | fyc_company_name | fyc_API_version | Test_4k |


@FYCRegression @TC-2244 @FYCRoku @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline:  FY048: Verify castlabs multiple audio video playback
    Given  I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> <project_name_ipad> search term with multiple audio in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    When  Click on <video> inside the project
    When  click on the playbutton video
    When  I access the audio track selection options
    Then  I verify the default audio is selected
    When  I select different <audio> tracks during playback
    Then  I verify that the screener plays correctly with the selected audio track
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    # Screenshot should be added for audio track verification
    Examples:
        | pin                  | brand                 |  project_name       | project_name_ipad | audio |    roku_brandIndex  | server    | company_name     | API             |   video |         
        | fyc_execution_id     | fyc_brand_with_poster |  episodic_project2  | episodic_project2 | fyc_audio_selection | 1      |fyc_server  | fyc_company_name | fyc_API_version | 5_1_audio_channel_video_s3_key |


@FYCRegression @FYCRoku @FYCipad 
Scenario Outline:  FY049: Verify partial watermark at intended intervals
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field for admin
    When  Submit the search
    Then  I verify the <project_name> of the search results for watermark Video
    When  Click on <project_name> from Search Result
    When  Click on <video> inside the project
    When  click on the playbutton video
    And   I click back from Roku device
    Then  I verify partial watermark is displayed during playback
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin               | brand                 |  project_name            | roku_brandIndex | server    | company_name     | API             |   video |           
        | fyc_execution_id  | fyc_brand_with_poster |  standard_security_episodic03 | 1           |fyc_server  | fyc_company_name | fyc_API_version | 5_1_audio_channel_video_s3_key |
    
 
@FYCRegression @TC-2239 @FYCRoku @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCSupportedDeviceCheck2 
Scenario Outline:  FY050: Verify overlay, no security and forensiic screeners in the same guild
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <overlay_project_name> <no_security_project_name> <forensic_project_name> different projects in the Search field for admin
    When  Click on <forensic_project_name> from Search Result
    When  Click on <video> inside the project
    When  click on the playbutton video
    And   I click back from Roku device
    Then  verify playback in media player
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin               | brand                 | overlay_project_name         | no_security_project_name   | forensic_project_name     | roku_brandIndex | server    | company_name     | API             |   video |          
        | fyc_execution_id  | fyc_brand_with_poster | standard_security_episodic03 | no_security_episodic_fyc01 | AB_Security_nonepisodic01 |  1               |fyc_server  | fyc_company_name | fyc_API_version | Test_4k |


@FYCRegression @TC-2250 @FYCipad 
Scenario Outline:  FY051: Verify Minimizing and Launching the App
    Given I launch FYC Application
    When  I am in Login Page
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    When  Click on Brand icon from the menu
    Then  Verify Division page is displayed 
    When  Minimize the application
    When  ReLaunch the <application>
    Then  Verify app launches in the same page  
    When  I select <brand> or <roku_brandIndex> options
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                 | brand                 | application   | roku_brandIndex |
        | fyc_execution_id    | fyc_brand_with_poster | FYC_bundle_ID | 1 |


@FYCRegression @TC-2251 @FYCipad 
Scenario Outline:  FY052: Verify Killing and Relaunching the App
    Given I launch FYC Application
    When  I am in Login Page
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  Click on Brand icon from the menu
    Then  Verify Division page is displayed 
    When  Close the <application> completely
    When  ReLaunch the <application>
    Then  Verify app launches in the same page
    When  I select <brand> or <roku_brandIndex> options
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                 | brand                 | application   | roku_brandIndex |
        | fyc_execution_id    | fyc_brand_with_poster | FYC_bundle_ID | 1 |


@FYCRegression @TC-2165 @FYCRoku @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY053: Verify that the application enforces the minimum version requirement.
    Given I launch FYC Application
    When  I am in Login Page
    When  The user clicks on the Settings button
    When  I update the <server> <server_ipad> <company_name> <API_old> and <API_ipad_old> key fields
    Then  The fields should be updated successfully
    Then  verify old version <errormessage>
    When  The user clicks on the Settings button
    When  I update the <server> <server_ipad> <company_name> <API_new> and <API_ipad_new> key fields
    Then  The fields should be updated successfully
    Then  Old version error message should not display <errormessage>
    Examples:
        | server     | server_ipad         | company_name       | API_old                | API_ipad_old               | API_new           | API_ipad_new         | errormessage                  |
        | fyc_server | fyc_server_url_ipad | fyc_company_name   | fyc_API_old_version    | fyc_API_old_version        | fyc_API_version   | fyc_API_ipad_version | fyc_old_version_error_message |


@FYCRegression @TC-2215 @FYCRoku @NimaadScript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline:  FY054: Verify the resume playback disable field in Nimaad
    Given I launch nimaad link  
    When  I login with valid <username> and <password> credentials
    And   I navigate to Watch product section   
    Then  I disable resume playback and verify the watchlist is disabled
    Given I launch FYC Application
    When  I am in Login Page
    When  The user clicks on the Settings button
    When  I update the <server> <server_ipad> <company_name> <API> and <API_ipad> key fields
    Then  The fields should be updated successfully
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    Then  Verify remaining views should be less than or equal to 20
    When  Click on <video> inside the project
    When  click on the playbutton video 
    And   CLick on forward and pause the playback
    When  I close the media player
    When  I close the playback
    Then  Verify resume playback is not displayed in the videos details page
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username        | password        | pin                     | server     | server_ipad         | company_name     | API             | API_ipad             | project_name        | brand                 |  roku_brandIndex | video |
        | nimaad_username | nimaad_password | fyc_token_with_20_views | fyc_server | fyc_server_url_ipad | fyc_company_name | fyc_API_version | fyc_API_ipad_version | episodic_project3   | fyc_brand_with_poster |  1               | 5_1_audio_channel_video_s3_key |


@FYCRegression @TC-2214 @FYCRoku1 @NimaadScript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline:  FY055: Verify the resume playback enable field in Nimaad
    Given I launch nimaad link  
    When  I login with valid <username> and <password> credentials
    And   I navigate to Watch product section   
    Then  I enable resume playback and verify the watchlist is enabled
    Given I launch FYC Application
    When  I am in Login Page
    When  The user clicks on the Settings button
    When  I update the <server> <server_ipad> <company_name> <API> and <API_ipad> key fields
    Then  The fields should be updated successfully
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    Then  Verify remaining views should be less than or equal to 20
    When  Click on <video> inside the project
    When  click on the playbutton video 
    And   CLick on forward and pause the playback
    When  I close the media player
    When  I close the playback
    Then  Verify resume playback is displayed in the videos details page
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username        | password        | pin              | server     | server_ipad         | company_name     | API             | API_ipad             | project_name                | brand                 | roku_brandIndex | video |
        | nimaad_username | nimaad_password | fyc_token_with_20_views | fyc_server | fyc_server_url_ipad | fyc_company_name | fyc_API_version | fyc_API_ipad_version | episodic_project3    | fyc_brand_with_poster |  1 | 5_1_audio_channel_video_s3_key |

  
@FYCRegression @TC-2166 @NimaadScript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline:  FY056: Update API key Expiry date in nimaad and verify the API error message in FYC app
    Given I launch nimaad link  
    When  I login with valid <username> and <password> credentials
    And   I navigate to API Key section   
    And   I navigate to API Key for Validation
    Then  I modify the <expiry_date> and verify the updated Date 
    Given I launch FYC Application
    When  I am in Login Page
    When  The user clicks on the Settings button
    When  I update the <server> <server_ipad> <company_name> <API> and <API_ipad> key fields
    Then  The fields should be updated successfully
    When  Enter <pin> in Login page
    And   I click on the Enter button
    Then  I verify API failure <API_error_message> is displayed
    Examples:
        | username        | password        | pin              | server     | server_ipad         | company_name     | API             | API_ipad             | API_error_message     | expiry_date         |
        | nimaad_username | nimaad_password | fyc_execution_id | fyc_server | fyc_server_url_ipad | fyc_company_name | fyc_API_version | fyc_API_ipad_version | fyc_api_error_message | fyc_api_expiry_date |


@FYCRegression @TC-2166 @FYCRoku @NimaadScript 
Scenario Outline:  FY057: Update API key Expiry date in nimaad and verify the API error message in FYC app for roku
    Given I launch nimaad link  
    When  I login with valid <username> and <password> credentials
    And   I navigate to API Key section   
    And   I navigate to API Key for Validation
    Then  I modify the <expiry_date> and verify the updated Date 
    Given I launch FYC Application
    When  I am in Login Page
    When  The user clicks on the Settings button
    When  I update the <server> <server_ipad> <company_name> <API> and <API_ipad> key fields
    Then  The fields should be updated successfully
    When  Enter <pin> in Login page
    And   I click on the Enter button
    Then  I verify API failure <API_error_message> is displayed
    Examples:
        | username        | password        | pin              | server     | server_ipad         | company_name     | API             | API_ipad             | API_error_message     | expiry_date         |
        | nimaad_username | nimaad_password | fyc_execution_id | fyc_server | fyc_server_url_ipad | fyc_company_name | fyc_API_version | fyc_API_ipad_version | fyc_api_error_message | fyc_api_expiry_date |


@FYCRegression @TC-2167 @NimaadScript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline:  FY058: Delete API key in nimaad and verify the API error message in FYC app
    Given I launch nimaad link  
    When  I login with valid <username> and <password> credentials
    And   I navigate to API Key section   
    And   I navigate to API Key for Validation 
    And   I delete the API key in nimaad
    Given I launch FYC Application
    When  I am in Login Page
    When  The user clicks on the Settings button
    When  I update the <server> <server_ipad> <company_name> <API> and <API_ipad> key fields
    Then  The fields should be updated successfully
    When  Enter <pin> in Login page
    And   I click on the Enter button
    Then  I verify API failure <API_error_message> is displayed
    Given I launch nimaad link  
    #When  I login with valid <username> and <password> credentials
    When   I navigate to API Key section 
    And   I click on add API key  
    And   I add new API key and save it
    Examples:
        | username        | password        | pin              | server     | server_ipad         | company_name     | API             | API_ipad             | API_error_message |
        | nimaad_username | nimaad_password | fyc_execution_id | fyc_server | fyc_server_url_ipad | fyc_company_name | fyc_API_version | fyc_API_ipad_version | fyc_api_error_message |


@FYCRegression @TC-2167 @FYCRoku @NimaadScript 
Scenario Outline:  FY059: Delete API key in nimaad and verify the API error message in FYC app for roku
    Given I launch nimaad link  
    When  I login with valid <username> and <password> credentials
    And   I navigate to API Key section   
    And   I navigate to API Key for Validation 
    And   I delete the API key in nimaad
    Given I launch FYC Application
    When  I am in Login Page
    When  The user clicks on the Settings button
    When  I update the <server> <server_ipad> <company_name> <API> and <API_ipad> key fields
    Then  I verify API failure <API_error_message> is displayed
    Given I launch nimaad link  
    When   I navigate to API Key section 
    And   I click on add API key  
    And   I add new API key and save it
    Examples:
        | username        | password        | server     | server_ipad         | company_name     | API             | API_ipad             | API_error_message |
        | nimaad_username | nimaad_password | fyc_server | fyc_server_url_ipad | fyc_company_name | fyc_API_version | fyc_API_ipad_version | fyc_api_error_message |


@FYCRegression @TC-2191 @FYCRoku @NimaadScript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline:  FY060: Verify the watchlist disable field in Nimaad
    Given I launch nimaad link  
    When  I login with valid <username> and <password> credentials
    And   I navigate to Watch product section   
    Then  I disable watchlist and verify the watchlist is disabled 
    Given I launch FYC Application
    When  I am in Login Page
    When  The user clicks on the Settings button in Loginpage
    When  I update the <server> <server_ipad> <company_name> <API> and <API_ipad> key fields
    Then  The fields should be updated successfully
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  Verify that the WatchList on the Home Page is not displayed
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username        | password        | pin              | server     | server_ipad         | company_name     | API             | API_ipad             | brand                 |  roku_brandIndex |
        | nimaad_username | nimaad_password | fyc_execution_id | fyc_server | fyc_server_url_ipad | fyc_company_name | fyc_API_version | fyc_API_ipad_version | fyc_brand_with_poster |  1 |


@FYCRegression @TC-2190 @FYCRoku @NimaadScript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline:  FY061: Verify the watchlist enable field in Nimaad
    Given I launch nimaad link  
    When  I login with valid <username> and <password> credentials
    And   I navigate to Watch product section   
    Then  I enable watchlist and verify the watchlist is enabled
    Given I launch FYC Application
    When  I am in Login Page
    When  The user clicks on the Settings button in Loginpage
    When  I update the <server> <server_ipad> <company_name> <API> and <API_ipad> key fields
    Then  The fields should be updated successfully
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  Verify that the WatchList on the Home Page is displayed
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username        | password        | pin              | server     | server_ipad         | company_name     | API             | API_ipad             | brand                 | roku_brandIndex |
        | nimaad_username | nimaad_password | fyc_execution_id | fyc_server | fyc_server_url_ipad | fyc_company_name | fyc_API_version | fyc_API_ipad_version | fyc_brand_with_poster | 1|


@FYCRegression @TC-2259 @FYCRoku @NimaadScript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY062: Verify view enagagement data recorded on playback
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    When  Click on <video> inside the project
    And   click on the playbutton video
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Given I launch nimaad link  
    When  I login with valid <username> and <password> credentials
    When  I click on view Engagement table
    Then  I verify the project view and device data
    Examples:
      | pin                  | brand                 |  project_name       | username        | password        | roku_brandIndex | server     | company_name     | API             | video |          
      | fyc_execution_id     | fyc_brand_with_poster |  episodic_project2  | nimaad_username | nimaad_password | 1               | fyc_server | fyc_company_name | fyc_API_version | 5_1_audio_channel_video_s3_key |


@FYCRegression @TC-2253 @FYCipad 
Scenario Outline:  FY063: Verify playback after uninstalling and reinstalling latest app from the testflight
    Given I launch FYC Application
    When  I am in Login Page
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    When  The user uninstalls the <application> from the device
    When  The user re-installs the <application> on the same device
    Given I launch FYC Application
    When  I am in Login Page
    When  The user clicks on the Settings button
    When  I update the <server> <server_ipad> <company_name> <API> and <API_ipad> key fields
    Then  The fields should be updated successfully
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    When  Click on <video> inside the project
    When  click on the playbutton video
    Then  verify playback in media player
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Given  I install FYC <application_name> from testflight for <api_version> with <build_number>
    When  The user clicks on the Settings button
    When  I update the <server> <server_ipad> <company_name> <API> and <API_ipad> key fields
    Then  The fields should be updated successfully
    Examples:
        | pin                | brand                 | application   | server     | server_ipad         | company_name     | API             | API_ipad             | project_name | roku_brandIndex | video                 | application_name     | api_version                | build_number     | 
        | fyc_execution_id   | fyc_brand_with_poster | FYC_bundle_ID | fyc_server | fyc_server_url_ipad | fyc_company_name | fyc_API_version | fyc_API_ipad_version | episodic_project2 | 1 | 5_1_audio_channel_video_s3_key | fyc_app_name         | fyc_api_version_to_install | fyc_build_number | 


@FYCRegression @TC-2252 @FYCipad 
Scenario Outline:  FY064: Verify playback after updating app from the testflight
    Given I launch Testflight application
    When  I am in Testflight app
    When  I install previous build application from testflight
    When  Launch the installed <application>
    Then  I verify app launch in previous build
    When  I update the <application> from testflight
    Given I launch FYC Application
    When  I am in Login Page
    When  The user clicks on the Settings button
    When  I update the <server> <server_ipad> <company_name> <API> and <API_ipad> key fields
    Then  The fields should be updated successfully
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    When  Click on <video> inside the project
    When  click on the playbutton video
    Then  verify playback in media player
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Given  I install FYC <application_name> from testflight for <api_version> with <build_number>
    When  The user clicks on the Settings button
    When  I update the <server> <server_ipad> <company_name> <API> and <API_ipad> key fields
    Then  The fields should be updated successfully
    Examples:
        | pin              | brand                 | application   | server     | server_ipad         | company_name     | API             | API_ipad             | project_name | roku_brandIndex | video                 | application_name     | api_version                | build_number     | 
        | fyc_execution_id | fyc_brand_with_poster | FYC_bundle_ID | fyc_server | fyc_server_url_ipad | fyc_company_name | fyc_API_version | fyc_API_ipad_version | episodic_project2 | 1 | 5_1_audio_channel_video_s3_key | fyc_app_name         | fyc_api_version_to_install | fyc_build_number | 


@FYCRegression
Scenario Outline:  FY064:  verify carousel image in prereq json file
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    And   I select <brand> options
    Then  I verify that the Search field is present and visible
    Then  I validate the availability of carousal by searching using <project_name>
    When  I verify by entering a <project_name> search term in the Search field for admin
    When  Submit the search
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin               |  brand                 | project_name   |
        | fyc_execution_id  |  fyc_brand_with_poster | carousel_image1 |


@FYCRegression @TC-2254 @NimaadScript @FYCFireStick @FYCFireStick2 @FYCUnSupportedDeviceCheck @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY065: Verify cmaf error banner in login page and playback of forensic video for unsupported devices
    Given I launch nimaad link  
    When  I login with valid <username> and <password> credentials
    When  I click on unsupported devices
    When  I add the device under unsupported devices
    Given  I launch FYC Application
    When  I am in Login Page
    When  Enter <pin> in Login page
    And   I click on the Enter button
    Then  I verify Unsupported device error banner is displayed
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    When  Click on <video> inside the project
    And   click on the playbutton video
    Then  I verify Unsupported device error banner is displayed in forensic playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                  | brand                 |  project_name            | username        | password        | roku_brandIndex | video |
        | fyc_execution_id     | fyc_brand_with_poster |  AB_Security_episodic01  | nimaad_username | nimaad_password | 1             | Test_4k |


@FYCRegression @TC-2255 @NimaadScript @FYCFireStick2 @FYCUnSupportedDeviceCheck @FYCUnSupportedDeviceCheck2 
Scenario Outline:  FY066: Verify cmaf error banner is displayed in login page and not in playback of overlay video for unsupported devices
    Given I launch nimaad link  
    When  I login with valid <username> and <password> credentials
    When  I click on unsupported devices
    When  I add the device under unsupported devices
    Given  I launch FYC Application
    When  I am in Login Page
    When  Enter <pin> in Login page
    And   I click on the Enter button
    Then  I verify Unsupported device error banner is displayed
    When  I click on cmaf button
    And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    When  Click on <video> inside the project
    And   click on the playbutton video
    Then  I verify Unsupported device error banner is not displayed in overlay playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                  | brand                 |  project_name               | username        | password        | roku_brandIndex | video |
        | fyc_execution_id     | fyc_brand_with_poster |  AB_Security_nonepisodic01  | nimaad_username | nimaad_password | 1               | Test_4k |


@FYCRegression @TC-2257 @TC-2256 @NimaadScript @FYCFireStick2 @FYCSupportedDeviceCheck @FYCSupportedDeviceCheck2 
Scenario Outline:  FY067: Verify cmaf error banner is not displayed in login page and playback of forensic video for supported devices
    Given I launch nimaad link  
    When  I login with valid <username> and <password> credentials
    When  I click on unsupported devices
    When  I delete the device from unsupported devices
    Given  I launch FYC Application
    When  I am in Login Page
    When  Enter <pin> in Login page
    And   I click on the Enter button
    Then  I verify Unsupported device error banner is not displayed
    When  I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    When  Click on <video> inside the project
    And   click on the playbutton video
    Then  I verify Unsupported device error banner is not displayed in forensic playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                  | brand                 |  project_name            | username        | password        | roku_brandIndex | video |
        | fyc_execution_id     | fyc_brand_with_poster |  AB_Security_episodic01  | nimaad_username | nimaad_password | 1               | Test_4k |


@FYCRegression @TC-2258 @NimaadScript @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCSupportedDeviceCheck2 
Scenario Outline:  FY068: Verify cmaf error banner is not displayed in login page and playback of overlay video for supported devices
    Given I launch nimaad link  
    When  I login with valid <username> and <password> credentials
    When  I click on unsupported devices
    When  I delete the device from unsupported devices
    Given  I launch FYC Application
    When  I am in Login Page
    When  Enter <pin> in Login page
    And   I click on the Enter button
    Then  I verify Unsupported device error banner is not displayed
    When  I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    When  Click on <video> inside the project
    And   click on the playbutton video
    Then  I verify Unsupported device error banner is not displayed in overlay playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                  | brand                 |  project_name            | username        | password        | roku_brandIndex | video |
        | fyc_execution_id     | fyc_brand_with_poster |  AB_Security_episodic01  | nimaad_username | nimaad_password | 1               | Test_4k |


@FYCRegression @Adminscript @PinConfiguration @FYCFireStick @FYCFireStick2 @FYCipad @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline:  FY069: Enable Pin Configuration In Nimaad
    Given I launch nimaad link  
    When  I login with valid <username> and <password> credentials
    And   I navigate to application configuration and search for the <pin>
    And   I select <brand> to enable <pin> configuration
    And   I enable pin configuration and save it
    Examples:
        | username        | password        | pin              | brand |
        | nimaad_username | nimaad_password | fyc_execution_id | fyc_admin_brand_selection |


@FYCRegression @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY070: Verify adding the project videos to publish
    Given I launch Admin Server
    When  I Login with Admin <client_email>, <internal_email> and <password> Credentails
    And   I navigate to projects and Add new project
    And   I enter the required <Project_Name>, <Description> and <Generes_Content> details 
    And   I enter the required <video_name> details and upload video
    Examples:
        | Project_Name                | video_name                | Description              | Generes_Content       | client_email | internal_email | password      |
        | fyc_project_name_to_publish | fyc_video_name_to_publish | project_description_data | project_action_genre  | clientemail  | internalemail  | adminpassword |


@FYCRegression @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY071: Verify adding the project videos to delete
    Given I launch Admin Server
    When  I Login with Admin <client_email>, <internal_email> and <password> Credentails
    And   I navigate to projects and Add new project
    And   I enter the required <Project_Name>, <Description> and <Generes_Content> details for deleting video
    And   I enter the required <video_name> details and upload video
    Examples:
        | Project_Name             | video_name                | Description              | Generes_Content      | client_email | internal_email | password      |  
        | fyc_admin_project_name_2 | fyc_video_name_to_publish | project_description_data | project_action_genre | clientemail  | internalemail  | adminpassword |  


@FYCRegression @TC-2182 @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY072: verify adding swimlanes on admin 
    Given I launch Admin Server
    When  I Login with Admin <client_email>, <internal_email> and <password> Credentails
    And   I navigate to FYC portal
    And   I verify by adding swimlanes
    Examples:
        | client_email | internal_email | password      |         
        | clientemail  | internalemail  | adminpassword |  


@FYCRegression @TC-2182 @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY073: verify added swimlane in FYCApp
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    #And   I select <brand> or <roku_brandIndex> options
    Then  Verify added <swimlane> is displayed in the app
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin              | brand           | swimlane          | roku_brandIndex | server    | company_name     | API             |              
        | fyc_execution_id | fyc_admin_brand | new_admin_swimlane_name | 2          |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2182 @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY074: verify editing swimlanes on admin 
    Given I launch Admin Server
    When  I Login with Admin <client_email>, <internal_email> and <password> Credentails
    And   I navigate to FYC portal
    And   I verify by editing swimlanes
    Examples:
        | client_email | internal_email | password      |         
        | clientemail  | internalemail  | adminpassword |  


@FYCRegression @TC-2182 @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY075: verify editing swimlane in FYCApp
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    #And   I select <brand> or <roku_brandIndex> options
    Then  Verify edited <swimlane> is displayed in the app
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin              | brand           | swimlane          | roku_brandIndex  | server    | company_name     | API             |              
        | fyc_execution_id | fyc_admin_brand | fyc_admin_edited_swimlane_name | 2    |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2185 @TC-2184 @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY076: verify rearranging swimlanes on admin 
    Given I launch Admin Server
    When  I Login with Admin <client_email>, <internal_email> and <password> Credentails
    And   I navigate to FYC portal
    And   I verify by rearranging projects within swimlanes
    And   I verify by rearranging swimlanes
    Examples:
        | client_email | internal_email | password      |         
        | clientemail  | internalemail  | adminpassword |  


@FYCRegression @TC-2185 @TC-2184 @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY077: verify rearranging swimlane in FYCApp
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    #And   I select <brand> or <roku_brandIndex> options
    Then  Verify rearranged <swimlane> <swimlane_position> is displayed in the app
    Then  I verify <projects> within swimlane is rearranged
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin              | brand           | swimlane                       | projects                        | swimlane_position | roku_brandIndex | server    | company_name     | API             |              
        | fyc_execution_id | fyc_admin_brand | fyc_admin_edited_swimlane_name | standard_security_nonepisodic02 | rearranged_swimlane_position | 2      |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2183 @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY078: verify removing projects from swimlanes
    Given I launch Admin Server
    When  I Login with Admin <client_email>, <internal_email> and <password> Credentails
    And   I navigate to FYC portal
    And   I verify by removing projects from swimlanes
    Examples:
        | client_email | internal_email | password      |         
        | clientemail  | internalemail  | adminpassword |  


@FYCRegression @TC-2183 @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY079: verify removing projects from swimlanes in FYCApp
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    #And   I select <brand> or <roku_brandIndex> options
    Then  Verify <projects> removed from <swimlane> is not displayed in the app
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin              | brand           |  projects       | swimlane          | roku_brandIndex  | server    | company_name     | API             |              
        | fyc_execution_id | fyc_admin_brand | no_security_episodic_fyc01 | fyc_admin_edited_swimlane_name | 2   |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2183 @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY080: verify deleting swimlanes on admin 
    Given I launch Admin Server
    When  I Login with Admin <client_email>, <internal_email> and <password> Credentails
    And   I navigate to FYC portal
    And   I delete the swimlane after removing projects
    Examples:
        | client_email | internal_email | password      |         
        | clientemail  | internalemail  | adminpassword |  


@FYCRegression @TC-2183 @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY081: verify swimlane deletion in FYCApp
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    #And   I select <brand> or <roku_brandIndex> options
    Then  Verify deleted <swimlane> is not displayed in the app
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin              | brand           | swimlane          | roku_brandIndex | server    | company_name     | API             |              
        | fyc_execution_id | fyc_admin_brand | fyc_admin_edited_swimlane_name | 2  |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2249 @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY082: Verify publishing the videos
    Given I launch Admin Server
    When  I Login with Admin <client_email>, <internal_email> and <password> Credentails
    And   I search for the <Project_Name> to publish
    And   I navigate to the <Project_Name> to publish 
    And   I navigate to send screeners and publish video
    And   I publish video with <Project_Name> for the paramount brand
    Examples:
        | Project_Name                | video_name                | Description              | Generes_Content       | client_email | internal_email | password      |
        | fyc_project_name_to_publish | fyc_video_name_to_publish | project_description_data | project_action_genre  | clientemail  | internalemail  | adminpassword |


@FYCRegression @TC-2249 @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY083: Verify publishing the videos in FYCApp
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    #And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field for published project
    When  Submit the search
    Then  I verify the content of the search <project_name> results for published project
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin              | brand           | project_name                | roku_brandIndex | server    | company_name     | API             |              
        | fyc_execution_id | fyc_admin_brand | fyc_project_name_to_publish | 1                |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2246 @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY084: Verify unpublishing projects in admin
    Given I launch Admin Server
    When  I Login with Admin <client_email>, <internal_email> and <password> Credentails
    And   I search for the <Project_Name> to unpublish
    And   I navigate to the <Project_Name> to unpublish 
    Then  I verify that the project is unpulished
    Examples:
        | Project_Name                | client_email | internal_email | password      |           
        | fyc_project_name_to_publish | clientemail  | internalemail  | adminpassword |   


@FYCRegression @TC-2246 @FYCRoku @Adminscript @FYCipad @FYCFireStick2 @FYCFireStick @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY085: Verify Unpublishing the videos in FYCApp
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    #And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field for unpublished project
    When  Submit the search
    Then  Verify unpublished project is not displayed in the app
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin              | brand           | project_name | roku_brandIndex | server    | company_name     | API             |              
        | fyc_execution_id | fyc_admin_brand | fyc_project_name_to_publish | 1 |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2247 @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY086: Verify deleting the videos inside project
    Given I launch Admin Server
    When  I Login with Admin <client_email>, <internal_email> and <password> Credentails
    And   I search for the <Project_Name> to publish for deleting video under project
    And   I navigate to the <Project_Name> to publish for deleting video under project
    And   I navigate to send screeners and publish video
    And   I publish video with <Project_Name> for the paramount brand for deleting video under project
    And   I search for the <Project_Name> to delete the video
    And   I navigate to the <Project_Name> to delete the video 
    Then  I verify the video inside the <Project_Name> is deleted
    Examples:
        | Project_Name             | video_name                | Description              | Generes_Content      | client_email | internal_email | password      |  
        | fyc_admin_project_name_2 | fyc_video_name_to_publish | project_description_data | project_action_genre | clientemail  | internalemail  | adminpassword |  


@FYCRegression @TC-2247 @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY087: Verify Deleted Video Under Project Is Not Displayed in FYCApp
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    #When  I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field for deleted video under project
    When  Submit the search
    Then  Verify deleted video under project is not displayed in the app
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin              | brand           | project_name             | roku_brandIndex  | server    | company_name     | API             |              
        | fyc_execution_id | fyc_admin_brand | fyc_admin_project_name_2 | 1 |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2248 @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY088: Verify deleting the projects in admin
    Given I launch Admin Server
    When  I Login with Admin <client_email>, <internal_email> and <password> Credentails
    And   I search for the <Project_Name> to delete
    And   I navigate to the <Project_Name> to delete 
    Then  I verify that the <Project_Name> is delete
    Examples:
        | Project_Name             | client_email | internal_email | password      |         
        | fyc_admin_project_name_2 | clientemail  | internalemail  | adminpassword |  


@FYCRegression @TC-2248 @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline: FY089: Verify Deleted Project Is Not Displayed in FYCApp
    Given I launch FYC Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    #And   I select <brand> or <roku_brandIndex> options
    Then  I verify that the Search field is present and visible
    When  I verify by entering a <project_name> search term in the Search field for deleted project
    When  Submit the search
    Then  Verify deleted project is not displayed in the app
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin              | brand           | project_name | roku_brandIndex   | server    | company_name     | API             |              
        | fyc_execution_id | fyc_admin_brand | fyc_admin_project_name_2 | 1 |fyc_server  | fyc_company_name | fyc_API_version | 


@FYCRegression @TC-2180 @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline:  FY090: verify by uploading the carousel image
    Given I launch Admin Server
    When  I Login with Admin <client_email>, <internal_email> and <password> Credentails
    And   I navigate to FYC portal
    When  I verify by uploading the carousel image
    Examples:
        | client_email | internal_email | password      |         
        | clientemail  | internalemail  | adminpassword |  


@FYCRegression @TC-2180 @FYCRoku @FYCFireStick @Adminscript @FYCipad @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline:  FY091: Verify Added Carousel image is reflected in app
    Given I launch FYC Application
    When  I am in Login Page
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    #And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    Then  Carousel Image should be displayed on Top of Homepage Page
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                  | brand                 | roku_brandIndex |
        | fyc_execution_id     | fyc_brand_with_poster | 1 |


@FYCRegression @TC-2179 @FYCRoku @Adminscript @FYCipad @FYCFireStick @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline:  FY092: verify by deleting the carousel image 
    Given I launch Admin Server
    When  I Login with Admin <client_email>, <internal_email> and <password> Credentails
    And   I navigate to FYC portal
    When  I verify by deleting the carousel image  
    Examples:
        | client_email | internal_email | password      |         
        | clientemail  | internalemail  | adminpassword |  


@FYCRegression @TC-2179 @FYCRoku @FYCFireStick @Adminscript @FYCipad @FYCFireStick2 @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck @FYCSupportedDeviceCheck2 @FYCUnSupportedDeviceCheck2 
Scenario Outline:  FY093: Verify Deleted Carousel image is not displayed in app
    Given I launch FYC Application
    When  I am in Login Page
    When  Enter <pin> in Login page
    And   I click on the Enter button
    When  I click on cmaf button
    #And   I select <brand> or <roku_brandIndex> options
    When  I navigate to home page
    Then  Carousel Image should not be displayed on Top of Homepage Page
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | pin                  | brand                 | roku_brandIndex |
        | fyc_execution_id     | fyc_brand_with_poster | 1 |


@FYCRegression @Adminscript @PinConfiguration @FYCipad @FYCSupportedDeviceCheck @FYCUnSupportedDeviceCheck
Scenario Outline:  FY094: Disable Pin Configuration In Nimaad
    Given I launch nimaad link  
    When  I login with valid <username> and <password> credentials
    And   I navigate to application configuration and search for the <pin>
    And   I select <brand> to disable <pin> configuration
    And   I disable pin configuration and save it
    Examples:
        | username        | password        | pin              | brand |
        | nimaad_username | nimaad_password | fyc_execution_id | fyc_admin_brand_selection |
    