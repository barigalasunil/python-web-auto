@ScreenerAppValidations
Feature: Screener Sanity Feature


@ScreenerRegression @ScreeneriPad 
Scenario Outline: SCR000: Install Application From TestFlight
    Given  I install Screener <application> from testflight for <api_version> with <build_number>
    Examples:
        | application        | api_version                      | build_number           | 
        | sreeners_app_name  | screeners_api_version_to_install | screeners_build_number | 


@ScreenerRegression @ScreenerSettings @TC-1965 @ScreenerRoku @ScreeneriPad @ScreenerFireStick @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR001: Update settings in the TV application
    Given I launch Screener Application
    When  I am in Login Page
    When  The user clicks on Settings button
    When  I update the <server> <server_ipad> <company_name> and <API> key fields
    Then  The fields should be updated successfully
    Examples:
        | server           | server_ipad           | company_name           | API           |
        | screeners_server | screeners_server_ipad | screeners_company_name | screeners_api |


@ScreenerRegression @TC-1952 @TC-1951 @TC-1950 @TC-1949 @ScreenerRoku @ScreeneriPad @ScreenerFireStick @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR002: Launch app and validate login screen elements
    Given I launch Screener Application
    Then  I verify The app load image is present
    When  I am in Login Page
    Then  I verify Login Page BackGround image is loaded
    Then  I verify App icon is present
    Then  I verify Sign in header is present
    Then  I verify Email and Password Fields Present
    Then  I verify Forget Password Link is present
    Then  I verify Sign In Button is Present
    Then  I verify Sign In With QR Code Button is Present
    Then  I Verify terms and services is displayed
    Then  I verify App Version is present 
    Then  I verify Settings button is Present
    Then  I Verify the chat support
    Then  I verify Login Checkbox is present with correct Text
   

@ScreenerRegression @TC-1954 @ScreenerRoku @ScreeneriPad @ScreenerFireStick @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline: SCR003: Forget password Link popup message 
    Given I launch Screener Application
    When  I am in Login Page
    Then  I verify that the Forgot Password link is visible and clickable
    Then  I navigate into Forgot Password link and validate the popup message

@ScreenerRegression @IpadOnly @TC-1955 @ScreeneriPad
Scenario Outline:  SCR004 : Forget password Link popup message In Ipad
    Given I launch Screener Application
    When  I am in Login Page
    Then  I verify Forget Password Link is present
    When  Click on the Forgot Password link
    Then  I verify enter email address popup messsage is displayed
    When  Enter <email_address> to request reset password link
    Then  Verify email successfully sent <success_message>
    Examples:
        | email_address                     | success_message |
        | screener_change_password_username | An email containing the password reset link has been sent to your email ID. |


@ScreenerRegression @IpadOnly @TC-1962 @TC-1956 @ScreeneriPad 
Scenario Outline:  SCR005 : Verify and Validate Change Password and Login Functionality in iPad
    Given I launch Screener Application
    When  I am in Login Page
    Then  I verify Forget Password Link is present
    When  Click on the Forgot Password link
    Then  I verify enter email address popup messsage is displayed
    When  Enter <email_address> to request reset password link
    Then  Verify email successfully sent <success_message>
    Given I launch Nimaad portal
    When  I login with nimaad <username_nimaad> and <password_nimaad>
    When  I select user <email_address> to change password
    When  I verify the mail and click on reset password button
    When  I create new password for the user
    Then  I verify password changed message
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <email_address> and password credentials after changing password
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | email_address                     | username_nimaad | password_nimaad    | success_message |
        | screener_change_password_username | nimaad_username | nimaad_password | An email containing the password reset link has been sent to your email ID. |

   
@ScreenerRegression @TC-1959 @ScreenerRoku @ScreeneriPad @ScreenerFireStick @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR006 : Verify the appropriate message displayed while entering wrong credentials
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    Then  I verify the appropriate error message <errormessage> is displayed 
    Examples:
        | username                   | password         | errormessage               |
        | screener_invalid_username  | invalid_password | Screener_wrong_password |


