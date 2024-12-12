# Created by lana at 11/23/24
Feature: Tests for search

  Scenario: User can search for a product
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

