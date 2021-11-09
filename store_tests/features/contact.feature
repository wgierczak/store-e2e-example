Feature: Contact feature
  User can send message to customer service

  Scenario: User sends message to customer service
    Given user is in "CONTACT_US" section
    When user provides correct email
    And user fills rest of form
    And clicks on send button
    Then success message is visible

  Scenario: User provides wrong email in contact us form
    Given user is in "CONTACT_US" section
    When user provides wrong email
    Then warning about wrong email is displayed
    When clicks on send button
    Then error message is visible