@ScreenerRegression @TC-1960 @ScreenerRoku @ScreeneriPad @ScreenerFireStick @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR007 : Non verified/account user login failing with correct error message
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials with Non verified 
    Then  I verify the appropriate error message <errormessage>, <error_message_ipad> is displayed for non verified user
    Examples:
        | username          | password         | errormessage                         | error_message_ipad         |
        | unverified_email  | valid_password   | screener_Non_verified_error_message1 | Screener_invalid_pin_error |


@ScreenerRegression @TC-1976 @TC-1963 @TC-1958 @ScreenerRoku @ScreeneriPad @ScreenerFireStick @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR008 : Successful Login and loggout
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username                | password                | 
        | valid_user | valid_password |


@ScreenerRegression @TC-1961 @ScreenerFireStick @ScreenerRoku @ScreeneriPad @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR009 : Verify the appropriate message displayed while entering wrong password
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    Then  I verify the appropriate error message <errormessage> is displayed
    Examples:
        | username                 | password                  | errormessage          |
        | valid_user  | Screener_invalid_password | Screener_wrong_password |


@ScreenerRegression @IpadOnly @TC-1971 @ScreeneriPad 
Scenario Outline:  SCR010 : Verify application navigate user to homepage After tapping the header logo IPAD
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  Click on header logo
    Then  Verify home page is navigated on clicking on header logo
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password        | project_name                     |
        | valid_user | valid_password  | no_watermark_no_security_project |

@ScreenerRegression @TC-1970 @ScreenerRoku @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR011 : Verify header logo display on top left corner of the screen
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    Then  I verify that the header logo is displayed correctly
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username                | password                | 
        | valid_user | valid_password |


@ScreenerRegression @TC-1972 @ScreenerRoku @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR012 : Verify the genres dropdown in Homepage
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    Then  I verify that the Genres dropdown is visible
    When  I click on <genres> dropdown
    Then  Verify respective <project> is displayed under selected genre  
    Then  I click on Logout and verify Loggedout successfully   
    Examples:
        | username   | password       | genres               | project                          |
        | valid_user | valid_password | project_action_genre | no_watermark_no_security_project |   
  

@ScreenerRegression @TC-1973 @TC-1974 @ScreenerRoku @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR013 : Verify the Menu bar in Homepage
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility  
    Then  I verify that each menu item is present and visible     
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username                | password                | 
        | valid_user | valid_password |    


@ScreenerRegression @TC-1975 @ScreenerRoku @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR014 : Verify the Help section in Homepage Menu bar
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  Click on help icon from the menu
    Then  I verify the Help document is displayed 
    Then  I click on Logout and verify Loggedout successfully
    # Help section document is not displaying
    Examples:
        | username                | password                | 
        | valid_user | valid_password | 


@ScreenerRegression @TC-1977 @TC-1978 @ScreenerRoku @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR015 : Verify the Search field in Homepage Menu bar  
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    Then  I verify the <project_name> content of the search results
    # When  Click on first video inside the project
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password       | project_name |
        | valid_user | valid_password | downloadable_screener_project |


@ScreenerRegression @TC-1980 @ScreenerRoku @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR016 : Verify the Pagination call Search field  
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    Then  I verify the pagination call after receiving search results
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password        | project_name          |
        | valid_user | valid_password  | search_string_project |


@ScreenerRegression @TC-1983 @TC-1982 @TC-1981 @TC-1980 @ScreenerRoku @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR017 : Validation of Project and Video Details
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  I Click On Details Tab
    Then  Project <project_synopsis> Information Should be Displayed
    Then  Project <cast> and <crew> and <crew_ipad> Information Should be Displayed in Details Tab 
    When  I Click On Videos Tab
    When  I Click On <video_name> Inside Project
    Then  Video <video_synopsis> Information Should be Displayed
    Then  Video <cast> and <crew> and <crew_ipad> Information Should be Displayed in Details Tab
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password        | project_name                                        | project_synopsis    | video_synopsis   | cast                 | crew                 | crew_ipad            | video_name |
        | valid_user | valid_password  | forensic_burned_watermark_password_security_project | project_description | episode_synopsis | project_cast_lengthy | project_crew_lengthy | project_cast_lengthy | video_name_one_usg_episodic    |


