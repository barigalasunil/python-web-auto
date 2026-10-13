@CinemaAppValidations
Feature: Cinema Sanity Feature

@CinemaRegression @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline: CI001 : Update settings in the TV application
    Given I launch Cinema Application on Respective platform
    When  I am in Login Page
    When  The user clicks on the Settings button
    When  I update the <server> <company_name> and <API> key fields
    Then  The fields should be updated successfully
    Examples:
        | server       | company_name              | API            |
        | cinema_server | cinema_company_name      | cinema_API    | 

@CinemaRegression @CinemaRoku @CinemaFireStick @TC-2060 @TC-2061 @TC-2062 @TC-2067 @TC-2064 @TC-2065 @TC-2070 @TC-2065 @TC-2063 @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline:  CI002: Launch app and validate login screen elements
    Given I launch Cinema Application on Respective platform
    Then  The app load image is present
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    Then  I verify Login Page BackGround image is loaded
    Then  I verify Cinema App icon is present
    Then  I verify Sign in header is present
    Then  I verify Access Key field is present with <text>
    Then  I verify Enter Button is Present
    Then  I verify App Version is present 
    Then  I verify Settings button is Present
    Then  Where can I find my access code
    Examples:
    | server       | company_name              | API            |  text |
    | cinema_server | cinema_company_name      | cinema_API    |  cinema_Accesscode |

@CinemaRegression @TC-2070 @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline:  CI003: Verify Terms and Conditions    
    Given I launch Cinema Application on Respective platform
    Then  I verify terms and services is displayed
    Then  I verify by tapping on Terms and services
    Then  I navigate back to login page
    # terms and terms is blocked in firestick

@CinemaRegression @TC-2071 @CinemaRoku @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline: CI004: Verify Privacy policy    
    Given I launch Cinema Application on Respective platform
    Then  I verify Privacy policy is displayed
    Then  I verify by tapping on Privacy policy 
    # terms and terms is blocked in firestick

@CinemaRegression @TC-2065 @CinemaRoku @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline:  CI005: Verify Where can I find my access code    
    Given I launch Cinema Application on Respective platform
    Then  I verify Where can I find my access code field    

@CinemaRegression @TC-2069 @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline:  CI006: Verify Error Message without entering Pin
    Given I launch Cinema Application on Respective platform
    When  User update the <server> <company_name> and <API> key fields in roku
    Then  verify <errormessage_without_entering_pin> without entering pin
    Examples:
        |errormessage_without_entering_pin  | server       | company_name              | API            |
        |errormessage_without_entering_pin  | cinema_server | cinema_company_name      | cinema_API    | 
        
   
@CinemaRegression @TC-2068 @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline:  CI007: Verify and Validate Login with Invalid pin
    Given I launch Cinema Application on Respective platform
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter <invalid_pin> in Login page
    And   I click on the Enter button
    Then  I verify the <errormessage_invalid_pin> on Loginpage
    Examples:
        | invalid_pin              | errormessage_invalid_pin   | server       | company_name              | API            |
        | invalid_pin               | error_message_expired_access_code  | cinema_server | cinema_company_name      | cinema_API    | 

@CinemaRegression @TC-2090 @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline:  CI008: Verify and Validate Login with valid pin
    Given I launch Cinema App URL to fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button 
    Then  I verify the screener has projects
    Then  I logout from the application and verify logged out  
    Examples:
    | server       | company_name              | API            |
    | cinema_server | cinema_company_name      | cinema_API    |   


@CinemaRegression @TC-2066 @CinemaFireStick @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline:  CI009: Verify Sign In Button Focused In Login Screen
    Given  I launch Cinema App URL to fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button 
    Then  I logout from the application and verify logged out  
    Examples:
    | server       | company_name              | API            |
    | cinema_server | cinema_company_name      | cinema_API    |  


@CinemaRegression @TC-2072 @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline:  CI010: Verify Successfull login with same access code once and again login will through error
    Given I launch Cinema App URL to fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button 
    Then  I verify the screener has projects
    Then  I logout from the application and verify logged out 
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    Then  I verify the expired pin <error_message_expired_access_code> on the Login
    Examples:
        |error_message_expired_access_code   | server       | company_name              | API            |
        |error_message_expired_access_code    | cinema_server | cinema_company_name      | cinema_API    | 
 

@CinemaRegression @TC-2074 @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline:  CI011: Verify the first video in the project gets highlighted after successful login.
    Given I launch Cinema App URL to fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button  
    Then  I verify the screener has projects
    Then  Verify the first video in the project gets highlighted
    Then  I logout from the application and verify logged out 
    Examples:
    | server       | company_name              | API            |
    | cinema_server | cinema_company_name      | cinema_API    | 
   

