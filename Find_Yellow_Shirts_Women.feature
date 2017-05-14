Feature: Use the website to change how search results are displayed    
        So that I can select my yellow t shirts
        I want to be able to refine search by gender


    Scenario: Display search results of yellow shirts for women
        Given I want to order a shirt
        When I search for yellow t shirts in the searchbar
        And I refine by "women"
        Then I should see some yellow t shirts for women