@ScreenerRegression @TC-1985 @ScreenerRoku @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline: SCR018 : Verify and Validate the Videos Tab on Videos Listing page
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  I Click On Videos Tab
    Then  I verify that the correct content is displayed under the Videos tab
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password        | project_name                                |
        | valid_user | valid_password  | forensic_only_watermark_no_security_project | 


@ScreenerRegression @ScreenerRoku @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR019 : Verify and Validate the Details Tab on Videos Listing page
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  I Click On Details Tab
    Then  I verify that the correct content is displayed under the Details tab   
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password        | project_name                                |
        | valid_user | valid_password  | forensic_only_watermark_no_security_project | 


@ScreenerRegression @TC-1986 @ScreenerRoku  @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR020 : Validate Airdate Information Not Displayed on Episodic and Non-Episodic Content
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name_episodic> in the Search field
    When  Click on <project_name_episodic> from Search Result
    When  I Click On Details Tab
    Then  Airdate Should not be Displayed on Project Information
    When  I navigate to home page
    When  I click on search button in home page
    Then  I verify by entering a <project_name_nonepisodic> in the Search field
    When  Click on <project_name_nonepisodic> from Search Result
    When  I Click On Details Tab
    Then  Airdate Should not be Displayed on Project Information
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password        | project_name_episodic                         | project_name_nonepisodic         |
        | valid_user | valid_password  | forensic_burned_watermark_no_security_project | no_watermark_no_security_project | 


@ScreenerRegression @TC-1987 @ScreenerRoku @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck 
Scenario Outline:  SCR021 : Verify and Validate the maximum count in remaining views
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    Then  Verify that the <project_video> has remaining views greater than <count> 
    Then  I verify playback of the video that has views greater than 20
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password        | project_name                                  | count         | project_video |
        | valid_user | valid_password  | forensic_burned_watermark_no_security_project | maximum_count | Test_4k       |


@ScreenerRegression @TC-1994 @ScreenerRoku @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR022 : Verify and Validate the with Switching subtitle
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  I Click On <video_name> Inside Project
    When  I do remote activity in Roku
    When  I start the video playback    
    And   I Tap on the subtitle options menu in the video player  
    Then  I verify that multiple subtitle options are available
    When  I select a different <subtitle> option
    Then  I verify that the selected subtitle is displayed correctly during playback
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password        | project_name                     | subtitle        | video_name |
        | valid_user | valid_password  | no_watermark_no_security_project | french_subtitle | Test_4k    |


@ScreenerRegression @TC-2043 @ScreenerRoku 
Scenario Outline:  SCR023 : Verify Login With Remote Functionality
    Given I launch Screener Application
    When  I am in Login Page
    When  Click on Sign In With QR Code
    Then  Validate QR Screen elements
    When  Click on Sign in with Remote Button
    Then  Verify Navigation To Login Page


@ScreenerRegression @TC-2040 @ScreenerFireStick @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR024 : Verify a new QR code is generated each time "LOG IN WITH QR" is selected
    Given I launch Screener Application
    When  I am in Login Page
    When  Click on Sign In With QR Code
    Then  Verify Sign In With QR Code Page Reached
    Then  Compare QR codes generated upon selecting Login with QR Screen button two times


@ScreenerRegression @TC-2041 @ScreenerRoku @ScreenerFireStick @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR025 :  Verify New QR Code Generation Every 5 Minutes
    Given I launch Screener Application
    When  I am in Login Page
    When  Click on Sign In With QR Code
    Then  Verify Sign In With QR Code Page Reached
    Then  Validate QR Screen elements for 5min


