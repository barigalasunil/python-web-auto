@GDAppValidations
Feature: GD Sanity Feature


@GDRegression @GDipad 
Scenario Outline: GD000: Install Application From TestFlight
    Given  I install GD <application> from testflight for <api_version> with <build_number>
    Examples:
        | application  | api_version               | build_number    | 
        | gd_app_name  | gd_api_version_to_install | gd_build_number | 


@GDSettings @GDRegression @GDNimaad @GDRoku @TC-2303 @GDipad @GDFireStick @GDFireStick1 @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline: GD001: Update settings in the TV application
    Given I launch GD Application
    When  I am in GD  Login Page
    When  The user clicks on the Settings button
    When  user update the <server> <server_ipad> <company_name> <API> <API_ipad> and <API_Key> key fields
    Then  The fields should be updated successfully
    Examples:
        | server    | server_ipad    | company_name    | API            | API_ipad            | API_Key    |
        | gd_server | gd_server_ipad | gd_company_name | gd_API_version | gd_API_version_ipad | gd_API_key |


@GDRegression @TC-2294 @TC-2295 @TC-2296 @TC-2297 @TC-2297 @TC-2299 @TC-2300 @TC-2301 @TC-2302 @TC-2315 @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline:  GD002: Launch app and validate login screen elements
    Given I launch GD Application
    When  I am in GD  Login Page
    Then  The app load image is present
    Then  I verify Login Page BackGround image is loaded
    Then  I verify GD App icon is present
    Then  I verify Sign in header is present
    Then  I verify Email and Password Fields Present
    Then  I verify Forget Password Link is present
    Then  I verify Sign In Button is Present
    Then  I verify Sign In With QR Code Button is Present
    Then  I verify App Version is present 
    Then  I verify Settings button is Present
    Then  I verify Login Checkbox is present and <checbox_status> and <text>
    Then  I verify Terms and condition button is Present
    Examples:
    | checbox_status | text | 
    | GD_Login_checkbox_status  | GD_Login_checkbox_text | 

@GDRegression @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline: GD003 : Verify adding the project videos to publish
    Given I launch Admin Server
    When  I Login with Admin Credentails
    And   I navigate to projects and Add new project
    And   I enter the required <Project_Name> <Description> and <Generes_Content> details 
    And   I enter the required <video_name> details and upload video
    Examples:
        | Project_Name          | Description              | Generes_Content      | video_name |
        | gd_admin_project_name | project_description_data | project_action_genre | gd_video_name_to_publish |

@GDRegression @TC-2304 @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline:  GD004 : Unsuccessful Login Without Credentials  
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Email and Password Fields Are Cleared
    When  Click on Sign in Button
    Then  Enter Credentials <errormessage> Should be Displayed 
    Examples:
        | errormessage               |
        | error_email_field_blank |



@GDRegression @TC-2379 @GDRoku @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline:  GD005 : Verify Login With Remote Functionality 
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Click on Sign In With QR Code
    Then  Verify Sign In With QR Code Page Reached
    Then  Validate QR Screen elements
    When  Click on Sign in with Remote Button
    Then  Verify Navigation To Login Page


@GDRegression @GDRoku @GDipad @GDRoku @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline:  GD006 : Forget password Link popup message 
    Given I launch GD Application
    When  I am in GD  Login Page
    Then  I verify that the Forgot Password link is visible and clickable
    When  Click on the Forgot Password link
    Then  I navigate into Forgot Password link and validate the popup message <forgot_password_text>  and <forgot_password_popup_text>
    Then  I click Go Back Button in FogotPassword popup
    Examples:
        | forgot_password_text  |forgot_password_popup_text |
        | forgot_password_text |           forgot_password_popup_text |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   


@GDRegression @TC-2306 @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline:  GD007 : Verify the appropriate message displayed while entering wrong credentials
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter incorrect <username> and <password> for invalid password
    And   Click on Sign in Button    
    Then  I verify the appropriate error message <errormessage> is displayed 
    Examples:
        | username                 | password         | errormessage |
        | valid_email_gd  | invalid_password | error_message_invalid |


