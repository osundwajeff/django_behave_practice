Feature: testing website navigation

  Scenario: logging into admin page
    Given user is on 'Admin Log in page'
    When user clicks on 'Log in'
    Then page is 'Admin page'