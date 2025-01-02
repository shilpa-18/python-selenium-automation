# Created by saradhya at 1/1/25
Feature: Tests for sign in page opened

  Scenario: Click on sign in page
    Given Open target main page
    When Click on Sign in
    And Click on Sign in page
    Then Verify Sign in form opened
