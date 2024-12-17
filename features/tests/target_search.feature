Feature: Tests for search

  Scenario: User can search for tea
    Given Open target main page
    When Search for tea
    Then Verify search results shown for tea

  Scenario: User can search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify search results shown for coffee

  Scenario: User can search for a mug
    Given Open target main page
    When Search for a mug
    Then Verify search results shown for a mug

  Scenario: User can search for a mug
    Given Open target main page
    When Search for lamp
    Then Verify search results shown for lamp