@GDRegression @TC-2376 @GDdemoexecution @GDRoku @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline:  GD008 : Verify a new QR code is generated each time "LOG IN WITH QR" is selected
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Click on Sign In With QR Code
    Then  Verify Sign In With QR Code Page Reached
    Then  Compare QR codes generated upon selecting Login with QR Screen button two times
    When  Click on Sign in with Remote Button

 
@GDRegression @AppleTest @GDipad
Scenario Outline:  GD009: Verify Terms Of Service
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Click on terms of service button
    Then  Verify terms of service document 

# Ipad only Solution


@GDRegression @TC-2329 @TC-2313 @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline:  GD010 : Verify the Menu bar in Homepage
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully    
    Then  I verify that each menu item is present and visible     
    When  I click on Logout 
    Then  Click Signout in Confirmation screen    
    Then  Verify Navigation To Login Page
    Examples:
        | username                  | password   | 
        | valid_email_gd | valid_password  |      

 
@GDRegression @TC-2317 @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline:  GD011 : Verify and Validate Carousel view
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    Then  The Carousel View should be visible on the screen
    When  I click on Logout 
    Then  Click Signout in Confirmation screen
    Examples:
        | username                  | password   | application |
        | valid_email_gd | valid_password  | gd_bundle_id|


@GDRegression @TC-2322 @TC-2326 @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDSupportedDeviceCheck1
Scenario Outline:  GD012 : Validate Swimlanes and Associated Projects
    Given  I launch GD Application
    When   I am in GD  Login Page
    When   Enter <username> and <password> Credentials and Login
    When   I click on cmaf button
    Then   Verify User Login Successfully
    Then   Swimlanes Should be Displayed on the Home Screen
    Then   Each Swimlane Should Display its Respective Projects
    Then   User Should be able to Play Videos Play For the Selected Project
    When   I close the playback
    When   I click on Logout
    Then   Click Signout in Confirmation screen
    Examples:
        | username                  | password   | 
        | valid_email_gd | valid_password  |         


@GDRegression @TC-2331 @TC-2332 @TC-2333 @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline:  GD013 : Verify the Search field in Homepage Menu bar  
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    Then  I verify the <project_name> content of the search results
    Then  I verify the pagination call after receiving search results
    When  Click on <project_name> from Search Result
    When  I click on Logout from Player
    Then  Click Signout in Confirmation screen
    Examples:
        | username                | password   | project_name |
        | valid_email_gd | valid_password  | project_with_poster_and_banner |



@GDRegression @GDTestnew @TC-2328 @GDRokuGeneres @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline:  GD014 : Verify the genres dropdown in Homepage
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    Then  I verify that the Genres dropdown is visible
    When  I click on <genres> dropdown
    Then  Verify all genres titles are displayed with <expected_project>  
    When  I click on Logout from Player
    Then  Click Signout in Confirmation screen
    Examples:
        | username                | password        | genres               | expected_project                |
        | valid_email_gd | valid_password  | project_action_genre | episodic_with_poster_and_banner |  


@GDRegression @TC-2358 @TC-2361 @TC-2360 @TC-2363 @GDipad 
Scenario Outline: GD015 : Verify Project Playback by adding and deleting projects from downloads
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    Then  Verify User Login Successfully
    When  I Click on download button
    Then  I verify navigation to download page
    Then  I verify no projects in downloads
    When  I click on home button from menu
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    And   Click on Project <Video_name>
    And   I download the project video
    And   I Click on download button
    Then  I verify navigation to download page
    Then  I verify <project_name> added in downloads
    When  I play the downloaded project
    When  I select the project to delete
    And   I delete the downloaded project by clicking on confirm delete
    Then  I verify <project_name> is deleted from downloads
    When  I click on Logout 
    Then  verify Loggedout successfully
    Examples:
        | username                | password        | project_name              | Video_name |
        | valid_email_gd | valid_password  | episodic_with_only_banner | 5_1_audio_channel_video_s3_key |


