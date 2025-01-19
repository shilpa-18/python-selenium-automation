# Created by lana at 12/5/24
Feature: User can filter the Secondary deals by Unit price range

  Scenario: User can go to the main page
    Given Open “Secondary” option at the left side menu
    Then Verify the price in all cards is inside the range "(1200000 - 2000000)"


