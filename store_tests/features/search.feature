Feature: Search feature
  User can search for products

  Scenario: User is looking for shirt
    When user search for shirt
    Then shirt is available in results
    When user click on search
    Then details of product are displayed