@CinemaRegression @TC-2075 @TC-2076 @TC-2077 @TC-2079 @TC-2078 @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck   
Scenario Outline:  CI012: Verify Header Logo
    Given I launch Cinema App URL to fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button 
    When  I click on cmaf button 
    Then  I verify the screener has projects
    Then  I verify the Header logo on Homepage
    Then  I verify that the header logo,project poster,banner,see more button,<Project_description>
    Then  I logout from the application and verify logged out
    Examples:
    | server       | company_name              | API            |Project_description|
    | cinema_server | cinema_company_name      | cinema_API    |Episodic_description|


# @CinemaSanity17
# Scenario Outline:  FY003: Verify project related in Homepage
#     Given I launch Cinema App URL to fetch Access Code
#     When  I launch Cinema Application
#     When  I am in Login Page
#     When  Enter AccessCode in Login page
#     And   I click on the Enter button 
#     Then  I verify project banner in Homepage
#     And   I verify project poster in Homepage
#     And   I verify see more button in Homepage 
#     And   I verify the project description 
# Alreday completed in above Header Logo- Verify Header Logo

@CinemaRegression @TC-2083 @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline:  CI013: Verify the synopsis in episodic project
    Given I launch Cinema App URL to fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button  
    Then  I verify the screener has projects 
    When  I click on the project <roku_index> displayed on Homepage
    Then  Verify synopsis in episodic project is displayed 
    Then  I logout from the application and verify logged out  
    Examples:
    | server       | company_name              | API            | roku_index |
    | cinema_server | cinema_company_name      | cinema_API    |  1 |


@CinemaRegression @TC-2085 @TC-2086 @CinemaRoku1 @CinemaFireStick @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline: CI014: Verify the season number in episodic project
    Given I launch Cinema App URL to fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button 
    Then  I verify the screener has projects 
    When  I click on the project <roku_index> displayed on Homepage
    Then  Verify season number in episodic project is displayed  
    And   Verify episodic number in episodic project is displayed 
    Then  I logout from the application and verify logged out  
    # FOR for season number no need to click on project video
    Examples:
    | server       | company_name              | API            | roku_index |
    | cinema_server | cinema_company_name      | cinema_API    |  1  |


@CinemaRegression @TC-2085 @CinemaFireStick @CinemaRoku @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline:  CI015: Verify the season number in multiple episodic project
    Given I launch Cinema App URL to fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button 
    Then  I verify the screener has projects   
    Then  Verify multiple episodic project is displayed     
    Then  I logout from the application and verify logged out    
    Examples:
    | server       | company_name              | API            |
   | cinema_server | cinema_company_name      | cinema_API    |    
                  

@CinemaRegression @TC-2081 @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline: CI016: Verify Cast and crew info in Project Page and video
    Given I launch Cinema App URL to fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button  
    Then  I verify the screener has projects  
    When  I click on the project <roku_index> displayed on Homepage
    Then  Project <Cast> and <Crew> Information Should be Displayed
    Then  I logout from the application and verify logged out  
    Examples:
        | Cast        | Crew      | server       | company_name              | API            | roku_index |
        | Cast       | Crew       |  cinema_server | cinema_company_name      | cinema_API    |  1 |


@CinemaRegression @TC-2099 @CinemaFireStick @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline: CI017: Verify invalid Password screener playback
    Given I launch Cinema App URL for <project_link> and fetch Access Code 
    When  I launch Cinema Application
    When  I am in Login Page
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button   
    Then  I verify the screener has projects  
    When  I click on the project <roku_index> displayed on Homepage 
    And   I click on the Watch now button
    And   I enter the <invalid_password> and submit
    Then  I verify the <invalid_password_error_message> playback
    Then  I click on close button
    Then  I logout from the application and verify logged out  
    # In admin add the password athentication
    Examples:
        | invalid_password                 | invalid_password_error_message | roku_index | project_link |
        | cinema_invalid_password         |  invalid_password_error_message  |  1 | NoWMPwd |


@CinemaRegression  @CinemaTest007 @TC-2102 @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline: CI018: Verify Phone verification screener playback
    Given I launch Cinema App URL for <project_URL_link> and fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button  
    Then  I verify the screener has projects  
    When  I click on the project <roku_index> displayed on Homepage
    And   I click on the Watch now button
    When  I enter the valid <phone_number> 
    And   I enter the otp 
    Then  I verify the <invalid_password_error_message> on the OTP sections OTP
    Then  I click on close button
    Then  I logout from the application and verify logged out  
    Examples:
        | invalid_password_error_message                | server       | company_name              | API            | roku_index | phone_number | project_URL_link |
        | cimena_invalid_password_error_message         | cinema_server | cinema_company_name      | cinema_API    |   1 | 4843734025 | PhoneNoWM |
        
   

