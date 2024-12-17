# Created by saradhya at 12/12/24
Feature: Tests for adding to cart

  Scenario: User can search for christmas ornament
    Given Open target main page
    When Search for and add christmas ornament santa to the cart
    Then Verify that the search results shown for christmas ornament santa