@GDRegression @GDipad @TC-2362 
Scenario Outline:  GD016 : Verify that Downloaded Videos are Not Retained After Reinstalling the App
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    Then  Verify User Login Successfully
    When  I Click on download button
    Then  I verify navigation to download page
    Then  I verify no projects in downloads
    When  I click on home button from menu
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    And   Click on Project <Video_name>
    And   I download the project video
    And   I Click on download button
    Then  I verify navigation to download page
    Then  I verify <project_name> added in downloads
    When  The user uninstalls the <application> from the device
    When  The user re-installs the <application> on the same device
    Given I launch GD Application
    When  I am in GD  Login Page
    When  The user clicks on the Settings button
    When  user update the <server> <server_ipad> <company_name> <API> <API_ipad> and <API_Key> key fields
    Then  The fields should be updated successfully
    When  Enter <username> and <password> Credentials and Login
    Then  Verify User Login Successfully
    When  I Click on download button
    Then  I verify navigation to download page
    Then  I verify <project_name> is deleted from downloads
    When  I click on Logout from Player
    Then  verify Loggedout successfully
    Given  I install GD <application_name> from testflight for <api_version> with <build_number>
    When  The user clicks on the Settings button
    When  user update the <server> <server_ipad> <company_name> <API> <API_ipad> and <API_Key> key fields
    Then  The fields should be updated successfully
    Examples:
        | username                | password        | application  | project_name              | server    | server_ipad    | company_name    | API            | API_ipad   | API_Key    | Video_name                  | application_name | api_version               | build_number    | 
        | valid_email_gd | valid_password  | gd_bundle_id | episodic_with_only_poster | gd_server | gd_server_ipad | gd_company_name | gd_API_version | gd_API_version_ipad | gd_API_key | video_name_one_usg_episodic | gd_app_name      | gd_api_version_to_install | gd_build_number | 


@GDRegression @GDipad 
Scenario Outline:  GD017 : Verify that Downloaded Videos are Not Retained After Logging Out Of The App
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    Then  Verify User Login Successfully
    When  I Click on download button
    Then  I verify navigation to download page
    Then  I verify no projects in downloads
    When  I click on home button from menu
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    And   Click on Project <Video_name>
    And   I download the project video
    And   I Click on download button
    Then  I verify navigation to download page
    Then  I verify <project_name> added in downloads
    When  I click on Logout
    Then  Click Signout in Confirmation screen
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    Then  Verify User Login Successfully
    When  I Click on download button
    Then  I verify navigation to download page
    Then  I verify <project_name> is deleted from downloads
    When  I click on Logout from Player
    Then  verify Loggedout successfully
    Examples:
        | username                | password        | project_name              | server    | server_ipad    | company_name    | API            | API_ipad            | API_Key    | Video_name |
        | valid_email_gd | valid_password  | episodic_with_only_poster | gd_server | gd_server_ipad | gd_company_name | gd_API_version | gd_API_version_ipad | gd_API_key | video_name_one_usg_episodic |


@GDRegression @TC-2337 @TC-2339 @TC-2340 @TC-2341 @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline:  GD018 : Validation of Project and Video Details
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    When  I click on home button from menu
    When  I click on search button in home page
    When  Search for <Episodic_Project> on the HomeScreen
    When  Click on <Episodic_Project> from Search Result
    Then  Project Information <project_synopsys> Should be Displayed
    Then  Project <project_cast> and <project_crew> Information Should be Displayed
    When  Click on Project <Video_name>
    Then  Video Information Should be Displayed
    Then  Video <video_cast> and <video_crew> Information Should be Displayed
    When  I click on Logout 
    Then  verify Loggedout successfully
    Examples:
        | username       | password        | Episodic_Project                   | project_synopsys            | project_cast         | project_crew         | video_cast    | video_crew      | Video_name |
        | valid_email_gd | valid_password  | episodic_without_poster_and_banner | project_description_lengthy | project_crew_lengthy | project_cast_lengthy | project_crew_lengthy | project_cast_lengthy | multiple_audio_video |