@ScreenerRegression @TC-1997 @TC-1996 @ScreenerFireStick @ScreenerRoku @ScreeneriPad @ScreenerSupportedDeviceCheck
Scenario Outline:  SCR026 :  Verify Playback on Multiple Audio Screeners
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  I Click On Project Video With Multiple Audio <Audio_video> Under Selected Project
    When  I start the video playback    
    And   I Tap on the audio options menu in the video player  
    Then  I verify that multiple audio options are available
    Then  I verify default audio is selected
    When  I select a different <audio>, <audio_ipad> option from the list
    Then  I verify that the selected audio is played correctly during playback
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password        | project_name                                | audio_ipad                         | Audio_video |audio  |
        | valid_user | valid_password  | forensic_only_watermark_no_security_project | screener_audio_selection_ipad | multiple_audio_video_name |screener_audio_selection|


@ScreenerRegression @TC-1999 @ScreenerFireStick @ScreenerRoku @ScreeneriPad @ScreenerSupportedDeviceCheck 
Scenario Outline: SCR027 : Verify Auto Playback Functionality
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  I Click On <video_name> Inside Project
    When  I start the video playback    
    And   I play the video to the fullest
    Then  I verify that the auto playback functionality works as expected
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password        | project_name                                | video_name |
        | valid_user | valid_password  | forensic_only_watermark_no_security_project | 5_1_audio_channel_video_s3_key |


@ScreenerRegression @IpadOnly @TC-2031 @ScreeneriPad 
Scenario Outline:  SCR028 : Verify Minimizing and Launching the App In IPAD
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by search page is reached
    When  Minimize the application
    When  ReLaunch the <application>
    Then  Verify app launches in same page after relaunching
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username                | password                | application         |
        | valid_user | valid_password | screeners_bundle_id |


@ScreenerRegression @IpadOnly @TC-2032 @ScreeneriPad 
Scenario Outline:  SCR029 : Verify Killing and Relaunching the App In IPAD
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by search page is reached
    When  Close the <application> completly
    When  ReLaunch the <application>
    Then  Verify app launches in home page after killing an relaunching
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username                | password                | application         |
        | valid_user | valid_password | screeners_bundle_id |


@ScreenerRegression @TC-1984 @ScreenerFireStick @ScreenerRoku @ScreeneriPad @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR030 : Verify and validate pagination call in the project listing page
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    Then  verify pagination call in the project listing page
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username                | password                | 
        | valid_user | valid_password | 
        

@ScreenerRegression @IpadOnly @TC-2020 @TC-2014 @TC-2015 @TC-2016 @TC-2017 @TC-2019 @ScreeneriPad 
Scenario Outline:  SCR031: Verify playback of the downloaded project and deleting the project from downloads
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on download button
    Then  I verify navigation to download page
    Then  I verify no projects in downloads
    When  I navigate to home page
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    #When  I select <season_number> with multiple audio and subtitle videos
    When  I Click On Project Video With Multiple Audio <Audio_video> Under Selected Project
    When  I click on download button inside project 
    When  I click on download button
    Then  I verify navigation to download page
    Then  I verify <project_name> added in downloads
    When  I play the downloaded project
    Then  verify the downloaded project has multiple <audio> and <subtitle> tracks
    When  I select the project to delete
    And   I delete the downloaded project by clicking on confirm delete
    Then  I verify <project_name> is deleted from downloads
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password       | project_name                  | season_number          | Audio_video               | subtitle        | audio |
        | valid_user | valid_password | downloadable_screener_project | download_season_number | multiple_audio_video_name | select_subtitle | screener_audio_selection_ipad |


@ScreenerRegression @IpadOnly @TC-2018 @ScreeneriPad 
Scenario Outline:  SCR032: Verify downloaded project is deleted after logging out of the application 
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on download button
    Then  I verify navigation to download page
    Then  I verify no projects in downloads
    When  I navigate to home page
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  I Click On <video_name> Inside Project
    When  I click on download button inside project 
    When  I click on download button
    Then  I verify navigation to download page
    Then  I verify <project_name> added in downloads
    Then  I click on Logout and verify Loggedout successfully
    When  Enter <username> and <password> Credentials
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on download button
    Then  I verify navigation to download page
    Then  I verify <project_name> is deleted from downloads
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password       | project_name                  | video_name |
        | valid_user | valid_password | downloadable_screener_project | Test_4k    |


