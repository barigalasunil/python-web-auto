Feature: FYC Web Validation Tests
  As a web user of the FYC platform
  I want to validate the login, home, and logout functionality
  using a pure web Playwright + pytest-bdd framework

  @smoke
  Scenario: Verify FYC login page structure
    Given I launch FYC Application homepage
    When I log in with "standard_user" and "secret_sauce"
    Then Verify the page title contains expected text
    And Verify the page URL contains "/inventory"
    And Verify sign-in header is displayed

  @sanity
  Scenario: Verify FYC home page and logout
    Given I launch FYC Application homepage
    When I log in with "standard_user" and "secret_sauce"
    Then Verify the page title contains expected text
    And Verify the page URL contains "/inventory"
    And Verify user can log out
    And Verify sign-in header after logout

  @regression
  Scenario: Complete FYC login-logout-login cycle
    Given I launch FYC Application homepage
    When I log in with "standard_user" and "secret_sauce"
    Then Verify the page title contains expected text
    And Verify the page URL contains "/inventory"
    And Verify sign-in header is displayed
    And Verify user can log out
    And Verify user can log back in with same credentials