@GDRegression @TC-2342 @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline:  GD019 : Validate Airdate Information on Episodic Content
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    When  I click on home button from menu
    When  I click on search button in home page
    When  Search for <Episodic_Project> on the HomeScreen
    When  Click on <Episodic_Project> from Search Result
    Then  Airdate <airdate_value> Should be Displayed on Project Information For The Selected <Video_name>
    When  I click on Logout 
    Then  verify Loggedout successfully
    Examples:
        | username       | password       | Episodic_Project                   | airdate_value  | Video_name |
        | valid_email_gd | valid_password | episodic_without_poster_and_banner | gd_airdate     | multiple_audio_video |


@GDRegression @TC-2343 @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline:  GD020 : Validate Airdate Information No Displayed on Non-Episodic Content
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    When  I click on home button from menu
    When  I click on search button in home page
    When  Search for <Non_Episodic_Project> on the HomeScreen
    When  Click on <Non_Episodic_Project> from Search Result
    Then  Airdate Should not be Displayed on Project Information For The Selected <Video_name>
    When  I click on Logout 
    Then  verify Loggedout successfully
    Examples:
        | username       | password       | Non_Episodic_Project     | Video_name |
        | valid_email_gd | valid_password | project_with_poster_and_banner    | Non_episodic_02 |

   
@GDRegression @TC-2334 @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline:  GD021 : Verify and Validate the Videos Tab on Videos Listing page
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    When  I click on home button from menu
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  Click on video tab in the project page
    Then  I verify that the correct content is displayed under the Videos tab 
    When  I click on Logout 
    Then  verify Loggedout successfully
    Examples:
        | username       | password        | project_name                        |
        | valid_email_gd | valid_password  | episodic_without_poster_and_banner  |


@GDRegression @TC-2335 @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline:  GD022 : Verify and Validate the Details Tab on Videos Listing page
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    When  I click on home button from menu
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  Click on details tab in the project page
    Then  I verify that the correct content is displayed under the Details tab
    When  I click on Logout 
    Then  verify Loggedout successfully    
    Examples:
        | username       | password        | project_name                       |
        | valid_email_gd | valid_password  | episodic_without_poster_and_banner |


@GDRegression @TC-2344 @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline:  GD023 : Verify and Validate the maximum count in remaining views 
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    When  I click on home button from menu
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    And   Click on first <video_name> inside the project
    Then  I verify that the selected project has remaining views greater than 20
    When  I click on Logout 
    Then  verify Loggedout successfully
    Examples:
        | username       | password        | project_name                       | video_name |
        | valid_email_gd | valid_password  | episodic_without_poster_and_banner | multiple_audio_video |


@GDRegression @GDipad @TC-2351 @TC-2352 @TC-2353 @TC-2355 @GDRoku @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDSupportedDeviceCheck1 
Scenario Outline:  GD024 : Verify and Validate the with Switching subtitle
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    When  I click on home button from menu
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  I play the project video 
    And   I Tap on the subtitle options menu in the video player  
    Then  I verify that multiple subtitle options are available
    When  I select a different <subtitle> option
    Then  I verify that the selected subtitle is displayed correctly during playback
    When  I click back from Roku device
    When  I click on Logout 
    Then  verify Loggedout successfully
    Examples:
        | username       | password        | project_name           | subtitle |
        | valid_email_gd | valid_password  | non_episodic_project6  | select_subtitle |


@GDRegression @GDAudioTest @TC-2354 @TC-2355 @TC-2356 @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDSupportedDeviceCheck1 
Scenario Outline:  GD025 :  Verify Playback on Multiple Audio Screeners
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    When  I click on search button in home page
    Then  I verify by entering a <project_name>, <project_name_ipad> in the Search field
    When  Click on <project_name> from Search Result
    When  I play the project video
    And   I access the audio track selection options
    And   I select different <audio> tracks during playback
    Then  I verify that the screener plays correctly with the selected audio track
    When  I click back from Roku device
    When  I click on Logout 
    Then  verify Loggedout successfully
    Examples:
        | username       | password        | project_name                | project_name_ipad                  | audio |
        | valid_email_gd | valid_password  | non_episodic_project8       | episodic_without_poster_and_banner | gd_audio_selection |


