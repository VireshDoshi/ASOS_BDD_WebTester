Feature: Display prices in New Zealand dollars in the Australian store.
        So that I can see the price of a shirt
        In New Zeland Dollars
        While in the Australlian store

    Scenario: NZ Dollar in AUS Store
        Given I want to order a shirt from the australlian store
        When I search for purple t shirts AUS
        And I change the currency to NZ Dollar
