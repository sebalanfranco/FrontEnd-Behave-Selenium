@signup
Feature: sign up
    In order to create my account
    As a potential customer
    I want to sign up

    Background:
        Given I navigate to Demoblaze site

    @smoke
    Scenario: successful sign up
        When I open the sign up modal
        And I provide my account information
        Then I should see the "Sign up successful." alert message

    @regression
    Scenario: try to sign up an existent account
        When I open the sign up modal
        And I provide an existent account information
        Then I should see the "This user already exist." alert message

    @regression
    Scenario: try to sign up an account with empty username
        When I open the sign up modal
        And I enter a new password
        Then I should see the "Please fill out Username and Password." alert message

    @regression
    Scenario: try to sign up an account with empty password
        When I open the sign up modal
        And I enter a new username
        Then I should see the "Please fill out Username and Password." alert message