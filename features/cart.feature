@cart
Feature: cart
    In order to checkout my products
    As a customer
    I want to review my cart

    Background:
        Given I navigate to Demoblaze site
        And I am logged in

    @sanity
    Scenario: review products
        Given I added a product to the cart
        When I open the cart
        Then I should see the product

    @wip @sanity
    Scenario: remove a product
        Given I added a product to the cart
        When I open the cart
        And I remove the first product
        Then I should see that a product was removed

    @smoke
    Scenario: purchase order
        Given I added a product to the cart
        When I open the cart
        And I purchase the order
        Then I should see that the purchase is confirmed
