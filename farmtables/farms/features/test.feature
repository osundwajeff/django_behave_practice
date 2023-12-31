Feature: testing website navigation

  Scenario: home page
    Given the user is on the homepage
    Then page is homepage

  Scenario: logging into admin page
    Given user is on 'Admin Log in page'
    When user clicks on 'Log in'
    Then page is 'Admin page'

  Scenario: accessing point of interest page
    Given user is on the homepage
    When user clicks on 'Point of Interest' link
    Then the page is 'point_of_interest' page