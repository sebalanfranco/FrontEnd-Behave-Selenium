Feature: login
    In order to manage my account
    As a customer
    I want to login

    Background:
        Given I navigate to Demoblaze site

    Scenario: successful login
        When I open the login modal
        And I provide my credentials
        Then I should be successfully logged in

    Scenario: try to login providing non-existent username
        When I open the login modal
        And I provide a non-existent username
        Then I should see the "User does not exist." alert message

    Scenario: try to login providing wrong password
        When I open the login modal
        And I provide a wrong password
        Then I should see the "Wrong password." alert message
