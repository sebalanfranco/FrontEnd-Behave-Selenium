Feature: login
    In order to manage my account
    As a customer
    I want to login

    Background:
        Given I navigate to Demoblaze site

    Scenario: successful login
        When I open the login modal
        And I provide my credentials
        Then I should be logged in
