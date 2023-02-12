Feature: Login
  Scenario: Login
    Given Launch Chrome Browser
    When Open Webpage phptravels
    Then Verify Account visible
    Then Click Account
    When Enter username "jmarijanovic000@gmail.com" and password "123456789jm"
    Then Profile Picture visible
    And Close Browser




