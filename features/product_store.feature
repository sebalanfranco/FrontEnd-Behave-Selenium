@product_store
Feature: product store
    In order to buy products
    As a customer
    I want to browse through the store

    Background:
        Given I navigate to Demoblaze site
        And I am logged in

    @smoke
    Scenario: open a product
        When I open the first product
        Then I should see the product information

    @sanity
    Scenario: add a product to cart
        When I open the first product
        And I add the product to the cart
        Then I should see the "Product added." alert message
