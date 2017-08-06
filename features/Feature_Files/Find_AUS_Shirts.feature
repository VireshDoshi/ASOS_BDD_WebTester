Feature: Use the website to find products in the Australian store
  So that I can order a shirt
  As an Australian customer
  I want to be able to find t shirts in my store

Scenario: Search for t shirts in Australian store
  Given I want to order a shirt
  When in the Australian store
  When I search for yellow t shirts
  Then I should see some yellow t shirts