@ScreenerRegression @IpadOnly @TC-2013 @ScreeneriPad 
Scenario Outline:  SCR033: Verify Playback on Downloadable Screeners Disabled Screener
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  I Click On <video_name> Inside Project
    Then  I verify download screeners is disabled
    When  I start the video playback    
    Then  verify the downloaded project has multiple <audio> and <subtitle> tracks
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password        | project_name                                | subtitle        | audio                         | video_name |
        | valid_user | valid_password  | forensic_only_watermark_no_security_project | french_subtitle | screener_audio_selection_ipad | 5_1_audio_channel_video_s3_key |


@ScreenerRegression  @TC-2010 @ScreenerRoku @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR034: Verify Multiple Audio Playback on No Security Screener
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  I Click On Project Video With Multiple Audio <Audio_video> Under Selected Project
    When  I start the video playback    
    And   I Tap on the audio options menu in the video player  
    Then  I verify that multiple audio options are available
    Then  I verify default audio is selected
    When  I select a different <audio>, <audio_ipad> option from the list
    Then  I verify that the selected audio is played correctly during playback
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password        | project_name                     | Audio_video               | audio_ipad                         |audio|
        | valid_user | valid_password  | no_watermark_no_security_project | multiple_audio_video_name | screener_audio_selection_ipad |screener_audio_selection|


@ScreenerRegression @TC-2009 @TC-2002 @ScreenerRoku @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck 
Scenario Outline:  SCR035: Verify Multiple Audio Playback on Forensic Screener
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  I Click On Project Video With Multiple Audio <Audio_video> Under Selected Project
    When  I start the video playback    
    And   I Tap on the audio options menu in the video player  
    Then  I verify that multiple audio options are available
    Then  I verify default audio is selected
    When  I select a different <audio>, <audio_ipad> option from the list
    Then  I verify that the selected audio is played correctly during playback
    Then  I verify forensic watermark in the media player
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password        | project_name                     | Audio_video               | audio_ipad                         |audio|
        | valid_user | valid_password  | forensic_only_watermark_no_security_project | multiple_audio_video_name | screener_audio_selection_ipad |screener_audio_selection1|


@ScreenerRegression @TC-2008 @TC-2003 @ScreenerRoku @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR036: Verify Multiple Audio Playback on Overlay Screener
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  I Click On Project Video With Multiple Audio <Audio_video> Under Selected Project
    When  I start the video playback    
    And   I Tap on the audio options menu in the video player  
    Then  I verify that multiple audio options are available
    Then  I verify default audio is selected
    When  I select a different <audio>, <audio_ipad> option from the list
    Then  I verify that the selected audio is played correctly during playback
    Then  I verify overlay watermark in the media player
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password        | project_name                     | Audio_video               | audio_ipad                         |audio|
        | valid_user | valid_password  | overlay_watermark_no_security_project | multiple_audio_video_name | screener_audio_selection_ipad |screener_audio_selection|


@ScreenerRegression @TC-2004 @TC-2005 @ScreenerRoku @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck 
Scenario Outline:  SCR037: Verify Playback on Forensic Burned Watermark Screener
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  I Click On <video_name> Inside Project
    When  I start the video playback    
    Then  verify playback in media player
    Then  I verify forensic burned watermark in the media player
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password        | project_name                                  | video_name |
        | valid_user | valid_password  | forensic_burned_watermark_no_security_project | Test_4k    |


@ScreenerRegression @IpadOnly @ScreeneriPad 
Scenario Outline:  SCR038: Verify Playback on 2FA password Screener
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  I Click On <video_name> Inside Project
    When  I start the video playback    
    Then  I verify 2FA password authetication popup is displayed
    When  I enter <screener_password> in authentication popup and unlock the project video
    Then  verify playback in media player
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password        | project_name                                | screener_password       | video_name |
        | valid_user | valid_password  | overlay_watermark_password_security_project | valid_screener_password | Test_4k    |