@CinemaRegression @TC-2093 @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline: CI019: Verify Watch now button display
    Given I launch Cinema App URL for <project_URL_link> and fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button   
    Then  I verify the screener has projects 
    When  I click on the project <roku_index> displayed on Homepage
    Then  I verify the watch now button is displayed on project
    Then  I logout from the application and verify logged out
    # Video is not playing
    Examples:
    | server       | company_name              | API            | roku_index | project_URL_link |
    | cinema_server | cinema_company_name      | cinema_API    |  1                 | NoSecurityNoWM |
  

@CinemaRegression @TC-2095 @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck 
Scenario Outline: CI020: Verify the video duration visibility on projects
    Given I launch Cinema App URL for <project_URL_link> and fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button   
    Then  I verify the screener has projects 
    Then  Verify the video duration visibility on projects
    Then  I logout from the application and verify logged out
    Examples:
    | server       | company_name              | API            | project_URL_link |
    | cinema_server | cinema_company_name      | cinema_API    | Cinema_URL_Forensic_watermark |


@CinemaRegression  @TC-2114 @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline: CI021: Verify the navigate back using Back option and login to application
    Given I launch Cinema App URL to fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button   
    Then  I verify the screener has projects 
    And   I navigate back to the home using navigate back option
    When  I relaunch Cinema Application
    Then  I verify the launch page 
    Examples:
    | server       | company_name              | API            |
    | cinema_server | cinema_company_name      | cinema_API    |  


@CinemaSettings @CinemaRegression2 @indee @CinemaRoku @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline: CI022: Update settings in the TV application After App navigation
    Given I launch Cinema Application on Respective platform
    When  I am in Login Page
    When  The user clicks on the Settings button
    When  I update the <server> <company_name> and <API> key fields
    Then  The fields should be updated successfully
    Examples:
        | server | company_name   | API      |
        | cinema_server | cinema_company_name      |cinema_API    |     


@CinemaRegression @TC-2115 @CinemaRoku @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline: CI023: Verify the navigate back using Home option and login to application
    Given I launch Cinema App URL to fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button  
    Then  I verify the screener has projects  
    And   I navigate back to the home using Home option
    When  I relaunch Cinema Application
    Then  I verify the launch page
    Examples:
    | server       | company_name              | API            |
    | cinema_server | cinema_company_name      | cinema_API    | 


@CinemaSettings @CinemaRegression2 @indee @CinemaRoku @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline: CI024: Update settings in the TV application for Home button
    Given I launch Cinema Application on Respective platform
    When  I am in Login Page
    When  The user clicks on the Settings button
    When  I update the <server> <company_name> and <API> key fields
    Then  The fields should be updated successfully
    Examples:
        | server | company_name   | API      |
        | server | company_name      | API    | 


@CinemaRegression @TC-2103 @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck 
Scenario Outline: CI025: Verify the Forensic with Standard watermark
    Given I launch Cinema App URL for <project_URL_link> and fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button   
    Then  I verify the screener has projects 
    When  I click on the project <roku_index> displayed on Homepage 
    And   I click on the Watch now button
    And   I enter the <password> and submits
    Then  I verify the successfull playbacks
    Then  I logout from the application and verify logged out  
    Examples:
    | server       | company_name              | API            | roku_index | project_URL_link | password |
    | cinema_server | cinema_company_name      | cinema_API    |   2 | ForensicOnlyPwd | Test@123 |


@CinemaRegression @TC-2104 @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck 
Scenario Outline: CI026: Verify the Forensic with Adjustable watermark
    Given I launch Cinema App URL for <project_URL_link> and fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button   
    Then  I verify the screener has projects 
    When  I click on the project <roku_index> displayed on Homepage 
    And   I click on the Watch now button
    And   I enter the <password> and submits
    And   I Tap on the subtitle options menu in the video player
    Then  I verify by selecting the different <subtitle>   
    Then  I verify the successfull playbacks
    Then  I logout from the application and verify logged out  
    # Water mark video is expired
    Examples:
    | server       | company_name              | API            | password | roku_index | project_URL_link | subtitle |
    | cinema_server | cinema_company_name      | cinema_API     | Test@123 | 1               | ForensicOnlyPwd  | select_subtitle |