@GDRegression @TC-2347  
Scenario Outline:  GD026 : Verify and Validate the Overlay playback
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    When  I should Tap on the video with Overlay watermark
    Then  I should verify the video playing with standard watermark
    When  I click back from Roku device
    When  I click on Logout 
    Then  verify Loggedout successfully
    Examples:
        | username       | password        | 
        | valid_email_gd | valid_password  | 


@GDRegression @GDTest28 @TC-2348 
Scenario Outline:  GD027 : Verify and Validate the No watermark playback
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    When  I should Tap on the video with No watermark Overlay watermark
    Then  I should verify the video playing with No watermark 
    When  I click back from Roku device
    When  I click on Logout 
    Then  verify Loggedout successfully   
    Examples:
        | username       | password        | 
        | valid_email_gd | valid_password  |  


@GDRegression @TC-2336 @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline:  GD028 : Verify and validate pagination call in the project listing page
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    Then  verify pagination call in the project listing page
    When  I click on Logout 
    Then  verify Loggedout successfully
    Examples:
        | username       | password        | 
        | valid_email_gd | valid_password  | 


@GDRegression @TC-2346 @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDSupportedDeviceCheck1 
Scenario Outline: GD029 : Verify Auto Playback Functionality
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Submit the search
    When  Click on <project_name> from Search Result
    And   Click on Project <Video_name>
    And   I play the video to the fullest
    When  I click back from Roku device
    Then  I verify that the correct content is displayed after auto playback
    When  I click on Logout 
    Then  verify Loggedout successfully
    Examples:
        | username       | password        | project_name             | Video_name |
        | valid_email_gd | valid_password  | non_episodic_project8      | multiple_audio_video |

@GDRegression @GDAdmin @TC-2320 @GDipad @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline:  GD030 : verify by deleting the carousel image 
    Given I launch Admin Server
    When  I Login with Admin Credentails
    And   I navigate to Global description portal
    Then  I verify by deleting the carousel image  

@GDRegression @TC-2320 @GDdemoexecution @GDipad @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline: GD031 : Verify Carousel image deleted reflecting in GD app
    Given  I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    Then  verify Carousel image deleted in app
    When  I click on Logout 
    Then  verify Loggedout successfully
    Examples:
        | username       | password        | 
        | valid_email_gd | valid_password  | 


@GDRegression @TC-2321 @GDdemoexecution @GDFireStick @GDipad @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline:  GD032: verify by uploading the carousel image
    Given I launch Admin Server
    When  I Login with Admin Credentails
    And   I navigate to Global description portal
    Then  I verify by uploading the carousel image <imagefile>
    Examples:
            | imagefile |
            |pexels-vlasceanu-1403653.jpg |

@GDRegression @TC-2321 @GDdemoexecution @GDipad @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline: GD033 : Verify Carousel image added reflecting in GD app
    Given  I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    Then  verify Carousel image added in app
    When  I click on Logout 
    Then  verify Loggedout successfully
    Examples:
        | username       | password   | 
        | valid_email_gd | valid_password  | 
 
 
@GDRegression @GDRoku @GDipad @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline: GD034 : Verify publishing the videos
    Given I launch Admin Server
    When  I Login with Admin Credentails
    And   I search for the <Project_Name> to publish
    And   I navigate to the <Project_Name> to publish 
    And   I navigate to send screeners and publish video
    Examples:
        | Project_Name          | 
        | gd_admin_project_name |


@GDRegression @GDRoku @GDipad @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline: GD035 : Verify publishing the videos in GDApp
    Given  Go to GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field for pulished project
    When  Submit the search
    Then  I verify the <project_name> content of the search results for published project
    When  I click on Logout 
    Then  verify Loggedout successfully
    Examples:
        | username                  | password   | project_name |
        | valid_email_gd | valid_password  | gd_admin_project_name |


