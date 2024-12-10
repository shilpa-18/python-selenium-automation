# Created by saradhya at 12/9/24
Feature: Tests for search


  Scenario: User can open target page and verify the cart is empty
    Given open target main page
    When click on the cart icon
    Then verify your cart is empty message is shown
