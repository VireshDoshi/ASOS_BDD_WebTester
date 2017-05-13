Feature: Use the website to save an item for later.
        So that I can order a shirt
        As a customer
        I want to be able to save an item for later

    Scenario: Search for t shirts and save for later
        Given I want to order a shirt from the australlian store
        When I search for purple t shirts AUS
        And I click on the save symbol
        Then I should see saved items in my saved item page