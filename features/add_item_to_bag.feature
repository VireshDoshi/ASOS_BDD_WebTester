Feature: Use the website to add an item to my bag
        So that I can order a shirt
        As a customer
        I want to be able to add an item to my bag

    Scenario: Search for t shirts and add one to my bag
        Given I want to order a shirt from the australlian store
        When I search for purple t shirts AUS
        And I click on an image of a shirt to take me to the product page
        And I select a size
        And I Click on add to bag
        Then I should see saved items in my basket item page