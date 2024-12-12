Feature: Tests for Target circle page

  Scenario: User can see header links
    Given Open target circle page
    Then Verify at least 10 benefit cells are shown