@ScreenerRegression @TC-2001 @ScreenerRoku @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR039: Verify Playback on 2FA Verification via Phone
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  I Click On <video_name> Inside Project
    When  I start the video playback    
    Then  I verify 2FA phone authetication popup is displayed
    When  I enter <country_code> <mobile_number> in authentication popup and get the code
    Then  verify enter code popup is displayed
    Then  I verify playback after unlocking by entering code
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password        | project_name                        | mobile_number          | country_code          | video_name |
        | valid_user | valid_password  | no_watermark_phone_security_project | screener_mobile_number | screener_country_code | Test_4k    |


@ScreenerRegression @TC-2007  
Scenario Outline:  SCR040: Verify The Guild Contains No Security, Forensic and Overlay Screeners
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    When  I verify by entering a <no_security_project_name> <forensic_project_name> <overlay_project_name> different projects in the Search field
    When  Click on <overlay_project_name> from Search Result
    When  I Click On <video_name> Inside Project
    When  I start the video playback    
    Then  verify playback in media player
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password        | no_security_project_name         | forensic_project_name                       | overlay_project_name                  | video_name |
        | valid_user | valid_password  | no_watermark_no_security_project | forensic_only_watermark_no_security_project | overlay_watermark_no_security_project | Test_4k    |


@ScreenerRegression @TC-1988 @ScreenerRoku @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck 
Scenario Outline:  SCR041: Verify Expired Screeners Label
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    Then  I verify the project videos are <expired_message>
    Then  I click on Logout and verify Loggedout successfully
    # View are more same is video is not expired
    Examples:
        | username   | password        | project_name                                   | expired_message                |
        | valid_user | valid_password  | forensic_only_watermark_phone_security_project | expired_screener_error_message |


@ScreenerRegression @TC-1990 @TC-1989 @ScreenerRoku @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR042: Verify Expiring Screeners With Expiry Date Is Future Dated Displayed
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    Then  I verify the expires on text is visible and the expiry date is future dated
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username   | password        | project_name         | 
        | valid_user | valid_password  | future_dated_project | 


@ScreenerRegression @TC-2000 @ScreenerRoku @ScreenerFireStick @ScreeneriPad @ScreenerSupportedDeviceCheck 
Scenario Outline:  SCR043: Verify Updating Screeners In Admin Reflected In App
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    Then  I validate remaining views and expiry date
    Then  I click on Logout and verify Loggedout successfully
    Given I launch Admin Server
    When  I Login with Admin Credentials
    And   I search for the <project_name> to update screeners
    And   I click on <project_name> from search results in admin
    And   I navigate to screeners tab and select the <user>
    When  I select <video_name> to update screeers
    And   I update the screeners expiry date and remaining views 
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  I click on cmaf button
    When  Click on <project_name> from Search Result
    Then  I verify remaining views and expiry date value is updated
    Then  I click on Logout and verify Loggedout successfully
    # Use headless mode admin-firestick
    Examples:
        | username   | password        | project_name                                      | user       | video_name                | 
        | valid_user | valid_password  | forensic_only_watermark_password_security_project | valid_user | multiple_audio_video_name | 


@ScreenerRegression @ScreenerRoku @ScreenerFireStick @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR044 :  Verify URL Login with Valid Credentials and Auto-Login on Device
    Given I launch Screener Application
    When  I am in Login Page
    When  I select the option Enter with QR CODE to log in using a URL
    When  I copy the provided URL and opens it on a secondary device
    When  I enter <username> and <password> and submit
    Then  I verify the successful login <message> on the secondary device
    # Then  verify screener app on the primary device logs in automatically
    Then  I verify that each menu item is present and visible
    Then  I click on Logout and verify Loggedout successfully
    # User ID is not displayed
    Examples:
        | username          | password          |   message          |
        | valid_user   | valid_password          | gd_secondary_successfull_message |