@GDRegression @GDAdminTest @TC-2357 @GDRoku @GDipad @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline: GD036 : Verify Unpublishing the videos
    Given I launch Admin Server
    When  I Login with Admin Credentails
    And   I search for the <Project_Name> to Unpublishing
    And   I navigate to the <Project_Name> to Unpublish 
    Then  I verify that the <Project_Name> is unpublished
    Examples:
        | Project_Name |           
        | gd_admin_project_name | 

@GDRegression @GDRoku @GDipad @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline: GD037 : Verify Unpublishing the videos in GDApp
    Given  Go to GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field for unpublished projects
    When  Submit the search
    Then  Verify unpublished project is not displayed in the app
    When  I click on Logout 
    Then  verify Loggedout successfully
    Examples:
        | username       | password   | project_name |
        | valid_email_gd | valid_password  | gd_admin_project_name |
        

@GDRegression @GDRoku @GDipad @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline: GD038 : verify adding swimlanes on admin 
    Given I launch Admin Server
    When  I Login with Admin Credentails
    And   I navigate to Global description portal
    And   I verify by adding swimlanes


@GDRegression @GDAdmin2 @GDRoku @GDipad @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline: GD039 : verify added swimlane in GDApp
    Given Go to GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    Then  Verify added <swimlane> is displayed in the app
    When  I click on Logout 
    Then  verify Loggedout successfully
    Examples:
        | username                  | password   | swimlane      |
        | valid_email_gd | valid_password  | gd_Swimlane |


@GDAdmin @GDRoku @GDipad @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline: GD040 : verify editing swimlanes on admin 
    Given I launch Admin Server
    When  I Login with Admin Credentails
    And   I navigate to Global description portal
    And   I verify by editing swimlanes


@GDAdmin @GDRoku @GDipad @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline: GD041 : verify editing swimlane in GDApp
    Given  Go to GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    Then  Verify edited <swimlane> is displayed in the app
    When  I click on Logout 
    Then  verify Loggedout successfully
    Examples:
        | username                  | password   | swimlane        |
        | valid_email_gd | valid_password  | gd_Swimlane1 |

@GDAdmin @TC-2325 @GDRoku @GDipad @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline: GD042 : verify rearranging swimlanes on admin 
    Given I launch Admin Server
    When  I Login with Admin Credentails
    And   I navigate to Global description portal
    And   I verify by rearranging projects within swimlanes
    And   I verify by rearranging swimlanes


@GDAdmin @GDRoku @GDipad @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline: GD043 : verify rearranging swimlane in GDApp swimlane
    Given  Go to GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    Then  Verify rearranged <swimlane> is displayed in the app
    Then  I verify <projects> within swimlane is rearranged
    When  I click on Logout 
    Then  verify Loggedout successfully
    Examples:
        | username                  | password   | swimlane        | projects |
        | valid_email_gd | valid_password  | gd_Swimlane1 | episodic_with_poster_and_banner |


@GDAdmin @GDRoku @GDipad @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline: GD044 : verify removing projects from swimlanes and deleting swimlanes on admin 
    Given I launch Admin Server
    When  I Login with Admin Credentails
    And   I navigate to Global description portal
    And   I verify by removing projects from swimlanes
    And   I delete the swimlane after removing projects


@GDAdmin @GDRoku @GDipad @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline: GD045 : verify swimlane deletion in GDApp
    Given  Go to GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    Then  Verify deleted <swimlane> is not displayed in the app
    When  I click on Logout 
    Then  verify Loggedout successfully
    Examples:
        | username       | password   | swimlane        |
        | valid_email_gd | valid_password  | gd_Swimlane1 |



