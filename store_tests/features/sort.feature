Feature: Sort feature
  User can sort products

  Scenario: User sorts bestsellers by highest to lowest price
    Given user is in "BESTSELLERS" section
    When user sorts products by highest to lowest price
    Then products are sorted by highest to lowest price