@ScreenerRegression @TC-2035  @ScreenerFireStick @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR045: Verify cmaf error banner in login page and playback of forensic video for unsupported devices
    Given I launch Nimaad portal
    When  I login with nimaad <username_nimaad> and <password_nimaad>
    When  I click on unsupported devices
    When  I add the device under unsupported devices
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    # When  Submit the search
    When  Click on <project_name> from Search Result
    When  I Click On Videos Tab
    When  I start the video playback
    Then  I verify Unsupported device error banner is displayed in forensic playback
    Then  I click on Logout and verify Loggedout successfully
    # forensic_only_watermark_no_security_project -video is not playing
    Examples:
        | username                | password                 | project_name                                |username_nimaad|password_nimaad|
        | valid_user | valid_password  | forensic_only_watermark_no_security_project |nimaad_username|nimaad_password|
        
@ScreenerRegression @TC-2036 @ScreenerFireStick @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR046: Verify cmaf error banner is displayed in login page and not in playback of overlay video for unsupported devices
    Given I launch Nimaad portal 
    When  I login with nimaad <username_nimaad> and <password_nimaad>
    When  I click on unsupported devices
    When  I add the device under unsupported devices
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    # When  Submit the search
    When  Click on <project_name> from Search Result
    When  I Click On Videos Tab
    When  I start the video playback
    Then  I verify Unsupported device error banner is displayed in overlay playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username                | password                 | project_name                                |username_nimaad|password_nimaad|
        | valid_user | valid_password  | AB_Security_nonepisodic01 |nimaad_username|nimaad_password|
    
@ScreenerRegression @TC-2037 @TC-2038 @ScreenerFireStick @ScreenerSupportedDeviceCheck 
Scenario Outline:  SCR047: Verify cmaf error banner is not displayed in login page and playback of forensic video for supported devices
    Given I launch Nimaad portal 
    When  I login with nimaad <username_nimaad> and <password_nimaad>
    When  I click on unsupported devices
    When  I add the device under unsupported devices
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    # When  Submit the search
    When  Click on <project_name> from Search Result
    When  I Click On Videos Tab
    When  I start the video playback
    Then  I verify Unsupported device error banner is not displayed in forensic playback
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username                | password                 | project_name                                |username_nimaad|password_nimaad|
        | valid_user | valid_password  | AB_Security_episodic01 |nimaad_username|nimaad_password|

    
@ScreenerRegression @TC-2039 @ScreenerFireStick @ScreenerSupportedDeviceCheck 
Scenario Outline:  SCR048: Verify cmaf error banner is not displayed in login page and playback of overlay video for supported devices
    Given I launch Nimaad portal
    When  I login with nimaad <username_nimaad> and <password_nimaad>
    When  I click on unsupported devices
    When  I add the device under unsupported devices
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    # When  Submit the search
    When  Click on <project_name> from Search Result
    When  I Click On Videos Tab
    When  I start the video playback
    Then  I verify Unsupported device error banner is not displayed in overlay playback 
    Then  I click on Logout and verify Loggedout successfully
    Examples:
        | username                | password                 | project_name                                |username_nimaad|password_nimaad|
        | valid_user | valid_password  | AB_Security_episodic01 |nimaad_username|nimaad_password|

@ScreenerRegression @TC-2050 @TC-2052 @TC-2053 @TC-2054 @ScreenerRoku @ScreenerFireStick @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline: SCR049: Verify URL Login negative scenarios
    Given I launch Screener Application
    When  I am in Login Page
    When  I select the option Enter with QR CODE to log in using a URL
    When  I copy the provided URL and opens it on a secondary device # if the test case continue from previous case, click count is changing
    When  I enter <username> and <password> and submit
    Then  Verify <errormessage> on the login page on secondary device for <disc>
    When  Click on Sign in with Remote Button
    Examples:
        | username         | password   | errormessage                  |  disc |
        | gd_empty_username | gd_password1    | gd_email_left_blank   | gd_empty_error_message |
        | screener_valid_username |    gd_empty_password        | gd_error_message_blank | gd_empty_password_error_message |
        | screener_invalid_username  | Screener_invalid_password          |  gd_invalid_credential  | gd_invalid_message |

@ScreenerRegression @TC-2042 @ScreenerRoku @ScreenerFireStick @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR050 : Verify Login Page Navigation From QR Screen After 10 Minutes
    Given I launch Screener Application
    When  I am in Login Page
    When  Click on Sign In With QR Code
    Then  Verify Sign In With QR Code Page Reached 
    Then  The application should automatically redirect the user to the login screen after 10min