@CinemaRegression @TC-2105 @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline: CI027: Verify the Overlay screener watermark
    Given I launch Cinema App URL for <project_URL_link> and fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button   
    Then  I verify the screener has projects 
    When  I click on the project <roku_index> displayed on Homepage 
    And   I click on the Watch now button
    Then  I verify the successfull playbacks
    Then  I logout from the application and verify logged out  
    Examples:
    | server       | company_name              | API            | roku_index | project_URL_link |
    | cinema_server | cinema_company_name      | cinema_API    |  1  | NoSecurityOverlayWM |

@CinemaRegression @TC-2106 @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline: CI028: Verify the No security watermark
    Given I launch Cinema App URL for <project_URL_link> and fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button   
    Then  I verify the screener has projects 
    When  I click on the project <roku_index> displayed on Homepage 
    And   I click on the Watch now button 
    Then  I verify the successfull playbacks     
    Then  I logout from the application and verify logged out   
    Examples:
    | server       | company_name              | API            | roku_index | project_URL_link |
    | cinema_server | cinema_company_name      | cinema_API    |  1  | NoSecurityNoWM |


@CinemaRegression  @TC-2113 @CinemaFireStick @CinemaRoku @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline: CI029: Verify the app by close and reopen
    Given I launch Cinema App URL to fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button 
    Then  I verify the screener has projects 
    When  I close the app
    When  I relaunch Cinema Application
    Then  I verify the launch page
    Examples:
    | server       | company_name              | API            |
    | cinema_server | cinema_company_name      | cinema_API    | 


@CinemaSettings @CinemaRegression2 @indee @CinemaRoku @CinemaSupportedDeviceCheck @CinemaUnSupportedDeviceCheck 
Scenario Outline: CI030: Update settings in the TV application for Closing app
    Given I launch Cinema Application on Respective platform
    When  I am in Login Page
    When  The user clicks on the Settings button
    When  I update the <server> <company_name> and <API> key fields
    Then  The fields should be updated successfully
    Examples:
        | server | company_name   | API      |
        | server | company_name      | API    | 


@CinemaRegression @TC-2099 @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck 
Scenario Outline: CI031: Verify invalid Password screener playback
    Given I launch Cinema App URL for <project_URL_link> and fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button  
    Then  I verify the screener has projects  
    When  I click on the project <roku_index> displayed on Homepage 
    And   I click on the Watch now button
    And   I enter the <invalid_password> and submit
    Then  I verify the <invalid_password_error_message> playback
    Then  I click on close button
    Then  I logout from the application and verify logged out
    Examples:
        | invalid_password                 |         invalid_password_error_message  |  server       | company_name              | API            | roku_index | project_URL_link |
        | invalid_password                 |         invalid_password_error_message  | cinema_server | cinema_company_name      | cinema_API    | 1 | ForensicOnlyPwd |
             
         
@CinemaRegression @TC-2087 @TC-2088 @CinemaRoku @CinemaFireStick @CinemaSupportedDeviceCheck 
Scenario Outline: CI032: Verify Expiry label with date and time display
    Given I launch Cinema App URL for <project_URL_link> and fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button 
    Then  I verify the screener has projects 
    When  I click on the project <roku_index> displayed on Homepage
    Then  I verify the <Expiry_date_and_time> displayed on project data
    Then  I logout from the application and verify logged out  
    # Video is expired
    Examples:
        |     Expiry_date_and_time       |   server       | company_name              | API            | roku_index | project_URL_link |
        |     Expiry_date_and_time       | cinema_server | cinema_company_name      | cinema_API    |         1 | Cinema_URL_Forensic_watermark |


@CinemaRegression @TC-2091 @CinemaFireStick @CinemaRoku @CinemaSupportedDeviceCheck 
Scenario Outline: CI033: Verify Remaining views display
    Given I launch Cinema App URL for <project_URL_link> and fetch Access Code
    When  I launch Cinema Application
    When  I am in Login Page
    When  User update the <server> <company_name> and <API> key fields in roku
    When  Enter AccessCode in Login page
    And   I click on the Enter button
    When  I click on cmaf button    
    Then  I verify the screener has projects 
    When  I click on the project <roku_index> displayed on Homepage
    Then  I verify the <Remaining_views> displayed on project
    Then  I logout from the application and verify logged out  
    # Video is expired
    Examples:
        |     Remaining_views        | server       | company_name              | API            | roku_index | project_URL_link |
        |     Remaining_views       |  cinema_server | cinema_company_name      | cinema_API    |   1 |     Cinema_URL_Forensic_watermark |   
    