@@GDRegression @GDipad @TC-2317 @TC-2319 @GDdemoexecution  
Scenario Outline: GD046 : verify Header Logo and Carousel image Functionality in ipad
    Given  I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    Then  Verify User Login Successfully
    Then  verify the header logo in the homepage screen
    When  I click on carousel image
    Then  I verify that the linked project to carousel image is loaded
    When  Click on header logo in Homescreen
    Then  Verify navigation to top in Homescreen
    Examples:
        | username       | password   | 
        | valid_email_gd | valid_password  | 


@GDRegression @GDipad @TC-2318 
Scenario Outline: GD047 : Verify Carousel image autoscroll in ipad
    Given  I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    Then  Verify User Login Successfully
    Then  verify Carousel image autoscroll
    Examples:
        | username                  | password   | 
        | valid_email_gd | valid_password  | 


@GDRegression @GDipad @TC-2374
Scenario Outline: GD048 : Verify Minimizing and launching the app
    Given  I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    Then  Verify User Login Successfully
    When  I click on search button in home page
    Then  I verify search page is reached
    When  I minimize the app
    When  I launch the <application> app
    Then  I verify app launches in the same screen
    Examples:
        | username                  | password   | application |
        | valid_email_gd | valid_password  | gd_bundle_id |


@GDRegression @GDipad @TC-2375 
Scenario Outline: GD049 : Verify Killing and relaunching the app
    Given  I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    Then  Verify User Login Successfully
    When  I click on search button in home page
    Then  I verify search page is reached
    When  I kill the <application> app
    When  I launch the <application> app
    Then  I verify app launches in the homescreen
    Examples:
        | username                  | password   | application |
        | valid_email_gd | valid_password  | gd_bundle_id |



@GDRegression @GDNimaad11 @TC-2397 @GDRoku @GDipad @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDSupportedDeviceCheck2 
Scenario Outline: GD050: Verify Engagement data on nimaad
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  I play the project video
    When  I click back from Roku device
    When  I click on Logout 
    Then  verify Loggedout successfully
    Given I launch Nimaad portal
    When  I login with nimaad <username_nimaad> and <password_nimaad>
    When  I click on view Engagement table
    Then  I verify the project view and device data
    Then  I click on Logout 
    Then  verify Loggedout successfully 
    Examples:
        | username       | password        | project_name           | username_nimaad          | password_nimaad   |
        | valid_email_gd | valid_password  | non_episodic_project6  | gd_nimaad_username | gd_nimaad_password |


@GDRegression @TC-2377 @GDdemoexecution @GDRoku @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline: GD051 :  Verify New QR Code Generation Every 5 Minutes
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Click on Sign In With QR Code
    Then  Verify Sign In With QR Code Page Reached
    Then  Validate QR Screen elements for 5min
    When  Click on Sign in with Remote Button


@GDRegression @GDQRCodeLogin @TC-2390 @TC-2389 @TC-2388 @TC-2387 @QRCOdeTest @GDRoku @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline:  GD052 :  Verify URL Login negative scenarios
    Given I launch GD Application
    When  I am in GD  Login Page
    When  I select the option Enter with QR CODE to log in using a URL
    When  I copy the provided URL and opens it on a secondary device # if the test case continue from previous case, click count is changing
    When  I enter <username> and <password> and submit
    Then  Verify <errormessage> on the login page on secondary device for <disc>
    When  Click on Sign in with Remote Button
    Examples:
        | username         | password   | errormessage                  |  disc |
        | gd_empty_username | gd_password1    | gd_email_left_blank   | gd_empty_error_message |
        | gd_user_name |    gd_empty_password        | gd_error_message_blank | gd_empty_password_error_message |
        | gd_user_name  | gd_password          |  gd_invalid_credential  | gd_invalid_message |


@GDRegression @TC-2310 @TC-2391 @GDRoku @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline:  GD053 :  Verify URL Login with Valid Credentials and Auto-Login on Device
    Given I launch GD Application
    When  I am in GD  Login Page
    When  I select the option Enter with QR CODE to log in using a URL
    When  I copy the provided URL and opens it on a secondary device
    When  I enter <username> and <password> and submit
    Then  I verify the successful login <message> on the secondary device
    Then  verify GD app on the primary device logs in automatically within <duration>
    Examples:
        | username          | password          |   message          | duration |
        | valid_email_gd | valid_password  | gd_secondary_successfull_message |gd_Duration|  


    
