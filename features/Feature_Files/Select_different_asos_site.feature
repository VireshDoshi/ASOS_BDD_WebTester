Feature: Use the website and select different sites
  In order to use the website
  As a customer from a particular locale
  I want to change to a different site

  @wip
  Scenario: From the .com website goto the uk website
    Given I am on the asos.com website
    When I select UK from the dropdown
    Then I am on the UK site

