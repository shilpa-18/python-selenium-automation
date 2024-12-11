# Created by saradhya at 12/9/24
Feature: Tests for search

Scenario: logged out user can navigate to Sign In
   Given open target main page
   When click Sign In
   Then verify Sign In form opened

Scenario: verifies that “Your cart is empty” message is shown
   Given open target main page
   When click on cart icon
   Then verify 'your cart is empty' message is shown