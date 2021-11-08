Feature: Compare feature
  User can compare products

  Scenario: User is adding two shirts and removing dress from cart
    When user search for "DRESS"
    Then number of products to compare is "0"
    When user adds "1" displayed product from list for comparison
    And user adds "2" displayed product from list for comparison
    Then number of products to compare is "2"
    When user clicks on compare button
    Then two products are available in comparison page
