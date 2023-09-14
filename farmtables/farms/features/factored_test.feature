Feature: testing website navigation

  Scenario: 'home page' to 'admin page' to point of 'interest page'
    Given user is on homepage
    When user clicks on 'Admin Page'
    Then user is on the 'Admin Log in page'
    Then user fills data and clicks on 'Log in'
    Then page is the 'Admin page'
    Then user returns to the homepage
    Then user clicks on the 'Point of Interest' link
    Then page is the 'point_of_interest' page