@ScreenerRegression @IpadOnly @TC-2033 @ScreeneriPad @ScreenerSupportedDeviceCheck @ScreenerUnSupportedDeviceCheck
Scenario Outline:  SCR051 : Verify Playback After Upgrading The Screeners App From TestFlight
    Given I launch Testflight application
    When  I am in Testflight app
    When  I install previous build application from testflight
    When  Launch the installed <application>
    Then  I verify app launch in previous build
    When  I update the <application> from testflight
    Given I launch Screener Application
    When  I am in Login Page
    When  The user clicks on Settings button
    When  I update the <server> <server_ipad> <company_name> and <API> key fields
    Then  The fields should be updated successfully
    When  Enter <username> and <password> Credentials
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  I Click On <video_name> Inside Project
    When  I start the video playback
    Then  verify playback in media player
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Given  I install Screener <application_name> from testflight for <api_version> with <build_number> 
    When  The user clicks on Settings button
    When  I update the <server> <server_ipad> <company_name> and <API> key fields
    Then  The fields should be updated successfully
    Examples:
        | username   | password       | application         | server           | server_ipad           | company_name           | API           | project_name                     | video_name | application_name        | api_version                      | build_number           | 
        | valid_user | valid_password | screeners_bundle_id | screeners_server | screeners_server_ipad | screeners_company_name | screeners_api | no_watermark_no_security_project | Test_4k    | sreeners_app_name       | screeners_api_version_to_install | screeners_build_number | 


@ScreenerRegression @IpadOnly @TC-2034 @ScreeneriPad 
Scenario Outline:  SCR052 : Verify Playback After Uninstalling and reinstalling The Screeners App From TestFlight
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials
    When  I click on cmaf button
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  The user uninstalls the <application> from the device
    When  The user re-installs the <application> on the same device
    Given I launch Screener Application
    When  I am in Login Page
    When  The user clicks on Settings button
    When  I update the <server> <server_ipad> <company_name> and <API> key fields
    Then  The fields should be updated successfully
    When  Enter <username> and <password> Credentials
    Then  Verify User Login Successfully by Validating HomeScreen Visibility
    When  I click on search button in home page
    Then  I verify by entering a <project_name> in the Search field
    When  Click on <project_name> from Search Result
    When  I Click On <video_name> Inside Project
    When  I start the video playback
    Then  verify playback in media player
    When  I close the playback
    Then  I click on Logout and verify Loggedout successfully
    Given  I install Screener <application_name> from testflight for <api_version> with <build_number> 
    When  The user clicks on Settings button
    When  I update the <server> <server_ipad> <company_name> and <API> key fields
    Then  The fields should be updated successfully
    Examples:
        | username   | password       | application         | server           | server_ipad           | company_name           | API           | project_name                     | video_name | application_name        | api_version                      | build_number           | 
        | valid_user | valid_password | screeners_bundle_id | screeners_server | screeners_server_ipad | screeners_company_name | screeners_api | no_watermark_no_security_project | Test_4k    | sreeners_app_name       | screeners_api_version_to_install | screeners_build_number | 


@ScreenerRegression @IpadOnly @TC-1966 @TC-1967 @TC-1968 @TC-1969 @ScreeneriPad 
Scenario Outline:  SCR053 : Verify Resend Verification Link For Non verified User
    Given I launch Screener Application
    When  I am in Login Page
    When  Enter <username> and <password> Credentials with Non verified 
    Then  I verify the resend verification email popup
    When  I click on resend verification link
    Then  I verify login page navigation after clicking on go back to sign in button
    Given I launch Nimaad portal
    When  I login with nimaad <username_nimaad> and <password_nimaad>
    When  I select user <username> to verify resend verification link
    Then  I verify resend verification email in nimaad
    Examples:
        | username                       | password        | username_nimaad | password_nimaad | 
        | screener_nonverified_username  | valid_password  | nimaad_username | nimaad_password |