@GDRegression @AppleTest @GDipad @TC-2308 @TC-2309 
Scenario Outline:  GD054 : Verify and validate change password functionality
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Click on the Forgot Password link
    Then  I navigate into Change Password popup message  
    When  Enter <username> in forgot password popup message
    Then  I validate <email_sent_message> in forgot password
    When  I click on done button in forgot password
    Then  I verify login page navigation
    Examples:
        | username                  | email_sent_message |
        | valid_email_gd | An email containing the password reset link has been sent to your email ID|


@GDRegression @TC-2378 @GDdemoexecution @GDRoku @GDFireStick @GDFireStick2 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck2 @GDUnSupportedDeviceCheck2
Scenario Outline: GD055 : Verify Login Page Navigation From QR Screen After 10 Minutes
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Click on Sign In With QR Code
    Then  Verify Sign In With QR Code Page Reached 
    Then  The application should automatically redirect the user to the login screen after 10min


@GDRegression @TC-2330 @GDdemoexecution1 @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline:  GD056 : Verify the Help section in Homepage Menu bar
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login
    When  I click on cmaf button
    Then  Verify User Login Successfully
    When  I click on help icon from the menu
    Then  I verify the Help document is displayed 
    Then  I click on Help document and verify the <help_page_header>,<expected_content>,<browsing_shows>,<selected_shows>,<settings_and_features>,<streaming_issues>,<expecteedd_loggingout> contents
    Then  verify the header logo in the homepage screen
    When  I click on Logout 
    Then  Click Signout in Confirmation screen
    Examples:
        | username                | password        |help_page_header| expected_content           | browsing_shows           | selected_shows            | settings_and_features           | streaming_issues                  | expecteedd_loggingout         |
        | valid_email_gd | valid_password  | help_page_header | help_page_expected_content | help_page_browsing_shows | help_page_selecting_shows | help_page_settings_and_features | help_page_solving_straming_issues | help_page_expected_loggingout |


@GDRegression1 @TC-2305 @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline:  GD057 : Non verified/account user login failing with correct error message -
    Given I launch GD Application
    When  I am in GD  Login Page
    When  Enter <username> and <password> Credentials and Login with Non verified 
    Then  I verify the appropriate error message <errormessage> <error_message_ipad> is displayed for Non verified user
    Examples:
        | username          | password        | errormessage                       | error_message_ipad |
        | unverified_email  | valid_password  | GD_NON_VERIFIED | error_message_non_verified_ipad |


@GDRegression @TC-GD010 @GDdemoexecution @GDRoku @GDipad @GDFireStick @GDFireStick1 @GDSupportedDeviceCheck @GDUnSupportedDeviceCheck @GDSupportedDeviceCheck1 @GDUnSupportedDeviceCheck1 
Scenario Outline: GD058 : Verify that the application enforces the minimum version requirement.
    Given I launch GD Application
    When  I am in GD  Login Page
    When  The user clicks on the Settings button
    When  user update the <server> <server_ipad> <company_name> <API_old> <API_ipad_old> and <API_Key> key fields
    Then  The fields should be updated successfully
    Then  verify old version <errormessage>
    When  The user clicks on the Settings button
    When  user update the <server> <server_ipad> <company_name> <API_new> <API_ipad_new> and <API_Key> key fields
    Then  The fields should be updated successfully
    Then  Old version error message should not display
    Examples:
        | server    | server_ipad    | company_name    | API_old            | API_new        | API_ipad_old       | API_ipad_new        | API_Key    | errormessage |
        | gd_server | gd_server_ipad | gd_company_name | gd_old_API_version | gd_API_version | gd_old_API_version | gd_API_version_ipad | gd_API_key | old_version_error_message |
        
