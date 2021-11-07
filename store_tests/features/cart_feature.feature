Feature: Cart feature
  User can add and edit products in cart

  Scenario: User is adding two shirts and removing dress from cart
    When user search for "SHIRT"
    And user adds product to cart
    And user search for "DRESS"
    And user adds product to cart
    And user opens checkout sections
    And user change quantity of "SHIRT" to "2"
    Then number of unique products in cart is "2"
    When user removes "DRESS" from cart
    Then number of unique products in cart is "1"

