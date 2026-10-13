Feature: Sauce Demo Login
  As a standard user
  I want to log in to the Sauce Demo web app
  so that I can verify the inventory page is displayed

  @smoke
  Scenario: Standard user login validates page structure
    Given I launch the Sauce Demo login page
    When I log in with "standard_user" and "secret_sauce"
    Then the page title should be "Swag Labs"
    And the page URL should contain "/inventory"